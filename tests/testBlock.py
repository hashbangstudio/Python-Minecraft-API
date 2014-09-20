import unittest
from block import *

class TestBlock(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testRepresentation(self):
        # Test repr
        b = Block(2,8)
        expectedString = "Block(%d, %d)"%(b.id,b.data)
        rep = repr(b)
        self.assertEqual(rep, expectedString)

    def testInstantiationAndWithDataFunction(self):
        blck = Block(12)
        self.assertEqual(blck.id, 12)
        self.assertEqual(blck.data, 0)
        blckWithData = Block(12, 4)
        self.assertEqual(blckWithData.id, 12)
        self.assertEqual(blckWithData.data, 4)
        otherBlckWithData = blck.withData(8)
        self.assertEqual(otherBlckWithData.id, 12)
        self.assertEqual(otherBlckWithData.data, 8)

    def testComparison(self):
        b1 = Block(8,3)
        bSame = Block(8,3)
        bDiffId = Block(12,3)
        bDiffData = Block(8,7)
        bDiffIdAndData = Block(51,7)

        self.assertTrue(b1 == b1)
        self.assertTrue(b1 == bSame)
        self.assertTrue(b1 != bDiffId)
        self.assertTrue(b1 != bDiffData)
        self.assertTrue(b1 != bDiffIdAndData)

    def testIteration(self):
        idAndData = [35,4]
        b = Block(idAndData[0], idAndData[1])
        v =  list(b.__iter__())
        self.assertEqual(v, idAndData)

    def testBlockConstants(self):
        self.assertEqual(AIR  ,  Block(0))
        self.assertEqual(STONE,  Block(1))
        self.assertEqual(GRASS,  Block(2))
        self.assertEqual(DIRT ,  Block(3))
        self.assertEqual(COBBLESTONE   ,  Block(4))
        self.assertEqual(WOOD_PLANKS   ,  Block(5))
        self.assertEqual(SAPLING   ,  Block(6))
        self.assertEqual(BEDROCK   ,  Block(7))
        self.assertEqual(WATER_FLOWING ,  Block(8))
        self.assertEqual(WATER,  WATER_FLOWING)
        self.assertEqual(WATER_STATIONARY  , Block(9))
        self.assertEqual(LAVA_FLOWING  ,  Block(10))
        self.assertEqual(LAVA ,  LAVA_FLOWING)
        self.assertEqual(LAVA_STATIONARY , Block(11))
        self.assertEqual(SAND ,  Block(12))
        self.assertEqual(GRAVEL    ,  Block(13))
        self.assertEqual(GOLD_ORE  ,  Block(14))
        self.assertEqual(IRON_ORE  ,  Block(15))
        self.assertEqual(COAL_ORE  ,  Block(16))
        self.assertEqual(WOOD ,  Block(17))
        self.assertEqual(LEAVES    ,  Block(18))
        self.assertEqual(GLASS,  Block(20))
        self.assertEqual(LAPIS_LAZULI_ORE    , Block(21))
        self.assertEqual(LAPIS_LAZULI_BLOCK  , Block(22))
        self.assertEqual(SANDSTONE ,  Block(24))
        self.assertEqual(BED  ,  Block(26))
        self.assertEqual(COBWEB    ,  Block(30))
        self.assertEqual(GRASS_TALL,  Block(31))
        self.assertEqual(WOOL ,  Block(35))
        self.assertEqual(FLOWER_YELLOW ,  Block(37))
        self.assertEqual(FLOWER_CYAN   ,  Block(38))
        self.assertEqual(MUSHROOM_BROWN,  Block(39))
        self.assertEqual(MUSHROOM_RED  ,  Block(40))
        self.assertEqual(GOLD_BLOCK,  Block(41))
        self.assertEqual(IRON_BLOCK,  Block(42))
        self.assertEqual(STONE_SLAB_DOUBLE   , Block(43))
        self.assertEqual(STONE_SLAB,  Block(44))
        self.assertEqual(BRICK_BLOCK   ,  Block(45))
        self.assertEqual(TNT  ,  Block(46))
        self.assertEqual(BOOKSHELF ,  Block(47))
        self.assertEqual(MOSS_STONE,  Block(48))
        self.assertEqual(OBSIDIAN  ,  Block(49))
        self.assertEqual(TORCH,  Block(50))
        self.assertEqual(FIRE ,  Block(51))
        self.assertEqual(STAIRS_WOOD   ,  Block(53))
        self.assertEqual(CHEST,  Block(54))
        self.assertEqual(DIAMOND_ORE   ,  Block(56))
        self.assertEqual(DIAMOND_BLOCK ,  Block(57))
        self.assertEqual(CRAFTING_TABLE,  Block(58))
        self.assertEqual(FARMLAND  ,  Block(60))
        self.assertEqual(FURNACE_INACTIVE    , Block(61))
        self.assertEqual(FURNACE_ACTIVE,  Block(62))
        self.assertEqual(DOOR_WOOD ,  Block(64))
        self.assertEqual(LADDER    ,  Block(65))
        self.assertEqual(STAIRS_COBBLESTONE  , Block(67))
        self.assertEqual(DOOR_IRON ,  Block(71))
        self.assertEqual(REDSTONE_ORE  ,  Block(73))
        self.assertEqual(SNOW ,  Block(78))
        self.assertEqual(ICE  ,  Block(79))
        self.assertEqual(SNOW_BLOCK,  Block(80))
        self.assertEqual(CACTUS    ,  Block(81))
        self.assertEqual(CLAY ,  Block(82))
        self.assertEqual(SUGAR_CANE,  Block(83))
        self.assertEqual(FENCE,  Block(85))
        self.assertEqual(GLOWSTONE_BLOCK     , Block(89))
        self.assertEqual(BEDROCK_INVISIBLE   , Block(95))
        self.assertEqual(STONE_BRICK   ,  Block(98))
        self.assertEqual(GLASS_PANE,  Block(102))
        self.assertEqual(MELON,  Block(103))
        self.assertEqual(FENCE_GATE,  Block(107))
        self.assertEqual(GLOWING_OBSIDIAN    , Block(246))
        self.assertEqual(NETHER_REACTOR_CORE , Block(247))


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestBlock)
    unittest.TextTestRunner(verbosity=2).run(suite)
