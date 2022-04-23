import timeit

import matplotlib.pyplot as plt
import networkx as nx

from vertex_covering_approximations import Algorithm
from vertex_covering_approximations.visualization import visualization
from . import logger


def greedy_2_approx(dataset_path, visualize=False, plot_path=None):
    """Compute greedy () approximation solution for the graph covering problem.

    :param dataset_path: path to the file containing the graph description (in the form of an edge list)
    :param visualize: visualize the solution or not
    :param plot_path: path to directory in which to save the visualization plots
    :return: set of vertices constituting the approximate solution for the graph covering problem and the running time (in seconds)
    """

    start_time = timeit.default_timer()

    # set of covering nodes
    node_set = set()

    # also construct NetworkX Graph (for visualization)
    nx_graph = nx.Graph()
    with open(dataset_path, 'r') as f:
        n_nodes = int(f.readline().strip())
        n_edges = int(f.readline().strip())

        logger.info('Using greedy (2) approximation algorithm for the graph covering problem for a graph specified in \'{0}\' with {1} nodes and {2} edges.'.format(dataset_path, n_nodes, n_edges))

        # go over edges and add adjacent nodes if edge not covered
        for edge_raw in f:
            edge_nxt = tuple(map(int, edge_raw.strip().split(' ')))
            nx_graph.add_edge(edge_nxt[0], edge_nxt[1])
            if edge_nxt[0] not in node_set and edge_nxt[1] not in node_set:
                node_set.update(edge_nxt)

    running_time = timeit.default_timer() - start_time

    if visualize:
        visualization.visualize_covering(node_set, nx_graph, plot_path, Algorithm.NAIVE_APPROX.value[0], dataset_path)

    return node_set, running_time


def visualize_covering(covering_set, nx_graph):
    """Visualize computed graph covering

    :param covering_set: set of nodes constituting the covering
    :param nx_graph: NetworkX Graph instance representing the graph
    """

    nx.draw(nx_graph, node_color=['green' if node in covering_set else 'blue' for node in nx_graph.nodes()])
    plt.savefig('./res3.png')
