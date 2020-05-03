from backend.parser import BaseParser, CountryParser, isValidMessage
from flask import Flask
from flask import request
from flask import render_template
from twilio.twiml.messaging_response import MessagingResponse
from backend.sms import API, Sender
from backend.models.data import Data

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about/")
def about():
    return render_template("about.html")


@app.route("/api/country/<country_name>")
def message(country_name):
    api = API(country_name)
    api.getAll()
    return api.buildMessage()

# helper method
def getMessage(country:str) -> str:
    api = API(country)
    api.getAll()
    return api.buildMessage()



@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    """Respond to incoming messages with a friendly SMS."""
    # Start our response
    resp = MessagingResponse()

    message = request.values.get('Body', None)
    message = message.lower()

    # If message is not False
    if message:
        if (isValidMessage(message)):
            parser = CountryParser(BaseParser(message))
            country = parser.getText()
            messageToSend = getMessage(country)
            # Add a message
            resp.message(messageToSend)
        else:
            resp.message("Could not understand. Try show me stats for <Country Name>.")

        return str(resp)
    # If no message
    else:
        return str(resp.message("Could not understand."))



"""
if __name__ == "__main__":
    app.run(debug=True)
"""