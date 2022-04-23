import csv
from city import City

class DataLoader:
    def getData(self, path):
        data_file = open(path)
        csvreader = csv.reader(data_file)
        data = []
        for row in csvreader:
            data.append(City(name = row[0], latitude = float(row[1]), longitude = float(row[2])))
        data_file.close()
        return data
