import re
import xml.etree.ElementTree as ET

from network_objects import Node, Link, Demand


class SNDlibParser(object):
    def __init__(self, source_path):
        self.network_xml = ET.parse(source_path)
        self.root = self.network_xml.getroot()
        self.namespace = self.parse_namespace(self.root)
        self.networkStructure = self.root.findall(self.namespace + 'networkStructure')[0]

    def parse_to_object(self, network):
        self.parse_nodes(self.networkStructure.findall(self.namespace + 'nodes')[0], network)
        self.parse_links(self.networkStructure.findall(self.namespace + 'links')[0], network)
        # self.parse_demands(self.root.findall(self.namespace + 'demands')[0], network)

    def parse_nodes(self, nodes, network):
        for node in self.parse_nodes_list(nodes):
            network.nodes.append(Node(self.parse_id(node), self.parse_coordinates(node)))

    def parse_links(self, links, network):
        for link in self.parse_links_list(links):
            network.links.append(
                Link(self.parse_id(link), self.parse_source(link), self.parse_target(link),
                     self.parse_setup_cost(link), self.parse_modules(link)))

    def parse_demands(self, demands, network):
        for demand in self.parse_demands_list(demands):
            network.demands.append(
                Demand(self.parse_id(demand), self.parse_source(demand), self.parse_target(demand),
                       self.parse_demand_value(demand),
                       self.parse_admissible_paths(demand)))

    def parse_namespace(self, root):
        namespace = re.match('\{.*\}', root.tag)
        return namespace.group(0) if namespace else ''

    def parse_coordinates(self, node):
        coordinates = node.find(self.namespace + 'coordinates')
        x = float(coordinates.find(self.namespace + 'x').text)
        y = float(coordinates.find(self.namespace + 'y').text)
        return {'x': x, 'y': y}

    def parse_id(self, node):
        return node.attrib['id']

    def parse_nodes_list(self, nodes):
        return nodes.findall(self.namespace + 'node')

    def parse_links_list(self, nodes):
        return nodes.findall(self.namespace + 'link')

    def parse_demands_list(self, nodes):
        return nodes.findall(self.namespace + 'demand')

    def parse_source(self, node):
        return node.find(self.namespace + 'source').text

    def parse_target(self, node):
        return node.find(self.namespace + 'target').text

    def parse_setup_cost(self, node):
        return node.find(self.namespace + 'setupCost').text

    def parse_modules(self, node):
        modules = []
        additional_modules = node.find(self.namespace + 'additionalModules')
        for module in additional_modules.findall(self.namespace + 'addModule'):
            capacity = module.find(self.namespace + 'capacity').text
            cost = module.find(self.namespace + 'cost').text
            modules.append({capacity: cost})
        return modules

    def parse_demand_value(self, node):
        return node.find(self.namespace + 'demandValue').text

    def parse_admissible_paths(self, node):
        paths = []
        admissible_paths = node.find(self.namespace + 'admissiblePaths')
        for path in admissible_paths.findall(self.namespace + 'admissiblePath'):
            id = self.parse_id(path)
            links = [linkId.text for linkId in path.findall(self.namespace + 'linkId')]
            paths.append({id: links})
        return paths
