from django.db import models
import datetime
import random

from django.db import models
from django.utils import timezone
from django.db.models import F, Sum, Count


class typeList(models.Model): #ประเภทการแข่ง
    nameType = models.CharField(max_length=50, default="")
    gender = models.TextField(max_length=400, default="")
    def __str__(self):
        return self.nameType + ":" + self.gender

class Director(models.Model): #กรรมการ
    name = models.CharField(max_length=50, default="")
    gender = models.TextField(max_length=40, default="")
    birthday = models.DateTimeField(max_length=40, default="")
    tel = models.CharField(max_length=10, default="")
    address = models.CharField(max_length=400, default="")
    def __str__(self):
        return self.name + ":" + self.gender + ":" + self.birthday + ":" + self.tel + ":" + self.address



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


