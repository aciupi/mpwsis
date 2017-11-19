from network_objects import Network
from SNDlib_parser import SNDlibParser
from collections import defaultdict

# if __name__ == '__main__':
#     network = Network()
#     SNDlibParser("sndlib_network.xml").parse_to_object(network)
#     # network.count_flow_values()
#     network.fill_link_index_pair()
#     network.get_neighbours()
#     network.count_flow_values_and_cost()
#     # print network.nodes[0].get_description()
#     # print network.nodes[1].get_description()
#     #for node in network.nodes:
#     #    print node.get_description()
#     #print network.demands
#     #print network.link_distance
#     #print network.link_cost
#         # network.calculate_paths()
#         # print network.paths[5,3]
#
#
#
#         # print network.flow_values
#         # print network.links[0].index_pair
#         # print len(network.calculate_paths())
#         # print network.get_node_coordinates('Bydgoszcz')
#         # print network.get_target('Link_0_5')
#         # dist = count_distance(network.get_node_coordinates('Rzeszow'), network.get_node_coordinates('Krakow'))
#         # print network.get_node_coordinates('Bydgoszcz')
#         # print network.get_target('Link_0_5')
#         # dist = count_distance(network.get_node_coordinates('Rzeszow'), network.get_node_coordinates('Krakow'))
#
#
#     # Step 1: Distribution of network traffic
#     network.distribute_traffic()
#     #for key, value in network.link_cost.iteritems():
#     #    print key[0], key[1],value
#
#     #network.count_existing_link_cost()
#     for i in network.links:
#         print (i.source, i.target, i.cost)





#===========================================================================================

from collections import defaultdict
from heapq import *

class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}

    def add_node(self, value):
        self.nodes.add(value)

    def add_edge(self, from_node, to_node, distance):
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.distances[(from_node, to_node)] = distance
        self.distances[(to_node, from_node)] = distance


def dijkstra(graph, initial):
    visited = {initial: 0}
    path = defaultdict(list)

    nodes = set(graph.nodes)

    while nodes:
        min_node = None
        for node in nodes:
            if node in visited:
                if min_node is None:
                    min_node = node
                elif visited[node] < visited[min_node]:
                    min_node = node

        if min_node is None:
            break

        nodes.remove(min_node)
        current_weight = visited[min_node]

        for edge in graph.edges[min_node]:
            weight = current_weight + graph.distances[(min_node, edge)]
            if edge not in visited or weight < visited[edge]:
                visited[edge] = weight
                path[edge] = min_node

    return path,visited

if __name__ == '__main__':

    g = Graph()
    g.add_node('a')
    g.add_node('b')
    g.add_node('c')
    g.add_node('d')

    g.add_edge('a', 'b', 10)
    g.add_edge('b', 'c', 10)
    g.add_edge('a', 'c', 15)
    g.add_edge('c', 'd', 20)

    print(dijkstra(g, 'd'))
    #print(dijkstra(g, 'A')['B'])
    #dijkstra(g,'A')
    # g = Graph()
    #
    # g.add_node('A')
    # g.add_node('B')
    # g.add_node('C')
    # g.add_node('D')
    # g.add_node('E')
    # g.add_node('F')
    # g.add_node('G')
    #
    # g.add_edge('A', 'B', 12)
    # g.add_edge('A', 'C', 7)
    # g.add_edge('B', 'D', 1)
    # g.add_edge('B', 'A', 12)
    # g.add_edge('D', 'E', 8)
    # g.add_edge('C', 'F', 3)
    # g.add_edge('D', 'G', 5)
    # g.add_edge('F', 'B', 1)
    # g.add_edge('F', 'G', 2)
    # g.add_edge('C', 'D', 13)
    # g.add_edge('E', 'B', 6)
    #
    # print(dijkstra(g, 'A'))
