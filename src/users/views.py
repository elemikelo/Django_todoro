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
            django_login(request, user)
            # usuario autenticado
            return redirect('tasks_list')
        else:
            # usuario no autenticado
            context["error"] = "Wrong username or password"

    return render(request, 'login.html', context)
