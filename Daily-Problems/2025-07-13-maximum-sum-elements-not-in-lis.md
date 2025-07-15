# 🚀 Maximum Sum of Elements Not in Longest Increasing Subsequence (LNDS)

## 📝 Problem Statement
Given an array `arr[]` of positive integers, your task is to find the **maximum possible sum of all elements that are not part of the Longest Non-Decreasing Subsequence (LNDS)**. Among all possible LNDS of the same length, choose the one with the maximum sum.

Finally, return the total sum of the array minus the sum of elements in the LNDS.

---

## 🔔 Examples

### Input:
arr = [4, 7, 5, 3, 7, 7, 1, 4, 8]

### Output:
22


### Explanation:
LNDS: `[3, 7, 7, 7]`  
Sum of LNDS: `3 + 7 + 7 + 7 = 24`  
Total Sum: `46`  
Answer: `46 - 24 = 22`

---

# 💡 Algorithm 1️⃣ — **Dynamic Programming (O(N²))**

### Steps:
1. Use `dp_len[i]` to track the longest non-decreasing subsequence length ending at index `i`.
2. Use `dp_sum[i]` to track the maximum sum of such subsequences ending at index `i`.
3. For every `j < i`, if `arr[i] >= arr[j]`:
    - Update `dp_len[i]` and `dp_sum[i]` accordingly.
    - Prefer longer sequences first, and larger sums next.
4. Return `total sum - max subsequence sum`.

---

## ⏳ Time Complexity (DP)
| Step                         | Complexity  |
|-------------------------------|-------------|
| Outer Loop (i)                | O(N)        |
| Inner Loop (j < i)            | O(N)        |
| **Total**                     | **O(N²)**   |

---

## 🛑 Space Complexity (DP)
- `O(N)` for `dp_len[]`
- `O(N)` for `dp_sum[]`

---

## 🧑‍💻 Solution Code (DP)

```python
class Solution:
    def nonLisMaxSum(self, arr):
        n = len(arr)
        dp_len = [1] * n
        dp_sum = arr[:]

        for i in range(n):
            for j in range(i):
                if arr[i] >= arr[j]:
                    if dp_len[j] + 1 > dp_len[i]:
                        dp_len[i] = dp_len[j] + 1
                        dp_sum[i] = dp_sum[j] + arr[i]
                    elif dp_len[j] + 1 == dp_len[i]:
                        dp_sum[i] = max(dp_sum[i], dp_sum[j] + arr[i])

        max_len = max(dp_len)
        max_sum = max(dp_sum[i] for i in range(n) if dp_len[i] == max_len)

        total_sum = sum(arr)
        return total_sum - max_sum
```

## 💡 Algorithm — Using Bisect / Binary Search (O(N log N))

### Steps:
1. Maintain an array `lis[]` where `lis[i]` stores the index of the smallest possible ending element of a non-decreasing subsequence of length `i+1`.
2. Maintain a `prev[]` array to help reconstruct the LNDS.
3. For each element `arr[i]`:
   - Use `bisect_left` on `arr[lis]` to find the first element greater than or equal to `arr[i]`.
   - Update `lis[]` at the found position.
   - Update `prev[i]` to point to the previous index of the subsequence.
4. Rebuild the LNDS from the `prev[]` array and calculate its sum.
5. Return `total_sum - lnds_sum`.

---

## ⏳ Time Complexity (Bisect)
| Step                         | Complexity  |
|-------------------------------|-------------|
| Binary Search for each element| O(log N)    |
| Total for N elements          | O(N log N)  |
| Reconstruct LNDS sum          | O(N)        |
| **Total**                     | **O(N log N)** |

---

## 🛑 Space Complexity (Bisect)
- `O(N)` for `prev[]`
- `O(N)` for `lis[]`
- **Total: O(N)**

---

## 🧑‍💻 Solution Code (Bisect)

```python
from bisect import bisect_left
class Solution:
    def nonLisMaxSum(self, arr):
        n = len(arr)
        prev = [-1] * n
        total_sum = arr[0]
        lis = [0]
        for i in range(1, n):
            total_sum += arr[i]
            j = bisect_left(lis, arr[i], key=lambda k: arr[k])
            if j == 0:
                lis[0] = i
            else:
                prev[i] = lis[j - 1]
                if j == len(lis):
                    lis.append(i)
                else:
                    lis[j] = i
        lis_sum = 0
        i = lis[-1]
        while i != -1:
            lis_sum += arr[i]
            i = prev[i]
        return total_sum - lis_sum
```

## 📚 Applications of This Problem / Approach

- **Sequence Optimization Problems**  
  Useful when identifying parts of data that contribute least to an optimal subsequence.

- **Stock Market Analysis**  
  Helps in identifying days or prices that break a growing or stable trend.

- **Data Compression Algorithms**  
  Finding non-decreasing patterns assists in reducing redundancy.

- **Game Development / Level Design**  
  Useful in scenarios where sequences of increasing challenges or rewards need to be maintained while minimizing distractions.

- **Competitive Programming**  
  Strengthens concepts of Dynamic Programming, Binary Search, and Subsequence Patterns.

- **Memory Management Systems**  
  Helps analyze sequences of memory allocations/deallocations where stability patterns matter.

- **AI / Machine Learning Preprocessing**  
  Identifying outliers or noise that disrupts trends in sequential data.

---
**Tags:** `#DynamicProgramming`, `#BinarySearch`, `#LongestNonDecreasingSubsequence`, `#Subsequence`, `#Greedy`, `#Array`, `#MaximumSum`, `#Optimization`, `#CompetitiveProgramming`
