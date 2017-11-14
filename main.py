from network_objects import Network
from SNDlib_parser import SNDlibParser
import numpy as np


def count_distance(node1, node2):
    distance = np.arccos((np.sin(node1['x']) * np.sin(node2['y'])) + (
    np.cos(node1['x']) * np.cos(node2['x']) * np.cos(np.abs(node1['y'] - node2['y']))))
    return distance * 111.195


def count_cost(distance):
    return 2 * pow(distance, 4)


#Logika algorytmy poprawna, ale dzialania na typie Network mmaja rozny wymiar -> musimy wyluskac odpowiednie dane
#i wpisac je w miejsca kosztu postawienia sciezki
def dijkstra(initial, node1, node2):
    visited = {initial: 0}
    nodes = network.get_nodes()
    path = {}

#nodes powinno przyjmowac nazwy nodow czyli np nazwe miasta
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
        #current_weight = visited(min_node)

#wyliczanie kosztu w tej chwili jest statyczne -> zachodzi tylko dla 2 wybranych nodow. Trzeba uogolnic tak, zeby
#kalkulacje odnosily sie do wszystkich linkow. Tu cos nie bangla :(
        edges = network.get_links()
        for edge in edges:
            weight = count_cost(count_distance(node1, node2))
            if edge not in visited or weight < visited[edge]:
                visited[edge] = weight
                path[edge] = min_node

    return visited, path

if __name__ == '__main__':
    network = Network()
    SNDlibParser("sndlib_network.xml").parse_to_object(network)
    #print network.get_node_coordinates('Bydgoszcz')
    #print network.get_target('Link_0_5')
    #dist = count_distance(network.get_node_coordinates('Rzeszow'), network.get_node_coordinates('Krakow'))
    print (dijkstra('Rzeszow',network.get_node_coordinates('Rzeszow'), network.get_node_coordinates('Krakow')))
