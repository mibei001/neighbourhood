from django.urls import path
from .import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path("add_hood/", views.create_mtaa, name="add_hood"),
    path("accounts/profile/", views.profile, name="profile")
]
