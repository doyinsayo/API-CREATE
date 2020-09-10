from rest_framework import serializers
from django.db import models
from . models import Post
from django import forms

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'title','description','owner'
        )        


