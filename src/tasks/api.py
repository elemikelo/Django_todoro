from rest_framework.response import Response
from rest_framework.views import APIView

from tasks.models import Task
from tasks.serializers import TaskSerializer


class TasksAPI(APIView):

    """
    lists (GET) and creates (POST) Tasks

    """
    def get(self, request):
        """
        Returns a list of tasks
        :param request: httpRequest
        :return: Response
        """

        tasks = Task.objects.all()

        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)
