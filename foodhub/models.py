from django.db import models
from django.contrib.auth.models import User

class Follower(models.Model):
    follower = models.ForeignKey(User, related_name='follower')
    following = models.ForeignKey(User, related_name='following')

class Ingredient(models.Model):
    name = models.CharField(max_length=32)

class Unit(models.Model):
    name = models.CharField(max_length=16)

class IngredientInstance(models.Model):
    ingredient = models.ForeignKey(Ingredient)
    num = models.IntegerField()
    units = models.ForeignKey(Unit)

class Recipe(models.Model):
    name = models.CharField(max_length=64)
    user = models.ForeignKey(User)
    create_date = models.DateTimeField('date created')
    ingredients = models.ManyToManyField(IngredientInstance)

class RecipeFork(models.Model):
    fork = models.ForeignKey(Recipe, related_name='fork')
    forked = models.ForeignKey(Recipe, related_name='forked')
