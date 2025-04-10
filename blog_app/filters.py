import django_filters
from . models import *


class PostFilter(django_filters.FilterSet):
    class Meta:
        model = Post
        fields = {
            'title': ['icontains'],
            'category': ['exact'],
            'tags': ['exact'],
        }
