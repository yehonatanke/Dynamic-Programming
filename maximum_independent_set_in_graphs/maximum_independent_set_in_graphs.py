from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)


def max_independent_set_tree(tree, root):
    def dfs(node, parent):
        include = 1
        exclude = 0
        for child in tree.graph[node]:
            if child != parent:
                child_include, child_exclude = dfs(child, node)
                include += child_exclude
                exclude += max(child_include, child_exclude)
        return include, exclude

    return max(dfs(root, None))


def decompose_graph(graph):
    visited = set()
    subgraphs = []

    for v in graph.graph:
        if v not in visited:
            if len(graph.graph[v]) == 0:
                subgraphs.append(([v], []))
                visited.add(v)
            elif len(graph.graph[v]) == 1:
                u = graph.graph[v][0]
                subgraphs.append(([v, u], [(v, u)]))
                visited.add(v)
                visited.add(u)
            else:  # Star graph
                subgraph = ([v], [])
                for u in graph.graph[v]:
                    subgraph[0].append(u)
                    subgraph[1].append((v, u))
                    visited.add(u)
                subgraphs.append(subgraph)
                visited.add(v)

    return subgraphs


def max_independent_set_subgraph(subgraph):
    vertices, edges = subgraph
    if len(vertices) == 1:
        return 1
    elif len(vertices) == 2:
        return 1
    else:  # Star graph
        return max(1, len(vertices) - 1)


def max_independent_set_degree3(graph):
    subgraphs = decompose_graph(graph)
    return sum(max_independent_set_subgraph(sg) for sg in subgraphs)


# Example usage
if __name__ == "__main__":
    # Tree example
    tree = Graph()
    edges = [(0, 1), (0, 2), (1, 3), (1, 4), (2, 5), (2, 6)]
    for u, v in edges:
        tree.add_edge(u, v)

    print("Maximum Independent Set size for the tree:", max_independent_set_tree(tree, 0))

    # Graph with max degree 3 example
    graph = Graph()
    edges = [(0, 1), (0, 2), (0, 3), (1, 4), (2, 5), (3, 6), (4, 7), (5, 8), (6, 9)]
    for u, v in edges:
        graph.add_edge(u, v)

    print("Maximum Independent Set size for the graph with max degree 3:", max_independent_set_degree3(graph))
