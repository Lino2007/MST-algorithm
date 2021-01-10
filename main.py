import networkx as nx
import matplotlib.pyplot as plt
import math
import sys

inf = sys.maxsize
def get_graph_info (G):
    size = len(graph)
    graphEdges = [(i, j) for i in range(size) for j in range(size)
                if i != j and G[i][j] != inf]

   # markedEdges = [item for item in graphEdges if item not in U]



def draw_graph(MST):
    # marked_edges, unmarked_edges = get_graph_info(G)
    # extract nodes from graph
    graphEdges = [(i, j) for i in range(len(MST[0])) for j in range(len(MST[0]))
                  if i != j and MST[0][i][j] != inf]
    sfc = [[i, j] for i in range(len(MST[0])) for j in range(len(MST[0]))
                  if i != j and MST[0][i][j] != inf]
    graphEdges += [(j, i) for i in range(len(MST[0])) for j in range(len(MST[0])) if i != j and MST[0][i][j] != inf]
    nodes = [*range(0, len(MST[0]), 1)]

    # create networkx graph
    G=nx.Graph()
    G.add_edges_from(sfc)
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
            edge_list.append([l ,r])
        else:
            edge_p = edge[1], edge[0]
            if edge_p not in MST[1] and edge_p not in edge_list:
                # G.add_edge("x" + str(edge[0]), "x" + str(edge[1]), color="black", weight=1)
                G.add_edge(edge[0], edge[1], color="black", weight=1)
                edge_list.append([edge[0], edge[1]])
    print(str(edge_list))
    colors = nx.get_edge_attributes(G, 'color').values()
    weights = nx.get_edge_attributes(G, 'weight').values()
    # draw graph
    pos = nx.shell_layout(G)
    nx.draw(G, pos, edge_color=colors, width=list(weights), with_labels=True, edgelist = edge_list)

    edge_labels = nx.get_edge_attributes(G, 'edge')  # key is edge, pls check for your case
    formatted_edge_labels = {(elem[0], elem[1]): 'edge_labels[elem]' for elem in edge_labels}  # use this to modify the tuple keyed dict if it has > 2 elements, else ignore
    nx.draw_networkx_edge_labels(G, pos, edge_labels=formatted_edge_labels, font_color='red')
    plt.show()

def dr_ff ():
    G = nx.Graph()
    G.add_edge(0, 1, color='r', weight=2)
    G.add_edge(1, 2, color='g', weight=4)
    G.add_edge(2, 3, color='b', weight=6)
    G.add_edge(3, 4, color='y', weight=3)
    G.add_edge(4, 0, color='m', weight=1)

    colors = nx.get_edge_attributes(G, 'color').values()
    weights = nx.get_edge_attributes(G, 'weight').values()

    pos = nx.circular_layout(G)
    nx.draw(G, pos,
            edge_color=colors,
            width=list(weights),
            with_labels=True,
            node_color='lightgreen')
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
        node, edge, nv,found = find_node(G, U, V)
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

inf = sys.maxsize
graph = [[ sys.maxsize,           12, sys.maxsize,          25, sys.maxsize ],
         [          12,  sys.maxsize,          11,           8,          12 ],
         [ sys.maxsize,           11, sys.maxsize, sys.maxsize,          17 ],
         [          25,            8, sys.maxsize, sys.maxsize,          15 ],
         [ sys.maxsize,           12,          17,          15, sys.maxsize ]]

W4 = [[ sys.maxsize,26,41,59,26,60,71,22,12,30,32,42,51, 9,26,80, 3,92,73,49],
      [26, sys.maxsize,58,24,46,96,55,52,23,49,62,68,40,37,98, 4,88,91,79,10],
      [41,58, sys.maxsize,26,34,68,14,72,11,65,49,78,71,90,89,34,70,20, 4,74],
      [59,24,26, sys.maxsize,50,48,90,61,62,86,80,58,19,24,88, 3,49,17,97,71],
      [26,46,34,50, sys.maxsize,50,47, 6,68, 5, 8,52,10,81,81,72,15,66,52,97],
      [60,96,68,48,50, sys.maxsize,65,80,45,43,82, 9,14,18,39,83,80, 6,40,53],
      [71,55,14,90,47,65, sys.maxsize,42,66,63,29,43, 2,98,17,11,37,20,49,34],
      [22,52,72,61, 6,80,42, sys.maxsize,95,92, 6,74,27,42,55,94,42,98,30,70],
      [12,23,11,62,68,45,66,95, sys.maxsize,66,54,70,66,18,13,99,17, 4,56,88],
      [30,49,65,86, 5,43,63,92,66, sys.maxsize,67,19,37,46,98,16,85,64,38,19],
      [32,62,49,80, 8,82,29, 6,54,67, sys.maxsize,43,48,12,59,23,39,58,25,29],
      [42,68,78,58,52, 9,43,74,70,19,43, sys.maxsize,62,27,82,98,73,35,58,11],
      [51,40,71,19,10,14, 2,27,66,37,48,62, sys.maxsize,90,88,81,26,59, 3,43],
      [ 9,37,90,24,81,18,98,42,18,46,12,27,90, sys.maxsize,31,16,18,42,10,60],
      [26,98,89,88,81,39,17,55,13,98,59,82,88,31, sys.maxsize,47,69,70,64, 4],
      [80, 4,34, 3,72,83,11,94,99,16,23,98,81,16,47, sys.maxsize, 7,32,53,65],
      [ 3,88,70,49,15,80,37,42,17,85,39,73,26,18,69, 7, sys.maxsize,41,82,72],
      [92,91,20,17,66, 6,20,98, 4,64,58,35,59,42,70,32,41, sys.maxsize,96,53],
      [73,79, 4,97,52,40,49,30,56,38,25,58, 3,10,64,53,82,96, sys.maxsize,33],
      [49,10,74,71,97,53,34,70,88,19,29,11,43,60, 4,65,72,53,33, sys.maxsize]]
W3 = [[ sys.maxsize,28, 7,15, 9,24, 8,30,29,16],
      [28, sys.maxsize,28, 7,12,14, 2,26,19, sys.maxsize],
      [ 7,28, sys.maxsize,15,20, 1,19, sys.maxsize, 3,17],
      [15, 7,15, sys.maxsize,19,30, 6,17, sys.maxsize,13],
      [ 9,12,20,19, sys.maxsize,11,30,18, sys.maxsize, 2],
      [24,14, 1,30,11, sys.maxsize, 1,29,29,13],
      [ 8, 2,19, 6,30, 1, sys.maxsize,25,30,22],
      [30,26, sys.maxsize,17,18,29,25, sys.maxsize, 6,26],
      [29,19, 3, sys.maxsize, sys.maxsize,29,30, 6, sys.maxsize,29],
      [16, sys.maxsize,17,13, 2,13,22,26,29, sys.maxsize]]

#print(find_node(graph, [3, 4], [0, 1, 2, 3, 4]))
#A = [0,1,2,3]
#B = [3,2,1,0]
#print(A == B)
#MST_PRIM(W3, 0)
MST = MST_PRIM(W3, 0)
draw_graph(MST)
print_result(MST)
# print(pairList)
# draw example
# graph = [(20, 21),(21, 22),(22, 23), (23, 24),(24, 25), (25, 20)]
# draw_graph(graph)

