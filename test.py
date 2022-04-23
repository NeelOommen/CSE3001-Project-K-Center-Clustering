import unittest
from loader import DataLoader
from distanceFunction import distance
import KCenter


class TestClustering(unittest.TestCase):
    def test_clustering_case1(self):
        loader = DataLoader()
        data = loader.getData("in.csv")
        clusterOutput = KCenter.cluster().kCenter(data,50)
        self.assertEqual(len(clusterOutput), 243)


    def test_clustering_case2(self):
        loader = DataLoader()
        data = loader.getData("in.csv")
        clusterOutput = KCenter.cluster().kCenter(data,100)
        self.assertEqual(len(clusterOutput), 132)


    def test_clustering_case3(self):
        loader = DataLoader()
        data = loader.getData("in.csv")
        clusterOutput = KCenter.cluster().kCenter(data,150)
        self.assertEqual(len(clusterOutput), 81)

    
    def test_clustering_case4(self):
        loader = DataLoader()
        data = loader.getData("in.csv")
        clusterOutput = KCenter.cluster().kCenter(data,200)
        self.assertEqual(len(clusterOutput), 59)

    
    def test_clustering_case5(self):
        loader = DataLoader()
        data = loader.getData("in.csv")
        clusterOutput = KCenter.cluster().kCenter(data,250)
        self.assertEqual(len(clusterOutput), 47)
    

    def test_distance_case1(self):
        self.assertEqual(round(distance(28.66,77.23,18.9667,72.8333),2), 1166.63)

    
    def test_distance_case2(self):
        self.assertEqual(round(distance(18.9667,72.8333,22.5411,88.3378),2), 1659.46)

    
    def test_distance_case3(self):
        self.assertEqual(round(distance(22.5411,88.3378,12.9699,77.598),2), 1556.24)
    

    def test_distance_case4(self):
        self.assertEqual(round(distance(12.9699,77.598,13.0825,80.275),2), 290.28)
    

    def test_distance_case5(self):
        self.assertEqual(round(distance(13.0825,80.275,17.3667,78.4667),2), 514.35)


if __name__ == '__main__':
    unittest.main()