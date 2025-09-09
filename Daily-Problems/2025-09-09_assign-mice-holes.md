# 🐭 Assign Mice to Holes  

## 📖 Problem Statement  
You are given two arrays `mices[]` and `holes[]` of the same size.  
- The array `mices[]` represents the positions of the mice on a straight line.  
- The array `holes[]` represents the positions of the holes on the same line.  
- Each hole can accommodate exactly **one mouse**.  
- A mouse can stay in its position, move one step right, or move one step left, where **each move takes 1 minute**.  

The task is to **assign each mouse to a distinct hole** such that the **time taken by the last mouse to reach its hole is minimized**.  

### Constraints  
- 1 ≤ mices.size() = holes.size() ≤ 10^5  
- -10^5 ≤ mices[i], holes[i] ≤ 10^5  

### Examples  
```text
Example1
Input: mices[] = [4, -4, 2], holes[] = [4, 0, 5]
Output: 4
Explanation:
- Mouse at 4 → Hole at 4 → Time = 0  
- Mouse at -4 → Hole at 0 → Time = 4  
- Mouse at 2 → Hole at 5 → Time = 3  
Maximum time = **4**  

Example2
Input: mices[] = [1, 2], holes[] = [20, 10]
Output: 18
Explanation:
- Mouse at 1 → Hole at 10 → Time = 9  
- Mouse at 2 → Hole at 20 → Time = 18  
Maximum time = **18**  
```
---

### Approach
- Sort both arrays.
- Pair the `i-th` mouse with the `i-th` hole.
- The time for a mouse-hole pair = `abs(mices[i] - holes[i])`.
- The minimum possible time for the last mouse = **maximum of all pair times**.
---
## ⏱️ Complexity Analysis  

| Operation | Complexity |
|-----------|------------|
| Sorting mices & holes | O(n log n) |
| Assigning mice to holes | O(n) |
| **Total Time Complexity** | **O(n log n)** |
| **Space Complexity** | **O(1)** (in-place sorting) |

---

## 💻 Code Solution  

```python
class Solution:
    def assignHole(self, mices, holes):
        mices.sort()
        holes.sort()
        
        max_time = 0
        for i in range(len(mices)):
            max_time = max(max_time, abs(mices[i] - holes[i]))
        
        return max_time
```
---
## 🔍 Dry Run  

**Example:**  
mices = [4, -4, 2]
holes = [4, 0, 5]


**Step 1:** Sort both arrays  
mices = [-4, 2, 4]
holes = [0, 4, 5]

**Step 2:** Assign each mouse to a hole in sorted order  
- | -4 - 0 | = 4  
- | 2 - 4 | = 2  
- | 4 - 5 | = 1  

**Step 3:** Maximum time = **4**  

---

## 🌍 Applications  

- Resource allocation where tasks (mice) must be assigned to servers (holes).  
- Job scheduling with location/distance constraints.  
- Matching problems in **operations research**.  
- Network load balancing where distances (latency) need to be minimized.  

---

## 🏷️ Tags  
`#Greedy` `#Sorting` `#TwoPointers` `#Arrays`
