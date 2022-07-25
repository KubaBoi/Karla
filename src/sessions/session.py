from ast import Eq
import os
import platform
import json
import subprocess
import time

from Cheese.resourceManager import ResMan
from Cheese.Logger import Logger
from Cheese.appSettings import Settings

from src.commands.tools.stringer import Stringer

class Session:

    def __init__(self, ip):
        self.fazeCount = 0
        self.faze = 0
        self.ip = ip
        self.command = None
        self.lastAction = time.time()

    # wakes Karla up
    def createSession(self, text):
        commands = self.loadCommands()

        starter = Stringer.starts(text, commands[0]["starters"])
        if (starter):
            return True
        return False

    def findCommand(self, text):
        commands = self.loadCommands()

        for command in commands[1:]:
            if (Stringer.starts(text, command["starters"]) and Stringer.ends(text, [command["ending"].replace("& ", "")])):
                
                for starter in command["starters"]:
                    textArray = text.split(" ")
                    fullText = " ".join([starter, command["ending"]]).strip()
                    if (len(textArray) == len(fullText.split(" "))):
                        self.command = command
                        self.fazeCount = command["fazes"]
                        if (command["ending"].find("&") != -1):
                            return textArray[len(starter.split(" "))]
                        return "data"
        return False

    def loadCommands(self):
        with open(os.path.join(ResMan.resources(), "commands.json"), "r") as f:
            return json.loads(f.read())["COMMANDS"]

    def doCommand(self, text):
        python = "python"
        if (platform.system() != "Windows"):
            python = "python3"

        command = f"{python} \"{ResMan.src('commands', self.command['name'])}.py\" --faze {self.faze} --data \"{text}\" --port {Settings.port}"
        Logger.info(command, silence=False)
        p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
        resp, err = p.communicate()

        if (not resp.decode("utf-8").startswith("&")):
            self.faze += 1
        
        return resp.decode("utf-8")

    def isDone(self):
        return self.fazeCount >= self.faze
