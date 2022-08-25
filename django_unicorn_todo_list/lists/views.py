from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import List


@login_required
def index(request):
    return render(request, "lists/index.html", {})


@login_required
def tasks(request, list_id):
    parent = List.objects.get(pk=list_id)
    return render(request, "lists/tasks.html", {'list': parent, 'tasks': parent.tasks})
