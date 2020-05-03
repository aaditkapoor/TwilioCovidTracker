"""
    Parse a message within the request context.
"""
import os
import logging
import json
import abc
from abc import abstractmethod


# helper (can be changed)
def isValidMessage(message:str) -> bool:
    if "show" in message.split():
        return True
    else:
        return False

class BaseParser:
    def __init__(self, message:str):
        self.message = message
    
    def parse(self):
        raise NotImplementedError

    def getText(self):
        raise NotImplementedError

class CountryParser(BaseParser):
    def __init__(self, parser:BaseParser):
        self.parser=parser
    def parse(self):
        words = self.parser.message.split(" ")
        # show me stats for <country_name>
        if len(words) == 1:
            self.country = "India" # by default
        self.country = words[-1] # last element in country
    def getText(self):
        return self.country

# We can similarily make custom parsers for anything and we can further enhance
# the chatbot with NLP techniques.

