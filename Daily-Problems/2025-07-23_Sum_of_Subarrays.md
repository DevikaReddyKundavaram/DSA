# 🧮 Problem: Sum of Subarrays

**Difficulty:** Medium  
---
## 🔍 Problem Statement

Given an array `arr[]`, find the **sum of all the subarrays** of the given array.

It is guaranteed that the total sum will fit within a 32-bit integer range.

---

## 🧪 Examples

### Example 1:
**Input:**  
`arr = [1, 2, 3]`  
**Output:**  
`20`  
**Explanation:**  
All subarray sums are:  
`[1] = 1`, `[2] = 2`, `[3] = 3`, `[1, 2] = 3`, `[2, 3] = 5`, `[1, 2, 3] = 6`  
Total sum = `1 + 2 + 3 + 3 + 5 + 6 = 20`

---

### Example 2:
**Input:**  
`arr = [1, 3]`  
**Output:**  
`8`  
**Explanation:**  
All subarray sums:  
`[1] = 1`, `[3] = 3`, `[1, 3] = 4`  
Total sum = `1 + 3 + 4 = 8`

---

## 🔐 Constraints:
- `1 ≤ arr.length ≤ 10^5`  
- `0 ≤ arr[i] ≤ 10^4`

---

## 💡 Optimized Approach (Contribution Technique)

Each element `arr[i]` appears in several subarrays:
- It contributes to all subarrays where it is between start `j` and end `k` such that `j ≤ i ≤ k`.
- That count is `(i + 1) * (n - i)` → total subarrays including `arr[i]`

- So the total contribution is:  
- total += arr[i] * (i + 1) * (n - i)
---
## ⏱️ Time & Space Complexity

| Metric          | Value  |
|------------------|--------|
| Time Complexity  | O(n)   |
| Space Complexity | O(1)   |

---

## ✅ Python Code:

```python
class Solution:
    def subarraySum(self, arr):
        total = 0
        n = len(arr)
        for i in range(n):
            total += arr[i] * (i + 1) * (n - i)
        return total
```
---

## 📚 Applications

- Calculating cumulative influence of elements in array segments  
- Useful in financial models where each item contributes to multiple subgroups  
- Base idea for advanced algorithms like Segment Trees, Fenwick Trees  

---

## 🏷️ Tags

`#Arrays`, `#Mathematics`, `#Subarrays`, `#PrefixSum`, `#ContributionTechnique`
