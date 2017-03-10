import json

from django.contrib.auth.models import User
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from users.serializers import UserSerializer, UsersListSerializer
from rest_framework import status


class UsersAPI(APIView):
    """
    List (GET) and creates (POST) users
    """

    def get(self, request):

        """
        Returns a list of the system users
        :param request: HttpRequest
        :return:  HttpResponse
        """
        users = User.objects.all().values("id", "username")
        serializer = UsersListSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        """
        Create a user
        :param request: HttpRequest
        :return: HttpResponse
        """

        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetailAPI(APIView):

    """
    User detail (GET), update user (PUT), delete user (DELETE)
    """
    def get(self, request, pk):
        """
        Returns a requested user
        :param request: HttpRequest
        :param pk: user primary key
        :return: Response
        """
        user = get_object_or_404(User, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk):
        """
        Updates a user with the given data
        :param request:
        :param pk:
        :return:
        """

        user = get_object_or_404(User, pk=pk)

        serializer = UserSerializer(user, data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



    def delete(self, request, pk):
        """
        Delete user
        :param request: HttpRequest
        :param pk:  User primary key
        :return: Response
        """

        user = get_object_or_404(User, pk=pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


