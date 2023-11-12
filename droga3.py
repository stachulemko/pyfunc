def znajdz_node(graf, node_name):
    for node in graf:
        if node[0] == node_name:
            return node
    return None


def generuj_drogi(graf, start_node_name):
    jest_node = True
    drogi = []
    koszt = 0
    bierzacy_node_name = start_node_name
    while jest_node:
        node = znajdz_node(graf, bierzacy_node_name)
        if node == None or bierzacy_node_name > node[1]:
            jest_node = False
        else:
            bierzacy_node_name = node[1]
            koszt += 1
            droga = [bierzacy_node_name, koszt]
            drogi.append(droga)
        print(bierzacy_node_name)
    return drogi


print(generuj_drogi([['Z', 'D'], ['A', 'B'], ['F', 'B'],
                     ['B', 'C'], ['C', 'D'], ['D', 'F']], 'A'))
