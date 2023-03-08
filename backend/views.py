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
        last_two = Reading.objects.all().order_by('-id')[:2]
        serializer = ReadingSerializer(last_two, many=True)

        # VAprev = float(serializer.data[1]['v_oc'])
        # IAprev = float(serializer.data[1]['i_sc'])

        VAprev = 2.0
        IAprev = 1.0
        PAprev = IAprev * VAprev

        Dprev = 1.5

        D = Dprev
        # VA = float(serializer.data[0]['v_oc'])
        # IA = float(serializer.data[0]['i_sc'])

        VA = 1.0
        IA = 4.0
        PA = VA 

        DeltaVA = VA - VAprev
        DeltaPA = PA - PAprev

        if DeltaPA>0:
            if DeltaVA>0:
                D = Dprev - 0.0001
            elif DeltaVA<0:
                D = Dprev + 0.0001
        elif DeltaPA<0:
            if DeltaVA>0:
                D = Dprev + 0.0001
            elif DeltaVA<0:
                D = Dprev - 0.0001
        
        if D>0.9:
            D=0.9
        elif D<0:
            D=0
        
        return Response(D)