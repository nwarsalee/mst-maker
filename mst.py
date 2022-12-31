# Nabeel Warsalee
# Dec 30 2022
# MST Maker
# MST Creator class

from graph import Graph
from node import Nodes
from edge import Edges


class MST:
    def compute_mst(self, graph: Graph):
        # Function to compute MST of a given graph starting from root

        # Create empty graph to hold MST
        mst = Graph()

        # Add start node to MST
        # TODO: Make this random?
        start_node = graph.nodes.get(0)
        mst.nodes.add(start_node)

        # Store list of edges to add during algo
        possible_edges = Edges()
        edges_from_start = graph.edges.find_all(start_node)
        possible_edges.extend(edges_from_start)

        visited_nodes = Nodes()
        visited_nodes.add(start_node)

        while mst.total_nodes() < graph.total_nodes():
            # Find lowest edge amongst visited nodes
            lowest_edge = possible_edges.pop()
            
            # Add lowest weight edge to MST
            mst.add_to_graph(lowest_edge)

            # For all nodes that have not been visited, obtain their associated edges
            # add it to possible edge list
            unvisited = [x for x in mst.nodes.get_all() if x not in visited_nodes.get_all()]

            for node in unvisited:
                edges_for_node = graph.edges.find_all(node)
                possible_edges.extend(edges_for_node)
                # Add to visited after adding its edges
                visited_nodes.add(node)

        
        return mst