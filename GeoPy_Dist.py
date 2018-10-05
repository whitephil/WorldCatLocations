from geopy.distance import geodesic
import pandas as pd

Home = (40.005956, -105.26552) #Home location from which distance from each set of coordinates in input spreadsheet will be calculated.

df = pd.read_csv('FILE PATH TO INPUT CSV') #CSV with coordinate data. xy column should be formatted as such: (40.005956, -105.26552)

df['distFromHome'] = df.apply((lambda row: geodesic(Home, row['yx']).miles), axis = 1) #calculates distance from home location to each pair of coordinates and inputs to new column.

df.to_csv('PATH TO NEW OUTPUT CSV') #writes table with new column to CSV
