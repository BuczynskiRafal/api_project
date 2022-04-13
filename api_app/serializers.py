from rest_framework import serializers

from .models import AnnualEnterpriseSurvey


class AnnualEnterpriseSurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = AnnualEnterpriseSurvey
        fields = "__all__"