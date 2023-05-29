from rest_framework import serializers
from web.models import CDKey, Check, Country, Comment, CustomUser, Developer, Library, Media, Post, Product, Review, Tag

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'
        
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["username", "last_name", "first_name", "email", "phone", "country", "bio", "wishlist", "cart", "avatar", "background"]
        
class DeveloperSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Developer
        fields = '__all__'
        
class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        
class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class ReviewSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
        
class MediaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Media
        fields = '__all__'
                
class LibrarySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Library
        fields = '__all__'
        

class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        
class CDKeySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CDKey
        fields = '__all__'
        
class CheckSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Check
        fields = '__all__'