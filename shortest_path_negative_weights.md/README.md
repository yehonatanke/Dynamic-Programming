<div align="center">

# Shortest Path in Negative-Weight Graphs

</div>

## Table of Contents
- [Problem](#problem)
- [Solution](#solution)

## Problem

Given a directed graph $G = (V, E)$ where $V$ is the set of vertices and $E$ is the set of edges. Each edge $(u,v) \in E$ has a weight $w(e) \neq 0$. The graph may contain negative-weight edges but no negative-weight cycles. Find the shortest path from a source vertex $s$ to all other vertices.

## Solution

### General Explanation
We use a dynamic programming approach to solve this problem, utilizing the Bellman-Ford algorithm. This algorithm can handle graphs with negative edge weights, unlike Dijkstra's algorithm.

### The Regression Formula
The core of the algorithm is based on the following formula:

$Opt(s,t) = \min_{(u,v) \in E: w((u,v))>0} \{d(s,u) + d(v,t) + w((u,v))\}$

Where $Opt(s,t)$ represents the optimal (shortest) path from source $s$ to target $t$.

### Initialization of the Array
We initialize an array $d$ of size $|V|$ to store the shortest distances:
- $d[s] = 0$ (distance from source to itself is 0)
- $d[v] = \infty$ for all other vertices $v$

### Updating the Array
We perform $|V|-1$ iterations, where in each iteration we relax all edges:
For each edge $(u,v)$:
If $d[v] > d[u] + w(u,v)$, then update $d[v] = d[u] + w(u,v)$

### Final Result
After $|V|-1$ iterations, the array $d$ contains the shortest distances from the source $s$ to all other vertices.

### Correctness
The algorithm is correct because:
1. It considers all possible paths of up to $|V|-1$ edges.
2. In a graph without negative cycles, the shortest path cannot have more than $|V|-1$ edges.

### Efficiency
- Time complexity: $O(|V||E|)$
- Space complexity: $O(|V|)$

The algorithm runs in polynomial time, making it efficient for graphs without negative cycles.