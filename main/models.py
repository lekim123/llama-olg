# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Question(models.Model):
    name = models.CharField('Your First and Last Name', max_length=30, blank=False)
    question = models.TextField('Your Question', max_length=2000, blank=False)
    
    def __str__(self):
        return self.name
    
class Article(models.Model):
    name = models.CharField(max_length=50, blank=False)
    summary = models.TextField(max_length=500, blank=False)
    text = models.TextField(max_length=5000, blank=False)
    datePosted = models.DateTimeField(auto_now=True, auto_now_add=False)
    
    def __str__(self):
        return self.name
    
class Newspaper(models.Model):
    name = models.CharField(max_length=50, blank=False)
    articles = models.ManyToManyField(Article)
    
    def get_latest_post(self):
        return self.articles.all().latest('datePosted')
    
    def latest(self):
        return self.articles.order_by('-datePosted')
    
    def __str__(self):
        return self.name
    