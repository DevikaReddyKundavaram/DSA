# Longest Subarray Length

---
## Problem Statement
You are given an array of integers `arr[]`.  
Your task is to find the **length of the longest subarray** such that **all the elements of the subarray are smaller than or equal to the length of the subarray**.

---

## Examples
```text
Example 1
Input: arr[] = [1, 2, 3]
Output: 3
Explanation:
The longest subarray is the entire array itself, which has a length of 3.  
All elements in the subarray are less than or equal to 3.  

Example 2
Input: arr[] = [6, 4, 2, 5]  
Output: 0
Explanation:
There is no subarray where all elements are less than or equal to the length of the subarray.  
The longest subarray is empty, which has a length of 0.  
```
---

## Constraints
- `1 ≤ arr.size() ≤ 10^5`  
- `1 ≤ arr[i] ≤ 10^9`  

---
## Algorithm for Longest Subarray Length

1. **Initialize structures**  
   - Create two arrays:
     - `nextGreater[]` (size `n`) initialized with `n` → stores the index of the next greater element to the right.  
     - `prevGreater[]` (size `n`) initialized with `-1` → stores the index of the previous greater element to the left.  
   - Create an empty stack `st`.
2. **Find Next Greater Element (NGE) for each element**  
   - Traverse the array from **left to right**:  
     - While stack is not empty and `arr[st.top()] < arr[i]`,  
       update `nextGreater[st.top()] = i` and pop the stack.  
     - Push `i` onto the stack.

3. **Find Previous Greater Element (PGE) for each element**  
   - Clear the stack.  
   - Traverse the array from **right to left**:  
     - While stack is not empty and `arr[st.top()] < arr[i]`,  
       update `prevGreater[st.top()] = i` and pop the stack.  
     - Push `i` onto the stack.
4. **Check possible subarray length for each element**  
   - For each index `i`:  
     - Compute `windowSize = nextGreater[i] - prevGreater[i] - 1`.  
     - If `windowSize >= arr[i]`,  
       update `maxLength = max(maxLength, windowSize)`.

5. **Return result**  
   - The final answer is `maxLength`.  

### Key Idea
- `windowSize` represents the maximum subarray length where `arr[i]` is the largest element.  
- If that subarray length is at least `arr[i]`, then it is a valid subarray.  
- We maximize over all such possible subarrays.  
---
## Time and Space Complexities

- **Time Complexity:**  
  - Finding Next Greater Elements (NGE) → `O(n)`  
  - Finding Previous Greater Elements (PGE) → `O(n)`  
  - Final traversal to compute window size and check condition → `O(n)`  
  - **Overall:** `O(n)`  

- **Space Complexity:**  
  - Arrays `nextGreater[]` and `prevGreater[]` → `O(n)`  
  - Stack used for NGE and PGE computation → `O(n)` in worst case  
  - **Overall:** `O(n)`  
---

## Python Implementation

```python
from collections import deque

class Solution:
    def longestSubarray(self, arr):
        n = len(arr)

        nextGreater = [n] * n
        prevGreater = [-1] * n

        st = []

        for i in range(n):
            while st and arr[st[-1]] < arr[i]:
                nextGreater[st.pop()] = i
            st.append(i)

        st.clear()

        for i in range(n - 1, -1, -1):
            while st and arr[st[-1]] < arr[i]:
                prevGreater[st.pop()] = i
            st.append(i)

        maxLength = 0
        for i in range(n):
            windowSize = nextGreater[i] - prevGreater[i] - 1
            if windowSize >= arr[i]:
                maxLength = max(maxLength, windowSize)

        return maxLength
```
---
## Applications

- **Performance Analysis:**  
  Helps in finding segments of processes/tasks that can fit within a resource limit defined by subarray size.  

- **Data Stream Analysis:**  
  Useful for checking bounded subsequences in real-time data where values must not exceed subarray length.  

- **Scheduling & Resource Allocation:**  
  Ensures all jobs/tasks in a window can be executed within available slots.  

- **Array & Subarray Pattern Problems:**  
  The technique of using Next Greater and Previous Greater elements is widely used in problems like:  
  - Largest Rectangle in Histogram  
  - Sliding Window Maximum  
  - Range Queries  

- **Constraint Validation:**  
  Checking if elements of a subsequence meet length-based restrictions efficiently.
---
## Tags
`#Array` `#Stack` `#MonotonicStack` `#NextGreaterElement` `#Subarray` `#SlidingWindow` `#RangeQuery`
