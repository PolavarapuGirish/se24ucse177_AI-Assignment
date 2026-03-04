# AI Uninformed Search Algorithms Implementation

## Overview

This project implements **Uninformed Search Algorithms** in Artificial Intelligence, specifically **Breadth First Search (BFS)** and **Depth First Search (DFS)**, along with their application to classic AI search problems.

The implementation demonstrates how search algorithms explore the **state space** to find a path from the **initial state** to the **goal state**.

---

## Objectives

- Implement **BFS and DFS algorithms**
- Understand **state space search**
- Apply search algorithms to real problems
- Compare performance of BFS and DFS
- Demonstrate implementation using Python

---

## Implemented Algorithms

### 1. Breadth First Search (BFS)

BFS explores nodes **level by level** and uses a **FIFO queue**.

Characteristics:
- Complete
- Optimal when step cost is equal
- Uses more memory

---

### 2. Depth First Search (DFS)

DFS explores **deep into the search tree before backtracking** and uses a **stack (LIFO)**.

Characteristics:
- Less memory usage
- Not always optimal
- May not be complete in infinite spaces

---

## Variants of Search Algorithms

The following variants are discussed in this project:

- Depth Limited Search (DLS)
- Iterative Deepening DFS (IDDFS)
- Uniform Cost Search (UCS)
- Bidirectional Search

---

## Example Problem Implemented

### Water Jug Problem

Problem Description:

Two jugs are available:
- 4 litre jug
- 3 litre jug

Objective:
Measure exactly **2 litres of water**.

State Representation:
