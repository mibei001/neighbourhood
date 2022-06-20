from django.test import TestCase
from django.contrib.auth.models import User
from .models import Neighbour, Post, Profile, Business
import datetime

# Create your tests here.


class Neighbour(TestCase):
    def setUp(self):
        self.name = Neighbour(name='Jamuhuri')
        self.description = Neighbour(description='This is a Description')
        self.location = Neighbour(location='Nairobi')
        self.population = Neighbour(population='100')
        self.user = Neighbour(date='kevin')

    def test_string(self):
        self.assertEqual(str(self.name), 'Jamuhuri')

    def test_string(self):
        self.assertEqual(str(self.description), 'This is a Description')

    def test_string(self):
        self.assertEqual(str(self.location), 'Nairobi')

    def test_string(self):
        self.assertEqual(str(self.population), '100')

    def test_string(self):
        self.assertEqual(str(self.user), 'kevin')


class Post(TestCase):
    def setUp(self):
        self.title = Post(user='Noise')
        self.description = Post(bio='This is my bio')
        self.post_by = Post(bio='This is my bio')
        self.neighbourhood = Post(bio='This is my bio')
        self.posted_on = Post(bio='This is my bio')

    def test_string(self):
        self.assertEqual(str(self.title), 'kevin')

    def test_string(self):
        self.assertEqual(str(self.description), 'This is my bio')

    def test_string(self):
        self.assertEqual(str(self.post_by), 'kevin')

    def test_string(self):
        self.assertEqual(str(self.neighbourhood), 'kevin')

    def test_string(self):
        self.assertEqual(str(self.posted_on), 'kevin')


class Business(TestCase):
    def setUp(self):
        self.user = Business(user='kevin')
        self.name = Business(name='carwash')
        self.description = Business(description='This is a description')
        self.neighbourhood = Business(neighbourhood='Jamuhuri')
        self.email = Business(email='test@gmail.com')

    def test_string(self):
        self.assertEqual(str(self.user), 'kevin')

    def test_string(self):
        self.assertEqual(str(self.name), 'carwash')

    def test_string(self):
        self.assertEqual(str(self.description), 'This is a description')

    def test_string(self):
        self.assertEqual(str(self.neighbourhood), 'Jamuhuri')

    def test_string(self):
        self.assertEqual(str(self.email), 'test@gmail.com')


class Profile(TestCase):
    def setUp(self):
        self.username = Profile(username='kevin')
        self.bio = Profile(bio='this is my bio')
        self.neighbourhood = Profile(neighbourhood='Jamuhuri')

    def test_string(self):
        self.assertEqual(str(self.username), 'kevin')

    def test_string(self):
        self.assertEqual(str(self.bio), 'this is my bio')

    def test_string(self):
        self.assertEqual(str(self.neighbourhood), 'Jamuhuri')
