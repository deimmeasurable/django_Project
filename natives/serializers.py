from django import forms
from rest_framework import serializers

from .models import Native, Cohort


class CohortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cohort
        fields = '__all__'


class NativeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Native
        # fields = ('id', 'cohort', 'email', 'first_name', 'last_name', 'gender', 'number', 'data_0f_birth')
        fields = '__all__'
