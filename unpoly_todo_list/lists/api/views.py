from django.db.models.query import QuerySet
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from rest_framework import viewsets, status
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response

from .serializers import TaskSerializer, ListSerializer
from ..models import Task, List


class ListViewSet(viewsets.ModelViewSet):
    queryset = List.objects.all()
    serializer_class = ListSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self) -> QuerySet:
        user = self.request.user
        return List.objects.filter(user=user)

    def create(self, request: Request, *args, **kwargs) -> Response:
        serializer = ListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return render(request, "list_li.html", serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request: Request, pk=None):
        list_obj = get_object_or_404(List, id=pk)
        list_obj.delete()
        return HttpResponse(status=status.HTTP_200_OK)


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self) -> QuerySet:
        user = self.request.user
        return Task.objects.filter(parent_list__user=user)

    def create(self, request: Request, *args, **kwargs) -> Response:
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return render(request, "task_li.html", serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request: Request, pk=None) -> Response:
        task_obj = get_object_or_404(Task, id=pk)
        task_obj.completed = not task_obj.completed
        task_obj.save()
        task_obj.id = pk
        # context = {
        #     "id": pk,
        #     "title": task_obj.title,
        #     "completed": task_obj.completed,
        #     "parent_list": task_obj.parent_list,
        # }
        return render(request, "task_li.html", task_obj)

    def destroy(self, request: Request, pk=None):
        task_obj = get_object_or_404(Task, id=pk)
        task_obj.delete()
        return HttpResponse(status=status.HTTP_200_OK)
