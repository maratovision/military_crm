from django.contrib.auth.models import User
from django.db import models


class Dossier(models.Model):
    """This is model for Dossier of user"""
    full_name = models.CharField(max_length=50)
    date_birth = models.DateField()
    image = models.ImageField(blank=True, null=True)
    gender = models.CharField(choices=(
        ('Male', 'Male'),
        ('Female', 'Female')
    ), max_length=10)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name

class Car(models.Model):
    """This model is for cars of Military base"""
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.PositiveIntegerField()
    number = models.CharField(max_length=10)
    color = models.CharField(max_length=10)
    type = models.CharField(choices=(
        ('Personality', 'Personality'),
        ('Company', 'Company')
    ), max_length=20)
    dossier = models.ForeignKey(Dossier, on_delete=models.CASCADE, related_name='car')

    def __str__(self):
        return f'{self.brand} {self.model}'
