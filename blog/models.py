# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField
from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=255)
    summary = RichTextField()
    content = RichTextUploadingField()
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    create_at = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.title