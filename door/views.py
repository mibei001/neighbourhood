from django.shortcuts import render, redirect
from django.http import response
from django.contrib.auth.decorators import login_required
from django.http.response import Http404, HttpResponseRedirect
from .models import Neighbour, Profile, Business, Post
from django.contrib.auth.models import User
from django.contrib.auth import logout as django_logout
from .forms import *

# Create your views here.


@login_required(login_url='accounts/login/')
def home_page(request):
    try:
        mtaa = Neighbour.objects.all()
    except Exception as e:
        raise Http404
    return render(request, "index.html", {"mtaa": mtaa})
