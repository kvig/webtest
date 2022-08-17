from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
from rest_framework.request import Request
from rest_framework.response import Response

from .models import List


@login_required
def home(request: Request) -> Response:
    return render(request, "index.html", {"lists": request.user.lists.all()})


@login_required
def list_detail(request: Request, list_id: int) -> Response:
    user_list = get_object_or_404(List, id=list_id)
    return render(request, "detail.html", {"list": user_list})
