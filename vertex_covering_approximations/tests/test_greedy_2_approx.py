import os
import unittest

from vertex_covering_approximations.algorithms.greedy_2_approx import greedy_2_approx


class TestGreedyApprox(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls._node_set = greedy_2_approx(os.path.join(os.path.dirname(__file__), '../../sample-data/small_01.graph'))

    def testSample1Len(self):
        self.assertEqual(len(self._node_set), 20)

    def testSample1Covering(self):
        self.assertEqual({0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 17, 20, 22, 23, 24}, self._node_set)
