from requests.sessions import session
from requests_futures.sessions import FuturesSession

from datetime import datetime
from datetime import timedelta
from utils import datetimeutils as dutils

class DataProvider:

    def __init__(self):
        self.session = FuturesSession(max_workers = 30)
        self.url = 'https://api.skypicker.com/flights'

    def GetDataForNextMonth(self):
        pass
    def GetDataBy(self, fly_from, fly_to, date_from, date_to, response_handler = None):
        response_list = []
        PARAMS = {'fly_from':fly_from, 'fly_to': fly_to, "partner":"picky"}

        for date in dutils.datesIterator(date_from, date_to):
            self.on_loop_operation(self.url, PARAMS, date, response_list)

        return response_list
    

    def on_loop_operation(self, url, Params, desired_date: datetime, response_list):
            parameters = Params.copy()
            
            parameters.update(
                {'date_from' : desired_date.strftime('%d/%m/%Y'),
                 'date_to': desired_date.strftime('%d/%m/%Y') })

            action_item = self.session.get(url, params = parameters,)# hooks = {'response' : response_handler})

            response_list.append(action_item)
