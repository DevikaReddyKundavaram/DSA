# 📊 2D Difference Array

---

## 🧩 Problem Statement

You are given a 2D integer matrix `mat[n][m]` and a list of `q` operations `opr[][]`. Each operation is an array `[v, r1, c1, r2, c2]` which means:

- Add value `v` to every cell inside the submatrix defined by:
  - Top-left: `(r1, c1)`
  - Bottom-right: `(r2, c2)` (inclusive)

Return the final matrix after applying all operations.

---

## 🔍 Example



```text
### Input
mat = [
  [1, 2, 3],
  [1, 1, 0],
  [4, -2, 2]
]

opr = [
  [2, 0, 0, 1, 1],
  [-1, 1, 0, 2, 2]
]
### Output:
[
  [3, 4, 3],
  [2, 2, -1],
  [3, -3, 1]
]
```
---
## ⚙️ Algorithm: 2D Difference Array Approach

### Step 1: Initialize Difference Matrix
- Create a 2D difference matrix `diff[n+2][m+2]` initialized to zero.
- This helps in safely handling edge cases during updates.

### Step 2: Apply Range Updates using Difference Matrix
For each operation `[v, r1, c1, r2, c2]`:
- `diff[r1][c1] += v`
- `diff[r1][c2 + 1] -= v`
- `diff[r2 + 1][c1] -= v`
- `diff[r2 + 1][c2 + 1] += v`

This ensures that when the prefix sums are computed later, only the desired submatrix receives the value `v`.

### Step 3: Compute 2D Prefix Sum on `diff`
- Traverse the `diff` matrix and convert it to hold prefix sums.
- Use the formula:

- diff[i][j] = diff[i][j] + diff[i-1][j] + diff[i][j-1] - diff[i-1][j-1]

##This gives the cumulative impact of all operations up to cell `(i, j)`.

### Step 4: Add Difference to Original Matrix
- For each cell `(i, j)` in `mat`, do:
- mat[i][j] += diff[i][j]

---

## 🕒 Time & Space Complexities

### ⏱ Time Complexity

| Operation                     | Time      |
|------------------------------|-----------|
| Applying `q` operations      | O(q)      |
| Computing 2D prefix sums     | O(n × m)  |
| Updating original matrix     | O(n × m)  |
| **Total Time**               | O(n × m + q) |

> Efficient even for large inputs since both `n × m` and `q` can go up to 10⁵.

---

### 📦 Space Complexity

| Component            | Space     |
|----------------------|-----------|
| Difference Matrix    | O(n × m)  |
| Original Matrix      | O(n × m)  |
| **Total Space**      | O(n × m)  |

> No extra space per operation — just one extra matrix for range tracking.
---

## 🧾 Python Code: 2D Difference Array

```python
class Solution:
    def applyDiff2D(self, mat, opr):
        n, m = len(mat), len(mat[0])
        
        # Step 1: Initialize 2D difference array
        diff = [[0] * (m + 2) for _ in range(n + 2)]
        
        # Step 2: Apply each operation in O(1)
        for v, r1, c1, r2, c2 in opr:
            diff[r1][c1] += v
            diff[r1][c2 + 1] -= v
            diff[r2 + 1][c1] -= v
            diff[r2 + 1][c2 + 1] += v
        
        # Step 3: Compute 2D prefix sums
        for i in range(n):
            for j in range(m):
                if i > 0:
                    diff[i][j] += diff[i - 1][j]
                if j > 0:
                    diff[i][j] += diff[i][j - 1]
                if i > 0 and j > 0:
                    diff[i][j] -= diff[i - 1][j - 1]
        
        # Step 4: Add prefix diff values to original matrix
        for i in range(n):
            for j in range(m):
                mat[i][j] += diff[i][j]
        
        return mat
```
---
## 🎯 Applications of 2D Difference Array

The 2D Difference Array technique is highly useful in scenarios where multiple range updates are needed on a grid or matrix structure:

### 🔧 Common Use Cases

- **Image Editing Software**  
  Quickly apply brightness/contrast updates over rectangular areas.

- **Game Development (Grid Maps)**  
  Efficiently apply buffs/debuffs or terrain modifications over zones.

- **Geospatial Analysis**  
  Add elevation changes or temperature adjustments over subregions.

- **Spreadsheet Software**  
  Batch updates to rectangular cells based on user formulas or conditions.

- **Dynamic Programming (Grid-based)**  
  Optimizing prefix-based or rectangle-based state updates.

- **Competitive Programming**  
  Used in range update queries on 2D arrays where brute force would TLE.

- **Simulation of Events Over a Grid**  
  e.g., forest fire spread, population movement, or pollution levels in urban areas.

---

## 🏷️ Tags

`#2DDifferenceArray` &nbsp; `#PrefixSum` &nbsp; `#MatrixManipulation` &nbsp; `#RangeUpdate` &nbsp;  
`#GridOptimization` &nbsp; `#EfficientUpdates` &nbsp; `#Hashing2D` &nbsp; `#CompetitiveProgramming` &nbsp;  
`#AdvancedArrayTechniques` &nbsp; `#InterviewPrep` &nbsp; `#PythonImplementation`
