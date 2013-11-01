class Graph:
    def __init__(self):
        self.nodes = []
        self.edges = []

    def createNode(self, lat, lng):
        self.nodes.append(Node(lat, lng))

    def createEdge(self, node1, node2):
        e = Edge(node1, node2)
        node1.edges.append(e)
        node2.edges.append(e)
        self.edges.append(e)



class Node:
    def __init__(self, lat=0, lng=0):
        self.attributes = []
        self.edges = []
        self.lat = lat
        self.lng = lng


class Edge:
    def __init__(self, length=0):
        self.length = length
        self.node1 = node1
        self.node2 = node2

    def is_connected(self, node):
        return (node == self.node1 or node == self.node2)

