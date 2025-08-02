# 📊 Longest Subarray with Majority Greater than K


## 🧩 Problem Statement

Given an array `arr[]` and an integer `k`, find the length of the **longest subarray** in which the **count of elements greater than `k` is more than** the **count of elements less than or equal to `k`**.

---

## 🔍 Examples

### Example 1:
**Input:**  
`arr = [1, 2, 3, 4, 1]`, `k = 2`  
**Output:**  
`3`  
**Explanation:**  
Subarrays `[2, 3, 4]` or `[3, 4, 1]` both have more elements > 2 than ≤ 2. No subarray of length 4 or 5 satisfies the condition.

### Example 2:
**Input:**  
`arr = [6, 5, 3, 4]`, `k = 2`  
**Output:**  
`4`  
**Explanation:**  
All elements are greater than 2.

---

## 📘 Constraints

- `1 ≤ arr.size() ≤ 10^6`
- `1 ≤ arr[i] ≤ 10^6`
- `0 ≤ k ≤ 10^6`

---

## 💡 Approach

### ✅ Step-by-Step:

1. **Transform the array**:
   - Replace each element with:
     - `+1` if `arr[i] > k`
     - `-1` if `arr[i] <= k`

2. **Use Prefix Sum + Hash Map**:
   - We now need to find the **longest subarray with a positive sum**.
   - Keep a running `prefix_sum` and a dictionary to store the **first occurrence** of each prefix sum.
   - Update `max_len` whenever we find a valid subarray.

---

## 🧠 Intuition

- If a subarray has a positive sum after transformation, it means:
  - There are **more elements > k** than `<= k`.
- We use prefix sums to track this and efficiently find the longest such subarray.

---
## 🕒 Time & Space Complexities

### ⏱ Time Complexity: `O(n)`
- **Transform Step:** Creating the transformed array (`+1` for elements > `k`, `-1` otherwise) takes `O(n)` time.
- **Main Logic Loop:** Iterating through the array to compute prefix sums and use the hashmap takes another `O(n)` time.
- **Hashmap Access:** Insertions and lookups in the hashmap are constant time on average (`O(1)`).
- **Total:** `O(n)`

### 📦 Space Complexity: `O(n)`
- **Transformed Array:** The `diff` array holds `n` elements → `O(n)`.
- **HashMap:** Stores first occurrences of prefix sums. In the worst case, we may store up to `n` unique values → `O(n)`.
- **Total:** `O(n)`
---

## 🧾 Python Code

```python
class Solution:
    def longestSubarray(self, arr, k):
        # Step 1: Transform the array
        diff = [1 if num > k else -1 for num in arr]

        prefix_sum = 0
        max_len = 0
        first_occurrence = {0: -1}  # prefix_sum: index

        for i, val in enumerate(diff):
            prefix_sum += val

            # If prefix_sum > 0, subarray from 0 to i is valid
            if prefix_sum > 0:
                max_len = i + 1
            else:
                # Check if (prefix_sum - 1) existed before
                if (prefix_sum - 1) in first_occurrence:
                    max_len = max(max_len, i - first_occurrence[prefix_sum - 1])
            
            # Store the first occurrence of this prefix_sum
            if prefix_sum not in first_occurrence:
                first_occurrence[prefix_sum] = i

        return max_len
```

---
## 🚀 Applications

The technique used in solving this problem — **prefix sum with hashmap for subarray conditions** — is widely applicable in many real-world and coding interview scenarios. Some key applications include:

### 1. **Competitive Programming & Interviews**
- Frequently used in problems where subarrays must satisfy conditions like:
  - Sum > 0
  - Number of 1’s > number of 0’s
  - Majority element detection in subarrays

### 2. **Data Stream Analysis**
- Real-time analysis of streaming data where we want to monitor trends or thresholds crossing over time using sliding windows or prefix counts.

### 3. **Sentiment Analysis**
- If values are mapped to sentiment (+1 for positive, -1 for negative), this approach can find the longest time period with positive sentiment dominance.

### 4. **Stock Market Analytics**
- Track time windows (subarrays) where the number of gains is more than losses to evaluate investor confidence or market strength.

### 5. **Sensor Data Monitoring**
- In IoT or embedded systems, determining time spans where good readings (above a threshold) dominate poor readings.

### 6. **Binary Array Subproblems**
- Solving classic problems like:
  - Longest subarray with equal number of 0s and 1s
  - Longest subarray with more 1s than 0s (very similar logic!)

### 7. **Voting & Polling Analysis**
- Track windows where support for a candidate/product is greater than opposition/neutral votes.

---
## 🏷️ Tags

`Array` &nbsp; `Subarray` &nbsp; `Prefix Sum` &nbsp; `HashMap` &nbsp; `Sliding Window`  
`Majority Element` &nbsp; `Greedy` &nbsp; `Competitive Programming` &nbsp; `Algorithms` &nbsp; `Coding Interview`

