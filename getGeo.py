from github import Github
from dotenv import load_dotenv, find_dotenv
import os
import pdb
from pprint import pprint
import csv
import googlemaps
import re

load_dotenv(find_dotenv())
GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")

gmaps = googlemaps.Client(key=GOOGLE_API_KEY)

f = open('stargazers.csv', 'r')

reader = csv.reader(f)
header = next(reader)
for row in reader:
  if row[1] is not '':
    print(row)
    geocode_result = gmaps.geocode(re.sub(r' |,', '+', row[1]))
    if len(geocode_result) > 0:
      location = geocode_result[0]['formatted_address']
      print(location)
      file = open('countries.csv', 'a')
      writer = csv.writer(file, lineterminator='\n')
      csvlist = []
      csvlist.append(re.sub(r'^.*, ', '', location))
      writer.writerow(csvlist)
      file.close()

f.close()
