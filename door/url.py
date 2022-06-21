from django.urls import path
from .import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path("add_hood/", views.create_mtaa, name="add_hood"),
    path("new_post/", views.new_post, name="new_post"),
    path("posts/", views.post, name="post"),
    path("accounts/profile/", views.profile, name="profile"),
    path("business/", views.new_business, name="business"),
    path("logout/", views.logout, name="logout"),
    path("search/projects/results/", views.search, name="search"),

]
