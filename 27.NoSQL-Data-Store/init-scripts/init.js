db = db.getSiblingDB('nosql_db');

db.createCollection('toilets');

// Load initial mock data
var mockData = [
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
                "accessible": true,
                "baby_change": true,
                "drinking_water": false,
                "sharps_disposal": true
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
                "accessible": true,
                "baby_change": true,
                "drinking_water": true,
                "sharps_disposal": false
            },
            "opening_hours": "06:00 - 23:00",
            "maintained_by": "City of Melbourne"
        }
    }
];

db.toilets.insertMany(mockData);

// Create geospatial index for faster queries on geometry
db.toilets.createIndex({ "geometry": "2dsphere" });
