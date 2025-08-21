# Maximize the Minimum Difference between k Elements
---

## 📝 Problem Statement
Given an array `arr[]` of integers and an integer `k`, select `k` elements from the array such that the **minimum absolute difference** between any two of the selected elements is maximized. Return this maximum possible minimum difference.

### Example 1
**Input:**  
`arr = [2, 6, 2, 5], k = 3`  
**Output:**  
`1`  
**Explanation:**  
Selecting `[2, 5, 6]` results in minimum difference `1`, which is the maximum possible.

### Example 2
**Input:**  
`arr = [1, 4, 9, 0, 2, 13, 3], k = 4`  
**Output:**  
`4`  
**Explanation:**  
Selecting `[0, 4, 9, 13]` results in minimum difference `4`, which is the largest possible.

### Constraints
- `1 ≤ arr.size() ≤ 10^5`  
- `0 ≤ arr[i] ≤ 10^6`  
- `2 ≤ k ≤ arr.size()`

---

## ⚡ Algorithm
1. **Sort** the array.  
2. Perform **Binary Search on Answer** for the minimum difference.  
3. For each candidate difference `mid`:
   - Greedily try to place `k` elements ensuring difference ≥ `mid`.  
   - If possible → search right (increase `mid`).  
   - Otherwise → search left.  
4. The largest valid `mid` is the answer.  

---

## ⏱️ Complexity
- **Sorting:** `O(n log n)`  
- **Binary Search:** `O(log(max(arr)))`  
- **Feasibility Check:** `O(n)`  
- **Overall:** `O(n log n + n log(max(arr)))`

---

## 🧑‍💻 Code
```python
class Solution:
    def maxMinDiff(self, arr, k):
        arr.sort()
        
        def canPlace(diff):
            count = 1
            last = arr[0]
            for i in range(1, len(arr)):
                if arr[i] - last >= diff:
                    count += 1
                    last = arr[i]
                if count >= k:
                    return True
            return False
        
        lo, hi = 0, arr[-1] - arr[0]
        ans = 0
        
        while lo <= hi:
            mid = (lo + hi) // 2
            if canPlace(mid):
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1
        
        return ans
```
---
## 🎯 Applications
- **Resource Allocation:** Selecting positions to maximize spacing.  
- **Wireless Communication:** Placing towers/routers to minimize interference.  
- **Tournament Scheduling:** Ensuring maximum minimum distance between competitors.  
- **Server / Data Center Placement:** Optimal distribution to avoid congestion.  
- **Seating Arrangements:** Placing people with maximum spacing for comfort/safety.  
---
## 🏷️ Tags
- `#BinarySearch`  
- `#Greedy` 
- `#Arrays`  
- `#PlacementProblems`  
