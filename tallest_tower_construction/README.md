<div align="center">

# Tallest Tower Construction

</div>

## Table of Contents
- [Problem](#problem)
- [Solution](#solution)

## Problem

Given a sequence of $n$ boxes. For each box $i$ where $1 \leq i \leq n$, we have:
- Length $l(i)$
- Width $w(i)$
- Height $h(i)$

All lengths are different, all widths are different, and all heights are different. We want to build the tallest possible tower by stacking boxes on top of each other. A box can be placed on top of another box only if its length, width, and height are all smaller than the box below it.

## Solution

### General Explanation
We use a dynamic programming approach to solve this problem. We sort the boxes by a dimension (e.g., length) and then use a recursive formula to find the tallest tower that can be built ending with each box.

### The Regression Formula

$$Opt(i) = h(i) + \max_{k &lt i \text{ such that } w(k)>w(i)} \\\{ Opt(k) \cup \{0\}\\\}$$

Where $Opt(i)$ is the height of the tallest tower that can be built ending with box $i$.

### Initialization of the Array
We initialize $Opt(1) = h(1)$, as the first box can always form a tower by itself.

### Updating the Array
We iterate from $i=2$ to $n$, calculating $Opt(i)$ using the regression formula.

### Final Result
The height of the tallest possible tower is $Opt(n)$.

### Correctness
The algorithm correctly considers all valid stacking possibilities for each box.

### Efficiency
- Time complexity: $O(n^2)$
- Space complexity: $O(n)$

The algorithm requires a nested loop to calculate each $Opt(i)$, resulting in $O(n^2)$ time complexity.
