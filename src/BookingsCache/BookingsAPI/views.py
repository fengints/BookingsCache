from django.shortcuts import render
from rest_framework.response import Response

from rest_framework import views as rf_views

from .serializers import MySerializer
import asyncio
# Create your views here.

from .RedisDbContext.DbContext import RedisDbContext

class MyView(rf_views.APIView):
    '''Get data from redis instance'''
    def get(self, request):
        """ #define data
        dbc = RedisDbContext()
        dbc.set('MyKey',"value")
        
        #take it
        data = dbc.get('MyKey') """

        #start task
        #ioloop = asyncio.ProactorEventLoop()
        #asyncio.set_event_loop(ioloop)
        #mytask.delay(1,"123")

        #test taking data
        from .DataProvider import DataProvider
        import datetime as dtime

        #zone dataprovider test
        dp = DataProvider()
        ffrom = "ALA"; fto = "TSE"
        dfrom = dtime.date(2020, 11, 24)
        dto = dtime.date(2020, 12, 26)

        future_responses = dp.GetFutureDataBy(ffrom, fto, dfrom, dto)
        response = [resp.result().json() for resp in future_responses]
        #end zone

        yourdata= [{"data": response}]

        results = MySerializer(yourdata, many = True).data
        return Response(results)