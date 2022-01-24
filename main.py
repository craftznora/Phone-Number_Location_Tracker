import phonenumbers
from phonenumbers import geocoder
from opencage.geocoder import OpenCageGeocode
from phonenumbers import carrier
import folium

Key = 'Enter your OpenCage API key' # Sign up from the website https://opencagedata.com/ and take the geocoding API key and type here.

number = "Enter your country code and phone number here" # Example: +1-202-555-0125 https://countrycode.org/ get your country code here.

samNumber = phonenumbers.parse(number)
YourLocation = geocoder.description_for_number(samNumber, "en")
print(YourLocation)

service_provider = phonenumbers.parse(number)
print(carrier.name_for_number(service_provider, "en"))

geocoder = OpenCageGeocode(Key)
query = str(YourLocation)
results = geocoder.geocode(query)
# print(results)

lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']
print(lat, lng)

myMap = folium.Map(Location=[lat, lng], zoom_start=9)
folium.Marker([lat, lng], popup=YourLocation).add_to(myMap)

myMap.save("myMap.html")
