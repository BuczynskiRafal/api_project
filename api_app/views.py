import requests
from django.shortcuts import render
from rest_framework import generics
from rest_framework import filters
from django.shortcuts import get_object_or_404

from .models import AnnualEnterpriseSurvey
from .serializers import AnnualEnterpriseSurveySerializer


class AnnualEnterpriseSurveyApi(generics.ListCreateAPIView):
    queryset = AnnualEnterpriseSurvey.objects.all()
    serializer_class = AnnualEnterpriseSurveySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['year', 'industry_code_ANZSIC', 'industry_name_ANZSIC', 'rme_size_grp', 'variable', 'value', 'unit']


class AnnualEnterpriseSurveyApiDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = AnnualEnterpriseSurvey.objects.all()
    serializer_class = AnnualEnterpriseSurveySerializer
