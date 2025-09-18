# Next Greater Element in Circular Array

## 📌 Problem Statement
Given a circular integer array `arr[]`, the task is to determine the **next greater element (NGE)** for each element in the array.

The next greater element of an element `arr[i]` is the first element that is greater than `arr[i]` when traversing **circularly**. If no such element exists, return `-1` for that position.

---

## ✅ Examples
```text
Example 1
Input: arr = [1, 3, 2, 4]
Output: [3, 4, 4, -1]
Explanation:
- The next greater element for 1 is 3.
- The next greater element for 3 is 4.
- The next greater element for 2 is 4.
- The next greater element for 4 does not exist, so return -1.

Example 2
Input: arr = [0, 2, 3, 1, 1]
Output: [2, 3, -1, 2, 2]
Explanation:
- The next greater element for 0 is 2.
- The next greater element for 2 is 3.
- The next greater element for 3 does not exist, so return -1.
- The next greater element for 1 is 2 (from circular traversal).
- The next greater element for 1 is 2 (from circular traversal).
```
---

## 🔑 Constraints
- `1 ≤ arr.size() ≤ 10^5`  
- `0 ≤ arr[i] ≤ 10^6`  

---

## 💡 Approach
1. Since the array is **circular**, we need to traverse it **twice**.
2. Use a **monotonic stack** to store indices of elements whose next greater element is not yet found.
3. Traverse the array from **right → left** (simulate circularity).
4. For each element:
   - Pop smaller/equal elements from the stack.
   - If stack is not empty, the **top element is the NGE**.
   - Otherwise, mark `-1`.
   - Push current index into stack.

---

## 📝 Code (Python)

```python
class Solution:
    def nextGreater(self, arr):
        n = len(arr)
        res = [-1] * n   # result array
        st = []          # stack to store indices

        # traverse 2n times (circular array)
        for i in range(2 * n - 1, -1, -1):
            while st and arr[st[-1]] <= arr[i % n]:
                st.pop()
            if st:
                res[i % n] = arr[st[-1]]
            st.append(i % n)
        
        return res
```
---
## 📌 Applications

- 🔹 **Stock Span Problems** – Finding the next higher stock price in circular stock data.  
- 🔹 **Weather Forecasting** – Predicting the next hotter day in a cyclic temperature record.  
- 🔹 **Circular Scheduling** – Task/CPU scheduling where processes repeat in cycles.  
- 🔹 **Data Stream Processing** – Identifying the next higher element in continuous circular streams.  
- 🔹 **Competitive Programming** – Common pattern in array/stack-based problems.  
---
## 🏷️ Tags
- `#Array`  
- `#Stack`  
- `#MonotonicStack`  
- `#NextGreaterElement`  
- `#CircularArray`  

