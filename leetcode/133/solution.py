"""
https://leetcode.com/problems/clone-graph/description/?envType=problem-list-v2&envId=oizxjoit
"""


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def solution(node: Node) -> Node:
    edges: dict = (
        {}
    )  # keys are vals, and values are list of neighbour vals for a given val

    def update_edge_mapping(node: Node) -> None:
        if node == None or node.val in edges:
            return

        edges[node.val] = [n.val for n in node.neighbors]

        for n in node.neighbors:
            update_edge_mapping(n)

    update_edge_mapping(node)

    nodes: dict = {
        val: Node(val=val) for val in edges.keys()
    }  # keys are vals, values are Node copies

    for copy in nodes.values():
        neighbor_values: list = edges[copy.val]
        copy.neighbors = [nodes[val] for val in neighbor_values]

    for anyvalue in nodes:
        return nodes[anyvalue]
