# 📘 Problem: Subarrays with Sum K

## 📜 Problem Statement

Given an unsorted array `arr[]` of integers, find the number of subarrays whose sum is exactly equal to a given number `k`.

---

## 🧾 Input

- `arr[]`: List of integers
- `k`: Target sum (integer)

---

## 🧮 Output

- Return the number of subarrays with sum exactly equal to `k`.

---

## 🧪 Examples

### Example 1:
- Input: arr = [10, 2, -2, -20, 10], k = -10
- Output:3
- Explanation: Subarrays: [10, 2, -2, -20], [2, -2, -20, 10], [-20, 10]

### Example 2:

- Input: arr = [9, 4, 20, 3, 10, 5], k = 33
- Output: 2
- Explanation: Subarrays: [9, 4, 20], [20, 3, 10]

---

## 🧠 Algorithm

1. Initialize `prefix_sum = 0`, `count = 0`, and a hashmap `freq = {0: 1}`.
2. Iterate through the array:
   - Add current element to `prefix_sum`.
   - Check if `prefix_sum - k` exists in `freq` → if yes, add its frequency to `count`.
   - Update frequency map: `freq[prefix_sum] += 1`
3. Return `count`.

---

## 🧪 Dry Run

**Input:**  
`arr = [10, 2, -2, -20, 10]`, `k = -10`

| i | arr[i] | prefix_sum | prefix_sum - k | freq lookup | count | freq updated                        |
|---|--------|------------|----------------|-------------|-------|-------------------------------------|
| 0 | 10     | 10         | 20             | 0           | 0     | `{0: 1, 10: 1}`                      |
| 1 | 2      | 12         | 22             | 0           | 0     | `{0: 1, 10: 1, 12: 1}`               |
| 2 | -2     | 10         | 20             | 0           | 0     | `{0: 1, 10: 2, 12: 1}`               |
| 3 | -20    | -10        | 0              | 1 (✅)       | 1     | `{0: 1, 10: 2, 12: 1, -10: 1}`       |
| 4 | 10     | 0          | 10             | 2 (✅)       | 3     | `{0: 2, 10: 2, 12: 1, -10: 1}`       |

✅ Final Count: `3`

---

## 🧑‍💻 Code (Python)

```python
class Solution:
    def cntSubarrays(self, arr, k):
        prefix_sum = 0
        count = 0
        freq = {0: 1}

        for num in arr:
            prefix_sum += num
            if (prefix_sum - k) in freq:
                count += freq[prefix_sum - k]
            freq[prefix_sum] = freq.get(prefix_sum, 0) + 1

        return count
```
---
## 🚀 Applications

- ✅ **Budget Tracking:** Identify time windows where net expenses/income match a target value.
- ✅ **Time Series Analysis:** Detect periods in sensor data or logs where metrics match exact thresholds.
- ✅ **Game Development:** Track score segments or streaks matching a given value for triggering events.
- ✅ **Subarray Sum-Based Queries:** Forms the base for range-sum queries in streaming or live data.
- ✅ **Competitive Coding:** Common trick using prefix sums and hashing, found in many interview rounds.
- ✅ **Machine Learning:** Used in feature extraction for detecting specific behavior windows in sequences.
---

## 🏷️ Tags

`#PrefixSum` `#HashMap` `#Subarray` `#Array` `#Counting` `#SlidingWindowVariant` `#Optimization` `#Intermediate` `#FrequencyMap`
