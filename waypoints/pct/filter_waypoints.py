import sys
import json
from geojson import FeatureCollection

if (len(sys.argv) != 2):
    print("The script can only handle one geojson file at a time!")
    sys.exit(1)

fname = sys.argv[1]
print("Extracting Milemarkers from file: " + fname)

with open(fname, 'r') as fp:
    data = json.load(fp)

milemarkers = []
water_sources = []

for feature in data.get('features'):
    if feature.get('properties').get('sym') == 'Triangle, Red':
        milemarkers.append(feature)
    if feature.get('properties').get('sym') == 'Water Source':
        water_sources.append(feature)

mm = FeatureCollection(milemarkers)
ws = FeatureCollection(water_sources)

with open('milemarkers.geojson', 'w') as fp:
    json.dump(mm, fp)

with open('watersources.geojson', 'w') as fp:
    json.dump(ws, fp)
