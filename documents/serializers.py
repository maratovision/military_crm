import datetime
from django.utils import timezone
from rest_framework import serializers
from .models import *


class DocumentSerializer(serializers.ModelSerializer):
    check_date = serializers.SerializerMethodField()

    class Meta:
        model = Document
        fields = ['id', 'title', 'file', 'date_created', 'date_expired', 'status',
                  'document_root', 'text', 'check_date']

    def get_check_date(self, obj):
        date_expired = obj.date_expired
        date_now = datetime.datetime.date(timezone.now())
        if date_now > date_expired:
            obj.status = 'Death active'
            obj.save()
