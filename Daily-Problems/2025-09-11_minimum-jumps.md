# 🦘 Minimum Number of Jumps

## Problem Statement
You are given an array `arr[]` of non-negative numbers.  
Each element `arr[i]` represents the **maximum number of steps** you can jump forward from index `i`.  

- If `arr[i] = 3`, you may jump to index `i+1`, `i+2`, or `i+3`.  
- If `arr[i] = 0`, you cannot move forward from that index.  

Your task is to find the **minimum number of jumps** required to reach the **last index** of the array.  
If it is not possible to reach the end, return `-1`.

---

## Examples
```text
Example1:
Input: arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]  
Output: 3  
Explanation: Jump from index 0 → 1 (arr[0] = 1), then index 1 → 4 (arr[1] = 3), then directly to the last index.  

Example2:
Input: arr = [1, 4, 3, 2, 6, 7]  
Output: 2  
Explanation: Jump from index 0 → 1, then index 1 → last index.  

Example3:
Input: arr = [0, 10, 20]  
Output: -1  
Explanation: Cannot move from index 0.  
```
---

## Constraints
- 2 ≤ arr.size() ≤ 10⁵  
- 0 ≤ arr[i] ≤ 10⁵  

---
## Algorithm

1. **Handle Edge Cases**
   - If `arr[0] == 0`, return `-1` (cannot move anywhere).
   - If the array size `n == 1`, return `0` (already at the destination).

2. **Initialize Variables**
   - `steps = 0` → to count number of jumps.
   - `l = 0` → left boundary of current range.
   - `r = 0` → right boundary of current range.
   - `maxReach = 0` → stores farthest index reachable in the current jump.

3. **Iterate Through the Array**
   - For each index `i` in the array:
     - If `l > r`, return `-1` (we are stuck and cannot move forward).
     - Update `maxReach = max(maxReach, i + arr[i])`.
     - If `i == r`:
       - Increment `steps` (we finished a jump).
       - Update `l = i + 1`, `r = maxReach` (set the new range).
     - If `r >= n - 1`, return `steps`.

4. **Return Result**
   - If loop ends without reaching last index, return `-1`.
   - Otherwise, return `steps`.

---

## Complexity
- **Time Complexity:** `O(n)` → single traversal of the array.  
- **Space Complexity:** `O(1)` → only constant extra variables.

---
## Code Solution (Python)
```python
class Solution:
    def minJumps(self, arr):
        n = len(arr)
        
        if arr[0] == 0:
            return -1
        if n == 1:
            return 0

        l = r = maxReach = steps = 0
        
        for i in range(n):
            if l > r:  
                return -1 
            
            if r >= n - 1:
                return steps  
            
            maxReach = max(maxReach, i + arr[i])
            
            if i == r:  
                l = i + 1
                r = maxReach
                steps += 1
        
        return steps
```
# Applications of Minimum Jumps Problem

1. **Network Packet Hopping**
   - Finding the minimum number of hops required to send a packet across routers in a network.

2. **Game Development**
   - Used in path-finding problems (e.g., minimum moves to reach the destination in a board game).

3. **Robotics**
   - Helps in calculating the minimum number of steps a robot should take to reach a target while having limited moves per step.

4. **Compiler Optimization**
   - Useful in instruction scheduling where minimum jumps between code blocks reduce execution time.

5. **Dynamic Programming Problems**
   - Acts as a base problem for solving more complex **reachability** or **shortest path in arrays** problems.

6. **Logistics and Navigation**
   - Modeling scenarios like minimum stops needed to reach a destination when each stop allows a limited range of travel.
---
# Tags  
`#Greedy` `#DynamicProgramming` `#Array` `#JumpGame` `#Optimization`
---
