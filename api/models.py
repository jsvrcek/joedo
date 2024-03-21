from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models


class School(models.Model):
    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name


class JDUser(AbstractBaseUser):
    school = models.ForeignKey(School, on_delete=models.CASCADE)

    @property
    def name(self):
        return self.get_username()

    def __str__(self):
        return self.get_username()


class Level(models.Model):
    name = models.CharField(max_length=254)
    rank = models.IntegerField()
    school = models.ForeignKey(School, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Series(models.Model):
    name = models.CharField(max_length=254)
    alternate_name = models.CharField(max_length=254)
    description = models.TextField()

    def __str__(self):
        return self.name


class MovementCategory(models.Model):
    name = models.CharField(max_length=254)
    description = models.TextField()


class Movement(models.Model):
    name = models.CharField(max_length=254)
    alternate_name = models.CharField(max_length=254)
    description = models.TextField()
    category = models.ForeignKey(MovementCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class MovementStep(models.Model):
    name = models.CharField(max_length=254)
    description = models.TextField()
    image = models.ImageField()
    video = models.FileField()

    def __str__(self):
        return self.name


class Bookmark(models.Model):
    user = models.ForeignKey('JDUser', on_delete=models.CASCADE)
    movement = models.ForeignKey('Movement', on_delete=models.CASCADE)
