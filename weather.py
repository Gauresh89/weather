import requests


apikey="d2e207874e50efb18764a0d5de197d54"
baseURL="https://api.openweathermap.org/data/2.5/weather?q="
cityName= input("Enter city name : ")
completeURL=baseURL+cityName+"&appid="+apikey
response= requests.get(completeURL).json()
#data=response.json()
# print(response)
print("current Tem",response["main"]["temp"])
print("current Tem feels like",response["main"]["feels_like"])
print("maximum Tem",response["main"]["temp_max"])
print("minimum Tem",response["main"]["temp_min"])
print("description",response["weather"][0]["description"])
print("pressure",response["main"]["pressure"])
print("humidity",response["main"]["humidity"])