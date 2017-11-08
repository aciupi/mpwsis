from network_objects import Network
from SNDlib_parser import SNDlibParser

if __name__ == '__main__':
    network = Network()
    SNDlibParser("D:\userdata\ciupider\Desktop\sndlib_network.xml").parse_to_object(network)
    print network.get_node_coordinates('Bydgoszcz')
    print network.get_target('Link_0_5')
