# 🟩 Max Rectangle in Binary Matrix

## Problem Statement
You are given a 2D binary matrix `mat[][]`, where each cell contains either 0 or 1. Your task is to find the maximum area of a rectangle that can be formed using only 1's within the matrix.

---

## Examples
```text
Example 1:
mat = [
    [0, 1, 1, 0],
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 0, 0]
]
Output: 8
Explanation: The largest rectangle with only 1’s is:
[1, 1, 1, 1]
[1, 1, 1, 1]
Area = 4 * 2 = 8

Example 2:
mat = [
    [0, 1, 1],
    [1, 1, 1],
    [0, 1, 1]
]
Output: 6
Explanation: The largest rectangle with only 1’s is:
[1, 1]
[1, 1]
[1, 1]
Area = 2 * 3 = 6
```
---
## Constraints
- 1 ≤ mat.size(), mat[0].size() ≤ 1000
- 0 ≤ mat[i][j] ≤ 1
---
## Algorithm

1. Initialize `max_rectangle` to 0.
2. For each row in the matrix:
   - Convert the row into a histogram of heights:
     - If the current cell is 1, increment the height from the previous row.
     - If the current cell is 0, reset the height to 0.
   - Compute the maximum rectangular area in the histogram using a stack-based approach:
     - Initialize an empty stack.
     - Traverse each bar in the histogram:
       - If the stack is empty or current bar height ≥ stack top, push the index to the stack.
       - Else, pop the top and calculate area with the popped bar as the smallest bar.
     - Continue until all bars are processed.
     - Compute remaining areas for indices left in the stack.
   - Update `max_rectangle` with the maximum area found.
3. Return `max_rectangle`.
---
## Complexities

- **Time Complexity:**  
  O(N * M)  
  - N = number of rows, M = number of columns in the matrix  
  - Each row is processed as a histogram, and the stack-based histogram area calculation takes O(M) time per row.

- **Space Complexity:**  
  O(M)  
  - For the histogram heights array and stack used to compute the largest rectangle in a histogram.
---
## Code
```python
class Solution:
    def maxHistArea(self, heights):
        stack = []
        max_area = 0
        i = 0
        n = len(heights)

        while i < n:
            if not stack or heights[stack[-1]] <= heights[i]:
                stack.append(i)
                i += 1
            else:
                top = stack.pop()
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, heights[top] * width)

        while stack:
            top = stack.pop()
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, heights[top] * width)

        return max_area

    def maxArea(self, mat):
        if not mat:
            return 0

        n, m = len(mat), len(mat[0])
        heights = [0] * m
        max_rectangle = 0

        for i in range(n):
            for j in range(m):
                heights[j] = heights[j] + 1 if mat[i][j] == 1 else 0
            max_rectangle = max(max_rectangle, self.maxHistArea(heights))

        return max_rectangle
```
---
## Applications
- **Image Processing:** Detecting the largest rectangular regions in binary images (e.g., OCR, medical imaging).  
- **Data Analysis:** Finding maximal contiguous regions in occupancy grids, heatmaps, or binary data matrices.  
- **Pattern Recognition:** Identifying rectangular patterns in 2D binary grids for algorithms and AI tasks.  
- **Computer Vision:** Object detection in simplified binary representations of scenes.  
- **Game Development:** Collision detection or calculating largest empty rectangular areas in tile-based maps.  
- **Dynamic Programming Practice:** Serves as a foundation for solving more complex matrix-related DP problems.  
---
## 🏷️Tags
`#Stack` `#Histogram` `#Matrix` `#DynamicProgramming` `#Greedy` `#2DArray` `#Optimization`
