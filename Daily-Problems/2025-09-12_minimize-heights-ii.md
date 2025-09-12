# 🏰 Minimize the Heights II

### 📌 Problem Statement  
You are given an array `arr[]` of `n` tower heights and an integer `k`.  
For each tower, you must **either add `k` or subtract `k` exactly once**.  
Find the **minimum possible difference** between the maximum and minimum tower heights after modification.  

⚠️ **Note**: Heights cannot be negative.

## Examples:
```text
Example 1:
Input: k = 2, arr = [1, 5, 8, 10]
Output: 5
Explanation: The array can be modified as [1+2, 5-2, 8-2, 10-2] = [3, 3, 6, 8].
The difference between the maximum (8) and minimum (3) is 5.

Example 2:
Input: k = 3, arr = [3, 9, 12, 16, 20]
Output: 11
Explanation: The array can be modified as [3+3, 9+3, 12-3, 16-3, 20-3] = [6, 12, 9, 13, 17].
The difference between the maximum (17) and minimum (6) is 11.
```
---
## Constraints
- 1 ≤ N ≤ 10^5  
- 0 ≤ List[i] ≤ 10^9  
- Input list may contain duplicate elements  
- Order of elements after duplicate removal does not matter  
---

### 🔹 Algorithm
1. Sort the array.  
2. Compute initial difference: `ans = arr[n-1] - arr[0]`.  
3. Assume smallest tower = `arr[0] + k`, largest tower = `arr[n-1] - k`.  
4. Iterate `i` from `0` to `n-2`:  
   - Increase first `i` towers by `k`, decrease others by `k`.  
   - `mini = min(arr[0] + k, arr[i+1] - k)`  
   - `maxi = max(arr[i] + k, arr[n-1] - k)`  
   - If `mini >= 0`, update `ans = min(ans, maxi - mini)`.  
5. Return `ans`.

---

## Time Complexity
- **Set Conversion Method**: O(N)  
- **Manual Check Method**: O(N^2) (since for each element we check in another list)  

## Space Complexity
- **Set Conversion Method**: O(N) (extra space for set)  
- **Manual Check Method**: O(N) (extra list to store unique elements)  
---

### 🔹 Python Code
```python
class Solution:
    def getMinDiff(self, arr, k):
        n = len(arr)
        arr.sort()
        
        ans = arr[-1] - arr[0]  # initial difference

        for i in range(n - 1):
            mini = min(arr[0] + k, arr[i+1] - k)
            maxi = max(arr[i] + k, arr[-1] - k)

            if mini < 0:  # skip invalid case
                continue

            ans = min(ans, maxi - mini)

        return ans
```
---
### 📝 Dry Run of Minimize the Heights II

#### Example:
Input:  
k = 2, arr = [1, 5, 8, 10]  

---

**Step 1: Sort the array**  
arr = [1, 5, 8, 10] (already sorted)  

**Step 2: Initial difference**  
ans = arr[3] - arr[0] = 10 - 1 = 9  

**Step 3: smallest & largest setup**  
- smallest = arr[0] + k = 1 + 2 = 3  
- largest = arr[3] - k = 10 - 2 = 8  

**Step 4: Loop through array**  

- i = 0:  
  - mini = min(1 + 2, 5 - 2) = min(3, 3) = 3  
  - maxi = max(1 + 2, 10 - 2) = max(3, 8) = 8  
  - ans = min(9, 8 - 3 = 5) = 5  

- i = 1:  
  - mini = min(1 + 2, 8 - 2) = min(3, 6) = 3  
  - maxi = max(5 + 2, 10 - 2) = max(7, 8) = 8  
  - ans = min(5, 8 - 3 = 5) = 5  

- i = 2:  
  - mini = min(1 + 2, 10 - 2) = min(3, 8) = 3  
  - maxi = max(8 + 2, 10 - 2) = max(10, 8) = 10  
  - ans = min(5, 10 - 3 = 7) = 5  

**Step 5: Final Answer**  
- ans = 5  
✅ Output: **5**
---
## Applications
- **Construction Planning**: Adjusting building/tower heights to maintain skyline uniformity.  
- **Load Balancing**: Distributing workloads among servers to minimize the gap between heaviest and lightest loads.  
- **Resource Distribution**: Fair allocation of limited resources with minimum disparity.  
- **Network Optimization**: Keeping latency or bandwidth differences minimized across connected devices.  
- **Data Normalization**: Bringing dataset values within a smaller range to improve machine learning model stability.  
- **Game Development**: Balancing levels by slightly increasing/decreasing difficulty factors.  

---

## Tags
`Greedy` `Sorting` `Array` `Optimization`  


---
