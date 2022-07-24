#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

apiKey = "518877fa5da8c9993824911a1185bc60"
r = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q=Pilsen&units=metric&lang=en&appid={apiKey}")
data = r.json()

text = f"In {data['name']} is {data['weather'][0]['description']}\n"
text += f"Temperature is {data['main']['temp']}°C.\n"
text += f"But it feels like {data['main']['feels_like']}.\n"
text += f"Maximum temperature will be {data['main']['temp_max']}.\n"
text += f"And minimal will be {data['main']['temp_min']}.\n"
text += f"Atmospheric pressure is {data['main']['pressure']} kPa.\n"
text += f"And humidity is {data['main']['humidity']} %.\n"
print(text)