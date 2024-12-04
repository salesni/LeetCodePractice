"""
33. Clone Graph

Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}
 

Test case format:

For simplicity, each node's value is the same as the node's index (1-indexed). For example, the first node with val == 1, the second node with val == 2, and so on. The graph is represented in the test case using an adjacency list.

An adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.

The given node will always be the first node with val = 1. You must return the copy of the given node as a reference to the cloned graph.



"""
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node == None:
            return None
        

        old_node_dict = {}
        stack = [node]

        while stack:
            current = stack.pop()
            old_node_dict[current] = Node(val=current.val)
            for neighbor in current.neighbors:
                if neighbor not in old_node_dict:
                    stack.append(neighbor)
        
        for old_node, new_node in old_node_dict.items():
            for old_neighbor in old_node.neighbors:
                new_node.neighbors.append(old_node_dict[old_neighbor])
        
        return old_node_dict[node]
            
        


        
