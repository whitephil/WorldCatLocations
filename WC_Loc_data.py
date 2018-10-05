import requests
from time import sleep
import xml.etree.cElementTree as et
import csv
import pandas as pd

# oclcNumber = ['93', '966034982', '966041949', '822695808']
url = 'http://www.worldcat.org/webservices/catalog/content/libraries/' #URL of library locations API
qParams = '?location=80309&maximumLibraries=50&' #query parameters. see also api documentation to modify
key = 'wskey=[YOUR KEY GOES HERE]'

data = pd.read_csv('yourInputCSV.csv') #input CSV should have one column containing OCLC numbers in single quotes. Header column should be labeled Number.

numberList = list(data['Number'].values)

count = 0

with open('yourOutputCSV.csv', 'a', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['OCLCnumber', 'Location', 'Address'])
    for n in numberList:
        count += 1
        query = url+n+qParams+key
        sleep(0.6)
        if count % 400 == 0:
            sleep(60)
        response = requests.get(query)
        root = et.fromstring(response.content)
        holdings = root.findall('holding')
        for item in holdings:
            writer.writerow([n, item.find('physicalLocation').text, item.findall('physicalAddress')[0].find('text').text])

'''
-The loop above assembles the each query string and sends each query to the API every .6 seconds
-0.6 second delay between is out of politeness to OCLC APIs: follow their terms of service and do not query too fast and too long or you will get booted
-Every 400 querys the program takes a 1 minute break between queries. This is to be nice and not overload OCLC's servers
-Each response is read as xml and physical location and address fields are written to a new output csv, alongwith the original query
-Before using this script, you should understand how APIs work, polite use of APIs, how the Python Requests library works, and how to parse XML data.
'''
