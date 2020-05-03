"""
    Contains the source code for retreiving the data as well as sending
    an SMS from the twillio API
"""


import logging
import os
import json
import requests
from typing import Dict
from .models.data import Data
from typing import List, Type
from dataclasses import dataclass
from twilio.rest import Client
from sklearn.linear_model import LinearRegression
from .config.secret import KEYS, convertDateToDay

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







