from rest_framework import serializers
from .models import *


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'phone_number', 'bio', 'password']


class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'description', 'category', 'image']

class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class TagsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = ['id', 'name']

