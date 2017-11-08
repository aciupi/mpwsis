class Node(object):
    def __init__(self, id, coordinates):
        self.id = id
        self.coordinates = coordinates


class Link(object):
    def __init__(self, id, source, target, setupCost, modules=None):
        self.id = id
        self.source = source
        self.target = target
        self.setupCost = setupCost
        self.additionalModules = modules  # [{'capacity': , 'cost': }, ... ]


class Demand(object):
    def __init__(self, id, source, target, demandValue, admissiblePaths=None):
        self.id = id
        self.source = source
        self.target = target
        self.demandValue = demandValue
        self.admissiblePaths = admissiblePaths  # [{'path_id': [link.id, link.id ...]}, ... ]


class Network(object):
    def __init__(self):
        self.nodes = []
        self.links = []
        self.demands = []

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
