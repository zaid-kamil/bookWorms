from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings


# Create your views here.
def index(request):
    return render(request, 'index.html')


