import requests
import urllib.parse as urlparse
import datetime

# Route parameters
start = "37.77493,-122.419415"               # San Francisco
end = "34.052234,-118.243685"                # Los Angeles
routeType = "fastest"                        # Fastest route
traffic = "true"                             # To include Traffic information
travelMode = "truck"                         # Travel by truck
avoid = "unpavedRoads"                       # Avoid unpaved roads
departAt = "2021-10-20T10:00:00"             # Departure date and time
key = "<TYPE_YOUR_API_KEY_HERE>"             # API Key
 

def getEta(departureTime):
    # Building the request URL
    baseUrl = "https://api.tomtom.com/routing/1/calculateRoute/";

    requestParams = (
        urlparse.quote(start) + ":" + urlparse.quote(end) 
        + "/json?routeType=" + routeType
        + "&traffic=" + traffic
        + "&travelMode=" + travelMode
        + "&avoid=" + avoid 
        + "&departAt=" + urlparse.quote(departureTime))

    requestUrl = baseUrl + requestParams + "&key=" + key

    # Sending the request
    response = requests.get(requestUrl)

    if(response.status_code == 200):
        # Get response's JSON
        jsonResult = response.json()

        # Read summary of the first route
        routeSummary = jsonResult['routes'][0]['summary'];
        
        # Read ETA
        eta = routeSummary['arrivalTime']

        # Read travel time and convert it to hours
        travelTime = routeSummary['travelTimeInSeconds'] / 3600
        
        # Print results
        print(f"Depart at: {departureTime},\tETA: {eta},\tTravel time: {travelTime:.2f}h")

# Departure times
departureTimeStart = datetime.datetime(2021, 10, 20, 0, 0, 0)

for i in range(0,23):
    # Update an hour
    departureTime = departureTimeStart.replace(hour=departureTimeStart.hour + i)

    # Format datetime string
    departureTime = departureTime.strftime('%Y-%m-%dT%H:%M:%S')

    # Get ETA
    getEta(departureTime)    