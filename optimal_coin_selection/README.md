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

### Correctness
For each turn, given a subarray of coins $(v_i,...,v_j)$ where $1 \leq i < j \leq n$, we need to choose the step that ensures maximum profit among the two possible steps: choosing $v_i$ or choosing $v_j$. We assume the opponent will make the optimal move for themselves.

If we choose $v_i$, the opponent's optimal move will be the maximum between taking $v_{i+1}$ or $v_j$, leaving the first player with either subarray $(v_{i+2},...,v_j)$ or subarray $(v_{i+1},v_{j-1})$. Thus, the maximum profit is $v_i + \min(Opt(i+2,j), Opt(i+1,j-1))$.

Similarly, if we choose $v_j$, the maximum profit is $v_j + \min(Opt(i,j-2), Opt(i+1,j-1))$. We choose the maximum of these two steps, thus proving the correctness of the recurrence formula.

For initialization, we perform this for all pairs $(v_i, v_{i+1})$ as we need to choose the maximum among them to win. 

In other words, initialization is done for the diagonal below the main diagonal in the $Opt$ matrix of size $n \times n$. If $n$ can be odd, we initialize the main diagonal $Opt(i,i)=v_i$ (single coin in the sequence). The matrix is filled for all diagonals below the main diagonal, calculating the maximum profit for all subarrays of length 2, then length 3, and so on until we reach $Opt(1,n)$, which is the profit of the original sequence of length $n$ that we are looking for.



### Efficiency
- Time complexity: $O(n^2S)$, where $n$ is the number of coin denominations and $S$ is the target sum.
- Space complexity: $O(nS)$ for storing the dynamic programming array.

Note: The actual implementation requires careful handling of index boundaries and coin selection tracking.
