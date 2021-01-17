import networkx as nx
import matplotlib.pyplot as plt
import math
import sys

inf = sys.maxsize
def get_edges_and_nodes (G):
    edges = [(i, j) for i in range(len(G)) for j in range(len(G))
                  if i != j and G[i][j] != inf]
    edges += [(j, i) for i in range(len(G)) for j in range(len(G))
              if i != j and G[i][j] != inf]
    nodes = [*range(0, len(G), 1)]
    return edges, nodes



def draw_graph(MST):
    # marked_edges, unmarked_edges = get_graph_info(G)
    # extract nodes from graph
    graphEdges, nodes = get_edges_and_nodes(MST[0])

    # create networkx graph
    G=nx.Graph()

    # add nodes
    for node in nodes:
        # G.add_node("x" + str(node))
        G.add_node(node)


    # add edges
    edge_list = []
    for edge in graphEdges:
        if edge in MST[1]:
            l, r = edge[0], edge[1]
            if l > r:
                l, r = r, l
            G.add_edge(l, r, color="red", weight=3)
        else:
            edge_p = edge[1], edge[0]
            if edge_p not in MST[1] and edge_p not in edge_list:
                G.add_edge(edge[0], edge[1], color="black", weight=1)

    colors = nx.get_edge_attributes(G, 'color').values()
    weights = nx.get_edge_attributes(G, 'weight').values()
    # draw graph


    pos = nx.shell_layout(G)
    nx.draw(G, pos, edge_color=colors, width=list(weights), with_labels=True)

    edge_labels = G.edges
    formatted_edge_labels = {(elem[0], elem[1]): MST[0][elem[0]][elem[1]] for elem in edge_labels}  # use this to modify the tuple keyed dict if it has > 2 elements, else ignore
    nx.draw_networkx_edge_labels(G, pos, edge_labels=formatted_edge_labels, font_color='red')
    plt.show()


def pronadji_min (G, U, V):
    razlika = [item for item in V if item not in U]
    min, u, v, postoji = inf, 0, 0, False

    for c_u in U:
        for c_v in V:
            if G[c_u][c_v] != sys.maxsize and c_v in razlika:
                    tezina = G[c_u][c_v]
                    if tezina < min:
                        min, u, v = tezina, c_u, c_v
    if min != inf:
        postoji = True

    return v, (u, v), min, postoji

def MST_PRIM (G, s):
    V = {*range(0, len(G), 1)}
    U = {s}
    E_prim = set()
    ukupna_tezina = 0
    while U != V:
        cvor, min_grana, tezina, postoji = pronadji_min(G, U, V)
        if not postoji:
            raise Exception("Cvor nije pronadjen, prekidam izvrsenje!")
        U.add(cvor)
        E_prim.add(min_grana)
        draw_graph([G, E_prim, 0]) #crtaj u svakoj iteraciji
        ukupna_tezina += tezina
    return [G, E_prim, ukupna_tezina]




def print_result (MST):
    print("Minimum spanning tree has been found!")
    print("Edges of MST: " + str(MST[1]))
    print("Weight: " + str(MST[2]))



G1,G2,G3,G4 = [], [], [], []
exec(open("./grafovi.txt").read()) # ucitava grafove
MST = MST_PRIM(G4, 0)
draw_graph(MST)
print_result(MST)




