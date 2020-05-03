"""
    A script that can run commands specified in build.json
"""
import os
import json
import argparse
import enum
from typing import Dict
import logging

class Error(enum.Enum):
    COMMAND_NOT_FOUND_ERROR = "Command not found! Check build.json"


parser = argparse.ArgumentParser(description="command matching build.json")
BUILD_JSON = "build.json"

class Build:
    def __init__(self, build_file:str):
        try:
            self.build_file = open(build_file, "r")
        except OSError as error:
            print(error)

        self.commands = {}
    
    def parse(self) -> bool:
        json_data = json.loads(self.build_file.read())
        for key in json_data.keys():
            self.commands[key] = json_data[key]
        return True

    def run(self, key:str):
        if key in self.commands.keys():
            os.system(self.commands.get(key, Error.COMMAND_NOT_FOUND_ERROR))
        else:
            logging.error(f'{key}: command not found in build.json')
            




if __name__ == "__main__":
    parser.add_argument("run", help="Run the command")
    args = parser.parse_args()
    command = args.run

    # build the object, parse and run command
    builder = Build(BUILD_JSON)
    builder.parse()
    builder.run(command)


