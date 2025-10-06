# ⚡Minimum K Consecutive Bit Flips 

## Problem Statement
You are given a binary array `arr[]` (containing only 0's and 1's) and an integer `k`. In one operation, you can select a contiguous subarray of length `k` and flip all its bits (i.e., change every 0 to 1 and every 1 to 0).

Your task is to find the **minimum number of such operations** required to make the entire array consist of only 1's. If it is not possible, return `-1`.

---

## Examples
```text
Example 1:
Input: arr = [1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1], k = 2
Output: 4
Explanation:  
- Flip subarray [2, 3]: `[1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1]`  
- Flip subarray [4, 5]: `[1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1]`  
- Flip subarray [5, 6]: `[1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1]`  
- Flip subarray [6, 7]: `[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]`

Example 2:
Input: arr = [0, 0, 1, 1, 1, 0, 0], k = 3
Output: -1
Explanation: It is not possible to convert all elements to 1's by performing any number of operations.
```
---

## Constraints
- `1 ≤ arr.size() ≤ 10^6`  
- `1 ≤ k ≤ arr.size()`  

---

## Algorithm
1. Initialize a `flip` array of size `n` to keep track of flips ending at each position.  
2. Use `curr_flips` to maintain the **current number of active flips**.  
3. Iterate through the array:
    - If a flip ended `k` steps before, remove its effect from `curr_flips`.
    - If the current element after applying `curr_flips` is 0, flip starting from this position:
        - If flipping exceeds array bounds, return -1.
        - Increment answer and update `curr_flips` and `flip` array.
4. Return the total number of flips needed.

---

## Time and Space Complexity
- **Time Complexity:** `O(n)` — Each element is visited once.  
- **Space Complexity:** `O(n)` — For the `flip` array.

---

## Code

```python
class Solution:
    def kBitFlips(self, arr, k):
        n = len(arr)
        flip = [0] * n   # Track where flips end
        curr_flips = 0   # Current number of active flips
        ans = 0

        for i in range(n):
            # Remove effect of a flip that ended k steps before
            if i >= k:
                curr_flips ^= flip[i - k]
            
            # If current element is 0 after flips, flip starting here
            if (arr[i] ^ curr_flips) == 0:
                if i + k > n:  # Not enough space left
                    return -1
                ans += 1
                curr_flips ^= 1
                flip[i] = 1
        
        return ans
```
---
## Applications 
- **Error Correction:** Fixing errors in binary sequences by flipping bits in blocks.  
- **Hardware Simulation:** Optimizing operations in digital circuits that manipulate bits.  
- **Data Compression:** Transforming binary sequences efficiently.  
- **Competitive Programming:** Solving sliding window and greedy bit-manipulation problems.  
- **Network Protocols:** Correcting bursts of errors in transmitted data.
---
## 🏷️Tags
`#Greedy` `#SlidingWindow` `#BitManipulation` `#Queue` `#Array` `#DataStructures`
