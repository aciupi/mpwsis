from network_objects import Network
from SNDlib_parser import SNDlibParser
from collections import defaultdict

if __name__ == '__main__':
    network = Network()
    SNDlibParser("siec_testowa.xml").parse_to_object(network)
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
    # for node in network.nodes:
    #     print node.index, node.id
    #
    print "Amount of demands: " + str(len(network.demands))
    network.distribute_traffic()
    # network.print_final_distribution()

    print "Distributed: " + str(len(network.final_paths))
    print "Not distributed: " + str(len(network.not_distributed))
    # for i in network.not_distributed:
    #     for j in network.final_paths:
    #         if i == j:
    #             print i
    # print network.not_distributed
    # for node in network.nodes:
    #     if node.id == 'Gdansk':
    #         print node.id, node.shortest_paths

    # network.parse_shortest_path_to_links_list(0, 11)
    #for link in network.links:
    #    print link.capacity