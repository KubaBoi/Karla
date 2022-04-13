from ast import Eq
import os
import platform
import json
import subprocess

from cheese.resourceManager import ResMan
from cheese.Logger import Logger

from python.commands.tools.stringer import Stringer

class Session:

    def __init__(self):
        self.fazeCount = 0
        self.faze = 0
        self.index = 0
        self.command = {}

    def createSession(self, text):
        commands = self.loadCommands()

        for command in commands:
            starter = Stringer.starts(text, command["starters"])
            if (starter):
                
                textArray = text.split(" ")
                fullText = " ".join([starter, command["ending"]]).strip()
                if (len(textArray) == len(fullText.split(" "))):
                    self.command = command
                    self.fazeCount = command["fazes"]
                    newText = text.replace(starter, "").replace(command["ending"].replace("&", "").strip(), "").strip()
                    if (not newText):
                        return "data"
                    return newText
        return False

    def loadCommands(self):
        with open(os.path.join(ResMan.resources(), "commands.json"), "r") as f:
            return json.loads(f.read())["COMMANDS"]

    def doCommand(self, text):
        python = "python"
        if (platform.system() != "Windows"):
            python = "python3"

        command = f"{python} \"{os.path.join(ResMan.pythonSrc(), 'commands', self.command['name'])}.py\" --faze {self.faze} --data \"{text}\""
        Logger.info(command, silence=False)
        p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
        resp, err = p.communicate()

        if (not resp.decode("utf-8").startswith("&")):
            self.faze += 1
        
        return resp.decode("utf-8")

    def isDone(self):
        return self.fazeCount >= self.faze
