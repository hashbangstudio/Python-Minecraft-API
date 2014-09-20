import unittest
from minecraft import *

class TestMinecraft(unittest.TestCase):

    HOST = 'localhost'
    PORT = 4711
    conn = ""

    @classmethod
    def setUpClass(self):
        TestMinecraft.conn = Connection(TestMinecraft.HOST, TestMinecraft.PORT)

    @classmethod
    def tearDownClass(self):
        pass

    @staticmethod
    def isFloat(n):
        try:
            n = float(n)
        except ValueError:
            return False
        except TypeError:
            return False
        return True

    @staticmethod
    def isInt(n):
        try:
            n = int(n)
        except ValueError:
            return False
        except TypeError:
            return False
        return True

    def testIntFloor(self):
        arr = intFloor([1.2,[3.6, -6.7], -9.3])
        self.assertEqual(arr, [1,3,-7,-10])

    def testWorldGetHeight(self):
        response = TestMinecraft.conn.sendReceive("world.getHeight", [8,5])
        self.assertTrue(response != '')
        self.assertTrue(response.lstrip('-').isdigit())
        self.assertTrue(self.isInt(response))

    def testWorldGetBlock(self):
        response = TestMinecraft.conn.sendReceive("world.getBlock", [8, 10, 5])
        self.assertTrue(response != '')
        self.assertTrue(response.isdigit())

    def testWorldGetBlockWithData(self):
        response = TestMinecraft.conn.sendReceive("world.getBlockWithData", [8, 10, 5])
        self.assertTrue(response != '')
        data = response.split(',')
        self.assertTrue(len(data) == 2)
        for val in data:
            self.assertTrue(val.isdigit())
            self.assertTrue(self.isInt(val))

#    def testWorldGetBlocks(self):
#        response = TestMinecraft.conn.sendReceive("world.getBlocks", [8, 10, 5, 4, 2, 1])
#        print response
#        self.assertTrue(response != '')
#        self.assertTrue(response.isdigit())

    def testWorldGetPlayerEntityIds(self):
        response = TestMinecraft.conn.sendReceive("world.getPlayerIds", [])
        self.assertTrue(response != '')
        data = response.split("|")
        for val in data:
            self.assertTrue(val.isdigit())
            self.assertTrue(self.isInt(val))

    def testEventsPollBlockHits(self):
        response = TestMinecraft.conn.sendReceive("events.block.hits", [])
        self.assertTrue(response != '')
        data = response.split("|")
        for evnt in data:
            elements = evnt.split(',')
            for val in elements:
                self.assertTrue(val.lstrip('-').isdigit())
                self.assertTrue(self.isInt(val))


    def testPlayerGetTile(self):
        response = TestMinecraft.conn.sendReceive("player.getTile", [])
        self.assertTrue(response != '')
        data = response.split(',')
        self.assertTrue(len(data) == 3)
        for val in data:
            self.assertTrue(val.lstrip('-').isdigit())
            self.assertTrue(self.isInt(val))

    def testPlayerGetPos(self):
        response = TestMinecraft.conn.sendReceive("player.getPos", [])
        self.assertTrue(response != '')
        data = response.split(',')
        self.assertTrue(len(data) == 3)
        for val in data:
            self.assertTrue(self.isFloat(val))




if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestMinecraft)
    unittest.TextTestRunner(verbosity=2).run(suite)