# Counting Solutions for Linear Equations over Natural Numbers

## Problem Statement

Given a linear equation of the form:

a₁x₁ + a₂x₂ + ... + aₙxₙ = b

where all a₁, a₂, ..., aₙ, b are natural numbers, count the number of solutions where all xᵢ are also natural numbers.

For example, the equation 1·x₁ + 2·x₂ = 3 has exactly 2 solutions in natural numbers:
- x₁ = 3, x₂ = 0
- x₁ = 1, x₂ = 1

## Solution Approach

We use dynamic programming to solve this problem efficiently. The solution is based on the following recurrence relation:

Opt(i,j) = ∑(0≤k≤⌊j/aᵢ⌋) Opt(i-1, j - k·aᵢ)

Where:
- Opt(i,j) represents the number of solutions for the equation using the first i coefficients and summing to j.
- The base cases are:
    - Opt(i,0) = 1 for all 1 ≤ i ≤ n
    - Opt(1,j) = 1 if j/a₁ is an integer, 0 otherwise

The final answer is found in Opt(n,b).

## Implementation

The solution is implemented in Python. The main function `count_solutions` takes two parameters:
1. `coefficients`: A list of integers representing a₁, a₂, ..., aₙ
2. `b`: The right-hand side of the equation

The function returns the number of solutions for the given equation.

## Complexity

- Time complexity: O(n·b²), where n is the number of coefficients and b is the right-hand side of the equation.
- Space complexity: O(n·b) for the dynamic programming table.