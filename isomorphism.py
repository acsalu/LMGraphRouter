import ParsePy
from igraph import *

def initParse():
    ParsePy.APPLICATION_ID = "WGl0x5YuJqhwg8dbYG16snlA2WG5X26JJrI7d"
    ParsePy.MASTER_KEY = "9viWGl0x5YuJqhwg8dbYG16snlA2WG5X26JJrI7d"
    
def fetchGraph():
    g = Graph()
    query = ParsePy.ParseQuery("Node")
    nodes = query.fetch()
    
    for node in nodes:
        print("node (%.6f, %.6f)" % (node.lat, node.lng))









    return g
