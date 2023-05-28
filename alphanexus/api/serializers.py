from rest_framework import serializers
from web.models import CDKey, Check, Country, Comment, CustomUser, Developer, Library, Media, Post, Product, Review, Tag

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'
