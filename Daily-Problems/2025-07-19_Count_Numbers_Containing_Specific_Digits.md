# 📅 Date: 2025-07-19  
# 💡 Problem: Count Numbers Containing Specific Digits  

---

## 🚩 Problem Statement  
You are given an integer `n` representing the number of digits in a number, and an array `arr[]` containing digits from `0` to `9`.  
Your task is to count how many `n`-digit positive integers can be formed such that **at least one digit from the array `arr[]` appears in the number.**

---

## 🔍 Examples

### Example 1
**Input:**  
n = 1  
arr = [1, 2, 3]  
**Output:** 3  

---

### Example 2
**Input:**  
n = 2  
arr = [3, 5]  
**Output:** 34  

---

### Example 3
**Input:**  
n = 6  
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]  
**Output:** 900000  

---

## 🚀 Approach

1. **Total `n`-digit numbers** = `9 * 10^(n-1)`
2. **Find count of numbers with no digits from `arr`.**
3. **Answer = Total - Count with no digits from `arr`.**
4. Count valid first digit choices (cannot be `0`).
5. Count valid choices for other digits (can include `0`).

---
## 📊 Time & Space Complexity

### 🕒 Time Complexity

| Step                              | Complexity |
|-----------------------------------|------------|
| Iterating over digits `0-9`        | O(1)       |
| Calculating totals                 | O(1)       |
| **Total Time Complexity**          | **O(1)**   |

---

### 🗃️ Space Complexity

| Usage                              | Space |
|------------------------------------|-------|
| Storing sets (forbidden/allowed)    | O(1)  |
| **Total Space Complexity**          | **O(1)** |
---
## ✅ Python Solution

```python
class Solution:
    def countValid(self, n, arr):
        forbidden = set(arr)
        allowed = set(range(10)) - forbidden
        
        if not allowed:
            return 0
        
        first_digit_choices = len([d for d in allowed if d != 0])
        other_digit_choices = len(allowed)
        
        total_n_digit_numbers = 9 * (10 ** (n - 1))
        
        if first_digit_choices == 0:
            return total_n_digit_numbers
        
        count_without_forbidden = first_digit_choices * (other_digit_choices ** (n - 1))
        return total_n_digit_numbers - count_without_forbidden
```

## 🎯 Applications

- 📊 **Combinatorics in Digit-Based Problems**  
  Helps understand how to count combinations where certain digits must or must not appear.
  
- 📝 **Interview Preparation**  
  Strengthens concepts related to:
  - Permutations and Combinations
  - Set operations
  - Counting Principle
  
- 🏆 **Competitive Programming**  
  Useful in problems involving:
  - Valid number formations
  - Digit-based constraints
  
- 📐 **Mathematics in Digital Systems**  
  Relates to forming valid codes or numbers with specific restrictions.

---

## 🏷️ Tags

`#Strings`, `#Combinatorics`, `#Permutations`, `#Counting`, `#SetTheory`, `#NumberTheory`, `#Mathematics`
