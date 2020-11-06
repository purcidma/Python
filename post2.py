URL = "https://maps.googleapis.com/maps/api/geocode/json"
location = "Osmania University"
PARAMS = {'address':location}
 
response = requests.get(url = URL, params = PARAMS)
data = response.json()
 
latitude = data['results'][0]['geometry']['location']['lat']
longitude = data['results'][0]['geometry']['location']['lng']
formattedAddress = data['results'][0]['formatted_address']
 
print("Latitude : %snLongitude : %snAddress of the location : %s"
    %(latitude, longitude,formattedAddress))