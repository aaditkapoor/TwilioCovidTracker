# Download the helper library from https://www.twilio.com/docs/python/install
import os
import datetime
import logging

# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
KEYS = {}
KEYS["account_sid"] = 'AC3d1c37040cbb5a88673e3f7e46e5f9d4'
KEYS["auth_token"] = '8232af2bd0f4e31b53e0e9ed42fa7d54'
KEYS["from_"] = "+19382010923"
KEYS["to"] = ""


# some helper methods too

def convertDateToDay(date:str) -> str:
    """
        Convert date into a format of <day> and <date>.
        (str) -> str
    """
    converted = datetime.datetime.strptime(date,"%Y-%m-%dT%H:%M:%SZ")
    return f'{converted.strftime("%D")} {converted.strftime("%A")}'

