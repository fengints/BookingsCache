from django.shortcuts import render
from rest_framework.response import Response

from rest_framework import views as rf_views


from .serializers import MySerializer
# Create your views here.

from .RedisDbContext.DbContext import RedisDbContext

class MyView(rf_views.APIView):

    def get(self, request):
        """ #define data
        dbc = RedisDbContext()
        dbc.set('MyKey',"value")
        
        #take it
        data = dbc.get('MyKey') """
        
        yourdata= [{"data": {"1":"1 key", "2": [{"2.1": "sec 1" }] } }]

        results = MySerializer(yourdata, many = True).data
        return Response(results)