# 🔢 Set Matrix Zeroes

## 🧩 Problem Statement

You are given a 2D matrix `mat[][]` of size `n x m`. Your task is to **modify** the matrix such that if any element `mat[i][j]` is `0`, then **all elements** in the `i-th` row and `j-th` column must be set to `0`.

---

## 📥 Input

- A 2D matrix `mat` of dimensions `n x m` where:
  - `1 ≤ n, m ≤ 500`
  - `-2³¹ ≤ mat[i][j] ≤ 2³¹ - 1`

---

## 📤 Output

- The same matrix `mat` modified in-place, where:
  - If `mat[i][j] == 0`, the entire row `i` and column `j` are set to `0`.

---

## 🔄 Example

```python
Input:
mat = [
    [1, 2, 0],
    [4, 5, 6],
    [7, 0, 9]
]

Output:
[
    [0, 0, 0],
    [4, 0, 0],
    [0, 0, 0]
]
```
---
## 🧠 Algorithm

To solve the Set Matrix Zeroes problem **efficiently and in-place**, follow these steps:

### Step 1: Check First Row and Column for Zero
- Use two boolean flags:
  - `row0`: Set to `True` if any element in the **first row** is `0`.
  - `col0`: Set to `True` if any element in the **first column** is `0`.

### Step 2: Use First Row and Column as Markers
- Traverse the matrix from index `[1][1]` to `[n-1][m-1]`.
- If `mat[i][j] == 0`, mark the corresponding row and column:
  - Set `mat[i][0] = 0`
  - Set `mat[0][j] = 0`

### Step 3: Set Inner Matrix Elements to Zero
- Again traverse the matrix from index `[1][1]` to `[n-1][m-1]`.
- For each cell `mat[i][j]`, if either `mat[i][0] == 0` or `mat[0][j] == 0`, set `mat[i][j] = 0`.

### Step 4: Set First Row and Column to Zero (if needed)
- If `row0` is `True`, set all elements in the first row to `0`.
- If `col0` is `True`, set all elements in the first column to `0`.
---

## ⏱️ Time and Space Complexity

| Complexity Type | Value              | Explanation                                                                 |
|-----------------|--------------------|-----------------------------------------------------------------------------|
| Time Complexity | O(n × m)           | The entire matrix is traversed multiple times, but each pass is linear.    |
| Space Complexity| O(1)               | No extra space is used except for two boolean flags (in-place modification).|
---
## 🧾 Code (Python)

```python
class Solution:
    def setMatrixZeroes(self, mat):
        n, m = len(mat), len(mat[0])
        row0 = any(mat[0][j] == 0 for j in range(m))
        col0 = any(mat[i][0] == 0 for i in range(n))
        
        for i in range(1, n):
            for j in range(1, m):
                if mat[i][j] == 0:
                    mat[i][0] = 0
                    mat[0][j] = 0
                    
        for i in range(1, n):
            for j in range(1, m):
                if mat[i][0] == 0 or mat[0][j] == 0:
                    mat[i][j] = 0
                    
        if row0:
            for j in range(m):
                mat[0][j] = 0
                
        if col0:
            for i in range(n):
                mat[i][0] = 0
```
---
## 🚀 Applications

- **Data Preprocessing in Machine Learning**: Sometimes missing or corrupted data is represented as `0` and entire rows/columns need to be ignored or nullified.
- **Spreadsheet Software**: Tools like Excel or Google Sheets might apply similar operations when certain cells trigger full row/column formatting or clearing.
- **Image Processing**: Zeroing out rows/columns in pixel grids when noise or dead pixels are detected.
- **Matrix-based Computations**: Useful in simulations or matrix algebra where zero conditions force full linear constraints.
- **Database Table Sanitization**: Helps in nullifying rows and columns in tabular data when certain values violate constraints.
- ---
## 🏷️ Tags

-` Matrix`
- `In-place Algorithm`
- `Array Manipulation`
- `Space Optimization`
- `Simulation`
- `Coding Interview`
- `Medium Level`
- `2D Array`
