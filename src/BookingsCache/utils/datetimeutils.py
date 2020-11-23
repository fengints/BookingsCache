
'''Move to utils'''
def isDateEqual(date1, date2):
    if (date1.day != date2.day):
        return False
    if (date1.month != date2.month):
        return False
    if (date1.year != date2.year):
        return False
    return True   
      
from datetime import timedelta

class datesIterator:
    def __init__(self, date_start, date_end):
        self.date_start = date_start
        self.date_end = date_end

    def __iter__(self):
        self.curday = self.date_start
        return self

    def __next__(self):
        #exit if day is the same
        if (isDateEqual(self.curday, self.date_end)):
            raise StopIteration
        
        #add next day
        self.curday += timedelta(days=1)

        return self.curday
