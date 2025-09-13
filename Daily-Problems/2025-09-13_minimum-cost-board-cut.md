# ✂️ Minimum Cost to Cut a Board into Squares

## 📌 Problem Statement  
You are given a board of dimensions **n × m** that needs to be cut into **n × m** squares.  
The cost of making a cut along a **horizontal** or **vertical** edge is provided in two arrays:  

- `x[]`: Cutting costs along the vertical edges (length-wise).  
- `y[]`: Cutting costs along the horizontal edges (width-wise).  

Find the **minimum total cost** required to cut the board into squares optimally.


---
## Examples:
```text
Example 1:
Input: arr[] = [1, 5, 8, 10], K = 2
Output: 5
Explanation:
Increase 1 by 2 → 3
Decrease 10 by 2 → 8
New array: [3, 5, 8, 8]
Max = 8, Min = 3 → Difference = 5

Example 2:
Input: arr[] = [3, 9, 12, 16, 20], K = 3
Output: 11
Explanation:
Increase 3 by 3 → 6
Decrease 20 by 3 → 17
New array: [6, 9, 12, 16, 17]
Max = 17, Min = 6 → Difference = 11

Example 3:
Input: arr[] = [7, 4, 8, 8, 8, 9], K = 6
Output: 5
Explanation:
Increase 4 by 6 → 10
Decrease 9 by 6 → 3
New array: [7, 10, 8, 8, 8, 3]
Max = 10, Min = 3 → Difference = 7
But with better choices → Minimized difference = 5.
```
## Constraints
- 1 ≤ n ≤ 10^5   (Number of towers)
- 1 ≤ k ≤ 10^9   (Increment/Decrement value)
- 1 ≤ arr[i] ≤ 10^9   (Height of towers)
---
## 🔑 Algorithm  
1. Sort `x[]` and `y[]` in **descending order**.  
2. Initialize:  
   - `horizontal_segments = 1`  
   - `vertical_segments = 1`  
   - `total_cost = 0`  
3. While both arrays have cuts left:  
   - If `x[i] >= y[j]`:  
     - Take vertical cut → `total_cost += x[i] * horizontal_segments`  
     - Increase `vertical_segments++`  
   - Else:  
     - Take horizontal cut → `total_cost += y[j] * vertical_segments`  
     - Increase `horizontal_segments++`  
4. Add remaining cuts (if any).  
5. Return `total_cost`.

---
## ⏱️ Complexities  
- **Time Complexity:** `O(n log n + m log m)`  
- **Space Complexity:** `O(1)`  

---
## Code
```python
def getMinDiff(arr, n, k):
    arr.sort()
    ans = arr[n-1] - arr[0]   
    
    small = arr[0] + k
    big = arr[n-1] - k
    
    if small > big:
        small, big = big, small
    
    for i in range(1, n-1):
        subtract = arr[i] - k
        add = arr[i] + k
        
        if subtract >= small or add <= big:
            continue
        
        if big - subtract <= add - small:
            small = subtract
        else:
            big = add
    
    return min(ans, big - small)
```
---
## 🧮 Dry Run  
**Input:**  
n = 4, m = 6
x[] = [2, 1, 3, 1, 4]
y[] = [4, 1, 2]



**Sorted:**  
x = [4, 3, 2, 1, 1]
y = [4, 2, 1]


**Steps:**  
1. Take x=4 → cost = 4×1 = 4, vertical_segments=2  
2. Take y=4 → cost = 4×2 = 8, horizontal_segments=2 (total=12)  
3. Take x=3 → cost = 3×2 = 6, vertical_segments=3 (total=18)  
4. Take x=2 → cost = 2×2 = 4, vertical_segments=4 (total=22)  
5. Take y=2 → cost = 2×4 = 8, horizontal_segments=3 (total=30)  
6. Take x=1 → cost = 1×3 = 3, vertical_segments=5 (total=33)  
7. Take x=1 → cost = 1×3 = 3, vertical_segments=6 (total=36)  
8. Take y=1 → cost = 1×6 = 6, horizontal_segments=4 (total=42)  

✅ **Answer = 42**

---

## 🌍 Applications  
- Wood cutting and carpentry optimization.  
- Tile/metal/glass cutting in industries.  
- Grid partitioning in resource management.  
- Cost optimization in logistics and layout design.  

---

## 🏷️ Tags  
`#Greedy` `#Sorting` `#DivideAndConquer` `#Optimization`  
