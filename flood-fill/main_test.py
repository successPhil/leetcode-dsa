import unittest
from main import hello_world, floodFill

class TestFloodFill(unittest.TestCase):

    def test_hello_world(self):
        self.assertEqual(hello_world(), "Hello World!")
    
    def test_example1(self):
        self.assertEqual(floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2), [[2,2,2],[2,2,0],[2,0,1]])

    def test_example2(self):
        self.assertEqual(floodFill([[0,0,0],[0,0,0]], 0, 0, 0 ), [[0,0,0],[0,0,0]])












if __name__ == '__main__':
    unittest.main()