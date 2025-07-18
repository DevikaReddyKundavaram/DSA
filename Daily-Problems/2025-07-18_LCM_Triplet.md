# 📄 LCM Triplet Problem - Solution

## 📝 Problem Statement

Given a number `n`. Find the **maximum possible LCM (Lowest Common Multiple)** that can be obtained by selecting **three numbers less than or equal to `n`**.

### 🔍 Examples

| Input | Output | Explanation       |
|-------|--------|-------------------|
| 9     | 504    | Triplet: (7, 8, 9) |
| 7     | 210    | Triplet: (5, 6, 7) |

---

## 🔒 Constraints
1 ≤ n ≤ 10^3


---

## 💡 Algorithm

### **Observations:**
- The maximum LCM generally comes from the **largest numbers** less than or equal to `n`.
- If `n` is **even**, picking three consecutive numbers may result in two even numbers, reducing the LCM.
- Thus, special combinations like `(n, n-1, n-3)` should also be checked.
- If `n` is **odd**, `(n, n-1, n-2)` usually works well.

---

### **Steps:**
1. If `n <= 2`: Return `n`.
2. If `n <= 3`: Return `6` (since LCM of 1, 2, 3 is 6).
3. Calculate LCM of `(n, n-1, n-2)`.
4. If `n` is **even**:
    - Check `(n, n-1, n-3)`
    - Check `(n-1, n-2, n-3)`
5. If `n` is **odd**:
    - Optionally check `(n, n-1, n-3)`
6. Return the **maximum LCM** from these combinations.

---

## ⏳ Complexity Analysis

| Type             | Complexity |
|------------------|------------|
| **Time Complexity**   | O(1) (Constant operations for small `n`) |
| **Space Complexity**  | O(1) (No extra space used) |

---

## 🚀 Python Code

```python
from math import gcd
from math import lcm

class Solution:
    def lcmTriplets(self, n):
        def lcm_three(a, b, c):
            return lcm(lcm(a, b), c)
        
        if n <= 2:
            return n
        
        if n <= 3:
            return 6
        
        ans = lcm_three(n, n-1, n-2)
        
        if n % 2 == 0:
            ans = max(ans, lcm_three(n, n-1, n-3))
            ans = max(ans, lcm_three(n-1, n-2, n-3))
        else:
            ans = max(ans, lcm_three(n, n-1, n-3))
        
        return ans
```

## 🔧 Applications of LCM (Lowest Common Multiple)

### 1️⃣ **Scheduling & Timetables**
- **Use:** Find when two or more recurring events align again.
- **Examples:**
  - School bell schedules.
  - Exam timetables.
  - Public transportation frequency alignment.

---

### 2️⃣ **Engineering & Mechanical Systems**
- **Use:** Synchronizing cycles of rotating parts like gears or pulleys.
- **Examples:**
  - Rotating shafts meeting at common positions.
  - Gear teeth alignment after rotations.

---

### 3️⃣ **Networking & Communication**
- **Use:** Synchronizing repeating signals, packets, or tasks that occur at different intervals.
- **Examples:**
  - Data transmission intervals.
  - Signal broadcasting.

---

### 4️⃣ **Music Theory**
- **Use:** Finding when rhythms of different beats align again.
- **Examples:**
  - Drumming patterns.
  - Time signature combinations in compositions.

---

### 5️⃣ **Project Planning & Management**
- **Use:** Align milestones from tasks that repeat at different intervals.
- **Examples:**
  - Maintenance cycles.
  - Resource availability planning.

---

### 6️⃣ **Mathematical Puzzles & Competitive Programming**
- **Use:** Classic problem type in number theory.
- **Examples:**
  - Problems like "LCM Triplets" to practice logical and mathematical reasoning.

---

### 7️⃣ **Astronomy**
- **Use:** Finding when celestial cycles (e.g., orbits) coincide again.
- **Examples:**
  - Predicting planetary alignments.
## 🏷️ Tags
- `Number Theory`
- `LCM`
- `Mathematics`
- `Brute Force`
- `Optimization`
- `Competitive Programming`
- `Algorithms`
- `Python`
- `Interview Preparation`

