import itertools
import timeit

import networkx as nx

from vertex_covering_approximations import Algorithm
from vertex_covering_approximations.visualization import visualization
from . import logger


def exact(dataset_path, visualize=False, plot_path=None):
    """Compute exact solution for the graph covering problem by iterating over vertex subsets.

    :param dataset_path: path to the file containing the graph description (in the form of an edge list)
    :param visualize: visualize the solution or not
    :param plot_path: path to directory in which to save the visualization plots
    :return: set of vertices constituting the solution for the graph covering problem and the running time (in seconds)
    """

    start_time = timeit.default_timer()

    # edge list and set of unique nodes
    edge_list = []
    nodes = set()

    # also construct NetworkX Graph (for visualization)
    nx_graph = nx.Graph()
    with open(dataset_path, 'r') as f:
        n_nodes = int(f.readline().strip())
        n_edges = int(f.readline().strip())

        logger.info('Using exact algorithm for the graph covering problem for a graph specified in \'{0}\' with {1} nodes and {2} edges.'.format(dataset_path, n_nodes, n_edges))

        # construct edge list, get unique nodes and construct NetworkX Graph for visualization
        for edge_raw in f:
            edge_nxt = tuple(map(int, edge_raw.strip().split(' ')))
            nx_graph.add_edge(edge_nxt[0], edge_nxt[1])
            edge_list.append(edge_nxt)
            nodes.update(edge_nxt)

    # go over covering sizes
    for cov_size in range(1, n_nodes + 1):

        # generate subsets of nodes of specified size
        node_combs_nxt = itertools.combinations(nodes, cov_size)
        for nodes_nxt in node_combs_nxt:
            node_set_nxt = set(nodes_nxt)

            # check if nodes form a graph covering
            if check_covering(node_set_nxt, edge_list):
                running_time = timeit.default_timer() - start_time
                if visualize:
                    visualization.visualize_covering(node_set_nxt, nx_graph, plot_path, Algorithm.EXACT.value[0], dataset_path)
                return node_set_nxt, running_time


def check_covering(node_set, edge_list: list):
    """Check if set of nodes constitutes a graph covering.

    :param node_set: set of nodes to check
    :param edge_list: edge list describing the graph
    :return: does the set of nodes constitute a graph covering or not
    """

    for edge in edge_list:
        if edge[0] not in node_set and edge[1] not in node_set:
            return False
    return True
