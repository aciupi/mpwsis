from network_objects import Network
from SNDlib_parser import SNDlibParser
import numpy as np


def count_distance(node1, node2):
    distance = np.arccos((np.sin(node1['x']) * np.sin(node2['y'])) + (
    np.cos(node1['x']) * np.cos(node2['x']) * np.cos(np.abs(node1['y'] - node2['y']))))
    return distance * 111.195


def count_cost(distance):
    return 2 * pow(distance, 4)


if __name__ == '__main__':
    network = Network()
    SNDlibParser("sndlib_network.xml").parse_to_object(network)
    print network.get_node_coordinates('Bydgoszcz')
    print network.get_target('Link_0_5')
    dist = count_distance(network.get_node_coordinates('Rzeszow'), network.get_node_coordinates('Krakow'))
