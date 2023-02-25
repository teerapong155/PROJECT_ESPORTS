from django.db import models
import datetime
import random

from django.db import models
from django.utils import timezone
from django.db.models import F, Sum, Count

class Categories(models.Model):
    name = models.CharField(max_length=50, default="")
    desc = models.TextField(max_length=400, default="")
    def __str__(self):
        return str(self.id) + ":" + self.name

class TypeList(models.Model): #ประเภทการแข่ง
    nameType = models.CharField(max_length=50, default="")
    gender = models.TextField(max_length=400, default="")
    def __str__(self):
        return self.nameType + ":" + self.gender

class Director(models.Model): #กรรมการ
    name = models.CharField(max_length=50, default="")
    gender = models.TextField(max_length=40, default="")
    birthdate = models.DateField(default=None)
    tel = models.CharField(max_length=10, default="")
    address = models.CharField(max_length=400, default="")
    def __str__(self):
        return self.name + ":" + self.gender + ":" + str(self.birthdate) + ":" + self.tel + ":" + self.address



class AgeCategory(models.Model): #ช่วงอายุ
    name = models.CharField(max_length=50, default="")
    desc = models.TextField(max_length=400, default="")

    def __str__(self):
        return self.name + ":" + self.desc

class Season(models.Model): #ฤดูกาล
    name = models.CharField(max_length=50, default="")
    desc = models.TextField(max_length=400, default="")

    def __str__(self):
        return self.name + ":" + self.desc

class Team(models.Model): #ฤดูกาล
    nameTeam = models.CharField(max_length=50, default="")
    logo = models.ImageField(upload_to ='static/products/', default="")
    name1 = models.CharField(max_length=50, default="")
    name2 = models.CharField(max_length=50, default="")
    name3 = models.CharField(max_length=50, default="")
    name4 = models.CharField(max_length=50, default="")
    name5 = models.CharField(max_length=50, default="")
    name6 = models.CharField(max_length=50, default="")
    player1 = models.CharField(max_length=50, default="")
    player2 = models.CharField(max_length=50, default="")
    player3 = models.CharField(max_length=50, default="")
    player4 = models.CharField(max_length=50, default="")
    player5 = models.CharField(max_length=50, default="")
    player6 = models.CharField(max_length=50, default="")
    email1 = models.CharField(max_length=50, default="")
    email2 = models.CharField(max_length=50, default="")
    email3 = models.CharField(max_length=50, default="")
    email4 = models.CharField(max_length=50, default="")
    email5 = models.CharField(max_length=50, default="")
    email6 = models.CharField(max_length=50, default="")
    def __str__(self):
        return self.nameTeam + ":" \
        # + self.logo + ":" + self.name1 + ":" + self.name2 + ":" + self.name3 + ":" + self.name4
        # + ":" + self.name5 + ":" + self.name6 + ":" + self.player1 + ":" + self.player2 + ":" + self.player3 + \
        # ":" + self.player4 + ":" + self.player5 + ":" + self.player6 + ":" + self.email1 + ":" + self.email2 + ":" + self.email3
        # + ":" + self.email4 + ":" + self.email5 + ":" + self.email6


