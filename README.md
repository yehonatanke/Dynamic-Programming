# <h1 align="center">Dynamic Programming Problem Solutions</h1>


This repository contains solutions to various dynamic programming problems. Each problem is implemented in either C or Python and includes a detailed README explaining the problem statement and solution approach.

## Table of Contents
- [Overview](#overview)
- [Problems and Solutions](#problems-and-solutions)
- [Usage](#usage)
- [License](#license)

## Quick Navigation
- [Conglomerate Split Optimization](./conglomerate_split_optimization)
  - [C Implementation](./conglomerate_split_optimization/conglomerate_split_optimization.c)
  - [README](./conglomerate_split_optimization/README.md)
- [Count Linear Equation Solutions](./count_linear_equation_solutions)
  - [Python Implementation](./count_linear_equation_solutions/count_linear_equation_solutions.py)
  - [README](./count_linear_equation_solutions/README.md)
- [Count Payment Ways](./count_payment_ways)
  - [Python Implementation](./count_payment_ways/count_payment_ways.py)
  - [README](./count_payment_ways/README.md)
- [Find Max Palindrome](./find_max_palindrome)
  - [Python Implementation](./find_max_palindrome/find_max_palindrome.py)
  - [README](./find_max_palindrome/README.md)
- [Longest Increasing Subsequence](./longest_increasing_subsequence)
  - [C Implementation](./longest_increasing_subsequence/longest_increasing_subsequence.c)
  - [README](./longest_increasing_subsequence/README.md)
- [Maximum Independent Set in Graphs](./maximum_independent_set_in_graphs)
  - [Python Implementation](./maximum_independent_set_in_graphs/maximum_independent_set_in_graphs.py)
  - [README](./maximum_independent_set_in_graphs/README.md)
- [Object Arrangement Count](./object_arrangement_count)
  - [C Implementation](./object_arrangement_count/object_arrangement_count.c)
  - [README](./object_arrangement_count/README.md)
- [Optimal Coin Selection](./optimal_coin_selection)
  - [Python Implementation](./optimal_coin_selection/optimal_coin_selection.py)
  - [README](./optimal_coin_selection/README.md)
- [Shortest Path with Negative Weights](./shortest_path_negative_weights.md)
  - [C Implementation](./shortest_path_negative_weights.md/shortest_path_negative_weights.c)
  - [README](./shortest_path_negative_weights.md/README.md)
- [Tallest Tower Construction](./tallest_tower_construction)
  - [C Implementation](./tallest_tower_construction/tallest_tower_construction.c)
  - [README](./tallest_tower_construction/README.md)

## Overview

This repository is a collection of dynamic programming problems and their solutions. Each problem is implemented in either C or Python, demonstrating various techniques and approaches in algorithm design and optimization.

## Problems and Solutions

### 1. [Conglomerate Split Optimization](./conglomerate_split_optimization)
- **Problem**: Optimize the splitting of a conglomerate for maximum profit.
- **Solution**: Dynamic programming approach to find the optimal split points.

### 2. [Count Linear Equation Solutions](./count_linear_equation_solutions)
- **Problem**: Count the number of non-negative integer solutions to a linear equation.
- **Solution**: Use dynamic programming to build up solutions for larger sums from smaller ones.

### 3. [Count Payment Ways](./count_payment_ways)
- **Problem**: Count the number of ways to make a payment using given coin denominations.
- **Solution**: Dynamic programming to build a table of possible payment combinations.

### 4. [Find Max Palindrome](./find_max_palindrome)
- **Problem**: Find the longest palindromic subsequence in a given string.
- **Solution**: Use a 2D dynamic programming table to store palindrome lengths.

### 5. [Longest Increasing Subsequence](./longest_increasing_subsequence)
- **Problem**: Find the length of the longest increasing subsequence in an array.
- **Solution**: Efficient O(n log n) algorithm using binary search and dynamic programming.

### 6. [Maximum Independent Set in Graphs](./maximum_independent_set_in_graphs)
- **Problem**: Find the maximum independent set in a graph.
- **Solution**: Dynamic programming on tree-structured graphs.

### 7. [Object Arrangement Count](./object_arrangement_count)
- **Problem**: Count the number of ways to arrange n objects with ordering constraints.
- **Solution**: Dynamic programming approach considering equality classes.

### 8. [Optimal Coin Selection](./optimal_coin_selection)
- **Problem**: Select coins to make a target sum with minimum number of coins.
- **Solution**: Bottom-up dynamic programming to build optimal solutions.

### 9. [Shortest Path with Negative Weights](./shortest_path_negative_weights.md)
- **Problem**: Find shortest paths in a graph with negative edge weights.
- **Solution**: Implementation of the Bellman-Ford algorithm.

### 10. [Tallest Tower Construction](./tallest_tower_construction)
- **Problem**: Construct the tallest tower from a set of boxes with constraints.
- **Solution**: Sort boxes and use dynamic programming to find the optimal stacking.

## Usage

Each problem directory contains:
- A README.md file with a detailed problem description and explanation of the solution.
- Source code file(s) implementing the solution.

To run a specific solution:
1. Navigate to the problem directory.
2. Follow the instructions in the problem-specific README.md file.

## License

This project is open-sourced under the MIT license.
