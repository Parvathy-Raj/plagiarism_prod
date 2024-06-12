from rest_framework import serializers
from plag.models import PlagData, DomainCount , journalDB

class PlagSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlagData
        fields = '__all__'
        
        
class DomainSerializer(serializers.ModelSerializer):
    class Meta:
        model = DomainCount
        fields = '__all__'

class JournalSerializer(serializers.ModelSerializer):
    class Meta:
        model = journalDB
        fields = '__all__'
        
