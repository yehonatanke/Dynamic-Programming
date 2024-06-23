<h1 align="center">Optimal Coin Selection</h1>

### Table of Contents
- [Problem](#problem)
- [Solution](#solution)

## Problem

### Problem Statement

Given a set of coin denominations $(v_1,...,v_n)$ and a target sum $S$, find the optimal way to select coins to reach the target sum. The optimality is determined by a combination of the number of coins used and their individual values.

## Solution

### General Explanation
We use dynamic programming to solve this problem efficiently. We create a 2D array $Opt$ where $Opt(i,j)$ represents the optimal solution for achieving sum $j$ using the first $i$ coin denominations.

### The Recurrence Formula
The core of the solution is based on the following recurrence relation:


The formula in mathematical notation is represented as:

$$
Opt(i,j) = \max\{
\begin{cases}
v_i + \min(Opt(i+2,j),  Opt(i+1,j-1)), \\
v_{i+1} + \min(Opt(i,j-2),  Opt(i+1,j-1))
\end{cases}}
$$

where:
- $Opt(i,j)$ denotes the maximum score achievable starting from position $i$ to $j$.
- $v_i$ and $v_{i+1}$ represent values associated with positions $i$ and $i+1$ respectively.


### Initialization of the Array
We initialize the array with base cases for $i \leq n$ and $j = 1$.

### Updating the Array
We fill the array iteratively, using the recurrence formula. For each cell $Opt(i,j)$, we consider two options: including the $i$-th coin or the $(i+1)$-th coin, and choose the maximum value.

### Location of the Solution
The final solution is found in $Opt(1,S)$, where $S$ is the target sum.

### Efficiency
- Time complexity: $O(n^2S)$, where $n$ is the number of coin denominations and $S$ is the target sum.
- Space complexity: $O(nS)$ for storing the dynamic programming array.

Note: The actual implementation requires careful handling of index boundaries and coin selection tracking.
