from django.urls import path
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
