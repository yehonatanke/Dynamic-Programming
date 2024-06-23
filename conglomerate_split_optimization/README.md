<div align="center">

# Conglomerate Split Optimization

</div>

## Table of Contents
- [Problem](#problem)
- [Solution](#solution)

## Problem

Given a cone of companies composed of n small companies. For each $1 \leq k \leq n$, a whole number $1 \leq w_k \leq n^2$ is defined, which represents the value of company number k in millions of dollars. According to the regulatory requirement, the cone must be split into two parts, such that each small company will belong to one of the two parts (and only one part can contain a small company). For the purpose of the division, the regulator demands that the total value of the two new parts will be as close as possible. Determine if this is possible (answer "yes" / "no"). Assume, for simplicity, that arithmetic operations (addition/subtraction/comparison of numbers) are performed in constant time.

## Solution

### General Explanation
We will use dynamic programming to solve this problem. The idea is to create a 2D array that represents whether it's possible to achieve a certain sum using a subset of the companies.

### The Withdrawal Formula
We define $Opt(i,j)$ as a boolean value:
$$Opt(i,j) = \begin{cases}
T, & \text{if } \exists A \subseteq \{1,2,\ldots,i\}: \sum_{a \in A} w_a = j \\
F, & \text{otherwise}
\end{cases}$$

Where $T$ (True) in cell $(i,j)$ of the array means it's possible to achieve a sum of $j$ using a subset of companies $\{1,2,\ldots,i\}$.

### The Initialization of the Array
We initialize the first row of the array as follows:
$Opt(1,j) = (w_1 == j)$ for all $1 \leq j \leq \frac{w}{2}$

### Updating the Array According to the Withdrawal Formula
For each cell in the array, we use the following formula:
$Opt(i,j) = Opt(i-1,j) \text{ OR } Opt(i-1,j-w_i)$

Note: If $j - w_i < 1$, we only use $Opt(i-1,j)$.

### Where is the Final Result Saved
The final result is found in $Opt(n,\frac{w}{2})$, where $w = \sum_{k=1}^n w_k$.

### Correctness
The algorithm correctly builds up all possible sums that can be achieved using subsets of companies. If $Opt(n,\frac{w}{2})$ is true, it means we can split the companies into two groups with equal sums, which is the optimal division.

### Efficiency
Time complexity: $O(\frac{w}{2}) = O(w) = O(\sum_{k=1}^n w_k) = O(n) \cdot O(n^2) = O(n^3)$
Space complexity: $O(n^4)$

The algorithm fills a 2D array of size $n \times \frac{w}{2}$, where $w$ can be at most $n \cdot n^2 = n^3$. Each cell operation takes $O(1)$ time.