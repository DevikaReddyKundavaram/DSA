# 🍬 Shop in Candy Store
---

## 📜 Problem Statement  
In a candy store, there are different types of candies available and `prices[i]` represent the price of the *i-th* type of candy.  
You are now provided with an attractive offer:  

> For every candy you buy from the store, you can get **up to k** other *different* candies for free.  

Find the **minimum** and **maximum** amount of money needed to buy **all the candies**.  

**Note:** In both cases, you must take the **maximum number of free candies possible** during each purchase.

---

## 📌 Examples  
```text
**Example 1**
Input: prices = [3, 2, 1, 4], k = 2 Output: [3, 7]

**Explanation:**  
- **Min cost:** Buy candy worth `1` → take `3` & `4` for free, then buy `2`.  
  Total = `1 + 2 = 3`.  
- **Max cost:** Buy candy worth `4` → take `1` & `2` for free, then buy `3`.  
  Total = `4 + 3 = 7`.  

---

**Example 2**

Input: prices = [3, 2, 1, 4, 5], k = 4 Output: [1, 5]

**Explanation:**  
- **Min cost:** Buy `1`, take all others for free.  
- **Max cost:** Buy `5`, take all others for free.  

---
```
## ⚙️ Constraints
- `1 ≤ prices.length ≤ 10^5`
- `0 ≤ k ≤ prices.length`
- `1 ≤ prices[i] ≤ 10^4`

---

## 💡 Approach
1. **Minimum Cost:**
   - Sort `prices` in **ascending** order.
   - Start from the **cheapest** candy and buy it.
   - Skip the next `k` candies (free ones) each time.
   
2. **Maximum Cost:**
   - Sort `prices` in **descending** order.
   - Start from the **most expensive** candy and buy it.
   - Skip the next `k` candies each time.

---
## ⏳ Complexity Analysis

### Time Complexity:
1. **Sorting the prices array** → `O(n log n)`  
   - We sort twice (once ascending, once descending), but both are `O(n log n)` and sorting once can be reused if we just reverse, so overall still `O(n log n)`.
2. **Traversing to calculate min cost** → `O(n)`
3. **Traversing to calculate max cost** → `O(n)`

**Total:** `O(n log n)`  
*(Sorting dominates the runtime)*

---

### Space Complexity:
- **Sorting:** Depending on the sorting algorithm, Python’s `sort()` uses `O(n)` in worst case (Timsort).
- **Extra variables:** `O(1)` (just counters & sums)  
- **Total:** `O(1)` auxiliary space (if we ignore sorting’s in-place nature in Python).

---

✅ **Final:**  
- **Time:** `O(n log n)`  
- **Space:** `O(1)` (auxiliary)

---
## 📝 Code Implementation

```python
class Solution:
    def minMaxCandy(self, prices, k):
        prices.sort()

        # Minimum cost
        min_cost = 0
        i = 0
        n = len(prices)
        while i < n:
            min_cost += prices[i]  # Buy cheapest available
            i += (k + 1)           # Skip k free candies

        # Maximum cost
        max_cost = 0
        i = n - 1
        while i >= 0:
            max_cost += prices[i]  # Buy most expensive available
            i -= (k + 1)           # Skip k free candies

        return [min_cost, max_cost]

```
---
## 📌 Applications of the Problem

This problem is not just about candies — it represents a class of **"buy X get Y free"** optimization problems.  
It can be applied in:

1. **Retail & E-Commerce Offers**
   - Determining the minimum and maximum spend for promotional offers like:
     - *Buy 1 get 1 free*
     - *Buy 1 get 2 free*
     - *Buy X get Y free*
   - Helps in analyzing **customer spending patterns** and **marketing campaign costs**.

2. **Inventory Management**
   - Calculating how much budget is needed to clear stock during sales when free products are given.
   - Helps in **stock clearance planning**.

3. **Event Management**
   - In events/fairs where tokens or passes have "buy X get Y" offers, it helps in estimating total cost for different purchase strategies.

4. **Game Economy Design**
   - In games where items can be purchased with in-game currency and bonuses/freebies exist, this logic is used to:
     - Calculate **minimum required coins**.
     - Determine **maximum spending paths**.

5. **Supply Chain Optimization**
   - Deciding purchase strategy to minimize procurement cost when suppliers provide free items with bulk orders.

---

💡 **Core Concept:**  
This problem is essentially about **greedy optimization** in selection under a "free item" constraint.  
- **Min cost** → buy the cheapest first.  
- **Max cost** → buy the most expensive first.
---
**🏷️ Tags:**  
`#Greedy` `#ArraySorting` `#TwoPointer` `#Optimization` `#BuyXGetYFree` `#InterviewPrep` `#ECommerce` `#CostMinimization` `#CostMaximization`
