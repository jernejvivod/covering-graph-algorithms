import os
import unittest

from vertex_cover_approximations.algorithms.naive_approx import naive_approx


class TestGreedyApprox(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls._node_set, _ = naive_approx(os.path.join(os.path.dirname(__file__), '../../sample-data/small_01.graph'))

    def testSample1Len(self):
        self.assertEqual(len(self._node_set), 17)

    def testSample1Cover(self):
        self.assertEqual({0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 15, 17, 19, 22}, self._node_set)
