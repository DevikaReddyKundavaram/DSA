# 💪 Powerful Integer

## 📝 Problem Statement

You are given a 2D integer array `intervals[][]` of length `n`, where each `intervals[i] = [start, end]` represents a closed interval (i.e., all integers from start to end, inclusive).  
You are also given an integer `k`.  
An integer is called **Powerful** if it appears in **at least k intervals**.  
Find the **maximum Powerful Integer**.

> **Note**: If no integer occurs at least `k` times, return `-1`.

---

## 📥 Input

- `n` — Number of intervals (1 ≤ n ≤ 10⁵)
- `intervals[i][0]`, `intervals[i][1]` — Start and End of ith interval (1 ≤ start ≤ end ≤ 10⁹)
- `k` — Minimum number of interval occurrences required (1 ≤ k ≤ 10⁵)

---

## 📤 Output

- Return the **maximum integer** that appears in at least `k` intervals.
- If no such integer exists, return `-1`.

---

## 🔁 Examples

### Example 1

**Input:**
- intervals = [[1, 3], [4, 6], [3, 4]], k = 2
**Output:**
- 4
**Explanation:**  
- Integers `3` and `4` appear in 2 intervals. The maximum is `4`.

---
## 🔁 Algorithm

1. **Initialize a frequency map** to track start and end+1 points of each interval using a sweep line technique.

2. **For each interval `[start, end]`**:
   - Increment `freq[start]` by 1 (start of interval).
   - Decrement `freq[end + 1]` by 1 (end of interval).

3. **Sort the keys** of the frequency map (all event points).

4. Initialize:
   - `curr = 0` — to store the current count of overlapping intervals.
   - `start_active = -1` — to mark the beginning of a potential powerful range.
   - `max_powerful = -1` — to track the maximum powerful integer found.

5. **Traverse all sorted keys**:
   - Add the value at each key to `curr` (apply frequency changes).
   - If `curr >= k`, it means we are inside a powerful region. Set `start_active = point`.
   - If `curr < k` and `start_active != -1`, this marks the end of a powerful range:
     - Update `max_powerful = max(max_powerful, point - 1)`
     - Reset `start_active = -1`

6. **Return `max_powerful`** after traversal.
   - If no powerful integer is found, it remains `-1`.

---
## ⏱️ Time & Space Complexity

### 🧮 Time Complexity:
- **O(N log N)**:  
  - We process all `N` intervals.
  - Sorting the keys of the map (at most `2N` keys) takes `O(N log N)`.
  - Traversing the sorted points is linear in the number of keys.

### 🗃️ Space Complexity:
- **O(N)**:
  - The frequency map stores at most `2N` keys (start and end+1 of each interval).

---
## 🧑‍💻 Code

```python
class Solution:
    def powerfulInteger(self, intervals, k):
        from collections import defaultdict

        freq = defaultdict(int)

        # Step 1: Use prefix-sum technique by marking +1 at start, -1 at end+1
        for start, end in intervals:
            freq[start] += 1
            freq[end + 1] -= 1

        # Step 2: Sort the keys for prefix sum traversal
        points = sorted(freq.keys())
        max_powerful = -1
        curr_count = 0

        for i in range(len(points) - 1):
            curr_point = points[i]
            curr_count += freq[curr_point]

            # If current frequency is at least k, all points in this range are powerful
            if curr_count >= k:
                next_point = points[i + 1]
                # All integers from curr_point to next_point - 1 are powerful
                max_powerful = max(max_powerful, next_point - 1)

        return max_powerful
```
## 🚀 Applications

- **Network Coverage Analysis:**  
  Determine the maximum point where at least `k` devices or towers have overlapping coverage.

- **Data Streaming Intervals:**  
  Useful in identifying peak activity windows when multiple users are simultaneously active.

- **Event Scheduling & Conflict Detection:**  
  Find the time where at least `k` events overlap—important for resource allocation and optimization.

- **Geospatial Range Analysis:**  
  Helps in identifying hotspots on maps where multiple activity zones intersect.

- **Memory or CPU Utilization Tracking:**  
  Track periods where multiple processes overlap on system resources to find high usage times.
---
## 🏷️ Tags

`#Greedy` `#PrefixSum` `#SweepLine` `#RangeCounting` `#Intervals` `#Optimization` `#BinarySearch` `#2Pointers`






