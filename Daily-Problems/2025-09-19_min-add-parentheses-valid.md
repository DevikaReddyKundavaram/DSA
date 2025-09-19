# 🔧 Min Add to Make Parentheses Valid
---

## 📖 Problem Statement  
You are given a string `s` consisting only of the characters `'('` and `')'`.  
Your task is to determine the **minimum number of parentheses** (either `'('` or `')'`) that must be inserted at any positions to make the string `s` a **valid parentheses string**.

A parentheses string is considered valid if:
1. Every opening parenthesis `'('` has a corresponding closing parenthesis `')'`.  
2. Every closing parenthesis `')'` has a corresponding opening parenthesis `'('`.  
3. Parentheses are properly nested.  

---

## 🔍 Examples  
```text
Example 1:
Input: s = "(()("
Output: 2  
Explanation: There are two unmatched '(' at the end, so we need to add two ')' to make the string valid.  

Example 2:
Input: s = ")))"  
Output: 3  
Explanation: Three '(' need to be added at the start to make the string valid.  

Example 3:
Input: s = ")()()"
Output: 1  
Explanation: The very first ')' is unmatched, so we need to add one '(' at the beginning.  
```
---

## 📏 Constraints
- `1 ≤ s.size() ≤ 10^5`  
- `s[i] ∈ { '(', ')' }`  

---
## 📝 Algorithm  

1. Initialize two counters:  
   - `open_count = 0` → tracks unmatched `'('`.  
   - `insertions = 0` → tracks the number of insertions needed.  

2. Traverse the string `s` character by character:  
   - If the character is `'('`, increment `open_count`.  
   - If the character is `')'`:  
     - If `open_count > 0`, decrement `open_count` (we matched one `'('`).  
     - Else, increment `insertions` (need an extra `'('` to balance).  

3. After traversal:  
   - Any remaining `open_count` means unmatched `'('`.  
   - Add this to `insertions`.  

4. Return `insertions` as the final answer.  
---
## ⏱️ Time & Space Complexity  

- **Time Complexity:** `O(n)`  
  - We traverse the string once, where `n = len(s)`.  

- **Space Complexity:** `O(1)`  
  - Only a few counters are used (`open_count`, `insertions`), independent of input size.  
---

## 🧩 Code (Python)

```python
class Solution:
    def minParentheses(self, s: str) -> int:
        open_count = 0  
        insertions = 0   
        
        for char in s:
            if char == '(':
                open_count += 1
            else:  # char == ')'
                if open_count > 0:
                    open_count -= 1  
                else:
                    insertions += 1  
        
        return insertions + open_count
```
---
## 📌 Applications  

- **Compilers & Parsers** – Ensuring balanced parentheses in programming languages.  
- **Expression Validation** – Checking correctness of mathematical expressions.  
- **Code Editors / IDEs** – Auto-fixing or highlighting unmatched parentheses.  
- **Query Languages (SQL, Regex)** – Validating nested query conditions.  
- **Interview Problems** – Classic stack/greedy problem often asked in coding interviews.  

---
## 🏷️ Tags  
`#String` `#Stack` `#Greedy` `#Parentheses` `#Validation`  
