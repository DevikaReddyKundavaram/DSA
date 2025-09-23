# 📏 Max of Min for Every Window Size

## Problem Statement
You are given an integer array `arr[]`. The task is to find the **maximum of minimum values** for every window size `k` where `1 ≤ k ≤ arr.size()`.

For each window size `k`:
- Consider all contiguous subarrays of length `k`.
- Determine the minimum element in each subarray.
- Take the **maximum among all these minimums**.

Return the results as an array, where the element at index `i` represents the answer for window size `i+1`.

---

## Examples
```text
Example1
Input: arr[] = [10, 20, 30, 50, 10, 70, 30]  
Output: [70, 30, 20, 10, 10, 10, 10]  

Explanation:
- Window size 1: minimums are [10, 20, 30, 50, 10, 70, 30], max = 70  
- Window size 2: minimums are [10, 20, 30, 10, 10, 30], max = 30  
- Window size 3: minimums are [10, 20, 10, 10, 10], max = 20  
- Window size 4–7: minimums are [10, 10, 10, 10], max = 10  

Example2
Input: arr[] = [10, 20, 30]
Output:  [30, 20, 10]
```
---

## Constraints
- `1 ≤ arr.size() ≤ 10^5`  
- `1 ≤ arr[i] ≤ 10^6`  

---
## Algorithm

1. **Initialize arrays**:  
   - `left[i]` to store the index of the **previous smaller element** for `arr[i]`.  
   - `right[i]` to store the index of the **next smaller element** for `arr[i]`.  
   - Use a **stack** to help compute these efficiently.

2. **Find Previous Smaller elements**:  
   - Traverse the array from left to right.  
   - For each element, pop from the stack until the top element is smaller than the current element.  
   - Assign `left[i] = index of previous smaller element` (or -1 if none).  
   - Push the current index onto the stack.

3. **Find Next Smaller elements**:  
   - Clear the stack.  
   - Traverse the array from right to left.  
   - For each element, pop from the stack until the top element is smaller than the current element.  
   - Assign `right[i] = index of next smaller element` (or n if none).  
   - Push the current index onto the stack.

4. **Calculate maximum of minimums for every window length**:  
   - For each element `arr[i]`, calculate `length = right[i] - left[i] - 1`.  
   - Update `res[length] = max(res[length], arr[i])`.

5. **Fill remaining positions**:  
   - Traverse `res` from right to left to ensure all window sizes are filled with the correct maximum of minimums.  

6. **Return** the result array excluding the dummy 0th index: `res[1:]`.
---
## Complexities

- **Time Complexity**: `O(n)`  
  - Finding previous smaller and next smaller elements takes `O(n)` using a stack.  
  - Filling the result array also takes `O(n)`.  
  - Overall: `O(n)`.

- **Space Complexity**: `O(n)`  
  - Arrays `left`, `right`, `res`, and the `stack` use linear extra space.
---
## Solution (Python3)
```python
class Solution:
    def maxOfMins(self, arr):
        n = len(arr)
        left = [-1] * n
        right = [n] * n
        stack = []

        # Previous smaller
        for i in range(n):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            left[i] = stack[-1] if stack else -1
            stack.append(i)

        stack.clear()

        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            right[i] = stack[-1] if stack else n
            stack.append(i)

        res = [0] * (n + 1)
        for i in range(n):
            length = right[i] - left[i] - 1
            res[length] = max(res[length], arr[i])

        for i in range(n - 1, 0, -1):
            res[i] = max(res[i], res[i + 1])

        return res[1:]
```
---
## Applications

- **Stock Market Analysis**: Determine the maximum minimum price for different time windows to analyze worst-case trends.  
- **Sliding Window Optimization**: Useful in scenarios where windowed minimums and maximums are required for performance monitoring or resource allocation.  
- **Signal Processing**: Analyze minimum values over sliding intervals to detect noise or signal drops.  
- **Histogram and Area Analysis**: Can be used in computing maximum rectangle areas in histograms efficiently.  
- **Competitive Programming**: Helps in solving many range query and subarray optimization problems efficiently.
---

## 🏷️Tags
`#Stack` `#NextSmallerElement` `#SlidingWindow` `#MonotonicStack` `#Array` `#RangeQuery` `#Optimization`
