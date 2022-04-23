import timeit

import networkx as nx

from vertex_cover_approximations import Algorithm
from vertex_cover_approximations.visualization import visualization
from . import logger


def greedy_logn_approx(dataset_path, visualize=False, plot_path=None):
    """Compute greedy (logn) approximation solution for the vertex cover problem.

    :param dataset_path: path to the file containing the graph description (in the form of an edge list)
    :param visualize: visualize the solution or not
    :param plot_path: path to directory in which to save the visualization plots
    :return: set of vertices constituting the approximate solution for the vertex cover problem and the running time (in seconds)
    """

    start_time = timeit.default_timer()

    # adjacency dictionary, edge list, set of covered edges, set of cover nodes
    adj_dict = dict()
    edge_list = []
    covered = set()
    node_set = set()

    # also construct NetworkX Graph (for visualization)
    nx_graph = nx.Graph()
    with open(dataset_path, 'r') as f:
        n_nodes = int(f.readline().strip())
        n_edges = int(f.readline().strip())

        logger.info('Using greedy (logn) approximation algorithm for the vertex cover problem for a graph specified in \'{0}\' with {1} nodes and {2} edges.'.format(dataset_path, n_nodes, n_edges))

        # construct edge list and adjacency dictionary
        for edge_raw in f:
            edge_nxt = tuple(map(int, edge_raw.strip().split(' ')))
            nx_graph.add_edge(edge_nxt[0], edge_nxt[1])
            edge_list.append(edge_nxt)
            adj_dict.setdefault(edge_nxt[0], set()).add(edge_nxt[1])
            adj_dict.setdefault(edge_nxt[1], set()).add(edge_nxt[0])

        # add nodes that have the maximum number of uncovered edges next to them to the cover set until all edges covered
        while len(covered) < len(edge_list):
            node_max_uncovered = get_node_max_uncovered(adj_dict, covered)

            covered.update({(node_max_uncovered, neigh) for neigh in adj_dict[node_max_uncovered]
                            if (node_max_uncovered, neigh) not in covered
                            and (neigh, node_max_uncovered) not in covered})

            adj_dict.pop(node_max_uncovered)
            node_set.add(node_max_uncovered)

        running_time = timeit.default_timer() - start_time

        if visualize:
            visualization.visualize_cover(node_set, nx_graph, plot_path, Algorithm.GREEDY_LOGN_APPROX.value[0], dataset_path)

        return node_set, running_time


def get_node_max_uncovered(adj_dict: dict, covered: set):
    """Get node that has the maximum number of uncovered edges adjacent to it.

    :param adj_dict: adjacency dictionary mapping nodes to the set of their neighbors
    :param covered: set of covered edges
    :return: node that has the maximum number of uncovered edges adjacent to it
    """
    max_uncovered = 0
    node_max_uncovered = None

    for adj_dict_item in adj_dict.items():
        uncovered_count = 0
        for neigh in adj_dict_item[1]:
            if (adj_dict_item[0], neigh) not in covered and (neigh, adj_dict_item[0]) not in covered:
                uncovered_count += 1

        if uncovered_count > max_uncovered:
            max_uncovered = uncovered_count
            node_max_uncovered = adj_dict_item[0]

    return node_max_uncovered
