import os
import unittest

from vertex_covering_approximations.algorithms.exact import exact


class TestExact(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls._node_set = exact(os.path.join(os.path.dirname(__file__), '../../sample-data/small_01.graph'))

    def testSample1Len(self):
        self.assertEqual(len(self._node_set), 13)

    def testSample1Covering(self):
        self.assertEqual({2, 4, 7, 8, 9, 11, 12, 16, 17, 19, 20, 21, 22}, self._node_set)
