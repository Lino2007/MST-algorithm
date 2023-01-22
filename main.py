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
    graphEdges, nodes = get_edges_and_nodes(MST[0])
    G=nx.Graph()

    for node in nodes:
        G.add_node(node)

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

    pos = nx.shell_layout(G)
    nx.draw(G, pos, edge_color=colors, width=list(weights), with_labels=True)

    edge_labels = G.edges
    formatted_edge_labels = {(elem[0], elem[1]): MST[0][elem[0]][elem[1]] for elem in edge_labels}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=formatted_edge_labels, font_color='red')
    plt.show()


def find_minimum (G, U, V):
    difference = [item for item in V if item not in U]
    min, u, v, exists = inf, 0, 0, False

    for c_u in U:
        for c_v in V:
            if G[c_u][c_v] != sys.maxsize and c_v in difference:
                    weight = G[c_u][c_v]
                    if weight < min:
                        min, u, v = weight, c_u, c_v
    if min != inf:
        exists = True

    return v, (u, v), min, exists

def MST_PRIM (G, s):
    V = {*range(0, len(G), 1)}
    U = {s}
    E_prim = set()
    total_weight = 0
    while U != V:
        gr_node, min_branch, weight, exists = find_minimum(G, U, V)
        if not exists:
            raise Exception("Node was not found!")
        U.add(gr_node)
        E_prim.add(min_branch)
        draw_graph([G, E_prim, 0]) 
        total_weight += weight
    return [G, E_prim, total_weight]


def print_result (MST):
    print("Minimum spanning tree has been found!")
    print("Edges of MST: " + str(MST[1]))
    print("Weight: " + str(MST[2]))

G1,G2,G3,G4 = [], [], [], []
exec(open("./graphs.txt").read())
MST = MST_PRIM(G4, 0)
draw_graph(MST)
print_result(MST)
