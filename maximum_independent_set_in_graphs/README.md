<h1 align="center">Maximum Independent Set in Graphs</h1>

### Table of Contents
- [Problem](#problem)
- [Solution](#solution)

## Problem

### Problem Statement

Given an undirected graph $G = (V, E)$, where $V$ is the set of vertices and $E$ is the set of edges, we need to find a maximum independent set. An independent set is a subset of vertices in which no two vertices are adjacent.

The problem is divided into two parts:
A. For a tree graph
B. For a general graph with maximum degree 3

## Solution

### A. Solution for Trees

For a tree $T \in V$, we can compute the size of the maximum independent set using dynamic programming:

1. Choose an arbitrary root $r \in V$.
2. For each vertex $v$, define $B(v)$ as the size of the maximum independent set in the subtree rooted at $v$.
3. The recurrence relation is:
   $B(v) = \max(1 + \sum_{g \in \text{grandchildren}(v)} B(g), \sum_{c \in \text{children}(v)} B(c))$

### B. Solution for Graphs with Maximum Degree 3

For a graph $G$ with maximum degree 3:

1. Decompose $G$ into a set of subgraphs $G_1, G_2, ..., G_k$ where each $G_i$ is either:
    - A single vertex
    - A single edge
    - A star graph (a central vertex connected to 1, 2, or 3 leaves)

2. For each subgraph $G_i$:
    - If it's a single vertex, $B(G_i) = 1$
    - If it's a single edge, $B(G_i) = 1$
    - If it's a star graph, $B(G_i)$ is the maximum of:
        - 1 (choosing the center)
        - The number of leaves (choosing all leaves)

3. The maximum independent set size for $G$ is $\sum_{i=1}^k B(G_i)$

### Efficiency
- For trees: $O(|V|)$ time complexity
- For graphs with max degree 3: $O(|V|)$ time complexity (linear in the number of vertices)

Note: The actual implementation would require careful handling of the graph structure and the decomposition process for graphs with maximum degree 3.
