# Team Graphhopper Integration
# Members: Christian Nenaria, Tristan Belarma, Jomar Diaz
# Description: Uses GraphHopper API to get coordinates from a location input

import requests

API_KEY = '2abfb176-6a6a-4108-8008-5fc63a0b8114'

# Function to save search history to a text file
def save_search_history(query, result):
    with open('search_history.txt', 'a') as file:
        file.write(f"Query: {query}\nResult: {result}\n\n")

# Function to geocode the address using GraphHopper API
def geocode_address(address):
    url = f"https://graphhopper.com/api/1/geocode?q={address}&key={API_KEY}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors (4xx, 5xx)

        if response.status_code == 200:
            data = response.json()
            if data['hits']:
                location = data['hits'][0]
                result = f"Location: {location['name']}, {location['country']}\nCoordinates: Lat {location['point']['lat']}, Lon {location['point']['lng']}"
                print(result)
                save_search_history(address, result)  # Save search history to the file
            else:
                print("No results found.")
                save_search_history(address, "No results found.")
        else:
            print("Error in API request.")
            save_search_history(address, "Error in API request.")

    except requests.exceptions.RequestException as e:
        # This will handle any error related to the request, including no internet or invalid requests
        print(f"Error: {e}")
        save_search_history(address, f"Error: {e}")  # Log the error message to the history file

# Main loop to ask the user for input
if __name__ == "__main__":
    while True:
        user_input = input("Enter a location (or type 'exit' to quit): ")
        if user_input.lower() == 'exit':
            print("Exiting the program.")
            break
        else:
            geocode_address(user_input)
