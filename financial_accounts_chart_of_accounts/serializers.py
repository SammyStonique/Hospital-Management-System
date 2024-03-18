from rest_framework import serializers
from .models import *

class ClientCategorySerializer(serializers.ModelSerializer):
    company = serializers.ReadOnlyField(source='company.company_id')
    class Meta:
        model = ClientCategory
        fields = ['category_id','name','company']

    def create(self, validated_data):
        category = ClientCategory.objects.create(**validated_data)
            
        return category
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)

        instance.save()
        return instance