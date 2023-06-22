from rest_framework import serializers
from .models import Finger,Image
 


class FingerSerializers(serializers.ModelSerializer):
    class Meta:
        model=Finger
        fields='__all__'


class ImageSerializers(serializers.ModelSerializer):
    class Meta:
        model=Image
        fields='__all__'

