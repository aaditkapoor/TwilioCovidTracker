# TwilioCovidTracker
A COVID Tracker that informs people COVID stats through SMS using the Twilio APIs.
The app can be seen as a chatbot but for the SMS platform. It features an API engine that sorts the data by country and sends it to user through SMS.
Due to the limitaion of Twilio Trial Version, the app can only operate with a specific set of phone numbers.

The web application is built using Python3.8 conforming to the typing protocols and has a concrete object oriented design model.

# Directory structure
```bash
├── LICENSE
├── Pipfile
├── Pipfile.lock
├── Procfile
├── README.md
├── app.py
├── backend
│   ├── __init__.py
│   ├── config
│   │   ├── __init__.py
│   │   └── secret.py
│   ├── models
│   │   ├── __init__.py
│   │   └── data.py
│   ├── parser.py
│   ├── sms.py
│   └── test_sms.py
├── build.json
├── build.py
├── runtime.txt
└── templates
    ├── about.html
    └── index.html
```

<b> backend: </b> All the backend related code <br>
<b> app.py: </b> The main Flask App <br>
<b> templates: </b> Templates for the project.

# Backend
All the source code for the backend lives in backend/. The app primarily uses Twilio API's to send and receive a message. It communicates with the COVID API using [API](https://api.covid19api.com/).

The API class is API and below is a short example of how it building the message.
```
api = API(country="India")
api.getAll() # Gather all the data and store in a list of Data Objects. See backend/models/data.py
message = api.buildMessage() # Build the message that should be sent.
```

This API and the Twilio SMS Sending and Receiving API IS glued together in the main Flask app (app.py)

# parser.py

The `BaseParser` Class is the crux of the parsing a given message. Currently the functionality is limited to a single command (`"show me stats for <country_name>"`) but as the application grows we would be adding more contextual features.

# build.py and build.json

Inspired by package.json, I created a similar mechanism for the application. build.json is a simple JSON file where each key is the name of command followed by the command.
```
{
  "test": "python run.py"
}
 ```
 
 build.py is the script that matches all the commands and helps the user run the command.
 `python build.py test` will run the command "python run.py"
 
To add a new command, just add it to the build.json

# Try the app

[SMS Covid Tracker] (https://twilio-covid-tracker.herokuapp.com/)

# Demo
[Youtube](https://www.youtube.com/watch?v=bKedoIgr8f0)

# Future Directions

Following are the future directions of the application:
- A fully functional chatbot that also features a predictive engine.
- Get COVID plots on your phone through SMS.
- Remove the Trial Version.

# LICENSE

Copyright 2020 Aadit Kapoor

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.
