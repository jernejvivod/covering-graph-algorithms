import os
import unittest

from vertex_covering_approximations.algorithms.greedy_logn_approx import greedy_logn_approx


class TestGreedyApprox(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls._node_set = greedy_logn_approx(os.path.join(os.path.dirname(__file__), '../../sample-data/small_01.graph'))

    def testSample1Len(self):
        self.assertEqual(len(self._node_set), 14)

    def testSample1Covering(self):
        self.assertEqual({0, 2, 4, 7, 8, 9, 11, 12, 16, 17, 19, 20, 21, 22}, self._node_set)
