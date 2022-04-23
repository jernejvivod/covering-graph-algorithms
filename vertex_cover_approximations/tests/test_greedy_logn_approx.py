import os
import unittest

from vertex_cover_approximations.algorithms.greedy_logn_approx import greedy_logn_approx


class TestGreedyApprox(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls._node_set, _ = greedy_logn_approx(os.path.join(os.path.dirname(__file__), '../../sample-data/small_01.graph'))

    def testSample1Len(self):
        self.assertEqual(len(self._node_set), 14)

    def testSample1Cover(self):
        self.assertEqual({0, 2, 4, 7, 8, 9, 11, 12, 16, 17, 19, 20, 21, 22}, self._node_set)
