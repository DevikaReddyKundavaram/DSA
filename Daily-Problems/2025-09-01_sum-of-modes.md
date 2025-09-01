# 📘 Problem: Sum of Modes

## 🔹 Description
Given an array `arr[]` of positive integers and an integer `k`.  
You need to find the **sum of the modes** of all the subarrays of size `k`.

- **Mode of a subarray** = element that occurs with the highest frequency.  
- If multiple elements have the same frequency → choose the **smallest element**.

---

## 🔹 Example
```text
Example 1:
Input: arr = [1, 2, 3, 2, 5, 2, 4, 4], k = 3
Output: 13
Explanation:  
Modes = [1, 2, 2, 2, 2, 4] → sum = 13

Example 2:
Input: arr = [1, 2, 1, 3, 5], k = 2
Output: 6
Explanation:  
Modes = [1, 1, 1, 3] → sum = 6
```
---

## 🔹 Approach
1. Maintain frequency map (`freq`) of elements in the current window.  
2. Maintain `count_map`: maps frequency → **sorted list of elements**.  
3. Always keep track of `max_freq`.  
4. Mode = **smallest element in `count_map[max_freq]`**.  
5. Slide the window, updating structures in `O(log k)` using binary search insertion/deletion.  

---
## 🔹 Complexity Analysis

| Operation              | Time Complexity | Space Complexity |
|-------------------------|-----------------|-----------------|
| Insert into window      | O(log k)        | O(k)            |
| Remove from window      | O(log k)        | O(k)            |
| Find current mode       | O(1)            | O(1)            |
| Process entire array    | O(n log k)      | O(k)            |

✅ **Overall Complexity**:  
- **Time** → `O(n log k)`  
- **Space** → `O(k)`  
---

## 🔹 Code (Python)

```python
from collections import defaultdict
import bisect

class Solution:
    def sumOfModes(self, arr, k):
        n = len(arr)
        if k > n: return 0
        
        freq = defaultdict(int)
        count_map = defaultdict(list)   # freq -> sorted list of elements
        max_freq = 0
        res = 0
        
        def add(x):
            nonlocal max_freq
            old = freq[x]
            new = old + 1
            freq[x] = new
            if old > 0:
                lst = count_map[old]
                idx = bisect.bisect_left(lst, x)
                if idx < len(lst) and lst[idx] == x:
                    lst.pop(idx)
            bisect.insort(count_map[new], x)
            max_freq = max(max_freq, new)
        
        def remove(x):
            nonlocal max_freq
            old = freq[x]
            if old == 0: return
            new = old - 1
            freq[x] = new
            lst = count_map[old]
            idx = bisect.bisect_left(lst, x)
            if idx < len(lst) and lst[idx] == x:
                lst.pop(idx)
            if new > 0:
                bisect.insort(count_map[new], x)
            if not count_map[max_freq]:
                max_freq -= 1
        
        # First window
        for i in range(k):
            add(arr[i])
        res += count_map[max_freq][0]
        
        # Slide window
        for i in range(k, n):
            remove(arr[i-k])
            add(arr[i])
            res += count_map[max_freq][0]
        
        return res
```
---
## 🚀 Applications

- **Data Stream Analysis** → Useful for finding the most frequent element in real-time sliding windows.  
- **Network Monitoring** → Detects most common packet types in the last `k` packets.  
- **Recommendation Systems** → Identifies trending items in a fixed-size user activity window.  
- **Text Processing** → Finds the most frequent word/character in a rolling set of sentences.  
- **Fraud Detection** → Spots frequently repeated transactions within a time window.  
---
## 🏷️ Tags  

`#SlidingWindow` `#HashMap` `#FrequencyCounting` `#Heap` `#GreedyLogic`
