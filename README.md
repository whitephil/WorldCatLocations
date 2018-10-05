# WorldCatLocations
Scripts used for a project using the WorldCat Search API Library Locations parameter. Other scripts for geocoding location data and calculating each distances between CU Boulder and all other libraries in dataset.

## Project Summary
The project looked examined location data from the WorldCat Search API to assess uniqueness and geographic distance of donated library materials. You will need a key to the WorldCat Search API (a developer key if you want to query more than times 100 in one day. 

We used 3 Python scripts:

### WC_Loc_data.py
This script builds a location query for the WorldCat Search API using OCLC numbers. To use this script, you should start with a CSV containing the OCLC numbers of all of the items you wish to query, formatted as such:

  Number
  
  
  '10223520'
  
  
  '10271962'
  
  
  '10401184'
  
  
  '1055546'
  
  
  '10605866'

The script will read this csv, build the query strings, and send each query one at a time at 0.6 second intervals. The script reads all of the XML response data and parses physical library locations (i.e., name of the library) and their addresses into columns of a new output csv. When finished, the parsed data will be saved to the output csv. If you run lots of queries, the script will pause every 400th query for 60 seconds, then resume. This is to avoid triggering a network alert on OCLC's servers. Sending requests over and over again for a long time has the appearance of a DOS attack. Be nice if you're going to use OCLC's APIs!!

### geocoder.py

This is a simple geocoding script. Geocoding is a process that assigns latitude and longitude coordinates to address data. This script makes use of the MapQuest geocoding API. You'll need all of your input addresses in a CSV file formatted as such:

  Address

  Boulder, CO 80309 United States

  Denver, CO 80204 United States

  Denver, CO 80208 United States

  Greeley, CO 80639 United States

  Chadron, NE 69337 United States

The more complete the address is, the more accurate your coordinate data will be (full street number would be best). The script assembles the query strings, sends each one to the MapQuest API in 1.5 second intervals, and parses the json response data into a new output csv.

### GeoPy_Dist.py

This script uses the GeoPy Python library to calculate geodesic distances between coordinates. You'll need an input CSV with a column formatted as follows:

yx

(40.005956, -105.26552)

(39.7345, -105.020783)

(39.7345, -105.020783)

(39.719483, -104.944353)

(40.40598, -104.697597)

You will also need to adjust the Home variable to the coordinate pair you wish to calculate distances from (i.e., the starting point). The script creates a new column with the results and writes the full table to a new CSV output file. Works fast!

### Required Python Libraries
requests

json

xml

pandas

csv

geopy

time

### Documentation
[WorldCat Search API](https://platform.worldcat.org/api-explorer/apis/wcapi) 

[MapQuest Geocoding API](https://developer.mapquest.com/documentation/geocoding-api/)

[GeoPy](https://geopy.readthedocs.io/en/stable/)

### End
See comments in scripts for more information. Contact [Phil White](mailto:philip.white@colorado.edu) with questions 
