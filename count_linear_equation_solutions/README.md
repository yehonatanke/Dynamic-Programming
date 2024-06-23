<h1 align="center">Counting Solutions for Linear Equations over Natural Numbers</h1>

### Table of Contents
- [Problem](#problem)
- [Solution](#solution)

## Problem

### Problem Statement

Given a linear equation of the form:

$a_1x_1 + a_2x_2 + ... + a_nx_n = b$

where all $a_1, a_2, ..., a_n, b$ are natural numbers, count the number of solutions where all $x_i$ are also natural numbers.

For example, the equation $1\cdot x_1 + 2\cdot x_2 = 3$ has exactly 2 solutions in natural numbers:
- $x_1 = 3, x_2 = 0$
- $x_1 = 1, x_2 = 1$

## Solution

### General Explanation
We use dynamic programming to solve this problem efficiently. We create a 2D array $Opt$ where $Opt(i,j)$ represents the number of solutions for the equation using the first $i$ coefficients and summing to $j$.

### The Recurrence Formula
The core of the solution is based on the following recurrence relation:

$Opt(i,j) = \sum_{0\leq k\leq \lfloor j/a_i \rfloor} Opt(i-1, j - k\cdot a_i)$

### Initialization of the Array
We initialize the array with the following base cases:
- $Opt(i,0) = 1$ for all $1 \leq i \leq n$
- $Opt(1,j) = 1$ if $j/a_1$ is an integer, 0 otherwise

### Updating the Array
We fill the array iteratively, using the recurrence formula. For each cell $Opt(i,j)$, we consider all possible values for the $i$-th variable and sum up the number of solutions for the remaining problem.

### Location of the Solution
The final answer, which is the total number of solutions, is found in $Opt(n,b)$.

### Efficiency
- Time complexity: $O(n\cdot b^2)$, where $n$ is the number of coefficients and $b$ is the right-hand side of the equation.
- Space complexity: $O(n\cdot b)$ for the dynamic programming table.

Note: The Python code provided in the accompanying file demonstrates an implementation of this solution. However, the core of the solution lies in the mathematical approach described above, which can be applied with pen and paper for smaller instances of the problem.
