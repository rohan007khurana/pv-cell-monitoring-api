from .models import Reading
from .serializers import ReadingSerializer
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response


class ReadingList(generics.ListCreateAPIView):
    queryset = Reading.objects.all()
    serializer_class = ReadingSerializer

class ReadingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reading.objects.all()
    serializer_class = ReadingSerializer


class DutyRatio(APIView):
    def get(self, request, format=None):
        return Response("55")