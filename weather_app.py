from tkinter import *
import requests
import json
from keys_and_passwords import weather_app_key


root = Tk()
root.title('Weather app')
root.geometry('600x100')

zip_entry = Entry(root)
zip_entry.grid(row=0, column=0, padx=(5, 0))

result_label = Label(root, font=('Helvetica', 15))
result_label.grid(row=1, column=0, columnspan=2, padx=(5, 0))


def zip_lookup():
    category_color = {'Good': '#00e400', 'Moderate': '#ffff00', 'Unhealthy for Sensitive Groups': '#ff7e00',
                      'Unhealthy': '#ff0000', 'Very Unhealthy': '#8f3f97', 'Hazardous': '#7e0023',
                      'Error': '#ffffff'}
    zip_code = zip_entry.get()

    try:
        api_request = requests.get(f'http://www.airnowapi.org/aq/observation/zipCode/current/'
                                   f'?format=application/json&zipCode={zip_code}&distance=25&API_KEY={weather_app_key}')
        api = json.loads(api_request.content)
        city = api[0]['ReportingArea']
        quality = api[0]['AQI']
        category = api[0]['Category']['Name']

        # set label text
        result_label['text'] = city + ' Air Quality: ' + str(quality) + ' ' + category

        # set label and root bg color
        result_label['background'] = category_color[category]
        root.configure(background=category_color[category])
    except Exception as e:
        result_label['text'] = 'Sorry, an error has occurred.'
        result_label['background'] = category_color['Error']
        root.configure(background=category_color['Error'])
    finally:
        zip_entry.delete(0, END)


zip_button = Button(root, text='Lookup zipcode', command=zip_lookup)
zip_button.grid(row=0, column=1, padx=(5, 0), pady=(5, 0))


root.mainloop()
