from city import City
from distanceFunction import distance

class cluster:
    
    def kCenter(self, cityList, operatingDistance):
        centers = []
        clusters = {}
        while len(cityList)>0:
            cent = cityList[0]
            cluster = [cent]
            centers.append(cityList[0])
            cityList.remove(cityList[0])
            for city in cityList:
                if distance(lat1 = cent.lat, long1 = cent.long, lat2 = city.lat, long2 = city.long) <= operatingDistance:
                    cluster.append(city)
                    cityList.remove(city)
            clusters[cent] = cluster
        return(clusters)
            
