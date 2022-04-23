import math

def distance(lat1, long1, lat2, long2):
        ### lat1,long1,lat2,long2
        #convert latitude and longitude to distance in km
        lat1radians = math.radians(lat1)
        long1radians = math.radians(long1)
        
        lat2radians = math.radians(lat2)
        long2radians = math.radians(long2)

        dlat = lat2radians - lat1radians
        dlon = long2radians - long1radians

        a = math.sin(dlat / 2)**2 + math.cos(lat1radians) * math.cos(lat2radians) * math.sin(dlon / 2)**2

        c = 2 * math.asin(math.sqrt(a))

        #radius of earth in kilometers
        radiusOfEarth = 6371

        return(c * radiusOfEarth)