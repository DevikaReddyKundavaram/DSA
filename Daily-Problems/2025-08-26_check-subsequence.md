# ✅ Problem: Check if a String is Subsequence of Other  

---

## 📌 Problem Statement
Given two strings `s1` and `s2`. You have to check if `s1` is a subsequence of `s2` or not.  

A **subsequence** is a sequence that can be derived from another sequence by deleting some elements without changing the order of the remaining elements.  

---

## 🔍 Examples

### Example 1
**Input:**  
s1 = "AXY"
s2 = "YADXCP"
**Output:**  
false
**Explanation:**  
`s1` is not a subsequence of `s2` as `'Y'` appears before `'A'`.

---

### Example 2
**Input:**  
s1 = "gksrek"
s2 = "geeksforgeeks"
**Output:**  
true
**Explanation:**  
If we combine the bold characters of `"geeksforgeeks"`, it equals `s1`.  
So `s1` is a subsequence of `s2`.  

---


## ⚙️ Constraints
- `1 ≤ |s1|, |s2| ≤ 10^6`

---

## 🧠 Approach
- Use **two pointers** technique:
  - One pointer `i` for `s1`
  - One pointer `j` for `s2`
- Traverse `s2`, and whenever `s1[i] == s2[j]`, move `i` ahead.
- At the end, if `i == len(s1)`, then `s1` is a subsequence of `s2`.

---
## ⏱ Complexity Analysis

- **Time Complexity:**  
  - We traverse the second string `s2` once while checking characters of `s1`.  
  - Hence, the time complexity is **O(|s2|)**.  

- **Space Complexity:**  
  - We only use a few integer variables (`i`, `j`) for pointers.  
  - No extra data structures are required.  
  - Hence, the space complexity is **O(1)**.  

- **Best Case:**  
  - When the first few characters of `s1` match early in `s2`.  
  - Runs faster but still bounded by **O(|s2|)**.  

- **Worst Case:**  
  - When either `s1` is not present at all, or all of its characters are found near the end of `s2`.  
  - Still **O(|s2|)**.  

- **Average Case:**  
  - On random strings, expected traversal is proportional to the length of `s2`.  
  - So complexity remains **O(|s2|)**.
---


## 📝 Code (Python)

```python
class Solution:
    def isSubSeq(self, s1, s2):## 🌍 Applications of Subsequence Checking

- 🔑 **String Pattern Matching**  
  - Used to verify if a smaller string exists as a subsequence in a larger string without exact continuity.  

- 📜 **Text Editing & Autocomplete Systems**  
  - Helps in checking if typed characters match possible dictionary words.  
  - Example: Typing "grmr" can match "grammar" as a subsequence.  

- 🧬 **DNA / Protein Sequence Analysis**  
  - In bioinformatics, subsequence checking is used to find gene/protein sequences within larger DNA chains.  

- 🛠 **Data Filtering**  
  - Useful in filtering items (like searching for a file by typing part of its name) when order matters but continuity doesn’t.  

- 🎮 **Gaming & Input Validation**  
  - Used in scenarios where a sequence of moves (like button presses) needs to be verified inside a larger sequence of actions.  

- 🔄 **Version Control & Merging**  
  - Detects whether a set of changes/edits is a subsequence of a master version.  
---
## 🏷️ Tags

`#Strings`  
`#TwoPointers`  
`#Greedy` 
`#PatternMatching`  
`#Subsequence`  
`#Searching`  

        i, j = 0, 0
        while i < len(s1) and j < len(s2):
            if s1[i] == s2[j]:
                i += 1
            j += 1
        return i == len(s1)
```
---

