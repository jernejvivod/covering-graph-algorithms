import os
import pathlib

import matplotlib.pyplot as plt
import networkx as nx

from . import logger


def visualize_cover(cover_set, nx_graph, plot_path, algorithm_name, dataset_path):
    """Visualize computed vertex cover.

    :param cover_set: set of nodes constituting the cover
    :param nx_graph: NetworkX Graph instance representing the graph
    :param plot_path: path to directory in which to save the visualization plots
    :param algorithm_name: name of algorithm used to compute the cover
    :param dataset_path: dataset path supplied to the algorithm used to compute the cover
    """

    logger.info('Creating visualization for {0} applied to graph specified in \'{1}\'.'.format(algorithm_name, dataset_path))

    pos = nx.spring_layout(nx_graph)
    nx.draw_networkx_nodes(nx_graph, pos=pos, nodelist=[node for node in nx_graph.nodes() if node in cover_set], node_color='green', label='selected')
    nx.draw_networkx_nodes(nx_graph, pos=pos, nodelist=[node for node in nx_graph.nodes() if node not in cover_set], node_color='blue')
    nx.draw_networkx_edges(nx_graph, pos=pos)

    plt.legend(scatterpoints=1)
    plt.savefig(os.path.join(plot_path, '{0}_{1}.svg').format(pathlib.Path(dataset_path).stem, algorithm_name))
