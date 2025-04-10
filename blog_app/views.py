import django_filters
from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, Category, Tags, CustomUser
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework import permissions

from . serializers import *
from . models import *
from . filters import PostFilter


class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializers
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_superuser:
            return CustomUser.objects.all()
        else:
            return CustomUser.objects.filter(is_superuser=False)


    def perform_create(self, serializer):
        serializer.save(author=self.request.user)




def main(request):
    return HttpResponse('<h1>Главная страница сайта!</h1>')


class PostsViewSet(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializers
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_class = PostFilter



class DetailPostViewSet(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializers


class CategoryViewSet(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers


class DetailCategoryViewSet(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers


class TagsViewSet(generics.ListCreateAPIView):
    queryset = Tags.objects.all()
    serializer_class = TagsSerializers



class DetailTagsViewSet(generics.RetrieveAPIView):
    queryset = Tags.objects.all()
    serializer_class = TagsSerializers




