from rest_framework.permissions import BasePermission


class UserPermission(BasePermission):

    def has_permission(self, request, view):
        """
        DEFINE SI UN USUARIO PUEDE USAR O NO EN EL ENDPOINT QUE QUIERE UTILIZAR
        :param request:  HttpRequest
        :param view: UserApi/UserDetailAPI
        :return: True si puede, False si no puede
        """
        from users.api import UserDetailAPI

        # cualquier puede crear un usuario (POST)

        if request.method == "POST":
            return True

        # si esta autenticado y quiere hacer algo sobre el detalle o es superuser y quiere hacer algo sobre el listd0
        if request.user.is_authenticated() and (request.user.is_superuser or isinstance(view, UserDetailAPI)):
                return True

        return False

    def has_object_permission(self, request, view, obj):
        """
        define si el usuario  puede realizar la accion sobre el objeto que quiere realzarla
        :param request: HttpRequest
        :param view: UserApi/UserDetailAPI
        :param obj: User
        :return: True si puede, False si no puede
        """
        # si es admin o es el mismo le dejamos
        return request.user.is_superuser or request.user == obj

