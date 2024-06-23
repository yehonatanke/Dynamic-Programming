<h1 align="center">Efficiently Counting Payment Options <br> Using 1, 3, and 5-Value Coins</h1>

## Table of Contents
- [Problem](#problem)
- [Solution](#solution)

## Problem

### Problem Statement

In a distant kingdom, all product prices are whole numbers. Payments can only be made using coins, and there are exactly three types of coins with values $1$, $3$, and $5$. Given a price $n \geq 1$ for a product, let $f(n)$ be the number of different ways to pay for it. The kingdom places great importance on the order of the coins used in payment.

For example, paying with a coin of value $3$ followed by a coin of value $1$ is considered different from paying with a coin of value $1$ followed by a coin of value $3$. Both are considered different ways to pay for a product priced at $4$.

Calculate $f(n)$ for any given $n \geq 1$.

## Solution

### General Explanation
We use dynamic programming to solve this problem efficiently. We create an array $Opt$ where $Opt(i)$ represents the number of ways to pay for a product priced $i$.

### The Recurrence Formula
The core of the solution is based on the following recurrence relation:

$Opt(i) = Opt(i-1) + Opt(i-3) + Opt(i-5)$

### Initialization of the Array
We initialize the array with the following base cases:
- $Opt(1) = 1$
- $Opt(2) = 1$
- $Opt(3) = 2$
- $Opt(4) = 3$
- $Opt(5) = 5$

### Updating the Array
We fill the array iteratively, using the recurrence formula. For each $i > 5$, we calculate $Opt(i)$ using the values of $Opt(i-1)$, $Opt(i-3)$, and $Opt(i-5)$.

### Location of the Solution
The final answer, which is the total number of ways to pay for a product priced $n$, is found in $Opt(n)$.

### Efficiency
- Time complexity: $O(n)$, as we calculate each value in the array once.
- Space complexity: $O(n)$ for storing the dynamic programming array.

### Proof of Exponential Growth
It can be proven that $f(n)$ grows exponentially. Specifically, $f(n) \geq c^n$ for some constant $c > 1$.

Proof sketch:
1. Observe that $f(n)$ is increasing.
2. Note that $f(n) \geq 3 \cdot f(n-5)$ (we can always add a coin of value 5 to any solution for $n-5$).
3. Expand this recursively: $f(n) \geq 3 \cdot 3 \cdot f(n-10) \geq ... \geq 3^{\lfloor n/5 \rfloor} \cdot f(1)$
4. Therefore, $f(n) \geq ({\sqrt[5]{3}})^n = c^n$, where $c = \sqrt[5]{3} > 1$

This proves that the function grows at least exponentially.

Note: The Python code provided in the accompanying file demonstrates an implementation of this solution. However, the core of the solution lies in the mathematical approach described above.