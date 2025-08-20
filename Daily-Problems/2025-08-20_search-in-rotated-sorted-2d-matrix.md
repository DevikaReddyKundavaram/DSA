# 🔍 Search in Fully Rotated Sorted 2D Matrix
  

---

## 📌 Problem Statement
We are given an `n x m` matrix `mat[][]` that was originally filled such that:
1. Each row is sorted in increasing order.
2. The first element of each row is greater than the last element of the previous row.  
👉 If flattened row-wise, it forms a strictly sorted 1D array.  

Later, this sorted array was **rotated at some pivot** and written back row-wise into the matrix.  

**Task:** Determine if an integer `x` exists in the matrix.  

---

## 🧩 Example
```text
Example1:
Input 1: x = 3
mat = [[7, 8, 9, 10],
[11, 12, 13, 1],
[2, 3, 4, 5]]
Output: `true`  
Explanation: `3` is at row 3, col 2.

Example2:
Input 2: x = 10
mat = [[6, 7, 8],
[9, 1, 2],
[3, 4, 5]]
Output: `false`  
Explanation: `10` does not exist.
```
---

## ⚙️ Algorithm
1. Flatten index mapping: treat matrix as an array of length `n*m`.  
   - Index → `(row, col)` = `(idx // m, idx % m)`.
2. Apply **binary search** on this conceptual rotated array:
   - Compute `mid` → get value at `(mid//m, mid%m)`.
   - If value matches `x`, return `True`.
   - Otherwise, decide which side of rotated array to move:
     - If left side is sorted, check if `x` lies in range.
     - Else, search right side.
3. Return `False` if not found.

---

## ⏱️ Time & Space Complexity
- **Time:** `O(log(n*m))`  
- **Space:** `O(1)`  

---

## 🧑‍💻 Code (Python)

```python
class Solution:
    def searchMatrix(self, mat, x):
        n, m = len(mat), len(mat[0])
        lo, hi = 0, n * m - 1
        
        while lo <= hi:
            mid = (lo + hi) // 2
            r, c = divmod(mid, m)
            mid_val = mat[r][c]
            
            if mid_val == x:
                return True
          
            lo_r, lo_c = divmod(lo, m)
            hi_r, hi_c = divmod(hi, m)
            lo_val, hi_val = mat[lo_r][lo_c], mat[hi_r][hi_c]
            
            if lo_val <= mid_val:
                
                if lo_val <= x < mid_val:
                    hi = mid - 1
                else:
                    lo = mid + 1
            else:
                
                if mid_val < x <= hi_val:
                    lo = mid + 1
                else:
                    hi = mid - 1
        
        return False
```
---
## 🌍 Applications

1. **Efficient Search in Rotated Datasets**  
   - Helps in scenarios where data gets cyclically shifted (logs, monitoring systems).  

2. **Database Indexing**  
   - Some DB systems rotate or reorder storage pages; binary search on rotated data is useful.  

3. **Search in Real-Time Systems**  
   - Sensor readings or event streams often wrap around — this method allows fast lookups.  

4. **Embedded Systems / Circular Buffers**  
   - Useful when data is stored in rotated/circular structures and needs quick searching.  

5. **Competitive Programming & Interview Problems**  
   - Classic variation of “search in rotated sorted array” extended to 2D, common in coding challenges.  
---
## 🏷️ Tags
- `Binary Search`  
- `Rotated Sorted Array`  
- `Matrix Manipulation`  
- `Flattening Techniques`  
- `Divide and Conquer`  
- `Searching Algorithms`  
- `Competitive Programming`  
- `Interview Problem` 


