from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.shortcuts import render, redirect
from django.views import View

from users.form import LoginForm


class LoginView(View):

    def get(self, request):
        """
        Hace login de un usuario
        :param request: HttpRequest
        :return: HttpResponse
        """
        context = {
            'form' : LoginForm()
        }
        return render(request, 'login.html', context)

    def post(self, request):
            form = LoginForm(request.POST)
            context = dict()
            if form.is_valid():
                username = request.cleaned_data.get('username')
                password = request.cleaned_data.get('password')
                user = authenticate(username=username, password=password)
                if user is not None:

                    # usuario autenticado
                    request.sesion["default-language"] = "es"
                    django_login(request, user)
                    url = request.GET.get('next', 'task_list')
                    return redirect(url)

                else:
                    # usuario no autenticado
                    context["error"] = "Wrong username or password"
            context["form"] = form
            return render(request, 'login.html', context)

def logout(request):
    """
    Hace logiyt de un usuario
    :param request: HttpRequest
    :return: HttpResponse
    """
    django_logout(request)
    return redirect('login')
