<div align="center">

# Counting Object Arrangements

</div>

## Table of Contents
- [Problem](#problem)
- [Solution](#solution)

## Problem

Let $f(n)$ be the number of ways to arrange $n$ objects using the relation $<$ (less than). For example:
- $f(2) = 3$ because for 2 objects $a,b$, there are 3 possible arrangements: $a < b$, $a = b$, or $b < a$.
- $f(3) = 13$ for 3 objects $a,b,c$, as there are 13 possible arrangements:

$\begin{cases}
a = b = c, & b = c < a, & c < a = b \\
a = b < c, & b < a = c, & c < a < b \\
a < b = c, & b < a < c, & c < b < a \\
a < b < c, & b < c < a, \\
a = c < b, \\
a < c < b,
\end{cases}$

Design an algorithm that calculates $f(n)$ in $O(n^2)$ time and $O(n)$ memory.

## Solution

### General Explanation
We use a dynamic programming approach to solve this problem. The key insight is that we can break down the problem into smaller subproblems based on the number of equality classes in the arrangement.

### The Regression Formula
$Opt(n,k) = k \cdot (Opt(n-1,k-1) + Opt(n-1,k))$

Where $Opt(n,k)$ is the number of ways to arrange $n$ objects into $k$ equality classes.

### Initialization of the Array
- $Opt(n,1) = 1$ for all $n$ (all objects in one equality class)
- $Opt(n,k) = 0$ for $k > n$ (impossible to have more equality classes than objects)

### Updating the Array
We calculate $Opt(n,k)$ for increasing values of $n$ and $k$, using the regression formula.

### Final Result
The final result is the sum of all possible arrangements:
$Ans = \sum_{k=1}^n Opt(n,k)$

### Correctness
The formula correctly accounts for all possible ways to add a new object to existing arrangements, either creating a new equality class or joining an existing one.

### Efficiency
- Time complexity: $O(n^2)$
- Space complexity: $O(n)$

We only need to store two rows of the $Opt$ array at any time, resulting in $O(n)$ space complexity.