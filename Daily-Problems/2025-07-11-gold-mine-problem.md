# 🪙 Problem: Gold Mine Problem

**Difficulty:** Medium  
**Problem Statement:**  
You're given a matrix `mat[][]` where each cell contains some amount of gold.  
The miner can start from **any row in the first column**, and can move:
- Right
- Diagonally right-up
- Diagonally right-down

Find the **maximum gold** the miner can collect.

---

## 🔢 Examples

### Example 1:
**Input:**
mat = [[1, 3, 3], 
       [2, 1, 4], 
       [0, 6, 4]]

## 🐢 Naive Algorithm (Recursive – Not Efficient)

We use a **recursive brute-force** approach to explore all possible paths from the first column.

### 🧠 Steps:

1. Start from each row in the **first column (col = 0)**.
2. From any cell `(i, j)`, recursively explore:
   - Right → `(i, j + 1)`
   - Right-up → `(i - 1, j + 1)` (if `i > 0`)
   - Right-down → `(i + 1, j + 1)` (if `i < n - 1`)
3. Base condition: if `j == m - 1`, return the gold at that cell.
4. At each step, collect the gold and return the maximum of all three paths.
5. Repeat this for every row in the first column and return the overall max.

---

### ⏱️ Time Complexity

- **Time:** O(3^m)  
- **Space:** O(m) (recursion stack)

> ❗ Very inefficient for large matrices due to repeated subproblem calculations.

## 🧑‍💻 Code – Naive Recursive (Brute Force)

```python
class Solution:
    def maxGold(self, mat):
        n = len(mat)
        m = len(mat[0])

        def collect(i, j):
            # Base case: last column
            if j == m - 1:
                return mat[i][j]

            # Move right
            right = collect(i, j + 1)

            # Move right-up
            right_up = collect(i - 1, j + 1) if i > 0 else 0

            # Move right-down
            right_down = collect(i + 1, j + 1) if i < n - 1 else 0

            return mat[i][j] + max(right, right_up, right_down)

        max_gold = 0
        for i in range(n):
            max_gold = max(max_gold, collect(i, 0))

        return max_gold
```
## 🏷️ Tags

- `#BruteForce`
- `#Recursion`
- `#Backtracking`
- `#GridTraversal`
- `#MatrixProblem`
- `#Inefficient`
- `#ExponentialTime`
- `#2DRecursion`



       
## 💡 Algorithm (Dynamic Programming)

We use **Dynamic Programming (Tabulation)**:

- Traverse from **right to left** across the columns.
- For each cell `(i, j)`, consider three possible moves:
  - Right → `dp[i][j+1]`
  - Right-up → `dp[i-1][j+1]` (if `i > 0`)
  - Right-down → `dp[i+1][j+1]` (if `i < n - 1`)
- The recurrence relation:
  dp[i][j] = mat[i][j] + max(right, right_up, right_down)

## ⏱️ Time and Space Complexity

| Type      | Complexity |
|-----------|------------|
| Time      | O(n × m)   |
| Space     | O(n × m)   |

Where:
- `n` = number of rows in the matrix  
- `m` = number of columns in the matrix  


## 🧑‍💻 Code

```python
class Solution:
    def maxGold(self, mat):
        n = len(mat)
        m = len(mat[0])
        dp = [[0]*m for _ in range(n)]

        for col in range(m-1, -1, -1):
            for row in range(n):
                right = dp[row][col+1] if col < m-1 else 0
                right_up = dp[row-1][col+1] if row > 0 and col < m-1 else 0
                right_down = dp[row+1][col+1] if row < n-1 and col < m-1 else 0

                dp[row][col] = mat[row][col] + max(right, right_up, right_down)

        return max(dp[row][0] for row in range(n))
```
---
## 🚀 Applications

- 🎮 **Game Grid Navigation**  
  Maximize collected resources like gold, gems, or coins in tile-based grid games using optimal paths.

- 🤖 **AI Resource Planning**  
  Useful in strategy games where AI must plan efficient collection of items with movement constraints.

- 📊 **Dynamic Programming Practice**  
  A classic 2D DP example to strengthen your understanding of tabulation and state transitions in matrices.

- 🧠 **Interview-Ready Problem**  
  Frequently asked in coding interviews to assess problem-solving using matrix traversal and DP.

- 🪨 **Mining & Geological Simulations**  
  Simulate best possible path for extracting minerals or resources from a mapped-out terrain.
---

## 🏷️ Tags

- `#DynamicProgramming`
- `#MatrixDP`
- `#GreedyMoves`
- `#GridTraversal`
- `#Tabulation`
- `#2DMatrix`
- `#MediumLevel`
- `#DailyDSA`

