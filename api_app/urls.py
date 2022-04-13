from django.urls import path

from .views import AnnualEnterpriseSurveyApi
from .views import AnnualEnterpriseSurveyApiDetail

urlpatterns = [
    path('api/', AnnualEnterpriseSurveyApi.as_view()),
    path('api/<int:pk>/', AnnualEnterpriseSurveyApiDetail.as_view()),
]
