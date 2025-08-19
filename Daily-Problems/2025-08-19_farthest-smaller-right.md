# 🧩 Problem: Farthest Smaller Right

## 📌 Problem Statement
You are given an array `arr[]`.  
For each element at index `i` (0-based indexing), find the **farthest index `j` to the right** (where `j > i`) such that `arr[j] < arr[i]`.  
If no such index exists for a given position, return `-1` for that index.  
Return the resulting array of answers.

---

## ✨ Examples
```text
Example 1:
Input: arr[] = [2, 5, 1, 3, 2]
Output: [2, 4, -1, 4, -1]
Explanation:
- arr[0] = 2 → farthest smaller is arr[2] = 1 → index 2  
- arr[1] = 5 → farthest smaller is arr[4] = 2 → index 4  
- arr[2] = 1 → no smaller element to the right → -1  
- arr[3] = 3 → farthest smaller is arr[4] = 2 → index 4  
- arr[4] = 2 → no elements to the right → -1  

Example 2:
Input: arr[] = [2, 3, 5, 4, 1]
Output: [4, 4, 4, 4, -1]
Explanation: 
- arr[4] is the farthest smaller element to the right for arr[0], arr[1], arr[2], arr[3].  
- arr[4] has no elements after it → -1  
```
---


## ⚙️ Algorithm
1. **Preprocessing with Suffix Minima:**  
   - Create a suffix minima array `suff[]` where `suff[i] = min(arr[i..n-1])`.  
   - This helps to quickly check if a smaller element exists in the right segment.

2. **Binary Search for Farthest Smaller:**  
   - For each index `i`, apply binary search on the suffix minima range `[i+1 … n-1]`.  
   - Keep track of the **rightmost index `j`** where `suff[j] < arr[i]`.  

3. **Store Results:**  
   - If found, record the farthest index `j`.  
   - Else, assign `-1`.  

---

## ⏱️ Complexities
- **Time Complexity:**  
  - Building suffix minima: **O(n)**  
  - Binary search for each element: **O(log n)**  
  - Overall: **O(n log n)**  
- **Space Complexity:**  
  - Extra suffix array: **O(n)**  

---

## 🧑‍💻 Code (Python)
```python
class Solution:
    def farMin(self, arr):
        n = len(arr)
        ans = [-1] * n

        # Step 1: Build suffix minima array
        suff = arr.copy()
        for i in range(n - 2, -1, -1):
            suff[i] = min(arr[i], suff[i + 1])

        # Step 2: Binary search for farthest smaller
        for i in range(n):
            lo, hi, res = i + 1, n - 1, -1
            while lo <= hi:
                mid = (lo + hi) // 2
                if suff[mid] < arr[i]:
                    res = mid
                    lo = mid + 1  # go farther right
                else:
                    hi = mid - 1
            ans[i] = res

        return ans
```
---
## 🚀 Applications

1. **Stock Market Analysis**  
   - Helps in finding the farthest future day with a lower stock price compared to today.  
   - Useful for predicting selling/buying strategies.  

2. **Competitive Programming Problems**  
   - Common in array manipulation and range-query based problems.  
   - Appears in coding contests like GFG, LeetCode, and Codeforces.  

3. **Data Compression & Encoding**  
   - Identifies farthest smaller values to optimize run-length encoding or delta compression.  

4. **Scheduling & Resource Allocation**  
   - In tasks or job scheduling, helps to decide the farthest point where a lower workload/resource requirement exists.  

5. **Game Development**  
   - Used for tracking farthest smaller positions (e.g., in character movement or obstacle detection).  

6. **Algorithmic Research**  
   - Acts as a base problem to study variations of "Next Greater/Smaller Element" concepts.  
---
## 🏷️ Tags:
`#BinarySearch` `#SuffixArray` `#Arrays` `#Searching` `#CustomComparator` `#RangeQueries` `#MonotonicProperties` `#GFG`  

