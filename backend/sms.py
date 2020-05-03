"""
    Contains the source code for retreiving the data as well as sending
    an SMS from the twillio API
"""


import logging
import os
import json
import requests
from typing import Dict
from typing import List, Type
from dataclasses import dataclass
from twilio.rest import Client
from sklearn.linear_model import LinearRegression
from .secret import KEYS, convertDateToDay


client = Client(KEYS["account_sid"], KEYS["auth_token"])
API_URL = "https://api.covid19api.com/live/country/"



class Sender:

    @staticmethod
    def send(client:Client, message:str, to=KEYS["to"]):
        message = client.messages.create(
                     body=message,
                     from_=KEYS["from"],
                     to=to
                 )
        return message.sid

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


class API:
    def __init__(self, country:str):
        self.country = country
    
    def getAll(self):
        data = []
        resp = requests.get(API_URL + self.country)

        if resp.status_code == 200:
            json_data = json.loads(resp.content)
            for row in json_data:
                data.append(
                    Data(country=row["Country"], confirmed=row["Confirmed"], deaths=row["Deaths"], recovered=row["Recovered"],
                active=row["Active"], date=convertDateToDay(row["Date"]) )
                )
            self.data = data
        else:
            logging.error(resp.status_code)
    
    def buildMessage(self) -> str:
        message = "Live stats for " + self.country
        message = message + "\n=============================="
        for item in self.data:
            message = message + "\n"
            message = message + f'Confirmed: {item.confirmed}' + "\n"
            message = message + f'Deaths: {item.deaths}' + "\n"
            message = message + f'Recovered: {item.recovered}' + "\n"
            message = message + f'Active: {item.active}' + "\n"
            message = message + f'date: {item.date}' + "\n"
        
        return message







