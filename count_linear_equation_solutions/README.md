<h1 align="center">Counting Solutions for Linear Equations over Natural Numbers</h1>

## Problem Statement

Given a linear equation of the form:

$a_1x_1 + a_2x_2 + ... + a_nx_n = b$

where all $a_1, a_2, ..., a_n, b$ are natural numbers, count the number of solutions where all $x_i$ are also natural numbers.

For example, the equation $1\cdot x_1 + 2\cdot x_2 = 3$ has exactly 2 solutions in natural numbers:
- $x_1 = 3, x_2 = 0$
- $x_1 = 1, x_2 = 1$

## Solution Approach

We use dynamic programming to solve this problem efficiently. The solution is based on the following recurrence relation:

$Opt(i,j) = \sum_{0\leq k\leq \lfloor j/a_i \rfloor} Opt(i-1, j - k\cdot a_i)$

Where:
- $Opt(i,j)$ represents the number of solutions for the equation using the first $i$ coefficients and summing to $j$.
- The base cases are:
  - $Opt(i,0) = 1$ for all $1 \leq i \leq n$
  - $Opt(1,j) = 1$ if $j/a_1$ is an integer, 0 otherwise

The final answer is found in $Opt(n,b)$.

## Implementation

The solution is implemented in Python. The main function `count_solutions` takes two parameters:
1. `coefficients`: A list of integers representing $a_1, a_2, ..., a_n$
2. `b`: The right-hand side of the equation

The function returns the number of solutions for the given equation.

## Complexity

- Time complexity: $O(n\cdot b^2)$, where $n$ is the number of coefficients and $b$ is the right-hand side of the equation.
- Space complexity: $O(n\cdot b)$ for the dynamic programming table.
