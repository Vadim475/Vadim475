import requests 



def get_address_from_coordinates(coordinates, api_key):
    base_url = "https://maps.googleapis.com/maps/api/geocode/json"
    
    params = {
        "latlng": coordinates,
        "key": api_key
    }
     
    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        if data["status"] == "OK":
            address = data["results"][0]["formatted_address"]
            return address
        else:
            return "No results ."
    else:
        return f"Error: {response.status_code}"


coordinates = '50.479945,30.489993'
api_key = '*************'  
address = get_address_from_coordinates(coordinates, api_key)

print(address)