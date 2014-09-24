import unittest
from vec3 import Vec3


class TestVec3(unittest.TestCase):
    """ Test the functions of the Vec3 class """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testInstantiation(self):
        v = Vec3(-1, 4, 6)
        expectedX = -1
        expectedY = 4
        expectedZ = 6
        self.assertEqual(v.x, expectedX, "Expected %d to be equal to %s but wasn't " %(v.x, expectedX))
        self.assertEqual(v.y, expectedY, "Expected %d to be equal to %s but wasn't " %(v.y, expectedY))
        self.assertEqual(v.z, expectedZ, "Expected %d to be equal to %s but wasn't " %(v.z, expectedZ))

    def testRepresentation(self):
        # Test repr
        v1 = Vec3(2, -3, 8)
        expectedString = "Vec3(%s,%s,%s)"%(v1.x,v1.y,v1.z)
        rep = repr(v1)
        self.assertEqual(rep, expectedString)

    def testIteration(self):
        coords = [1,9,6]
        v = Vec3(coords[0], coords[1], coords[2])
        li =  list(v.__iter__())
        self.assertEqual(li, coords)

    def testComparison(self):
        v1 = Vec3(2, -3, 8)
        vSame = Vec3(2, -3, 8)
        vDiff = Vec3(22, 63, 88)
        vXlarger = Vec3(5, -3, 8)
        vXsmaller = Vec3(0, -3, 8)
        vYlarger = Vec3(2, 9, 8)
        vYsmaller = Vec3(2, -10, 8)
        vZlarger = Vec3(2, -3, 12)
        vZsmaller = Vec3(2, -3, 4)

        self.assertTrue(v1 == vSame, "Expected %s to be equal to %s but wasn't " %(v1, vSame))
        self.assertFalse(v1 == vDiff, "Expected %s to be not be equal to %s but wasn't " %(v1, vDiff))
        self.assertTrue(v1 != vDiff, "Expected %s to be not equal to %s but wasn't " %(v1, vDiff))

        self.assertTrue(v1 < vXlarger, "Expected %s to be less than %s but wasn't " %(v1, vXlarger))
        self.assertTrue(v1 < vYlarger, "Expected %s to be less than %s but wasn't " %(v1, vYlarger))
        self.assertTrue(v1 < vZlarger, "Expected %s to be less than %s but wasn't " %(v1, vZlarger))

        self.assertTrue(v1 > vXsmaller, "Expected %s to be more than %s but wasn't " %(v1, vXsmaller))
        self.assertTrue(v1 > vYsmaller, "Expected %s to be more than %s but wasn't " %(v1, vXsmaller))
        self.assertTrue(v1 > vZsmaller, "Expected %s to be more than %s but wasn't " %(v1, vXsmaller))


    def testCloning(self):
        v = Vec3(2, -3, 8)
        vClone = v.clone()
        self.assertTrue(v == vClone)
        v.x += 1
        self.assertTrue(v != vClone)

    def testNegation(self):
        v1 = Vec3(2, -3, 8)
        vInverse = -v1
        self.assertEqual(v1.x, -vInverse.x)
        self.assertEqual(v1.y, -vInverse.y)
        self.assertEqual(v1.z, -vInverse.z)

    def testAddition(self):
        a = Vec3(10, -3, 4)
        b = Vec3(-7, 1, 2)
        c = a + b
        totV = Vec3(3, -2, 6)
        self.assertEqual(c, totV)
        d = c - b
        self.assertEqual(d, a)

    def testSubtraction(self):
        a = Vec3(10, -3, 4)
        b = Vec3(5, 3, 5)
        self.assertEqual((a - a), Vec3(0,0,0))
        self.assertEqual((a + (-a)) ,Vec3(0,0,0))
        self.assertEqual((a - b), Vec3(5,-6,-1))

    def testMultiplication(self):
        a = Vec3(2, -3, 8)
        self.assertEqual((a + a), (a * 2))
        k = 4
        a *= k
        self.assertEqual(a, Vec3(2*k, -3*k, 8*k))


    def testLength(self):
        v = Vec3(2, -3, 8)
        l = v.length
        ls = ((2*2) + (-3*-3) + (8*8))
        self.assertEqual(l, (ls ** 0.5))

    def testLengthSqr(self):
        v = Vec3(2, -3, 8)
        ls = v.lengthSqr
        self.assertEqual(ls, ((2*2) + (-3*-3) + (8*8)))

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestVec3)
    unittest.TextTestRunner(verbosity=2).run(suite)

