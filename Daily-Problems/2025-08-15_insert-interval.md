# 📝 Problem: Insert Interval
---

## 📜 Problem Statement
You are given an array of non-overlapping intervals `intervals[][]` where each `intervals[i] = [start_i, end_i]` represents the start and end of the *i-th* event.  
The intervals are sorted in **ascending order** by `start_i`.

You are also given a `newInterval[] = [newStart, newEnd]`.  
Insert `newInterval` into `intervals` so that:
- The result is still sorted by start time.
- No overlapping intervals remain (merge if necessary).

---
# Examples 
```text
Example 1:
Input:
intervals = [[1, 3], [4, 5], [6, 7], [8, 10]]
newInterval = [5, 6]

Output:[[1, 3], [4, 7], [8, 10]]

Explanation:
The new interval `[5, 6]` overlaps with `[4, 5]` and `[6, 7]`.  
Merged into `[4, 7]`.


Example 2:
Input:
intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
newInterval = [4, 9]

Output:[[1, 2], [3, 10], [12, 16]]
[[1, 2], [3, 10], [12, 16]]

Explanation:
Overlaps with `[3, 5]`, `[6, 7]`, and `[8, 10]`.  
Merged into `[3, 10]`.
```
---

## 🔒 Constraints
- `1 ≤ intervals.size() ≤ 10^5`
- `0 ≤ start_i ≤ end_i ≤ 10^9`
- `0 ≤ newStart ≤ newEnd ≤ 10^9`

---

## 💡 Approach
We can solve this in **O(n)** using a single pass:
1. Add all intervals that end before `newInterval` starts (no overlap).
2. Merge all intervals that overlap with `newInterval`.
3. Add all remaining intervals after merging.

---

## 🧮 Time & Space Complexity
- **Time Complexity:** `O(n)` — Single traversal of intervals.
- **Space Complexity:** `O(n)` — Output list.

---

## 🚀 Python Implementation
```python
class Solution:
    def insertInterval(self, intervals, newInterval):
        res = []
        i = 0
        n = len(intervals)

        # Step 1: Add intervals before newInterval
        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1

        # Step 2: Merge overlapping intervals
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        res.append(newInterval)

        # Step 3: Add remaining intervals
        while i < n:
            res.append(intervals[i])
            i += 1

        return res
```
---
## 📌 Applications of Insert Interval Problem

1. **Calendar Event Management**  
   - Adding a new event into a user’s schedule without time conflicts.
   - Example: Google Calendar automatically merges overlapping meeting slots.

2. **Booking Systems**  
   - Merging and managing booking slots for hotels, flights, conference rooms, etc.

3. **CPU Scheduling**  
   - Inserting new jobs into a timeline while merging overlapping execution windows.

4. **Memory Allocation in OS**  
   - Merging contiguous free/used memory blocks in memory management systems.

5. **Video Editing Timelines**  
   - Combining overlapping clip segments into one continuous scene.

6. **Data Compression**  
   - Merging overlapping data ranges when storing intervals to reduce redundancy.

7. **Network Bandwidth Reservation**  
   - Allocating and merging time slots for data transmission to avoid collisions.
---
**🏷️ Tags:**  
`#Arrays` `#Sorting` `#Greedy` `#Interval-Merging` `#Simulation`
