# Team Graphhopper Integration
# Members: Christian Nenaria, Tristan Belarma, Jomar Diaz
# Description: Uses GraphHopper API to get coordinates from a location input

import requests

API_KEY = '2abfb176-6a6a-4108-8008-5fc63a0b8114'

def geocode_address(address):
    url = f"https://graphhopper.com/api/1/geocode?q={address}&key={API_KEY}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if data['hits']:
            location = data['hits'][0]
            print(f"Location: {location['name']}, {location['country']}")
            print(f"Coordinates: Lat {location['point']['lat']}, Lon {location['point']['lng']}")
        else:
            print("No results found.")
    else:
        print("Error in API request.")

if __name__ == "__main__":
    user_input = input("Enter a location: ")
    geocode_address(user_input)
