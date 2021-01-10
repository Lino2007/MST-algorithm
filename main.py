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
            # G.add_edge("x" + str(l), "x" + str(r), color="red", weight=3)
            G.add_edge(l, r, color="red", weight=3)
            # edge_list.append([l ,r])
        else:
            edge_p = edge[1], edge[0]
            if edge_p not in MST[1] and edge_p not in edge_list:
                # G.add_edge("x" + str(edge[0]), "x" + str(edge[1]), color="black", weight=1)
                G.add_edge(edge[0], edge[1], color="black", weight=1)
                # edge_list.append([edge[0], edge[1]])

    colors = nx.get_edge_attributes(G, 'color').values()
    weights = nx.get_edge_attributes(G, 'weight').values()
    # draw graph

    print(G.nodes)
    pos = nx.shell_layout(G)
    nx.draw(G, pos, edge_color=colors, width=list(weights), with_labels=True)

    edge_labels = G.edges
    formatted_edge_labels = {(elem[0], elem[1]): MST[0][elem[0]][elem[1]] for elem in edge_labels}  # use this to modify the tuple keyed dict if it has > 2 elements, else ignore
    nx.draw_networkx_edge_labels(G, pos, edge_labels=formatted_edge_labels, font_color='red')
    plt.show()


def find_node (G, U, V):
    difference = [item for item in V if item not in U] # V - U
    string = ""
    minimum_weight, u, v, found = sys.maxsize, 0, 0, False
    for x_axis in V:
        for y_axis in V:
            if x_axis != y_axis and G[x_axis][y_axis] != sys.maxsize:
                if x_axis in U and y_axis in difference:
                    weight = G[x_axis][y_axis]
                    if weight < minimum_weight:
                       # string += str(G[x_axis][y_axis]) + " "
                        minimum_weight, u, v = weight, x_axis, y_axis
        #string += "\n"
    print(minimum_weight)
    if minimum_weight != sys.maxsize:
        found = True

    return v, (u, v), minimum_weight,found

def MST_PRIM (G, s):
    V = [*range(0, len(G), 1)]
    U = [s]
    E_prim = []
    wh = 0
    while U != V:
        node, edge, nv, found = find_node(G, U, V)
        if found == False:
            raise Exception("Error, node hasn't been found, terminating MST_PRIM")
        U.append(node)
        U.sort()
        E_prim.append(edge)
        wh += nv

    print(E_prim)
    print(wh)
    return [G, E_prim, wh]



def print_result (MST):
    print("Minimum spanning tree has been found!")
    print("Edges of MST: " + str(MST[1]))
    print("Weight: " + str(MST[2]))



G1,G2,G3,G4 = [], [], [], []
exec(open("./grafovi.txt").read()) # ucitava grafove
MST = MST_PRIM(G1, 0)
draw_graph(MST)
print_result(MST)



