from django.db import models


class Document(models.Model):
    title = models.CharField(max_length=50)
    text = models.CharField(max_length=200)
    file = models.FileField(blank=True, null=True)
    date_created = models.DateField(auto_now_add=True)
    date_expired = models.DateField()
    status = models.CharField(choices=(
        ('Active', 'Active'),
        ('Death active', 'Death active')
    ), max_length=20, default='Active')
    document_root = models.CharField(choices=(
        ('Public', 'Public'),
        ('Private', 'Private'),
        ('Secret', 'Secret'),
        ('Top-Secret', 'Top-Secret')
    ), max_length=50)

    def __str__(self):
        return self.title
