from rest_framework import serializers
from plag.models import PlagData, DomainCount

class PlagSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlagData
        fields = '__all__'
        
        
class DomainSerializer(serializers.ModelSerializer):
    class Meta:
        model = DomainCount
        fields = '__all__'
        
