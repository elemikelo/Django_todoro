from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from tasks.models import Task
from tasks.serializers import TaskSerializer, TasksListSerializer


class TasksViewSet(ModelViewSet):


    queryset = Task.objects.all()
    permission_classes = (IsAuthenticated,)
    def get_serializer_class(self):
        return TasksListSerializer if self.request.method == "list" else TaskSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


"""class TaskDetailAPI(RetrieveUpdateDestroyAPIView):

    #Retrieves (GET), updates(PUT) and destroy (DELETE) a given Task


    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticated,)"""

