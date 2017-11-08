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