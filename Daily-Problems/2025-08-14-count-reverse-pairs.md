## Count Reverse Pairs


## Problem Statement
You are given an array `arr[]` of positive integers, find the count of **reverse pairs**.  
A pair of indices `(i, j)` is said to be a **reverse pair** if:

1. `0 ≤ i < j < arr.size()`
2. `arr[i] > 2 * arr[j]`

---

## Examples
```text
Example 1:
Input: arr[] = [3, 2, 4, 5, 1, 20] 
Output: 3

Explanation: Reverse pairs are: (0, 4): 3 > 21 (2, 4): 4 > 21 (3, 4): 5 > 2*1

Example 2:

Input: arr[] = [5, 4, 3, 2, 2] 
Output: 2

Explanation: Reverse pairs are: (0, 3): 5 > 22 (0, 4): 5 > 22
```
---

## Constraints
- `1 ≤ arr.size() ≤ 5 * 10^4`
- `1 ≤ arr[i] ≤ 10^9`

---

## Approach

We can solve this efficiently using **Modified Merge Sort** in O(n log n):

1. **Divide** the array into two halves recursively.
2. **Count cross pairs**:  
   For each element in the left half, count how many elements in the right half satisfy `arr[i] > 2 * arr[j]`.
3. **Merge** the two halves while maintaining sorted order.
4. **Sum counts**: Total reverse pairs = pairs in left + pairs in right + cross pairs.

---
## ⏳ Complexities
- **Time Complexity:** O(n log n) — due to modified merge sort  
- **Space Complexity:** O(n) — extra space for temporary arrays during merge
---

## Code (Python)
```python
class Solution:
    def countRevPairs(self, arr):
        def merge_sort(nums, left, right):
            if left >= right:
                return 0
            mid = (left + right) // 2
            count = merge_sort(nums, left, mid) + merge_sort(nums, mid + 1, right)
            
            # Count cross pairs
            j = mid + 1
            for i in range(left, mid + 1):
                while j <= right and nums[i] > 2 * nums[j]:
                    j += 1
                count += (j - (mid + 1))
            
            # Merge step
            temp = []
            i, j = left, mid + 1
            while i <= mid and j <= right:
                if nums[i] <= nums[j]:
                    temp.append(nums[i])
                    i += 1
                else:
                    temp.append(nums[j])
                    j += 1
            while i <= mid:
                temp.append(nums[i])
                i += 1
            while j <= right:
                temp.append(nums[j])
                j += 1
            
            nums[left:right + 1] = temp
            return count
        
        return merge_sort(arr, 0, len(arr) - 1)

```
---
## Applications

- **Competitive Programming** – Efficiently counts constrained pairs in large datasets, often used in advanced problems.
- **Financial Analysis** – Detects unusual market movements by identifying instances where a value sharply exceeds another relative threshold.
- **Signal Processing** – Finds sudden changes or anomalies in a sequence of signals.
- **Data Compression** – Helps in identifying patterns where certain values dominate over others, optimizing compression strategies.
- **Algorithm Learning** – Demonstrates divide-and-conquer with counting logic, reinforcing merge sort modifications.
---
## 🏷️ Tags
'#DivideAndConquer',
'#MergeSort',
'#BinarySearch',
'#Sorting',
'#TwoPointers',
'#AdvancedCounting'
'#CompetitiveProgramming'
