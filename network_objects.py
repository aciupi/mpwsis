class Node(object):
    def __init__(self, id, coordinates):
        self.id = id
        self.coordinates = coordinates

    def get_description(self):
        return [self.id, self.coordinates]


class Link(object):
    def __init__(self, id, source, target, setup_cost, modules=None):
        self.id = id
        self.source = source
        self.target = target
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
        #self.demands = []

    def get_nodes(self):
        return [node.get_description() for node in self.nodes]

    def get_links(self):
        return [link.get_description() for link in self.links]

    def get_demands(self):
        return [demand.get_description() for demand in self.demands]

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
