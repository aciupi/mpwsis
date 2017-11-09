from SNDlib_parser import SNDlibParser

if __name__ == '__main__':
    network = SNDlibParser("D:\userdata\ciupider\Desktop\sndlib_network.xml").parse_to_object()
    print network.get_node_coordinates('Bydgoszcz')
    print network.get_target('Link_0_5')
    print '\n'.join(map(str, network.get_demands()))
    print '\n'.join(map(str, network.get_nodes()))
    print '\n'.join(map(str, network.get_links()))
