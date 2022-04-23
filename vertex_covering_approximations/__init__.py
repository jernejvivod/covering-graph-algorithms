import logging
from enum import Enum

# module logger

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class Algorithm(Enum):
    EXACT = ('exact', 'Exact Algorithm')
    NAIVE_APPROX = ('naive_approx', 'Naive Approximation Algorithm')
    GREEDY_LOGN_APPROX = ('greedy_logn_approx', 'Greedy logn-Approximation Algorithm')
    GREEDY_2_APPROX = ('greedy_2_approx', 'Greedy 2-Approximation Algorithm')


class RunMode(Enum):
    SPECIFIC = 'specific'
    ALL = 'all'
