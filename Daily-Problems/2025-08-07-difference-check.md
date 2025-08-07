# 🕒 Difference Check
---

## 🧾 Problem Statement

Given an array `arr[]` of time strings in **24-hour clock format** `"HH:MM:SS"`, return the **minimum difference** in **seconds** between any two time strings in the array.

🕛 The clock wraps around at midnight, so the time difference between `"23:59:59"` and `"00:00:00"` is **1 second**.

---

## 🔢 Input

- An array `arr[]` of strings of format `"HH:MM:SS"`
- `2 ≤ arr.length ≤ 10⁵`
- Each time is a valid string in 24-hour format

---

## 📤 Output

- Return an integer: the minimum time difference in **seconds**.

---

## 🧠 Examples

### Example 1
**Input:**  
`arr = ["12:30:15", "12:30:45"]`  
**Output:**  
`30`  
**Explanation:**  
Difference between both times is 30 seconds.

---

### Example 2
**Input:**  
`arr = ["00:00:01", "23:59:59", "00:00:05"]`  
**Output:**  
`2`  
**Explanation:**  
Minimum difference is between `23:59:59` and `00:00:01` = 2 seconds (wrap-around logic).

---

## 🧮 Algorithm

1. Convert all `"HH:MM:SS"` strings to **total seconds** since midnight.
2. Sort the list of total seconds.
3. Traverse through sorted list and compute the **difference** between consecutive elements.
4. Also compute **wrap-around** difference (between last and first: `86400 + first - last`).
5. Return the **minimum difference** found.

---

## ⏱️ Time and Space Complexity

| **Type**               | **Complexity**         | **Explanation**                                                                 |
|------------------------|------------------------|---------------------------------------------------------------------------------|
| 🕒 **Time Complexity**  | `O(n log n)`           | Sorting the `n` time values after converting them to seconds.                  |
| 🧠 **Space Complexity** | `O(n)`                 | Extra space used to store all time values as seconds in a new list.            |

---

## 🧠 Code (Python)

```python
class Solution:
    def minDifference(self, arr):
        def to_seconds(time_str):
            h, m, s = map(int, time_str.split(':'))
            return h * 3600 + m * 60 + s

        times = sorted(to_seconds(t) for t in arr)
        min_diff = float('inf')
        
        for i in range(1, len(times)):
            min_diff = min(min_diff, times[i] - times[i - 1])
        
        # wrap-around difference between last and first
        wrap_around = 86400 - times[-1] + times[0]
        min_diff = min(min_diff, wrap_around)

        return min_diff
```
---
### 🎯 Applications

- **Time Scheduling Systems**  
  Identifying the smallest time gap between events (e.g., meetings, alarms).

- **Log Analysis**  
  Computing the tightest interval between log entries in a system for anomaly detection.

- **IoT Device Sync**  
  Finding time discrepancies in timestamps collected from distributed devices.

- **Security Systems**  
  Detecting rapid access or breach attempts by analyzing login times.

- **Real-Time Monitoring**  
  Minimum time difference is critical in performance tracking and live systems.

- **Flight/Train Time Management**  
  Scheduling conflicts or shortest layovers can be managed via minimal time gaps.

- **Competitive Programming**  
  Trains problem-solving in edge handling like circular differences across a 24h clock.
---
### 🏷️ Tags

`#TimeConversion`  
`#Sorting`  
`#CircularDifference`  
`#24HourClock`  
`#EdgeCaseHandling`  
`#GreedyApproach`  
`#MinimumDifference`  
`#SystemDesignPrep`  
`#LogAnalysis`  
`#InterviewPrep`
  

