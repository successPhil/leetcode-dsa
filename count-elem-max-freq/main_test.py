import unittest

from main import countElementsMaxFrequency


class TestCountElementsMaxFrequency(unittest.TestCase):

    def test_example1(self):
        self.assertEqual(countElementsMaxFrequency([1,2,2,3,1,4]), 4)

    def test_exampe2(self):
        self.assertEqual(countElementsMaxFrequency([1,2,3,4,5]), 5)



if __name__ == '__main__':
    unittest.main()