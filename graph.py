import ParsePy
from igraph import *

def initParse():
    ParsePy.APPLICATION_ID = "9viWGl0x5YuJqhwg8dbYG16snlA2WG5X26JJrI7d"
    ParsePy.MASTER_KEY = "WWEZS3H9LCadSHLhwBPIbVk3nDEjeBAhEMGWDIJr"
    
def fetchGraph():
    
    g = Graph()

    query = ParsePy.ParseQuery("Node")
    nodes = query.fetch()
    query = ParsePy.ParseQuery("Edge")
    edges = query.fetch()

    
    g.add_vertices(len(nodes))

    for node in nodes:
        v = g.vs[nodes.index(node)]
        v['tag'] = 0

    for e in edges:
        v1 = g.vs[nodes.index(e.node1)]
        v2 = g.vs[nodes.index(e.node2)]
        e['lat'] = node.lat
        e['lng'] = node.lng
              


    return g
