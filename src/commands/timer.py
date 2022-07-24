#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json
from datetime import datetime, timedelta

from Cheese.appSettings import Settings

from tools.arguments import Arguments

args = Arguments()
args.getArguments()

request = {
    "END_TIME": datetime.now() + timedelta(minutes=int(args.data)),
    "REPEAT": -1,
    "DESCRIPTION": f"TIMER for {args.data} minutes is done crcrcr"
}

r = requests.post(f"http://localhost:{Settings.port}/notifications/create", data=json.dumps(request, indent=4, sort_keys=True, default=str))
if (r.status_code == 200):
    print(f"setting timer for {int(args.data)} minutes")
else:
    print("something went wrong. Timer was not set")