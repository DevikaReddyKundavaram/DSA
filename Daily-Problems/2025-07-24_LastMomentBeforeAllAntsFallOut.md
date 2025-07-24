# 🐜 Last Moment Before All Ants Fall Out

### 📌 Problem Statement

We have a wooden plank of length `n` units. Some ants are walking on the plank. Each ant moves with a speed of 1 unit per second. Some ants move to the **left**, others to the **right**.

- When two ants meet, they **change directions** and continue walking.
- Changing direction does **not take any extra time**.
- When an ant reaches the **end** of the plank, it **falls off immediately**.

You are given:
- An integer `n` (length of the plank)
- Two arrays `left[]` and `right[]` representing positions of ants moving left and right respectively.

Return the **time** when the **last** ant(s) fall off the plank.

---

### 🔢 Input

- Integer `n` (1 ≤ n ≤ 10⁵)
- Integer array `left[]` where 0 ≤ `left[i]` ≤ `n`
- Integer array `right[]` where 0 ≤ `right[i]` ≤ `n`
- The arrays `left` and `right` are disjoint and contain unique values.
- Total number of ants ≤ `n + 1`

---

### 📤 Output

- Return a single integer — the **last moment** when any ant falls off the plank.

---

### ✅ Examples

```text
Input: n = 4, left = [2], right = [0, 1, 3]
Output: 4

Input: n = 4, left = [], right = [0, 1, 2, 3, 4]
Output: 4

Input: n = 3q, left = [0], right = [3]
Output: 0

```
---
## 🧾 Code (Python)

```python
class Solution:
    def getLastMoment(self, n, left, right):
        max_left_time = max(left) if left else 0
        max_right_time = max(n - pos for pos in right) if right else 0
        return max(max_left_time, max_right_time)
```
---
## 🌍 Real-World Applications

- 🔁 **Collision Simulation**:  
  Simulating entities (ants, robots, particles) that change direction on impact but don’t physically stop.

- 🤖 **Robotics Navigation**:  
  Modeling simple one-dimensional track movement for autonomous bots that reroute without delay upon encounters.

- 📶 **Network Traffic Modeling**:  
  Simulating packet movement in a linear channel with dynamic redirection, similar to how ants reverse.

- 🧪 **Physics & Kinematics Problems**:  
  Demonstrates concepts of relative motion and symmetry in object movement, useful in physics classrooms.

- 🎮 **Game AI Pathing**:  
  Used in game development to simulate NPCs or mobs moving along rails or narrow paths with redirection logic.

---

## 🏷️ Tags

- Greedy
- Simulation
- Brainteaser
- Arrays
- Two Pointers
- 1D Movement
- Ant Logic
- Collision Modeling
- Relative Motion
  

