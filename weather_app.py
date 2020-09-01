from tkinter import *
import requests
import json
from api_keys import weather_app_key

root = Tk()
root.title('Weather app')
root.geometry('600x50')

city = ''
quality = 0
category = ''

category_color = {'Good': '#00e400', 'Moderate': '#ffff00', 'Unhealthy for Sensitive Groups': '#ff7e00',
                  'Unhealthy': '#ff0000', 'Very Unhealthy': '#8f3f97', 'Hazardous': '#7e0023'}

try:
    api_request = requests.get('http://www.airnowapi.org/aq/observation/zipCode/current/'
                               '?format=application/json&zipCode=20002&distance=25&API_KEY=' + weather_app_key)
    api = json.loads(api_request.content)
    city = api[0]['ReportingArea']
    quality = api[0]['AQI']
    category = api[0]['Category']['Name']

    root.configure(background=category_color[category])
except Exception as e:
    api = 'Error'

label = Label(root, text=city + ' Air Quality: ' + str(quality) + ' ' + category, font=('Helvetica', 20),
              background=category_color[category])
label.pack()


root.mainloop()
