## 🧩 Roman Number to Integer

### 📝 Problem Statement
Given a string `s` in Roman number format, convert it to an integer.

Roman numeral symbols and their corresponding values are as follows:

- I = 1  
- V = 5  
- X = 10  
- L = 50  
- C = 100  
- D = 500  
- M = 1000  

A Roman numeral is typically written from largest to smallest left to right. However, in some cases, a smaller number precedes a larger one to indicate subtraction.

---

### 📥 Input
- A string `s`, where `1 ≤ len(s) ≤ 15`
- `s[i]` belongs to `[I, V, X, L, C, D, M]`

---

### 📤 Output
- An integer representing the equivalent decimal value of the Roman numeral.

---

### 💡 Examples
```text
#### Example 1:
Input:  "IX"
Output: 9
Explanation: X (10) > I (1), so 10 - 1 = 9.

#### Example 2:

Input:  "XL"
Output: 40
Explanation: L (50) > X (10), so 50 - 10 = 40.
```
---

### 🧠 Algorithm

1. Create a dictionary `roman_map` for symbol-to-value mapping.
2. Initialize `total = 0`.
3. Loop through the characters in the string `s`:
   - If the current symbol has a smaller value than the next one, subtract it.
   - Otherwise, add it to the total.
4. Return the final `total`.

---

### ⏱️ Time & Space Complexity

- **Time Complexity:** O(n) — where n is the length of the string.
- **Space Complexity:** O(1) — only a fixed-size map is used.

---

### 👩‍💻 Code

```python
class Solution:
    def romanToDecimal(self, s):
        roman_map = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }
        total = 0
        n = len(s)
        
        for i in range(n):
            value = roman_map[s[i]]
            if i + 1 < n and value < roman_map[s[i + 1]]:
                total -= value
            else:
                total += value
                
        return total
```
### 🚀 Applications

- ✅ **Historical Data Conversion**  
  Used to interpret Roman numerals in ancient texts, inscriptions, and monuments.

- ✅ **Educational Tools**  
  Helps in building educational apps for understanding number systems and history.

- ✅ **Calendar & Clock Systems**  
  Roman numerals are often used in traditional clock faces and calendar formats.

- ✅ **Gaming Interfaces**  
  Frequently used in games to denote levels, stages, or ranks (e.g., Level IX, Chapter IV).

- ✅ **Document Formatting**  
  Roman numerals are used in outlines, appendices, and formal documents for sectioning.

### 🏷️ Tags

`#RomanNumerals`  
`#StringManipulation`  
`#GreedyApproach`  
`#MathLogic`  
`#InterviewQuestion`  
`#DataConversion`  
`#NumberSystems`  
`#BeginnerFriendly`
