# 🪣 Container With Most Water

---

## 📖 Problem Statement  
You are given an array `arr[]` of non-negative integers, where each element `arr[i]` represents the height of a vertical line.  
Find the maximum amount of water that can be contained between **any two lines** along with the x-axis.

⚠️ Note: A single vertical line cannot hold water.

---

## 🔍 Examples  
```text
Example 1
Input: arr = [1, 5, 4, 3]
Output: 6
Explanation:
Lines at index 1 and 3 → width = 2  
Height = min(5, 3) = 3  
Area = 2 × 3 = **6**  

Example 2 
Input: arr = [3, 1, 2, 4, 5]
Output: 12
Explanation:
Lines at index 0 and 4 → width = 4  
Height = min(3, 5) = 3  
Area = 4 × 3 = **12**  

Example 3
Input: arr = [2, 1, 8, 6, 4, 6, 5, 5]
Output: 25  
Explanation:
Lines at index 2 and 7 → width = 5  
Height = min(8, 5) = 5  
Area = 5 × 5 = 25  
```
---

## ✅ Constraints
- 1 ≤ arr.size() ≤ 10⁵  
- 0 ≤ arr[i] ≤ 10⁴  

---

## 💡 Approach (Two Pointers)  
1. Use two pointers: `left = 0`, `right = n-1`.  
2. Compute current area = `(right - left) × min(height[left], height[right])`.  
3. Keep track of maximum area.  
4. Move the pointer pointing to the smaller height (since it limits water).  
5. Continue until `left < right`.  
---
## Complexities
⏱️ **Time Complexity:** O(n)  
📦 **Space Complexity:** O(1)  
---

## 🧑‍💻 Code (Python)
```python
class Solution:
    def maxWater(self, arr):
        left, right = 0, len(arr) - 1
        max_area = 0

        while left < right:
            width = right - left
            height = min(arr[left], arr[right])
            area = width * height
            max_area = max(max_area, area)

            if arr[left] < arr[right]:
                left += 1
            else:
                right -= 1

        return max_area
```
---

## 🌍 Applications

- **Reservoir Design / Tank Construction** – determining max water capacity between two walls.  
- **Civil Engineering** – optimizing wall placement for water storage.  
- **Computer Graphics & Game Development** – modeling bounded fluid areas.  
- **Optimization Problems** – selecting optimal boundaries under constraints.  
- **Interview Insight** – tests understanding of two-pointer strategy on arrays.  
---
## 🏷️ Tags
`#Arrays` `#TwoPointers` `#Greedy` `#Optimization`





