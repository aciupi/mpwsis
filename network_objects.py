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
        self.demands = {}
        # self.flow_values = {}
        self.paths = {}

        # Logika algorytmy poprawna, ale dzialania na typie Network mmaja rozny wymiar -> musimy wyluskac odpowiednie dane
        # i wpisac je w miejsca kosztu postawienia sciezki

    def dijkstra(self, initial, node1, node2):
        visited = {initial: 0}
        nodes = [node1, node2]
        path = {}

        # nodes powinno przyjmowac nazwy nodow czyli np nazwe miasta

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
            # current_weight = visited(min_node)

            # wyliczanie kosztu w tej chwili jest statyczne -> zachodzi tylko dla 2 wybranych nodow. Trzeba uogolnic tak, zeby
            # kalkulacje odnosily sie do wszystkich linkow. Tu cos nie bangla :(
            edges = self.links
            for edge in edges:
                weight = count_cost(count_distance(node1, node2))

            if edge not in visited or weight < visited[edge]:
                visited[edge] = weight
            path[edge] = min_node

        return visited, path

    def calculate_paths(self):
        print "FLOW VALUES: " + str(self.demands)
        for demand in self.demands:
            print "flow" + str(demand)
            print "capacity: " + str(self.is_enough_capacity(demand[0], demand[1]))
            while self.paths[demand] is None:
                if self.is_connected(demand[0], demand[1]):         # jesli nody bezposrednio polaczone, to wez ta sciezke
                    self.paths[demand] = [demand[0], demand[1]]
                    print "PATHS I: " + str(self.paths[demand])
                    print "KONIEC: " + str(demand)
                else:                                               # jesli nie sa bezposrednio polaczone, to sprawdz, czy sasiedzi maja bezposredni dostep do celu
                    self.seek_another_connection(demand, [])
                    # neighbours = self.get_neighbour(demand[0])
                    # for neighbour in neighbours:
                    #     print neighbour, demand[1]
                    #     if self.is_connected(neighbour, demand[1]):
                    #         self.paths[demand] = [demand[0], neighbour, demand[1]]  # jesli sasiad ma polaczenie z celem to pusc ruch sciezka zrodlo-sasiad-cel
                    #         print "PATHS II: " + str(self.paths)
                    #     else:
                    #         print "BREAK"
                    #         for b in neighbours:
                    #             x = self.get_neighbour(b)
                    #             for i in x:
                    #                 print "I: "
                    #                 str(i), " X: "
                    #                 str(x)
                    #                 if self.is_connected(i, demand[1]):
                    #                     self.paths[demand] = [demand[0], b, i, demand[1]]
                    #                     print "PATHS III: " + str(self.paths)
                    #                 else:
                    #                     print "DUPA"
                    #                     self.paths[demand] = 'unconnected'
                    #                     # self.paths[flow] = 'unconnected'
                    #                     # self.seek_another_connection(flow, neighbours)

    def seek_another_connection(self, demand, points):
        print points
        while self.paths[demand] is None:
            if len(points) is not 0:
                neighbours = self.get_neighbour(points[-1])
            else:
                neighbours = self.get_neighbour(demand[0])
            for neighbour in neighbours:
                if self.is_connected(neighbour, demand[1]):
                    self.paths[demand] = [demand[0], points, neighbour, demand[1]]
                    print "FOUND PATH: " + str(self.paths[demand])
                    break
            else:
                for neighbour in neighbours:
                    if neighbour not in points:
                        points.append(neighbour)
                        print "NEW POINTS: " + str(points)
                        self.seek_another_connection(demand, points)
                        break
        print "KONIEC: " + str(demand)

    def get_neighbour(self, number):
        print "START"
        neighbour = []
        # return [link.index_pair for link in self.links if number in link.index_pair]
        for link in self.links:
            if number in link.index_pair:
                # print number, link.index_pair, link.index_pair.index(number)
                neighbour.append(link.index_pair[0]) if link.index_pair.index(number) == 1 else neighbour.append(
                    link.index_pair[1])
        print "NEIGHBOUR: " + str(neighbour) + " for " + str(number)
        return neighbour

    def calculate_demands(self):
        for node1 in self.nodes:
            for node2 in self.nodes:
                self.demands[self.nodes.index(node1), self.nodes.index(node2)] = 10 * abs(
                    self.nodes.index(node1) - self.nodes.index(node2))
                self.paths[self.nodes.index(node1), self.nodes.index(node2)] = None

    def fill_link_index_pair(self):
        for link in self.links:
            link.index_pair = [self.get_object_by_id(link.source).index, self.get_object_by_id(link.target).index]

    def is_enough_capacity(self, index1, index2):
        for link in self.links:
            # print link.additional_modules[0]
            # return True
            if link.additional_modules[0]['capacity'] > self.demands[index1, index2]: return True
        return False

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
