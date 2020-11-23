from requests.sessions import session
from requests_futures.sessions import FuturesSession

from datetime import datetime
from datetime import timedelta

class DataProvider:
    def __init__(self, max_workers = 30):
        self.session = FuturesSession(max_workers)
        self.url = 'https://api.skypicker.com/flights'

    def GetDataForNextMonth(self):
        pass
    def GetDataBy(self, fly_from, fly_to, date_from, date_to, response_handler = None):
        response_list = []

        PARAMS = {'fly_from':fly_from, 'fly_to': fly_to, "partner":"picky"}

        handler = lambda curday:(
            self.on_loop_operation(
                self.url, PARAMS,
                curday, response_list))

        self.loop_over_dates(handler,
                                date_from,
                                date_to)
        return response_list
        
    def loop_over_dates(self, on_loop: function, date_start, date_end):
            curday = date_start

            while (True):
                #perform operations
                on_loop(curday)

                #add next day
                curday += timedelta(days=1)
    
                #exit if day is the same
                if (isDateEqual(curday, date_end)):
                    break
    
    def on_loop_operation(self, url, params, desired_date: datetime, response_list):
            parameters = params.copy()
            
            parameters.update(
                {'date_from' : desired_date.strftime('%d/%m/%Y'),
                 'date_to': desired_date.strftime('%d/%m/%Y') })

            action_item = self.session.get(url, params = parameters,)# hooks = {'response' : response_handler})

            response_list.append(action_item)

    '''Move to utils'''
    def isDateEqual(date1, date2):
            if (date1.day != date2.day):
                return False
            if (date1.month != date2.month):
                return False
            if (date1.year != date2.year):
                return False
            return True   