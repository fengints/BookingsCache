from django.shortcuts import render
from rest_framework.response import Response

from rest_framework import views as rf_views

from .serializers import MySerializer
import asyncio
# Create your views here.

from .RedisDbContext.DbContext import RedisDbContext

from .tasks import mytask
class MyView(rf_views.APIView):

    def get(self, request):
        """ #define data
        dbc = RedisDbContext()
        dbc.set('MyKey',"value")
        
        #take it
        data = dbc.get('MyKey') """

        async def testAsync():
            asyncio.set_event_loop(asyncio.ProactorEventLoop())
            await asyncio.sleep(10)
            print("finished")

        #start task
        ioloop = asyncio.ProactorEventLoop()
        asyncio.set_event_loop(ioloop)
        ioloop.run_in_executor(mytask.apply_async())
        ioloop.close() 

        #test taking data
        from .DataProvider import DataProvider
        import datetime as dtime
        from requests_threads import AsyncSession

        loop = asyncio.ProactorEventLoop()
        asyncio.set_event_loop(loop)

        dp = DataProvider()
        ffrom = "ALA"; fto = "TSE"
        dfrom = dtime.date(2020, 11, 24)
        dto = dtime.date(2020, 11, 26)

        responses = dp.GetDataBy(ffrom, fto, dfrom, dto)

        yourdata= [{"data": {"1":"1 key", "2": [{"2.1": "sec 1" }] } }]

        results = MySerializer(yourdata, many = True).data
        return Response(results)