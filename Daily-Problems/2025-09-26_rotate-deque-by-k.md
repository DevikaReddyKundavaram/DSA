# 🔄 Rotate Deque By K

## 📌 Problem Statement

You are given a deque `dq[]` (double-ended queue) containing non-negative integers, along with two positive integers `type` and `k`.  
The task is to rotate the deque circularly by `k` positions.

- **Right Rotation (Clockwise):** If `type = 1`, move the last element to the front `k` times.  
- **Left Rotation (Anti-Clockwise):** If `type = 2`, move the first element to the back `k` times.  

---

## 📊 Examples
```text
Example 1
Input: dq = [1, 2, 3, 4, 5, 6], type = 1, k = 2
Output: [5, 6, 1, 2, 3, 4]`
Explanation:  
- After 1st right rotation → [6, 1, 2, 3, 4, 5]  
- After 2nd right rotation → [5, 6, 1, 2, 3, 4]  

Example 2
Input: dq = [10, 20, 30, 40, 50], type = 2, k = 3  
Output: [40, 50, 10, 20, 30]
Explanation:
- After 1st left rotation → [20, 30, 40, 50, 10]  
- After 2nd left rotation → [30, 40, 50, 10, 20]  
- After 3rd left rotation → [40, 50, 10, 20, 30]  
```
---

## ✅ Constraints
- `1 ≤ dq.size() ≤ 10^5`  
- `1 ≤ k ≤ 10^5`  
- `1 ≤ type ≤ 2`  

---

## 📝 Algorithm

1. **Input Handling**  
   - Let `n = len(dq)`.  
   - Compute `k = k % n` to avoid unnecessary full rotations.  

2. **Check Rotation Type**  
   - If `type = 1` → Perform **Right Rotation**.  
   - If `type = 2` → Perform **Left Rotation**.  

3. **Right Rotation (type = 1)**  
   - Repeat `k` times:  
     - Remove the last element using `pop()`.  
     - Insert it at the front using `appendleft()`.  

4. **Left Rotation (type = 2)**  
   - Repeat `k` times:  
     - Remove the first element using `popleft()`.  
     - Insert it at the back using `append()`.  

5. **Return Result**  
   - Convert deque to list and return as the final rotated sequence.  

---
## ⏳ Complexities

- **Time Complexity:**  
  - Each rotation (`pop` + `appendleft` or `popleft` + `append`) takes `O(1)`.  
  - Performed `k` times → **`O(k)`**.  

- **Space Complexity:**  
  - The deque is modified in place.  
  - No extra data structures are used.  
  - **`O(1)`**.  

---


## 🧑‍💻 Code (Python)

```python
from collections import deque

class Solution:    
    def rotateDeque(self, dq, type, k):
        n = len(dq)
        k = k % n   # Optimize for k > n

        if type == 1:  # Right Rotation
            for _ in range(k):
                dq.appendleft(dq.pop())  # Move last element to front
        else:  # Left Rotation
            for _ in range(k):
                dq.append(dq.popleft())  # Move first element to back
        
        return list(dq)
```
---
---

## 🚀 Applications

- 🔄 **Circular Buffers** – Used in memory management and real-time systems.  
- 🎮 **Game Mechanics** – Rotating turns in multiplayer games.  
- 📡 **Networking** – Round-robin scheduling for packets and processes.  
- 📊 **Data Analysis** – Shifting datasets for pattern recognition.  
- 🧮 **Mathematical Problems** – Handling circular arrays and cyclic permutations.  

---
---

## 🏷️ Tags

`#Queue` `#Deque` `#Rotation` `#CircularArray` `#DataStructures` `#Easy` `#ProblemSolving` `#CompetitiveProgramming` `#InterviewPreparation`

---
