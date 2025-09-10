# 🔢 Largest Number in One Swap

---

## 📝 Problem Statement
Given a string `s`, return the **lexicographically largest string** that can be obtained by swapping at most one pair of characters in `s`.

---

## 📌 Examples
```text
Example 1
Input: s = "768"
Output: "867"
Explanation:
Swapping the 1st and 3rd characters (7 and 8 respectively) gives the lexicographically largest string.

Example 2
Input: s = "333"  
Output: "333"  
Explanation:  
Performing any swaps gives the same result i.e "333".
```
---

## 🎯 Constraints
- 1 ≤ |s| ≤ 10⁵  
- '0' ≤ s[i] ≤ '9'  

---

## 💡 Algorithm
1. Store the **rightmost index** of each digit (0–9) in a dictionary.  
2. Traverse the string from **left to right**:
   - For the current digit `d`, check if there exists a **larger digit** (from 9 down to d+1) that appears **after** the current index.  
   - If found, **swap** them and return the result immediately.  
3. If no swap increases the lexicographic order, return the original string.  

---

## 🧩 Dry Run
**Input:** `s = "768"`  
- Last positions → `{7:0, 6:1, 8:2}`  
- At `i=0`, digit = `7`. Look for a bigger digit → finds `8` at pos `2`.  
- Swap → `"867"` ✅  

**Output:** `"867"`  

---

## ⏱️ Time & Space Complexity
- **Time Complexity:** `O(n * 10)` ≈ `O(n)`  
- **Space Complexity:** `O(1)` (only 10 digits stored in map).  

---

## 💻 Python Code

```python
class Solution:
    def largestSwap(self, s: str) -> str:
        s = list(s)
        n = len(s)

        # Track the rightmost position of each digit
        last_pos = {int(s[i]): i for i in range(n)}

        for i in range(n):
            curr_digit = int(s[i])
            # Look for a larger digit
            for d in range(9, curr_digit, -1):
                if d in last_pos and last_pos[d] > i:
                    # Swap and return result
                    s[i], s[last_pos[d]] = s[last_pos[d]], s[i]
                    return "".join(s)

        return "".join(s)
```
---
## 🌍 Applications
- 📱 **Mobile Keypad Optimization** – Arranging digits in the most efficient/optimal order.  
- 🔢 **Competitive Programming** – Problems where only limited swaps are allowed to maximize/minimize lexicographic/numeric value.  
- 💳 **Banking/Finance Systems** – Maximizing account or transaction codes with minimal swaps for validation checks.  
- 📊 **Data Sorting/Ranking** – Creating the highest rank possible with a single allowed modification.  
- 🧮 **Mathematical Puzzles** – Useful in greedy optimization puzzles where minimal operations are permitted.  
---
## 🏷️ Tags
`#Greedy` `#Strings` `#Lexicographic` `#Optimization` `#Swapping`
