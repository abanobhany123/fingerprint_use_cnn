
from .models import Finger,Image
from .serializers import FingerSerializers,ImageSerializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics

@api_view(['GET'])
def finger_api(request):
    all_finger= Finger.objects.all()
    data= FingerSerializers(all_finger, many=True).data
    return Response({'data':data}) 

class Finger_apii (generics.ListCreateAPIView):
    serializer_class=FingerSerializers
    queryset=Finger.objects.all()
     

class Finger_creat(generics.RetrieveUpdateDestroyAPIView):
    serializer_class=FingerSerializers
    queryset=Finger.objects.all()
    lookup_field = id

