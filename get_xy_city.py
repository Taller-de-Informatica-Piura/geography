import urllib.request
import urllib.parse
import json

city = input("Enter a city name: ")

# Prepare URL
base_url = "https://nominatim.openstreetmap.org/search"
params = {
    "q": city,
    "format": "json"
}

url = base_url + "?" + urllib.parse.urlencode(params)

# Add a user-agent header (important!)
request = urllib.request.Request(
    url,
    headers={"User-Agent": "thonny-school-project"}
)

# Send request and read response
with urllib.request.urlopen(request) as response:
    data = json.loads(response.read().decode())

# Show result
if len(data) > 0:
    print("City found!")
    print("Latitude:", data[0]["lat"])
    print("Longitude:", data[0]["lon"])
else:
    print("City not found.")
