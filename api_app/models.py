from django.db import models


class AnnualEnterpriseSurvey(models.Model):
    year = models.IntegerField(blank=True, null=True)
    industry_code_ANZSIC = models.CharField(max_length=200, blank=True, null=True)
    industry_name_ANZSIC = models.CharField(max_length=200, blank=True, null=True)
    rme_size_grp = models.CharField(max_length=200, blank=True, null=True)
    variable = models.CharField(max_length=200, blank=True, null=True)
    value = models.CharField(max_length=200, blank=True, null=True)
    unit = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f"{self.industry_name_ANZSIC}, - {self.year}"

    def __repr__(self):
        return f"{self.industry_name_ANZSIC}, - {self.year}"

