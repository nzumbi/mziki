from django.http import HttpResponse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic


def index(request):
        return render(request, "mzikiapp/home.html")


