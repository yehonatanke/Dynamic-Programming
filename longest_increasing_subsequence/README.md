<div align="center">

# Longest Increasing Subsequence (LIS)

</div>

## Table of Contents
- [Problem](#problem)
- [Solution](#solution)

## Problem

Given an array $A$ of length $n + 1$ with values in $\{-\infty, \infty, ..., \infty\}$, find the longest increasing subsequence.

Conditions:
1. For all $1 \leq i \leq n$:
   1.1. $A[i - 1] < x_i < A[i]$
   1.1.1. If no such $x_i$ exists in $A$, then $A[i] = x_i$
2. Initialize $A[0] = -\infty$ and $A[n] = \infty$

## Solution

### General Explanation
We use a dynamic programming approach to solve the Longest Increasing Subsequence (LIS) problem. The algorithm maintains an array that stores the smallest end element of all increasing subsequences of each length.

### The Regression Formula
For each element $x_i$ in the input, we find the largest $j$ such that $A[j] < x_i$. Then, we update $A[j+1] = \min(A[j+1], x_i)$.

### Initialization of the Array
We initialize $A[0] = -\infty$ and $A[n] = \infty$. All other elements are initially set to $\infty$.

### Updating the Array
For each input element $x_i$:
1. Find the largest $j$ such that $A[j] < x_i$ using binary search.
2. Update $A[j+1] = \min(A[j+1], x_i)$.

### Final Result
The length of the longest increasing subsequence is the largest $j$ such that $A[j] \neq \infty$.

### Correctness
The algorithm correctly maintains the invariant that $A[j]$ is the smallest end element of all increasing subsequences of length $j$.

### Efficiency
- Time complexity: $O(n \log n)$
- Space complexity: $O(n)$

The algorithm uses binary search to find the insertion position for each element, resulting in an efficient $O(n \log n)$ time complexity.