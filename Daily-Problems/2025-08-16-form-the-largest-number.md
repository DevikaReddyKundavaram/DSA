## 📝 Problem: Form the Largest Number


---

### 📜 Description
Given an array of integers `arr[]` representing non-negative integers, arrange them so that after concatenating all of them in order, it results in the largest possible number. Since the result may be very large, return it as a string.

---

### 🔹 Examples
```text
Example 1
Input: arr[] = [3, 30, 34, 5, 9]
Output: 9534330
Explanation: Arrange as [9, 5, 34, 3, 30] to get the largest number.

Example 2
Input: arr[] = [54, 546, 548, 60]
Output: 6054854654
Explanation: Arrange as [60, 548, 546, 54] to get the largest number.

Example 3
Input: arr[] = [3, 4, 6, 5, 9]
Output: 96543
Explanation: Arrange as [9, 6, 5, 4, 3] to get the largest number.
```
---

### 🎯 Constraints
- `1 ≤ arr.size() ≤ 10^5`
- `0 ≤ arr[i] ≤ 10^5`

---

### 💡 Approach
1. Convert all integers to strings for concatenation comparison.
2. Sort numbers with a **custom comparator**:
   - Compare `x+y` vs `y+x` (as strings).
   - If `x+y > y+x`, then `x` should come before `y`.
3. Concatenate sorted strings.
4. Handle edge case: if result starts with `'0'`, return `"0"`.

---

### 🖥️ Python Code
```python
from functools import cmp_to_key

class Solution:
    def findLargest(self, arr):
        arr = list(map(str, arr))
        
        def compare(x, y):
            if x + y > y + x:
                return -1
            elif x + y < y + x:
                return 1
            else:
                return 0
        
        arr.sort(key=cmp_to_key(compare))
        result = ''.join(arr)
        
        return result if result[0] != '0' else '0'
```
---

### ⏱️ Time and Space Complexity

- **Time Complexity:**  
  - Sorting: `O(N log N)` — due to custom comparator sorting.  
  - Concatenation: `O(N)` — joining all numbers into a string.  
  - **Overall:** `O(N log N)`

- **Space Complexity:**  
  - `O(N)` — for storing the string representations of the integers.  
  - Comparator overhead is constant.
---
### 🌍 Applications

- **Big Number Formation in Competitive Programming:**  
  Used in problems where you need to arrange digits or numbers to form the largest possible value.  

- **Custom Sorting Logic Demonstrations:**  
  Helps understand and implement **comparator-based sorting** beyond numerical order.  

- **Real-world Usage:**  
  - Arranging product IDs or SKUs to generate visually appealing largest codes.  
  - Forming the largest possible registration or identification number from given parts.  

- **Greedy Algorithm Illustration:**  
  A perfect example of a **Greedy + Sorting** hybrid problem.
---
**Tags:** 🏷️ `#GreedyAlgorithm` `#CustomSorting` `#StringManipulation` `#ComparatorLogic` `#Arrays`
