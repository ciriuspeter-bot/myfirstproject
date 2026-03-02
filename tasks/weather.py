import requests

def get_weather():
    api_key = ""
    lat = 33.44
    lon = -94.04
    part = "current"
    url = f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude={part}&appid={api_key}"
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        temp = data['main']['temp']
        desc = data['weather'][0]['description']
        print(f"{city} 날씨: {desc}, {temp}°C")
    else:
        print("도시를 찾을수 없습니다")

city = input("도시이름: ")
get_weather()