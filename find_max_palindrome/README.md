<h1 align="center">Maximum Palindrome</h1>

### Table of Contents
- [Problem](#problem)
- [Solution](#solution)

## Problem

### Problem Statement

A palindrome is a string that reads the same from left to right or right to left. For example, "ABBA" in English and "לא בוש אבוש שוב אליכם כי בא מועד" in Hebrew (ignoring spaces) are palindromes. Within a given string, a maximum palindrome is a palindrome that is not contained within any larger palindrome.

For example, in the string "abcbea", the maximum palindrome is "bcb" (not "abcba", which is not a palindrome).

Design a dynamic programming algorithm to find a maximum palindrome within a given string $x_1...x_n$ using the English alphabet.

## Solution

### General Explanation
We use dynamic programming to solve this problem efficiently. We create a 2D array $Opt$ where $Opt(i,j)$ represents whether the substring from index $i$ to index $j$ is a palindrome.

### The Recurrence Formula
The core of the solution is based on the following recurrence relation:

$Opt(i,j) = (x_i == x_j) \&\& (Opt(i+1, j-1) = T)$

Where $T$ represents True (is a palindrome) and $F$ represents False (is not a palindrome).

### Initialization of the Array
We initialize the array with the following base cases:
- $\forall_{1 \leq i \leq n}: Opt(i,i) = T$ (single characters are palindromes)
- $\forall_{1 \leq i \leq n-1}: Opt(i, i+1) = (x_i == x_{i+1})$ (check adjacent pairs)

### Updating the Array
We fill the array iteratively, using the recurrence formula. For each substring length $l$ from 3 to $n$, we calculate $Opt(i, i+l-1)$ for all valid $i$.

### Location of the Solution
The maximum palindrome can be found by keeping track of the largest substring for which $Opt(i,j) = T$.

### Efficiency
- Time complexity: $O(n^2)$, as we fill an $n \times n$ matrix.
- Space complexity: $O(n^2)$ for storing the dynamic programming array.

Note: The Python code provided in the accompanying file demonstrates an implementation of this solution. However, the core of the solution lies in the mathematical approach described above.
