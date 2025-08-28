#  Max Consecutive 1s After Flips

## 🔹 Problem Statement  
You are given a binary array `arr[]` containing only `0s` and `1s`, and an integer `k`.  
You can flip **at most k zeros into ones**.  
Find the maximum number of consecutive `1s` possible after at most `k` flips.  

---

## 🔸 Examples  
```text
Example 1:
Input: arr = [1, 0, 1], k = 1
Output: 3
Explanation: Flip index 1 → [1, 1, 1]

Example 2:
Input: arr = [1, 0, 0, 1, 0, 1, 0, 1], k = 2
Output: 5
Explanation: Flip indices 4 & 6 → subarray [3..7] = [1,1,1,1,1]

Example 3:
Input: arr = [1, 1], k = 2
Output: 2
Explanation: Already maximum consecutive 1s
```
---

## 🔹 Constraints  
- `1 ≤ arr.size() ≤ 10^5`  
- `0 ≤ k ≤ arr.size()`  
- `0 ≤ arr[i] ≤ 1`

---

## 🔸 Approach — Sliding Window  
We use a **sliding window** (two-pointer technique).  

- Expand the window with `right`.  
- Count zeros in the window.  
- If `zero_count > k`, shrink from `left` until valid.  
- Track maximum window length.  
---
### 🔹 Complexity Analysis  

| Complexity | Value |
|------------|-------|
| **Time**   | `O(n)` |
| **Space**  | `O(1)` |

---

## 🔹 Code (Python)  
```python
class Solution:
    def maxOnes(self, arr, k):
        left = 0
        zero_count = 0
        max_len = 0
        
        for right in range(len(arr)):
            if arr[right] == 0:
                zero_count += 1
            
            while zero_count > k:
                if arr[left] == 0:
                    zero_count -= 1
                left += 1
            
            max_len = max(max_len, right - left + 1)
```
---
### 🔹 Applications  

- 📶 **Network Optimization** → Maximizing continuous signal strength by allowing limited error corrections.  
- 🧪 **Genomics** → Finding the longest valid gene sequence after flipping a limited number of mutations.  
- 💾 **Data Compression** → Handling limited noise by flipping bits to maximize continuous blocks.  
- 🎮 **Gaming** → Tracking maximum streaks with limited retries or corrections.  
- 📊 **Streaming Data** → Ensuring maximum uptime/active session streaks by tolerating a few failures.  
---
### 🏷️ Tags  
`#SlidingWindow` `#TwoPointers` `#Greedy` `#Arrays` `#Medium`  

        
        return max_len
