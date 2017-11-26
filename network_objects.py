import numpy as np
from collections import defaultdict
from heapq import *
# from priodict import priorityDictionary

class Node(object):
    def __init__(self, index, id, coordinates):
        self.index = index
        self.id = id
        self.coordinates = coordinates
        self.neighbours = []
        self.shortest_paths = {}

    def get_description(self):
        return [self.index, self.id, self.coordinates, self.neighbours]


class Link(object):
    def __init__(self, id, source, target, capacity):
        self.id = id
        self.source = source
        self.target = target
        self.index_pair = []
        self.setup_cost = None
        self.capacity = capacity
        self.cost = None
        self.used_capacity = 0

    def get_description(self):
        return [self.id, self.source, self.target, self.setup_cost, self.capacity]


class Demand(object):
    def __init__(self, id, source, target, demand_value):
        self.id = id
        self.source = source
        self.target = target
        self.demand_value = demand_value
        #self.admissible_paths = admissible_paths  # [{'path_id': [link.id, link.id ...]}, ... ]

    def get_description(self):
        return [self.id, self.source, self.target, self.demand_value]


class Network(object):
    def __init__(self):
        self.nodes = []
        self.links = []
        self.demands = []
        self.link_distance = {}
        self.link_cost = {}
        self.paths = {}

    def get_neighbours(self):
        for node in self.nodes:
            for link in self.links:
                if node.index in link.index_pair:
                    node.neighbours.append(self.get_node_by_index(link.index_pair[0])) if link.index_pair.index(
                        node.index) == 1 else node.neighbours.append(self.get_node_by_index(link.index_pair[1]))

    def count_distance(self, node1, node2):
        distance = np.arccos((np.sin(node1.coordinates['x']) * np.sin(node2.coordinates['y'])) + (
            np.cos(node1.coordinates['x']) * np.cos(node2.coordinates['x']) * np.cos(
                np.abs(node1.coordinates['y'] - node2.coordinates['y']))))
        return np.around(distance * 111.195, 4)

    def count_cost(self, distance):
        return np.around(2 * pow(distance, 4), 2)

    def count_flow_values_and_cost(self):
        for node1 in self.nodes:
            for node2 in self.nodes:
                # self.demands[self.nodes.index(node1), self.nodes.index(node2)] = 10 * abs(
                #     self.nodes.index(node1) - self.nodes.index(node2))
                distance = self.count_distance(node1, node2)
                self.link_distance[self.nodes.index(node1), self.nodes.index(node2)] = distance
                self.link_cost[self.nodes.index(node1), self.nodes.index(node2)] = 1000 * (
                    self.count_cost(distance / 100))

    def fill_link_index_pair(self):
        for link in self.links:
            link.index_pair = [self.get_object_by_id(link.source).index, self.get_object_by_id(link.target).index]

    def is_connected(self, index1, index2):
        for link in self.links:
            if link.index_pair == [index1, index2] or link.index_pair == [index2, index1]: return True
        return False

    def get_nodes(self):
        return [node.get_description() for node in self.nodes]

    def get_links(self):
        return [link.get_description() for link in self.links]

    def get_demands(self):
        return [demand.get_description() for demand in self.demands]

    def get_node_by_index(self, index):
        return [node for node in self.nodes if node.index == index][0]

    def get_object_by_id(self, id):
        if id.startswith('Link_'):
            return [link for link in self.links if link.id == id][0]
        elif id.startswith('Demand_'):
            return [demand for demand in self.demands if demand.id == id][0]
        else:
            return [node for node in self.nodes if node.id == id][0]

    def get_link_by_source(self, source):
        return [link for link in self.links if link.source == source]

    def get_link_by_target(self, target):
        return [link for link in self.links if link.target == target]

    def get_demand_by_source(self, source):
        return [demand for demand in self.demands if demand.source == source]

    def get_demand_by_target(self, target):
        return [demand for demand in self.demands if demand.target == target]

    def get_node_coordinates(self, id):
        return self.get_object_by_id(id).coordinates

    def get_source(self, id):
        return self.get_object_by_id(id).source

    def get_target(self, id):
        return self.get_object_by_id(id).target

    def get_node_by_name(self, name):
        for node in self.nodes:
            if node.id == name:
                return node

    def count_existing_link_cost(self):
        for link in self.links:
            link.cost = abs((self.get_node_by_name(link.source).index - self.get_node_by_name(link.target).index)) * 10


    #KROK 1 ALGORYTMU - ROZLOZENIE RUCHU
    def distribute_traffic(self):
        self.find_the_shortest_paths()

    def find_the_shortest_paths(self):
        for node in self.nodes:
            node.shortest_paths = self.dijkstra(self.nodes, node.id)

    def dijkstra(self, nodes_list, initial):
        visited = {initial: 0}
        path = defaultdict(list)

        nodes = set(nodes_list)

        while nodes:
            min_node = None

            for node in nodes:
                if node.id in visited:
                    if min_node is None:
                        min_node = node
                    elif visited[node.id] < visited[min_node.id]:
                        min_node = node

            if min_node is None:
                break

            nodes.remove(min_node)
            current_weight = visited[min_node.id]

            for neighbour in self.get_node_by_name(min_node.id).neighbours:
                # weight=current_weight+abs((self.get_node_by_name(min_node.id).index-/
                #                           self.get_node_by_name(neighbour.id).index)) * 10
                weight=current_weight+1
                if neighbour.id not in visited or weight < visited[neighbour.id]:
                    visited[neighbour.id] = weight
                    for each in path[min_node.id]:
                        path[neighbour.id].append(each)
                    path[neighbour.id].append(min_node.id)
        return path



