from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets, permissions
from django_filters.rest_framework import DjangoFilterBackend
from web.models import CDKey, Check, Country, Comment, CustomUser, Developer, DeveloperRequest, Library, Media, Post, Product, Review, Tag
from .serializers import CDKeySerializer, CheckSerializer, CommentSerializer, CountrySerializer, DeveloperRequestSerializer, DeveloperSerializer, LibrarySerializer, MediaSerializer, PostSerializer, ProductSerializer, ReviewSerializer, TagSerializer, UserSerializer

class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('name',)

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('username', 'developer')
    
class DeveloperViewSet(viewsets.ModelViewSet):
    queryset = Developer.objects.all()
    serializer_class = DeveloperSerializer
    
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    
class MediaViewSet(viewsets.ModelViewSet):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer
    
class LibraryViewSet(viewsets.ModelViewSet):
    queryset = Library.objects.all()
    serializer_class = LibrarySerializer
    
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    
class CDKeyViewSet(viewsets.ModelViewSet):
    queryset = CDKey.objects.all()
    serializer_class = CDKeySerializer
    
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('content',)
    
    
class CheckViewSet(viewsets.ModelViewSet):
    queryset = Check.objects.all()
    serializer_class = CheckSerializer
        
class DeveloperRequestViewSet(viewsets.ModelViewSet):
    queryset = DeveloperRequest.objects.all()
    serializer_class = DeveloperRequestSerializer