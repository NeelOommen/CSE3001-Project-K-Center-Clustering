import unittest
from loader import DataLoader
import KCenter


class TestClustering(unittest.TestCase):
    def test_case1(self):
        loader = DataLoader()
        data = loader.getData("in.csv")
        clusterOutput = KCenter.cluster().kCenter(data,50)
        self.assertEqual(len(clusterOutput), 243)


    def test_case2(self):
        loader = DataLoader()
        data = loader.getData("in.csv")
        clusterOutput = KCenter.cluster().kCenter(data,100)
        self.assertEqual(len(clusterOutput), 132)


    def test_case3(self):
        loader = DataLoader()
        data = loader.getData("in.csv")
        clusterOutput = KCenter.cluster().kCenter(data,150)
        self.assertEqual(len(clusterOutput), 81)

    
    def test_case4(self):
        loader = DataLoader()
        data = loader.getData("in.csv")
        clusterOutput = KCenter.cluster().kCenter(data,200)
        self.assertEqual(len(clusterOutput), 59)



if __name__ == '__main__':
    unittest.main()