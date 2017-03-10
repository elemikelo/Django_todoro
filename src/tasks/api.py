from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from tasks.models import Task
from tasks.serializers import TaskSerializer, TasksListSerializer


class TasksAPI(ListCreateAPIView):

    """
    lists (GET) and creates (POST) Tasks

    """
    queryset = Task.objects.all()
    permission_classes = (IsAuthenticated,)
    def get_serializer_class(self):
        return TasksListSerializer if self.request.method == "GET" else TaskSerializer


class TaskDetailAPI(RetrieveUpdateDestroyAPIView):
    """
    Retrieves (GET), updates(PUT) and destroy (DELETE) a given Task
    """

    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticated,)

