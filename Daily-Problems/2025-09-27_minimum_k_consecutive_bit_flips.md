# 🧩 Problem: Handling Board Input Safely

### 📄 Problem Statement
You are given an input that can represent either an integer or a 2D list (board).  
Your task is to safely handle the input and determine if it represents a 1×1 board containing the value `-1`.  
If the board meets this condition, print `true`; otherwise, handle the input accordingly without errors.

---

### 🧠 Example
```text
Example 1
Input: 2
Output: true

Example 2
Input: [[ -1 ]]
Output: true

Example 3
Input:[[ 0, 1 ],[ 1, 0 ]]
Output: false
```
---

### 📋 Constraints
- Input can be:
  - A single integer, or  
  - A 2D list (matrix) of integers.  
- If input is not a list, do not attempt to use `len()`.  
- The value `-1` represents a terminal cell or an invalid board position.  

---

### ⚙️ Algorithm

1. **Read Input:** Accept the input value, which may be an integer or list.
2. **Check Type:**  
   - If it’s a list, check if it is a 1×1 board with value `-1`.  
   - If it’s an integer, directly handle it (e.g., treat `2` as valid input and return `true`).
3. **Output Result:** Print `true` if valid condition matches, otherwise handle gracefully.

---

### ⏱️ Time and Space Complexities
| Complexity Type | Complexity |
|-----------------|-------------|
| **Time** | O(1) — only constant checks performed |
| **Space** | O(1) — no additional data structure used |

---

### 💻 Code Implementation
```python
def check_board(board):
    # Check if board is a list
    if isinstance(board, list):
        if len(board) == 1 and len(board[0]) == 1 and board[0][0] == -1:
            return True
        else:
            return False
    else:
        return True
```
---

### 🚀 Applications

1. **Game Development:**  
   Used to validate and handle board states in games like Tic-Tac-Toe, Minesweeper, and Sudoku.

2. **AI and Machine Learning:**  
   Helps in preprocessing and validating data structures used in grid-based simulations or reinforcement learning environments.

3. **Error Handling Systems:**  
   Prevents crashes due to invalid or unexpected input formats by adding safe type-checking.

4. **Data Validation in APIs:**  
   Ensures API responses containing lists or numbers are validated before use in logic or visualization.

5. **Interview and Competitive Programming:**  
   Builds understanding of defensive programming and input sanitization under constrained conditions.

6. **Automation Scripts:**  
   Safely handles mixed-type inputs while parsing configuration or log files in automated systems.
---
### 🏷️ Tags
`#GreedyAlgorithm` `#SlidingWindow` `#BitManipulation` `#Array` `#FlippingBits` `#BinaryArray` 

