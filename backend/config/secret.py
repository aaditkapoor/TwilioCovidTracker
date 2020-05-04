import os
import datetime
import logging

# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
KEYS = {}
KEYS["account_sid"] = '<Add_your_sid>'
KEYS["auth_token"] = '<Add_your_token>'
KEYS["from_"] = "<paste_phone_number"
KEYS["to"] = ""


# some helper methods too

def convertDateToDay(date:str) -> str:
    """
        Convert date into a format of <day> and <date>.
        (str) -> str
    """
    converted = datetime.datetime.strptime(date,"%Y-%m-%dT%H:%M:%SZ")
    return f'{converted.strftime("%D")} {converted.strftime("%A")}'

