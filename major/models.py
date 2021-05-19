from django.db import models
from accounts.models import Dossier


class Education(models.Model):
    """This is model for apply about education of dossier"""
    start_date = models.DateField()
    end_date = models.DateField()
    school_name = models.CharField(max_length=50)
    major = models.CharField(max_length=20)
    dossier = models.ForeignKey(Dossier, on_delete=models.CASCADE, related_name='schools')

    def __str__(self):
        return f'{self.dossier} {self.school_name}'


class Warcraft(models.Model):
    """This is model for apply about warcraft of dossier"""
    start_date = models.DateField()
    end_date = models.DateField()
    military_area = models.CharField(max_length=50)
    major = models.CharField(max_length=50)
    end_pose = models.CharField(max_length=40)
    dossier = models.ForeignKey(Dossier, on_delete=models.CASCADE, related_name='war_crafts')

    def __str__(self):
        return f'{self.dossier} {self.military_area} {self.major}'
