# 📚 Allocate Minimum Pages  

## 📌 Problem Statement  
You are given an array `arr[]` of integers, where each element `arr[i]` represents the number of pages in the i-th book. You also have an integer `k` representing the number of students.  

The task is to allocate books to each student such that:  
1. Each student receives **at least one book**.  
2. Each student is assigned a **contiguous sequence of books**.  
3. No book is assigned to more than one student.  

The objective is to **minimize the maximum number of pages assigned to any student**.  

👉 If it is not possible to allocate books to all students, return `-1`.  

### Examples  
```text
Example 1:
Input: arr = [12, 34, 67, 90], k = 2
Output: 113
Explanation:  
Possible allocations:  
- [12] and [34, 67, 90] → max = 191  
- [12, 34] and [67, 90] → max = 157  
- [12, 34, 67] and [90] → max = 113 ✅ (minimum possible maximum).  

Example 2: 
Input: arr = [15, 17, 20], k = 5
Output: -1
Explanation: There are more students than books → impossible allocation.  
```
---
### Constraints  
- `1 ≤ arr.size() ≤ 10^6`  
- `1 ≤ arr[i], k ≤ 10^3`  

---

## ⚡ Algorithm / Approach  

1. **Check feasibility:** If `k > len(arr)`, return `-1` immediately (not enough books).  
2. **Binary Search on Answer:**  
   - The minimum possible pages = `max(arr)` (since one student must get the thickest book).  
   - The maximum possible pages = `sum(arr)` (one student gets all books).  
   - Perform binary search in this range to minimize the maximum pages.  
3. **Validation function:** For a candidate value `mid`, check if allocation is possible:  
   - Traverse books and assign them sequentially.  
   - If the current sum exceeds `mid`, assign the books to a new student.  
   - Count how many students are required.  
   - If required students > `k`, allocation is not possible.  
4. The smallest feasible `mid` is the answer.  

---

## ⏳ Time & Space Complexity  

- **Time Complexity:** `O(n log(sum(arr)))`  
  - Each binary search iteration → O(n) check.  
  - Range = sum(arr) → log(sum(arr)) steps.  
- **Space Complexity:** `O(1)`  

---

## 💻 Code (Python)  

```python
class Solution:
    def findPages(self, arr, k):
        n = len(arr)
        
        # If more students than books → not possible
        if k > n:
            return -1

        # Function to check if allocation possible with maxPages = mid
        def is_possible(mid):
            students, pages = 1, 0
            for a in arr:
                if pages + a > mid:
                    students += 1
                    pages = a
                    if students > k:
                        return False
                else:
                    pages += a
            return True

        low, high = max(arr), sum(arr)
        result = -1

        while low <= high:
            mid = (low + high) // 2
            if is_possible(mid):
                result = mid
                high = mid - 1  # try smaller maximum
            else:
                low = mid + 1  # need larger maximum

        return result
```
---
## 🌍 Applications  

- **Library & Resource Allocation:** Assigning books (or resources) to minimize overload on any student.  
- **Workload Distribution:** Assigning tasks to workers while minimizing the maximum workload.  
- **Server Load Balancing:** Distributing requests or jobs across servers to reduce peak load.  
- **Project Scheduling:** Assigning sequential tasks to teams while balancing workload.  
- **Educational Platforms:** Splitting chapters/modules among groups of students or teachers fairly.  
---

## 🏷️ Tags  
`#BinarySearch`, `#Greedy`, `#Arrays`, `#Allocation`, `#Medium`
