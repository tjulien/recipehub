from django.db import models
from django.contrib.auth.models import User

class Follower(models.Model):
    follower = models.ForeignKey(User, related_name='follower')
    following = models.ForeignKey(User, related_name='following')

class Recipe(models.Model):
    name = models.CharField(max_length=64)
    user = models.ForeignKey(User)
    create_date = models.DateTimeField('date created')
    preparation = models.TextField()
    overview = models.TextField()

class Ingredient(models.Model):
    name = models.CharField(max_length=64)
    list_num = models.PositiveIntegerField()
    recipe = models.ForeignKey(Recipe)

class RecipeFork(models.Model):
    fork = models.ForeignKey(Recipe, related_name='fork')
    forked = models.ForeignKey(Recipe, related_name='forked')
