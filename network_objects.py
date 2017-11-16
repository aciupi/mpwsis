class Node(object):
    def __init__(self, index, id, coordinates):
        self.index = index
        self.id = id
        self.coordinates = coordinates

    def get_description(self):
        return [self.index, self.id, self.coordinates]


class Link(object):
    def __init__(self, id, source, target, setup_cost, modules=None):
        self.id = id
        self.source = source
        self.target = target
        self.index_pair = []
        self.setup_cost = setup_cost
        self.additional_modules = modules  # [{'capacity': , 'cost': }, ... ]

    def get_description(self):
        return [self.id, self.source, self.target, self.setup_cost, self.additional_modules]


class Demand(object):
    def __init__(self, id, source, target, demand_value, admissible_paths=None):
        self.id = id
        self.source = source
        self.target = target
        self.demand_value = demand_value
        self.admissible_paths = admissible_paths  # [{'path_id': [link.id, link.id ...]}, ... ]

    def get_description(self):
        return [self.id, self.source, self.target, self.demand_value, self.admissible_paths]


class Network(object):
    def __init__(self):
        self.nodes = []
        self.links = []
        # self.demands = []
        self.flow_values = {}
        self.paths = {}

    def calculate_paths(self):
        print "FLOW VALUES: " + str(self.flow_values)
        for flow in self.flow_values:
            print "FLOW" + str(flow)
            if self.is_connected(flow[0], flow[1]):
                self.paths[flow] = [flow[0], flow[1]]
                print "PATH: " + str(self.paths)
            else:
                neighbours = self.get_neighbour(flow[0])
                for neighbour in neighbours:
                    print neighbour, neighbours
                    if self.is_connected(neighbour, flow[1]):
                        self.paths[flow] = [flow[0], neighbour, flow[1]]
                        print "PATHS: " + str(self.paths)
                        break
                    else:
                        print "BREAK"
                        for b in neighbours:
                            x = self.get_neighbour(b)
                            for i in x:
                                print "I: " + str(i), " X: " + str(x)
                                if self.is_connected(i, flow[1]):
                                    self.paths[flow] = [flow[0], b, i, flow[1]]
                                    print "PATHS: " + str(self.paths)
                                    break
                                else:
                                    print "DUPA"
                                    self.paths[flow] = 'unconnected'
                        # self.paths[flow] = 'unconnected'
                        # self.seek_another_connection(flow, neighbours)

    def seek_another_connection(self, flow, points):
        if points:
            for point in points:
                neighbours = self.get_neighbour(point)
                for neighbour in neighbours:
                    if self.is_connected(neighbour, flow[1]):
                        print "HERE"
                        self.paths[flow].append([point, neighbour, flow[1]])
                        print "PATHS II: " + str(self.paths)
                        break
                    else:
                        self.paths[flow] = 'unconnected'


    def get_neighbour(self, number):
        print "START"
        neighbour = []
        # return [link.index_pair for link in self.links if number in link.index_pair]
        for link in self.links:
            if number in link.index_pair:
                # print number, link.index_pair, link.index_pair.index(number)
                neighbour.append(link.index_pair[0]) if link.index_pair.index(number) == 1 else neighbour.append(link.index_pair[1])
        print "NEIGHBOUR: " + str(neighbour) + " for " + str(number)
        return neighbour

    def count_flow_values(self):
        for node1 in self.nodes:
            for node2 in self.nodes:
                self.flow_values[self.nodes.index(node1), self.nodes.index(node2)] = 10 * abs(
                    self.nodes.index(node1) - self.nodes.index(node2))

    def fill_link_index_pair(self):
        for link in self.links:
            link.index_pair = [self.get_object_by_id(link.source).index, self.get_object_by_id(link.target).index]

    def is_connected(self, index1, index2):
        for link in self.links:
            if link.index_pair == [index1, index2] or link.index_pair == [index2, index1]: return True
        return False
        # return True if self.get_link_by_source(node1.id) == self.get_link_by_target(node2.id) or self.get_link_by_source(
        #     node1.id) == self.get_link_by_target(node2.id) else False

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
