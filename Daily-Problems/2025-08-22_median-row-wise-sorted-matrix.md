# Median in a Row-wise Sorted Matrix  

## Problem Statement  
Given a row-wise sorted matrix `mat[][]` of size `n * m`, where the number of rows and columns is always odd, return the **median of the matrix**.  

### Examples  
```text
Example 1:
Input:  
mat = [[1, 3, 5],
[2, 6, 9],
[3, 6, 9]]
Output: 5
Explanation: Sorting matrix elements → `[1, 2, 3, 3, 5, 6, 6, 9, 9]`. Median = 5.  

Example 2:
Input:  
mat = [[2, 4, 9],
[3, 6, 7],
[4, 7, 10]]

Output: 6
Explanation: Sorting matrix elements → `[2, 3, 4, 4, 6, 7, 7, 9, 10]`. Median = 6.  

Example 3: 
Input: mat = [[3], [4], [8]]
Output: 4
Explanation: Sorting matrix elements → `[3, 4, 8]`. Median = 4.  
```
---
### Constraints  
- `1 ≤ n, m ≤ 400`  
- `1 ≤ mat[i][j] ≤ 2000`  
- Both `n` and `m` are odd.  

---

##Algorithm / Approach  

1. **Naive Approach (not efficient):**  
   - Flatten the matrix into a list.  
   - Sort the list.  
   - Pick the middle element → O((n*m) log(n*m)) time.  

2. **Optimized Approach (Binary Search):**  
   - The median is the `(n*m)//2 + 1`-th smallest element.  
   - Since each row is sorted, we can apply **binary search on the value range** (between the minimum and maximum matrix elements).  
   - For a mid-value, count how many elements are `<= mid` using binary search in each row.  
   - If the count is less than or equal to `(n*m)//2`, move the low bound up; else move the high bound down.  
   - Continue until `low == high`, which is the median.  

---

## Time & Space Complexity  

- **Time Complexity:** `O(32 * n * log(m))`  
  - Binary search on the value range (max 32 steps since values ≤ 2000).  
  - For each mid, count elements using `log(m)` binary search per row.  
  - Total = `O(n * log(m) * log(value_range))`.  

- **Space Complexity:** `O(1)` (no extra storage used).  

---

## Code (Python)  

```python
import bisect

class Solution:
    def median(self, mat):
        n, m = len(mat), len(mat[0])
        low, high = mat[0][0], mat[0][-1]
        for i in range(n):
            low = min(low, mat[i][0])
            high = max(high, mat[i][-1])

        desired = (n * m + 1) // 2

        while low < high:
            mid = (low + high) // 2
            count = 0
            for i in range(n):
                count += bisect.bisect_right(mat[i], mid)
            
            if count < desired:
                low = mid + 1
            else:
                high = mid
        return low
```
---

## Applications  

- **Databases:** Efficiently find medians in sorted datasets across multiple partitions.  
- **Statistics:** Quick computation of median in large datasets without full sorting.  
- **Image Processing:** Used in median filters for noise reduction in images.  
- **Big Data Systems:** Helps when handling large, distributed row-wise sorted data streams.  
- **Machine Learning:** Feature preprocessing where median is used as a robust central tendency measure.  
---
##🏷️ Tags  

- `#Binary Search ` 
- `#Matrix`  
- `#Sorting`  
- `#Median`  
