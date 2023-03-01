import requests

# replace with your API key
API_KEY = 'ce5069b9f8ed64bdaef8e2bfa3aca7ac'

# replace with the name of the city you want to get weather information for
city = "Canberra"

# construct the URL for the API request
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"

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
    print(data["weather"][3])

    # print the weather information
    print(f"The weather in {city} is {description} with a temperature of {round(temperature - 273.15, 2)} Celsius, humidity of {humidity}%, and wind speed of {wind_speed} m/s.")
else:
    # print an error message if the request was not successful
    print("Error retrieving weather information.")
