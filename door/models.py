from django.db import models
from cloudinary.models import CloudinaryField
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.


class Neighbour(models.Model):
    name = models.CharField(max_length=60, null=True)
    description = models.CharField(max_length=400, null=True)
    location = models.CharField(max_length=200, null=True)
    population = models.IntegerField()

    user = models.ForeignKey('Profile', null=True,
                             blank=True, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name

    def create_neighbour(self):
        self.save()

    def delete_neighbour(self):
        self.delete()

    @classmethod
    def find_neighbour(cls, id):
        jirani = cls.objects.get(id=id)
        return jirani

    def update_neighbour(self, name):
        self.name = name
        self.save()


class Post(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    post_by = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    neighbourhood = models.ForeignKey(Neighbour, on_delete=models.CASCADE)
    posted_on = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title

    def save_post(self):
        self.save()

    def delete_post(self):
        self.delete()


class Business(models.Model):
    user = models.OneToOneField(
        User, null=True, on_delete=models.CASCADE, blank=True)
    name = models.CharField(max_length=60, null=True)
    description = models.CharField(max_length=400, null=True)
    neighbourhood = models.ForeignKey(Neighbour, on_delete=models.CASCADE)
    email = models.EmailField()

    def __str__(self):
        return self.name

    def create_business(self):
        self.save()

    def delete_business(self):
        self.delete


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(max_length=300, blank=True)

    neighbourhood = models.ForeignKey(
        Neighbour, on_delete=models.SET_NULL, null=True, related_name='users')

    def __str__(self):
        return f'{self.user.username} profile'
