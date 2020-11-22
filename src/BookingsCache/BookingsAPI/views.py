from django.shortcuts import render
from rest_framework.response import Response

from rest_framework import views as rf_views


from .serializers import MySerializer
# Create your views here.

class MyView(rf_views.APIView):

    def get(self, request):
        yourdata= [{"data": "My name"}, {"data": "Next"}]
        results = MySerializer(yourdata, many=True).data
        return Response(results)