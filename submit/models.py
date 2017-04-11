# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class BeastPackage(models.Model):
    name = models.CharField(max_length=200)
    version = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    project_url = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    doi = models.CharField(max_length=200)

    def __str__(self):
        return self.name
