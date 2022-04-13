import os
import platform
import json
import subprocess

from cheese.resourceManager import ResMan

class Session:

    def __init__(self):
        self.fazeCount = 0
        self.faze = 0
        self.index = 0
        self.command = {}

    def createSession(self, text):
        commands = self.loadCommands()

        for command in commands:
            for starter in command["starters"]:
                if (text.startswith(starter)):
                    textArray = text.split(" ")
                    if (len(textArray) == len(starter.split(" ")) + len(command["ending"].split(" ")) + 1):
                        self.command = command
                        self.fazeCount = command["fazes"]
                        return text.replace(starter, "").replace(command["ending"], "").strip()
        return False

    def loadCommands(self):
        with open(os.path.join(ResMan.resources(), "commands.json"), "r") as f:
            return json.loads(f.read())["COMMANDS"]

    def doCommand(self, text):
        python = "python"
        if (platform.system() != "Windows"):
            python = "python3"

        command = f"{python} \"{os.path.join(ResMan.pythonSrc(), 'commands', self.command['name'])}.py\" --faze {self.faze} --data \"{text}\""
        print(command)
        p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
        resp, err = p.communicate()

        if (not resp.decode("utf-8").startswith("&")):
            self.faze += 1
        
        return resp

    def isDone(self):
        return self.fazeCount > self.faze
