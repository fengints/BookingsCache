from requests.sessions import session
from requests_futures.sessions import FuturesSession

from datetime import datetime
from datetime import timedelta
from utils import datetimeutils as dutils

class DataProvider:

    def __init__(self):
        self.session = FuturesSession(max_workers = 30)
        self.url = 'https://api.skypicker.com/flights'

    def GetDataForNextMonth(self, fly_from, fly_to):
        dfrom = datetime.now()
        dto = dfrom + timedelta(days=30)

        future_responses = self.GetFutureDataBy(fly_from, fly_to, dfrom, dto)
        responses = [resp.result().json() for resp in future_responses]

        return responses

    def GetFutureDataBy(self, fly_from, fly_to, date_from, date_to, response_handler = None):
        response_list = []
        PARAMS = {'fly_from':fly_from, 'fly_to': fly_to, "partner":"picky"}

        for date in dutils.datesIterator(date_from, date_to):
            future = self.request_data(self.url, PARAMS, date, response_handler)
            response_list.append(future)

        return response_list
    
    def request_data(self, url, Params, desired_date: datetime, response_handler = None):
        if (response_handler is None):
            response_handler = {}
            
        parameters = Params.copy()
        desired_dateStr = desired_date.strftime('%d/%m/%Y')
        parameters.update(
            {'date_from' : desired_dateStr,
             'date_to': desired_dateStr })

        return self.session.get(url, params = parameters, hooks = {'response' : response_handler})
