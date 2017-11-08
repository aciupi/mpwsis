import xml.etree.ElementTree as ET
from parser_functions import parse_to_object
from network_objects import Network

if __name__ == '__main__':
    network = Network()
    network_xml = ET.parse("D:\userdata\ciupider\Desktop\sndlib_network.xml")
    root = network_xml.getroot()
    parse_to_object(root, network)
