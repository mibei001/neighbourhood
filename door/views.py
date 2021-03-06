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


@login_required(login_url='accounts/login/')
def create_mtaa(request):
    if request.method == "POST":
        form = NeighbourForm(request.POST, request.FILES)
        if form.is_valid():
            mtaa = form.save(commit=False)
            mtaa.save()
        return redirect("profile")
    else:
        form = NeighbourForm()
    return render(request, "create_mtaa.html", {"form": form})


@login_required(login_url='accounts/login/')
def profile(request):
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("profile")

    else:
        form = ProfileForm()
    return render(request, "profile.html", {"form": form, "profile": profile})


@login_required(login_url='accounts/login/')
def post(request):
    posts = Post.objects.all().order_by('-posted_on')
    return render(request, "post.html", {"posts": posts})


@login_required(login_url='accounts/login/')
def new_post(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.neighbourhood = request.user.profile.neighbourhood
            post.posted_by = request.user
            post.save()
            return redirect("post")
    else:
        form = PostForm()
    return render(request, "new_post.html", {"form": form})


@login_required(login_url='accounts/login/')
def new_business(request):

    user = User.objects.filter(id=request.user.id).first()
    profile = Profile.objects.filter(user=user).first()
    if request.method == "POST":
        business_form = BusinessForm(request.POST, request.FILES)
        if business_form.is_valid():
            # business = Business(
            # name=request.POST['name'], neighbourhood=Profile.neighbourhood)
            business_form.save()

        return redirect('business')
    else:
        business_form = BusinessForm()
        business = Business.objects.all()
    return render(request, "new_business.html", {"business_form": business_form, "business": business})


@login_required
def logout(request):
    django_logout(request)
    return HttpResponseRedirect('/')


def search(request):
    if request.method == "POST":
        searched = request.POST['searched']
        business = Business.objects.filter(
            name=searched)

        return render(request, "search.html", {"business": business})
    else:
        message = "You havent searched any business"
        return render(request, "search.html", {"message": message})
