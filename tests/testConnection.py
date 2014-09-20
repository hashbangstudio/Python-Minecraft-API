import unittest
from connection import *
from tests.MinecraftTCPServerStub import *
import subprocess

class TestConnection(unittest.TestCase):

    HOST = 'localhost'
    PORT = 4711
    process = ""

    @staticmethod
    def isInt(n):
        try:
            n = int(n)
        except ValueError:
            return False
        except TypeError:
            return False
        return True

    @classmethod
    def setUpClass(self):
        # Could have the test stub server running to test correct operation
        pass


    @classmethod
    def tearDownClass(self):
        # TODO would have to terminate stib server here
        pass

    def testInstantation(self):
        conn = Connection(TestConnection.HOST, TestConnection.PORT)

    def testSendAndReceive(self):
        conn = Connection(TestConnection.HOST, TestConnection.PORT)
        # TODO find a test with less dependecy on minecraft commands than this for connection test
        response = conn.sendReceive("world.getHeight", [8, 5])
        self.assertTrue(response != '')
        self.assertTrue(response.lstrip('-').isdigit())
        self.assertTrue(self.isInt(response))

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestConnection)
    unittest.TextTestRunner(verbosity=2).run(suite)