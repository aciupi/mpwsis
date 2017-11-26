from network_objects import Network
from SNDlib_parser import SNDlibParser
from collections import defaultdict

if __name__ == '__main__':
    network = Network()
    SNDlibParser("sndlib_network.xml").parse_to_object(network)
    # network.count_flow_values()
    network.fill_link_index_pair()
    network.get_neighbours()
    network.count_flow_values_and_cost()
    # print network.nodes[0].get_description()
    # print network.nodes[1].get_description()
    #for node in network.nodes:
    #    print node.get_description()
    #print network.demands
    #print network.link_distance
    #print network.link_cost
        # network.calculate_paths()
        # print network.paths[5,3]



        # print network.flow_values
        # print network.links[0].index_pair
        # print len(network.calculate_paths())
        # print network.get_node_coordinates('Bydgoszcz')
        # print network.get_target('Link_0_5')
        # dist = count_distance(network.get_node_coordinates('Rzeszow'), network.get_node_coordinates('Krakow'))
        # print network.get_node_coordinates('Bydgoszcz')
        # print network.get_target('Link_0_5')
        # dist = count_distance(network.get_node_coordinates('Rzeszow'), network.get_node_coordinates('Krakow'))


    # Step 1: Distribution of network traffic
    network.distribute_traffic()
    #for key, value in network.link_cost.iteritems():
    #    print key[0], key[1],value
    # for node in network.nodes:
    #     print node.id, node.shortest_paths
    print network.demands