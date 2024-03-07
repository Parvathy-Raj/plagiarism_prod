from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework import permissions , status
from rest_framework.views import APIView
from rest_framework.response import Response

from plag_api.utils import search_and_similarity
from .serializers import PlagSerializer

class PlagDataView(APIView):
   
    permission_classes= [permissions.AllowAny]
    def post(self,request: any , format: any = None) -> any :
        print(request.data['text'])
        # serializer = PlagSerializer(data=request.data)
        # if serializer.is_valid():
        #     serializer.save()
        report = search_and_similarity(request.data['text'])
        del report['corpus_data']
        return Response(report, status=status.HTTP_200_OK)
        # else:
        #     return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)