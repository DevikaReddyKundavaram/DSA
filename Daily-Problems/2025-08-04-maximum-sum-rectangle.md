# 🟦 Problem: Maximum Sum Rectangle in a 2D Matrix
---
## 📘 Problem Statement

Given a 2D matrix `mat[][]` of size `n × m`, find the **maximum sum** of any submatrix in the matrix.

---

### 🧾 Examples

#### Example 1:
```text
Input:
mat = [
    [1, 2, -1, -4, -20],
    [-8, -3, 4, 2, 1],
    [3, 8, 10, 1, 3],
    [-4, -1, 1, 7, -6]
]

Output: 29
```
---
## 🧠 Algorithm: Maximum Sum Rectangle in 2D Matrix

The idea is to reduce the 2D problem into a 1D **maximum subarray sum** problem using Kadane’s Algorithm.

### 🔁 Steps:

1. **Initialize**:
   - `max_sum = -inf` to track the global maximum sum.
   - Loop through all possible pairs of rows: `top` and `bottom`.

2. **Compress Rows into 1D**:
   - For each `top` to `bottom` pair:
     - Initialize a `temp[]` array of size `m` with 0s.
     - For each column `col`:
       - Sum all elements from `mat[top][col]` to `mat[bottom][col]` and store in `temp[col]`.

3. **Kadane's Algorithm**:
   - Apply Kadane's algorithm on the `temp[]` array to find the **maximum subarray sum**.
   - Update `max_sum` if a higher value is found.

4. **Return**:
   - After processing all row pairs, return `max_sum`.

---

### 🔎 Why it works:

- A submatrix is defined by its top and bottom rows and left and right columns.
- By fixing rows and reducing the problem to column-wise sums, we transform it into a 1D problem solvable with Kadane’s algorithm.
- This approach avoids O(n⁴) brute force by smartly using prefix-style reduction.

---
## 🧾 Code: Maximum Sum Rectangle in 2D Matrix

```python
class Solution:
    def maxRectSum(self, mat):
        if not mat or not mat[0]:
            return 0
        
        n, m = len(mat), len(mat[0])
        max_sum = float('-inf')

        for top in range(n):
            temp = [0] * m
            for bottom in range(top, n):
                for col in range(m):
                    temp[col] += mat[bottom][col]
                
                max_sum = max(max_sum, self.kadane(temp))
        
        return max_sum

    def kadane(self, arr):
        max_ending_here = max_so_far = arr[0]
        for val in arr[1:]:
            max_ending_here = max(val, max_ending_here + val)
            max_so_far = max(max_so_far, max_ending_here)
        return max_so_far
```
----
## 🚀 Applications of Maximum Sum Rectangle Algorithm

1. **Image Processing**  
   📸 Used to detect the region of an image with the highest pixel intensity (brightness/darkness) — like heat maps or noise detection.

2. **Game Development**  
   🎮 Find areas with the highest rewards or danger zones within a 2D grid-based map (e.g., for optimizing AI decisions in maps or levels).

3. **Financial Analysis**  
   💹 Used in analyzing 2D tables of profits/losses across time and regions to detect maximum profitability windows or loss zones.

4. **Data Compression**  
   🗜️ Can help identify uniform subregions (high or low value) that can be encoded efficiently, reducing redundancy.

5. **Dynamic Weather Heatmaps**  
   🌦️ Analyze the region of highest temperature or rainfall in spatial-temporal data grids.

6. **Medical Imaging**  
   🧠 Detect abnormal growth or activity in brain scans (fMRI, PET) by identifying maximum activity regions in 2D scan matrices.

7. **Urban Planning / Satellite Analysis**  
   🛰️ Detect densest population zones or resource-abundant rectangles in grid-mapped urban/rural layouts.

8. **Competitive Coding + Interviews**  
   🔥 A classic advanced DP + Kadane problem often asked in top-tier coding interviews (Amazon, Google, Flipkart, etc.).

---
## 🏷️ Tags

`#DynamicProgramming`  
`#KadaneAlgorithm`  
`#2DMatrix`  
`#PrefixSum2D`  
`#SubmatrixSum`  
`#Optimization`  
`#Greedy`  
`#IntermediateToAdvanced`  
`#CompetitiveProgramming`  
`#GridBasedProblems`
