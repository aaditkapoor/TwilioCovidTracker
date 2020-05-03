from dataclasses import dataclass
from typing import List


# A representation for our data
@dataclass
class Data:
    """
        Representation of COVID data.
    """
    country:str
    confirmed:str
    deaths:str
    recovered:str
    active:str
    date:str

    def __str__(self):
        return "stats for: " + self.country


@dataclass
class DataAggregator:
    data:List[Data]

    def add(self, object:Data):
        self.data.append(object)
    
    def getByCountry(self, country) -> Data:
        found = None
        for i in self.data:
            if i.country == country:
                found=i
                break
        return found
            
    def getAllData(self):
        return self.data