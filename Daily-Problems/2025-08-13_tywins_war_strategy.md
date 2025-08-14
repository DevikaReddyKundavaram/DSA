# Tywin's War Strategy

---

## 🧩 Problem Statement

You are given an array `arr[]` of size `n`, where `arr[i]` represents the number of soldiers in the *i*-th troop, and an integer `k`.  
A troop is **lucky** if its soldier count is a **multiple of `k`**.  
Find the **minimum total number of soldiers to add** (across all troops) so that **at least** `⌈n/2⌉` troops become lucky.

> When adding soldiers to a troop, you may add any non-negative integer (including zero). You cannot remove soldiers.

---

## 🧪 Examples
```text
Example 1
Input:  arr = [5, 6, 3, 2, 1]
,k = 2
Output: 1
Explanation: Already lucky: 6, 2  → count = 2. Target = ceil(5/2) = 3, need 1 more. Cheapest fix is 1 → make 1 → 2. Total added = 1.

Example 2

Input:  arr = [3, 5, 6, 7, 9, 10], k = 4
Output: 4
Explanation: Target = ceil(6/2) = 3. Additions needed per troop (to next multiple of 4): 3→1, 5→3, 6→2, 7→1, 9→3, 10→2. Pick the 3 smallest: 1 + 1 + 2 = 4.
```
---
**Constrains**
- **Input:**
  - `arr` — list of integers, `1 ≤ arr[i] ≤ 1e5`
  - `k` — integer, `1 ≤ k ≤ 1e5`
- **Output:**  
  - Minimum total soldiers to add to ensure at least `⌈n/2⌉` troops are divisible by `k`.

---

## Algorithm
1. **Calculate Target Lucky Troops**
-target = ceil(n / 2)

2. **Count Already Lucky Troops**  
Count troops where `arr[i] % k == 0`.

3. **If Already Enough Lucky Troops → Return 0**  

4. **Find Additional Soldiers Needed**  
For each non-lucky troop:
-addition = k - (arr[i] % k)

5. **Sort Costs & Pick the Cheapest**  
Sort `additions` list and sum the smallest `(target - lucky_count)` values.

6. **Return the Sum**

---

## Code
```python
import math

class Solution:
 def minSoldiers(self, arr, k):
     n = len(arr)
     target = math.ceil(n / 2)  # Minimum lucky troops required
     
     lucky_count = sum(1 for x in arr if x % k == 0)
     
     if lucky_count >= target:
         return 0  # Already enough lucky troops
     
     additions = [(k - (x % k)) for x in arr if x % k != 0]
     
     additions.sort()
     
     need = target - lucky_count
     return sum(additions[:need])

```
---
## Applications
- **Military Logistics** – Efficiently allocate additional soldiers to meet minimum operational requirements.
- **Game Development** – Balancing teams or units in strategy games with minimal upgrades.
- **Resource Optimization** – Minimizing cost to meet certain thresholds in any allocation problem.
- **Operations Research** – Strategic decision-making for upgrades under constraints.
- **Competitive Programming** – Classic greedy optimization scenario.
---
## 🏷️ Tags
- `#GreedyAlgorithm`
- `#Sorting`
- `#Math`
- `#Optimization`
- `#ArrayManipulation`
