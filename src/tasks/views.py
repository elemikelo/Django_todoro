from django.http import HttpResponse
from django.shortcuts import render

from tasks.models import Task


def tasks_list(request):
    """
    Recupera todas las tareas de la base de datos y las pinta
    :param request: HttpRequest
    :return: HttpResponse
    """
    # recuperar todas las tareas de la base de datos
    tasks = Task.objects.all()

    # crear la forma de presentar los datos
    html = "<ul>"
    for task in tasks:
        html += "<li>" + task.name  + "</lis>"
    html += "</ul>"

    # devolver la respuesta
    return HttpResponse(html)





