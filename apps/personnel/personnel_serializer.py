from rest_framework import serializers
from .models import Personnel

class PersonnelSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    first_name=serializers.CharField(read_only=True)
    last_name=serializers.CharField(read_only=True)
    fun_fact=serializers.CharField(read_only=True)
    profile_image = serializers.FileField(read_only=True)
    created_at=serializers.DateTimeField(read_only=True)
    updated_at=serializers.DateTimeField(read_only=True)

    # class Meta:
    #     model = Personnel
    #     fields = ('id','first_name','last_name')
