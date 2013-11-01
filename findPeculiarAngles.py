class Node:
    def __init__(self, nodeId, edgeArray):
	self.nodeId = nodeId
	self.edgeArray = edgeArray

class Edge:
    def __init__(self, edgeId, length, node1, node2, bearing1, bearing2):
	self.edgeId = edgeId
	self.length = length
	self.node1  = node1
	self.node2  = node2
	self.bearing1 = bearing1
	self.bearing2 = bearing2      


edge1 = Edge( 0, 133.65, 0, 1, -4.828, 175.171 )
edge2 = Edge( 1, 151.63, 1, 2, 179.94, -0.0499 )
edge3 = Edge( 2, 283.85, 2, 3, 179.31, -0.6897 )
edge4 = Edge( 3, 342.09, 3, 4, 2.4606, -177.53 )
edge5 = Edge( 4, 126.56, 4, 5, -0.008, 179.991 )
edge6 = Edge( 5, 133.05, 5, 6, -114.9, 65.0229 )
edge7 = Edge( 6, 142.67, 6, 7, -176.7, 3.22734 )
edge8 = Edge( 7, 168.65, 7, 8, -0.577, 179.422 )
edges = [edge1, edge2, edge3, edge4, edge5, edge6, edge7, edge8]

node1 = Node(0, [0,1])
node2 = Node(1, [1,2])
node3 = Node(2, [2,3])
node4 = Node(3, [3,4])
node5 = Node(4, [4,5])
node6 = Node(5, [5,6])
node7 = Node(6, [6,7])
node8 = Node(7, [7,0])
nodes = [node1, node2, node3, node4, node5, node6, node7, node8]

#def findPeculiarAngle( N, E ):
print node1
print edge1










