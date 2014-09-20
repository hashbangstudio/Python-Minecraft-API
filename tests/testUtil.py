import unittest
from util import *

class TestUtil(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testFlatten(self):
        input = [0,1,2,[3,4,[5,6]]]
        expectedOutput = [0,1,2,3,4,5,6]
        self.assertEqual(list(flatten(input)), expectedOutput)

    def testFlattenToString(self):
        input = [0,1,2 ,[3,4,[5,6]]]
        expectedOutput = "0,1,2,3,4,5,6"
        self.assertEqual(flatten_parameters_to_string(input), expectedOutput)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestUtil)
    unittest.TextTestRunner(verbosity=2).run(suite)