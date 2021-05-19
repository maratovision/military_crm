from .models import *
from rest_framework import serializers


class EducationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Education
        fields = ['id', 'start_date', 'end_date', 'school_name', 'major']


class WarcraftSerializer(serializers.ModelSerializer):

    class Meta:
        model = Warcraft
        fields = ['id', 'start_date', 'end_date', 'military_area', 'major', 'end_pose']
