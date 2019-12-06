import networkx as nx
import matplotlib.pyplot as plt
import sys

#The file containing every input
file = sys.argv[1]

#Creates the graph
G = nx.Graph()

#Create every node from an external file, and connect them 
def GetInputs():
    with open(file) as f:
        listInputs = f.read().splitlines()
    for i in listInputs:
        j = i.split(")")
        G.add_node(j[0])
        G.add_node(j[1])
        G.add_edge(j[0], j[1])

# =====================
#        PART 1
# =====================

#Return the sum of all the possible paths (ie. the total number of direct and indirect orbits)
def SumPaths():
    s = 0
    for i in G.nodes:
        s += len(nx.shortest_path(G, "COM", i)) - 1
    return s

# =====================
#        PART 2
# =====================

#Returns the shortest path between YOU and SAN orbits
#(ie. the shortest path between YOU and SAN minus 2, hence the -3 replacing the -1 from SumPaths()
def MinimalPath():
    s = len(nx.shortest_path(G, "YOU", "SAN")) - 3
    return s

#Get the inputs, then print part 1 and 2 solutions
def Main():
    GetInputs()
    print("The solution to part 1 is: " + str(SumPaths()))
    print("The solution to part 2 is: " + str(MinimalPath()))

Main()
