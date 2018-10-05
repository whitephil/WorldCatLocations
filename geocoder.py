import requests
import json
import pandas as pd
import csv
from time import sleep

# the url for the mapquest api. This would also work with osm nominatim or other apis
url = 'http://www.mapquestapi.com/geocoding/v1/address?'

# the api key + the beginning of the location query
keyLoc = '[your API key goes here]&location='

# imports the input csv into a pandas dataframe, csv should have "Address" as header and full addresses in each row
data = pd.read_csv('your input csv goes here')

# creates a list from Address field from the input csv
addList = list(data['Address'].values)


with open('Name of your output CSV goes here', 'a', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    for address in addList:
        sleep(1.5)
        query = url + keyLoc + address
        response = requests.get(query)
        jsonContents = json.loads(response.content.decode('utf-8'))
        if len(jsonContents['results'])>0:
            writer.writerow([address,
                        jsonContents['results'][0]['locations'][0]['latLng']['lat'],
                        jsonContents['results'][0]['locations'][0]['latLng']['lng'],
                        jsonContents['results'][0]['locations'][0]['geocodeQualityCode'],
                        jsonContents['results'][0]['locations'][0]['geocodeQuality'],
                        query])
        else: writer.writerow(['No Data'])

''' 
The loop above creates a new output csv, 
iterates through list of addresses building a new query for each, 
sends a query every 1.5 seconds, 
parses json response, 
writes address, lat, long, quality codes, and query url into rows of the output csv
appends new row to output csv for each response
if the response contains no data, writes "no data" into first cell of row
'''
