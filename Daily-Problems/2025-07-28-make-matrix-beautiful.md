# 🧩 Make Matrix Beautiful

## 📝 Problem Statement

A matrix is called **beautiful** if the sum of every row and every column is the same.

You are given a square matrix `mat[][]` of size `n x n`.  
In one operation, you can increment any **single cell by 1**.

Your task is to determine the **minimum number of operations** required to make the matrix beautiful.

---

## 🔢 Input

- A square matrix `mat` of size `n x n` where:
  - `1 ≤ n ≤ 900`
  - `0 ≤ mat[i][j] ≤ 10⁶`

---

## 🎯 Output

- Return the minimum number of operations required to make the matrix beautiful.

---

## 📚 Examples

### ✅ Example 1


```python
Input
mat = [
    [1, 2],
    [3, 4]
]
output:
4
```
---
## ⚙️ Algorithm

1. **Initialize variables** to store:
   - `row_sum[i]`: sum of the i-th row
   - `col_sum[j]`: sum of the j-th column
   - `total_sum`: sum of all matrix elements

2. **Traverse the matrix**:
   - For each element `mat[i][j]`, add it to both `row_sum[i]` and `col_sum[j]`
   - Also accumulate it in `total_sum`

3. **Find the target sum**:
   - The matrix must be balanced so that all rows and columns have equal sums
   - This `target_sum` = `max(max(row_sum), max(col_sum))`

4. **Calculate total required operations**:
   - We only **increment**, so we must bring all row and column sums up to `target_sum`
   - Minimum operations needed = `target_sum * n - total_sum`

5. **Return** the number of operations

---

### 🔁 Dry Run Example

For matrix:
-[[1,2],[3,4]]
- row_sums = [3, 7], col_sums = [4, 6]
- max_sum = 7
- total_sum = 10
- required operations = 7×2 - 10 = 14 - 10 = **4**
---
## ⏱️ Time & Space Complexities

### ⌛ Time Complexity

**O(n²)**

- We traverse the entire matrix once to compute row sums, column sums, and the total sum.
- All operations (sum, max) are linear in terms of matrix size.
- Efficient for `n ≤ 900` (maximum constraint).

---

### 🧠 Space Complexity

**O(n)**

- `row_sum` and `col_sum` arrays of size `n` are used.
- No extra 2D space required — only auxiliary arrays for row and column tracking.

---

### ✅ Optimized

- No brute-force checking of each possibility.
- Greedy approach with direct math leads to minimal operations in linear time over input size.

---

## 💻 Code (Python)

```python
class Solution:
    def balanceSums(self, mat):
        n = len(mat)
        row_sum = [0] * n
        col_sum = [0] * n
        total_sum = 0

        # Step 1: Calculate row and column sums
        for i in range(n):
            for j in range(n):
                val = mat[i][j]
                row_sum[i] += val
                col_sum[j] += val
                total_sum += val

        # Step 2: Determine the target sum for each row/column
        target_sum = max(max(row_sum), max(col_sum))

        # Step 3: Calculate operations needed
        return target_sum * n - total_sum
```
---
## 🌐 Applications

This matrix transformation concept, although abstract, has real-world analogies and applications:

### 🔧 1. **Resource Balancing**
- In distributed systems or data centers, resources like CPU or memory need to be balanced across nodes.
- Incrementing a cell is like allocating more resources to achieve a balanced state.

### 📊 2. **Load Balancing in Grid Systems**
- Imagine a grid of machines where each cell is a processing node.
- Ensuring each row/column has the same "load" improves system efficiency.

### 🧮 3. **Fair Allocation Problems**
- Used in logistics, scheduling, or planning to ensure fairness in distribution across categories (rows/columns).

### 🧠 4. **Matrix Normalization**
- In ML preprocessing or image processing, this can be an early step in transforming data matrices to a desired format.

### 🧩 5. **Puzzle Design & Game Development**
- Core logic for level design in puzzle games where balance or symmetry is the goal.

### 📐 6. **Table & Spreadsheet Balancing**
- In financial models or inventory systems, where row/column totals must align.

---
## Tags

`matrix`  
`greedy`  
`optimization`  
`2d-array`  
`row-column-sum`  
`minimum-operations`  
`math`  
`simulation`  
`grid`  
`dynamic-thinking`
