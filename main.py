from tkinter import *
from PIL import ImageTk, Image
import requests
import country_converter as coco
import geocoder

cc = coco.CountryConverter()

is_searched = False
city = ''
to = 'name_short'

# replace with your API key
API_KEY = 'ce5069b9f8ed64bdaef8e2bfa3aca7ac'


def GetInfo():
  city = search_track.get()
  url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"

  g = geocoder.bing(city, key="AiVu8eZxmJe9taO2_axmK5nSEZQkqqlNBqeMaQgxLs9V84KZUpSzsAyIrknNvNZ0 ")
  results = g.json
  print(results['lat'], results["lng"])
  print(results['lat']/90, results["lng"]/180)

  
  # send a GET request to the API and store the response
  response = requests.get(url)

  # check if the request was successful
  if response.status_code == 200:
    # convert the response to a JSON object
    data = response.json()

    # extract the relevant weather information from the JSON object
    description = data["weather"][0]["description"]
    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    wind_speed = data["wind"]["speed"]
    country = coco.convert(names=data["sys"]["country"], to=to)

    # print the weather information
    print(
      f"The weather in {city} ({country}) is {description} with a temperature of {round(temperature - 273.15, 2)} Celsius, humidity of {humidity}%, and wind speed of {round(wind_speed * 3.6, 2)} km/h."
    )
  else:
    # print an error message if the request was not successful
    print("Error retrieving weather information.")


# Setup the Window
window = Tk()
window.geometry('1024x576')
frame = Frame(window, width=1024, height=576)
frame.pack()
frame.place(anchor='center', relx=0.5, rely=0.5)

mapframe = Frame(window, width=200, height=200)
mapframe.pack()
mapframe.place(anchor='center', relx=0.9, rely=0.85)

# Create an object of tkinter ImageTk
img = ImageTk.PhotoImage(Image.open("WeatherDEV.jpg"))

Mapimg = ImageTk.PhotoImage(Image.open("mapa.jpg"))

# Create a Label Widget to display the text or Image
label = Label(frame, image=img)
label.pack()
Mapalabel = Label(mapframe, image=Mapimg)
Mapalabel.pack()

search_track = Entry(window)
search_track.place(anchor='center', relx=0.5, rely=0.45, width=300)

search_btn = Button(text='Search', command=GetInfo)
search_btn.place(anchor='center', relx=0.5, rely=0.5)

window.mainloop()