from requests_threads import AsyncSession

import asyncio
from datetime import datetime
from datetime import timedelta

class DataProvider:
    def __init__(self):
        #self.loop = asyncio.new_event_loop()
        pass
    def GetDataForNextMonth(self):
        pass
    def GetDataBy(self, fly_from, fly_to, date_from, date_to, response_handler = None):
        url = 'https://api.skypicker.com/flights'
        response_list = []

        loop = asyncio.ProactorEventLoop()
        asyncio.set_event_loop(loop)
        self.session = AsyncSession(loop)

        PARAMS = {'fly_from':fly_from, 'fly_to': fly_to, "partner":"picky"}

        def isDateEqual(date1, date2):
            if (date1.day != date2.day):
                return False
            if (date1.month != date2.month):
                return False
            if (date1.year != date2.year):
                return False
            return True

        async def Loop_over_dates():
            while (True):
                #perform operations
                await operation(url, cday)
            
                #add next day
                cday += timedelta(days=1)
    
                #exit if day is the same
                if (isDateEqual(cday, date_to)):
                    break
        async def operation(url, desired_date):
            parameters = PARAMS.copy()
            parameters.update(
                {'date_from' : desired_date, 'date_to': desired_date })

            action_item = await self.session.get(url, params = parameters,)# hooks = {'response' : response_handler})

            # Add the task to our list of things to do via async
            response_list.append(action_item)

        cday = date_from
        loop = asyncio.set_event_loop(asyncio.new_event_loop())

        

        # Do our list of things to do via async
        loop.run_until_complete(Loop_over_dates)
        loop.close()
        #self.session.map(response_list)
