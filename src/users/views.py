from django.contrib.auth import authenticate, login as django_login
from django.shortcuts import render, redirect


def login(request):
    """
    Hace login de un usuario
    :param request: HttpRequest
    :return: HttpResponse
    """
    context = dict()
    if request.method == "POST":
        username = request.POST.get('usr')
        password = request.POST.get('pwd')
        user = authenticate(username=username, password=password)
        if user is not None:

            # usuario autenticado
            request.sesion["default-language"] = "es"
            django_login(request, user)
            url = request.GET.get('next', 'task_list')
            return redirect('tasks_list')

        else:
            # usuario no autenticado
            context["error"] = "Wrong username or password"

    return render(request, 'login.html', context)
