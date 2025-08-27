# Count the Number of Possible Triangles

---

## 📌 Problem
Given an integer array `arr[]`. Find the number of triangles that can be formed with three different array elements as lengths of three sides of the triangle.  
A triangle with three given sides is only possible if the sum of any two sides is always greater than the third side.

---

## 🔑 Examples
```text
Example1
Input: arr = [4, 6, 3, 7]
Output: 3
Explanation:
There are three triangles possible → `[3, 4, 6]`, `[4, 6, 7]`, `[3, 6, 7]`.  
Note: `[3, 4, 7]` is not a triangle.

Example2:
Input: arr = [10, 21, 22, 100, 101, 200, 300]
Output: 6
Explanation:
Valid triangles are `[10, 21, 22]`, `[21, 100, 101]`, `[22, 100, 101]`, `[10, 100, 101]`, `[100, 101, 200]`, `[101, 200, 300]`.
```
---

## 🚀 Approach

1. **Sort the array** to simplify checking triangle conditions.  
2. **Fix the largest side (`c`)** as `arr[k]`.  
3. Use **two pointers (`i, j`)** to find valid pairs `(a, b)` such that:

arr[i] + arr[j] > arr[k]

- If true → all pairs from `i..j-1` with `j` are valid.  
- Else → move `i` forward.  

---
## ⏱️ Complexity Analysis

- **Sorting:** O(n log n)  
- **Two-pointer traversal:** O(n²)  
- **Total Time Complexity:** O(n²)  
- **Space Complexity:** O(1) → in-place, no extra space required
---
## ✅ Code (Python)

```python
class Solution:
 def countTriangles(self, arr):
     n = len(arr)
     arr.sort()
     count = 0

     for k in range(n - 1, 1, -1):  # Fix largest side
         i, j = 0, k - 1
         while i < j:
             if arr[i] + arr[j] > arr[k]:
                 count += (j - i)
                 j -= 1
             else:
                 i += 1
     return count

```
---
## 🌍 Applications of Triangle Counting

- 🛠️ **Computational Geometry:** Validating triangle formations in polygon meshes.  
- 🎮 **Computer Graphics:** Modeling 3D objects using triangular meshes.  
- 📐 **Structural Engineering:** Checking feasibility of triangular supports.  
- 🧩 **Algorithmic Puzzles:** Used in competitive programming and interview problems.  
- 📊 **Data Analysis:** Triangle inequality checks in similarity/distance metrics.
---
## 🏷️ Tags

- `#Array` 
- `#Sorting`  
- `#Two-Pointer Technique`  
- `#Geometry`  
- `#Counting Problems`  
- `#Greedy`
