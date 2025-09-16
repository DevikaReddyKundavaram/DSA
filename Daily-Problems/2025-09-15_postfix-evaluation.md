# 🔢 Postfix Evaluation

## 📌 Problem Statement  
You are given an array of strings `arr[]` that represents a valid arithmetic expression written in **Reverse Polish Notation (Postfix Notation)**.  
Your task is to evaluate the expression and return an integer representing its value.

- A postfix expression is of the form `operand1 operand2 operator` (e.g., `a b +`).  
- Division between two integers always computes the **floor value**.  
- It is guaranteed that the result of the expression and all intermediate calculations will fit in a **32-bit signed integer**.

---

## ✅ Examples  
```text
Example 1:
Input: arr[] = ["2", "3", "1", "*", "+", "9", "-"]
Output: -4
Explanation:
Infix: 2 + (3 * 1) – 9 = 5 – 9 = -4 

Example 2:
Input: arr[] = ["2", "3", "^", "1", "+"]
Output: 9
Explanation:
Infix: 2 ^ 3 + 1 = 8 + 1 = 9
```
---

## 📏 Constraints  
- `3 ≤ arr.size() ≤ 10^3`  
- `arr[i]` is either:  
  - An operator → `"+"`, `"-"`, `"*"`, `"/"`, `"^"`  
  - Or an integer → in the range `[-10^4, 10^4]`  

---

## 🧮 Approach  
1. Use a **stack** to store operands.  
2. Traverse each element of `arr`:  
   - If it’s a number → push onto the stack.  
   - If it’s an operator → pop top two elements, apply operation, and push result back.  
3. At the end, the stack will contain the final evaluated result.  

---
### ⏱️ Complexities

- **Time Complexity:** `O(n)`  
  - We process each element in the postfix expression exactly once (push or pop operation).  

- **Space Complexity:** `O(n)`  
  - In the worst case, all operands may be pushed onto the stack before any operator is encountered.
---

## 📝 Code (Python)

```python
class Solution:
    def evaluatePostfix(self, arr):
        stack = []
        
        for token in arr:
            if token not in ["+", "-", "*", "/", "^"]:
                stack.append(int(token))  # push numbers
            else:
                b = stack.pop()
                a = stack.pop()
                
                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                elif token == "/":
                    # integer division with floor
                    stack.append(int(a / b))  
                elif token == "^":
                    stack.append(a ** b)
        
        return stack[-1]
```
---
### 🛠️ Applications

- **Compiler Design:** Used in parsing and evaluating arithmetic expressions efficiently.  
- **Expression Evaluation:** Helps in building calculators and interpreters for arithmetic expressions.  
- **Stack-based Machines:** Widely used in stack-oriented programming languages and virtual machines (e.g., JVM, PostScript).  
- **Arithmetic Optimizations:** Eliminates the need for parentheses in expressions, simplifying evaluation.  
- **Reverse Polish Calculators:** Basis for old and modern calculators that use postfix notation.
---
### 🏷️ Tags
- `#Stack`  
- `#ExpressionEvaluation`  
- `#PostfixNotation`  
- `#Mathematics`  
- `#CompilerDesign`
