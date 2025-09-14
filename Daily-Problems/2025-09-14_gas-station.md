# ⛽ Gas Station
---

## 📌 Problem Statement
There are **n** gas stations along a circular tour.  

- `gas[i]` → amount of gas available at station `i`.  
- `cost[i]` → gas needed to travel from station `i` to `(i+1)`.  

You have a car with an unlimited gas tank and start with an empty tank at some station.  

**Task:**  
Return the **index of the starting station** if it is possible to travel once around the circular route in a clockwise direction without running out of gas at any station; otherwise, return **-1**.  

✅ If a solution exists, it is guaranteed to be **unique**.  

---

## 📝 Examples
```text
Example 1
Input: gas = [4, 5, 7, 4], cost = [6, 6, 3, 5]
Output: 2
Explanation:
- Start at station 2 → tank = `0 + 7 = 7`.  
- Travel to station 3 → tank = `(7 - 3 + 4) = 8`.  
- Travel to station 0 → tank = `(8 - 5 + 4) = 7`.  
- Travel to station 1 → tank = `(7 - 6 + 5) = 6`.  
- Travel back to station 2 → tank = `(6 - 6) = 0`.  
✅ Possible to complete the tour, answer = **2**.

Example 2
Input: gas = [3, 9], cost = [7, 6]
Output: -1
Explanation: 
- No starting station allows completing the cycle.  
```
---

## 🎯 Constraints
- `1 ≤ n ≤ 10^6`  
- `1 ≤ gas[i], cost[i] ≤ 10^3`  

---

## 💡 Algorithm (Greedy Approach)
1. Compute the **total gas** and **total cost**.  
   - If `sum(gas) < sum(cost)` → return **-1**.  
2. Initialize:  
   - `start = 0` (potential start station)  
   - `tank = 0` (current fuel in tank)  
3. Traverse each station:  
   - Update `tank += gas[i] - cost[i]`.  
   - If `tank < 0`:  
     - Reset `start = i+1`.  
     - Reset `tank = 0`.  
4. Return `start` as the valid starting index.  

---
## ⏱️ Time & Space Complexity

| Complexity Type | Analysis |
|-----------------|-----------|
| **Time Complexity** | `O(n)` → We make a single pass through the `gas` and `cost` arrays. |
| **Space Complexity** | `O(1)` → Only a few variables (`start`, `tank`, `total_gas`, `total_cost`) are used. |
---

## 🧩 Code (Python)

```python
class Solution:
    def startStation(self, gas, cost):
        total_gas = sum(gas)
        total_cost = sum(cost)
        
        if total_gas < total_cost:
            return -1
        
        start, tank = 0, 0
        for i in range(len(gas)):
            tank += gas[i] - cost[i]
            if tank < 0:
                start = i + 1
                tank = 0
        
        return start
```
---
## 🚀 Applications

- **Route Optimization** → Helps in determining optimal starting points in circular routes (logistics, trucking, delivery).  
- **Energy Management** → Models scenarios where energy/fuel must be managed efficiently in cycles.  
- **Circular Scheduling** → Useful in problems where tasks/resources are cyclic and costs vary at each step.  
- **Battery Charging Stations** → Similar logic can apply to electric vehicles with charging stations.  
- **Network Design** → Can be extended to problems of data packets traveling in circular or ring topologies.  
---
## 🏷️ Tags  
`#Greedy` `#Array` `#CircularTour` `#Optimization`  
