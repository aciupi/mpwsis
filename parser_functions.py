import re
from network_objects import Node, Link, Demand


def parse_to_object(root, network):
    namespace = parse_namespace(root)
    networkStructure = root.findall(namespace + 'networkStructure')[0]
    parse_nodes(networkStructure.findall(namespace + 'nodes')[0], network, namespace)
    parse_links(networkStructure.findall(namespace + 'links')[0], network, namespace)
    parse_demands(root.findall(namespace + 'demands')[0], network, namespace)


def parse_nodes(nodes, network, namespace):
    for node in parse_nodes_list(nodes, namespace):
        network.nodes.append(Node(parse_id(node), parse_coordinates(node, namespace)))


def parse_links(links, network, namespace):
    for link in parse_links_list(links, namespace):
        network.links.append(
            Link(parse_id(link), parse_source(link, namespace), parse_target(link, namespace),
                 parse_setup_cost(link, namespace), parse_modules(link, namespace)))


def parse_demands(demands, network, namespace):
    for demand in parse_demands_list(demands, namespace):
        network.demands.append(
            Demand(parse_id(demand), parse_source(demand, namespace), parse_target(demand, namespace),
                   parse_demand_value(demand, namespace),
                   parse_admissible_paths(demand, namespace)))


def parse_namespace(root):
    namespace = re.match('\{.*\}', root.tag)
    return namespace.group(0) if namespace else ''


def parse_coordinates(node, namespace):
    coordinates = node.find(namespace + 'coordinates')
    x = coordinates.find(namespace + 'x').text
    y = coordinates.find(namespace + 'y').text
    return [x, y]


def parse_id(node):
    return node.attrib['id']


def parse_nodes_list(nodes, namespace):
    return nodes.findall(namespace + 'node')


def parse_links_list(nodes, namespace):
    return nodes.findall(namespace + 'link')


def parse_demands_list(nodes, namespace):
    return nodes.findall(namespace + 'demand')


def parse_source(node, namespace):
    return node.find(namespace + 'source').text


def parse_target(node, namespace):
    return node.find(namespace + 'target').text


def parse_setup_cost(node, namespace):
    return node.find(namespace + 'setupCost').text


def parse_modules(node, namespace):
    modules = []
    additionalModules = node.find(namespace + 'additionalModules')
    for module in additionalModules.findall(namespace + 'addModule'):
        capacity = module.find(namespace + 'capacity').text
        cost = module.find(namespace + 'cost').text
        modules.append({capacity: cost})
    return modules


def parse_demand_value(node, namespace):
    return node.find(namespace + 'demandValue').text


def parse_admissible_paths(node, namespace):
    paths = []
    admissible_paths = node.find(namespace + 'admissiblePaths')
    for path in admissible_paths.findall(namespace + 'admissiblePath'):
        id = parse_id(path)
        links = [linkId.text for linkId in path.findall(namespace + 'linkId')]
        paths.append({id: links})
    return paths
