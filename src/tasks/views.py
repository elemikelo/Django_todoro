from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import View

from tasks.forms import TaskForm
from tasks.models import Task


@login_required()
def tasks_list(request):
    """
    Recupera todas las tareas de la base de datos y las pinta
    :param request: HttpRequest
    :return: HttpResponse
    """
    # recuperar todas las tareas de la base de datos
    tasks = Task.objects.select_related("owner", "assignee").all()

    # comprobamos si se debe filtrar por tareas creadas por el user autenticado
    if request.GET.get('filter') == 'owned':
        tasks = tasks.filter(owner=request.user)

    # comprobamos si se debe filtrar por tareas asignadas al user autenticado
    if request.GET.get('filter') == 'assigned':
        tasks = tasks.filter(assignee=request.user)

    # devolver la respuesta
    context = {
        'task_objects': tasks
    }
    return render(request, 'tasks/list.html', context)


@login_required()
def tasks_detail(request, task_pk):
    """
    Recupera una tarea de la base de datos y la pinta con una plantilla
    :param request: HttpRequest
    :param task_pk: Primary key de la tarea a recuperar
    :return: HttpResponse
    """
    # recuperar la tarea
    try:
        task = Task.objects.select_related().get(pk=task_pk)
    except Task.DoesNotExist:
        return render(request, '404.html', {}, status=404)
    except Task.MultipleObjectsReturned:
        return HttpResponse("Existen varias tareas con ese identificador", status=300)

    # preparar el contexto
    context = {
        'task': task
    }

    # renderizar la plantilla
    return render(request, 'tasks/detail.html', context)


class NewTaskView(View):

    @method_decorator(login_required)
    def get(self, request):
        # crear el formulario
        form = TaskForm()

        # renderiza la plantilla con el formulario
        context = {
            "form": form
        }
        return render(request, 'tasks/new.html', context)

    @method_decorator(login_required)
    def post(self, request):
        # crear el formulario con los datos del POST
        task_with_user = Task(owner=request.user)
        form = TaskForm(request.POST, instance=task_with_user)

        # validar el formulario
        if form.is_valid():
            # crear la tarea
            task = form.save()

            # mostrar mensaje de exito
            message = 'Tarea creada con éxito! <a href="{0}">Ver tarea</a>'.format(
                reverse('tasks_detail', args=[task.pk])  # genera la URL de detalle de esta tarea
            )

            # limpiamos el formulario creando uno vacío para pasar a la plantilla
            form = TaskForm()
        else:
            # mostrar mensaje de error
            message = "Se ha producido un error"

        # renderizar la plantilla
        context = {
            "form": form,
            "message": message
        }
        return render(request, 'tasks/new.html', context)
