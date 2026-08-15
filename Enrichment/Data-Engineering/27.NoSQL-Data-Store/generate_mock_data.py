import json

# Generate mock data replicating complex nested GeoJSON structures
toilets = [
    {
        "type": "Feature",
        "geometry": {
            "type": "Point",
            "coordinates": [151.2093, -33.8688]
        },
        "properties": {
            "name": "Sydney Town Hall Public Toilets",
            "address": "483 George St, Sydney NSW 2000",
            "features": {
                "accessible": True,
                "baby_change": True,
                "drinking_water": False,
                "sharps_disposal": True
            },
            "opening_hours": "24/7",
            "maintained_by": "City of Sydney"
        }
    },
    {
        "type": "Feature",
        "geometry": {
            "type": "Point",
            "coordinates": [144.9631, -37.8136]
        },
        "properties": {
            "name": "Federation Square Toilets",
            "address": "Swanston St & Flinders St, Melbourne VIC 3000",
            "features": {
                "accessible": True,
                "baby_change": True,
                "drinking_water": True,
                "sharps_disposal": False
            },
            "opening_hours": "06:00 - 23:00",
            "maintained_by": "City of Melbourne"
        }
    },
    {
        "type": "Feature",
        "geometry": {
            "type": "Point",
            "coordinates": [153.0251, -27.4698]
        },
        "properties": {
            "name": "Brisbane City Botanic Gardens",
            "address": "Alice St, Brisbane City QLD 4000",
            "features": {
                "accessible": False,
                "baby_change": False,
                "drinking_water": True,
                "sharps_disposal": False
            },
            "opening_hours": "Daylight hours",
            "maintained_by": "Brisbane City Council"
        }
    }
]

with open('data/mock_toilets.json', 'w') as f:
    json.dump(toilets, f, indent=2)

print("Mock JSON data generated at data/mock_toilets.json")
