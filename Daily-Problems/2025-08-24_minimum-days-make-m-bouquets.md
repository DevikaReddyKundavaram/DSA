# 🌸 Minimum Days to Make M Bouquets  

---

## 📌 Problem Statement
You have a row of flowers, where each flower blooms after a specific day.  
- `arr[i]` = the day the flower at position `i` will bloom.  
- To create a **bouquet**, you need **k adjacent bloomed flowers**.  
- Each flower can only be used in **one bouquet**.  

Your task is to determine the **minimum number of days** required to make exactly **m bouquets**.  
If it is not possible, return `-1`.  

---

📝 Examples

```text
Example 1:
Input:
m = 3, k = 2
arr = [3, 4, 2, 7, 13, 8, 5]
Output: 8
Explanation:
- By day 8, the flowers look like: `[x, x, x, x, _, x, x]`  
- Bouquets possible: `[3,4]`, `[2,7]`, `[8,5]` → ✅ 3 bouquets  

Example 2:
Input: m = 2, k = 3
arr = [5, 5, 5, 5, 10, 5, 5]
Output: 10
Explanation: 
- By day 5 → only 1 bouquet of 3 possible  
- By day 10 → `[5,5,5]` and `[5,5,5]` → ✅ 2 bouquets  

Example 3:
Input: m = 3, k = 2
arr = [1, 10, 3, 10, 2]
Output: -1
Explanation:  
- Total flowers needed = `m * k = 6` but only 5 available ❌  
```
---

## ⚡ Algorithm
1. **Edge Case Check:** If `m * k > len(arr)` → return `-1`  
2. **Binary Search** between `low = min(arr)` and `high = max(arr)`  
3. For a given `mid`:  
   - Traverse `arr`, count consecutive bloomed flowers (`arr[i] <= mid`)  
   - When count == k → one bouquet formed, reset count  
   - Check if at least `m` bouquets can be formed  
4. If possible at `mid` → try smaller days (`high = mid - 1`)  
5. Otherwise → search larger days (`low = mid + 1`)  

---

## ⏳ Time & Space Complexity
- **Checking bouquets:** `O(n)`  
- **Binary search range:** `O(log(max(arr)))`  
- **Total Complexity:** `O(n * log(max(arr)))`  
- **Space Complexity:** `O(1)`  

---

## 💻 Python Code  

```python
class Solution:
    def minDaysBloom(self, arr, k, m):
        n = len(arr)

        if m * k > n:
            return -1

        def canMake(mid):
            bouquets, count = 0, 0
            for day in arr:
                if day <= mid:
                    count += 1
                    if count == k:
                        bouquets += 1
                        count = 0
                else:
                    count = 0
            return bouquets >= m

        low, high = min(arr), max(arr)
        ans = -1

        while low <= high:
            mid = (low + high) // 2
            if canMake(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans
```
---
## 🌍 Applications
- 🌸 **Florist Industry** → Planning the earliest day to deliver bulk bouquet orders.  
- 🏭 **Manufacturing** → Scheduling production batches when items must be grouped consecutively.  
- 🏡 **Agriculture** → Harvest planning when crops ripen on different days, but bundles are needed.  
- 🎟️ **Event Management** → Arranging decorations where consecutive available resources are needed.  
- 📦 **Supply Chain** → Grouping consecutive products that are available after certain days.  
---
## 🏷️ Tags
`#BinarySearch` `#Greedy` `#BouquetProblem` `#Arrays` `#Medium`

---
