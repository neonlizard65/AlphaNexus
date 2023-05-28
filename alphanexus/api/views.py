from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from web.models import CDKey, Check, Country, Comment, CustomUser, Developer, Library, Media, Post, Product, Review, Tag
from .serializers import CountrySerializer

@api_view(['GET'])
def getCountries(request):
    countries = Country.objects.all()
    serializer = CountrySerializer(countries, many=True)
    return Response(serializer.data)
