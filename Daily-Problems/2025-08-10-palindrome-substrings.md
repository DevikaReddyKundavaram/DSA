# Problem: Palindrome SubStrings
---

## 📜 Problem Statement
Given a string `s`, count all **palindromic substrings** present in the string, where the length of the substring is **greater than or equal to 2**.  
A substring is palindromic if it reads the same forwards and backwards.

---

## 📝 Input / Output

**Input:**  
- A string `s` containing only lowercase English letters.

**Output:**  
- An integer representing the count of palindromic substrings with length ≥ 2.

---
```text
## 🔍 Examples

**Example 1:**
Input: s = "abaab" Output: 3 Explanation: "aba", "aa", "baab"

**Example 2:**

Input: s = "aaa" Output: 3 Explanation: "aa", "aa", "aaa"

**Example 3:**

Input: s = "abbaeae" Output: 4 Explanation: "bb", "abba", "aea", "eae"
```
---

## 🔹 Constraints

- 2 ≤ s.size() ≤ 5 × 10^3 s contains only lowercase English letters

---

## ⚙️ Algorithm
**Approach: Expand Around Center**
1. Iterate over every character in the string, considering each as the center of a possible palindrome.
2. For each center, expand outward in both directions (left and right) while the characters match.
3. Count palindromes only if their length ≥ 2.
4. Do this for:
   - **Odd-length palindromes** (center at a single character).
   - **Even-length palindromes** (center between two characters).
5. Return the total count.

---
### ⏳ Complexity Analysis

**Time Complexity:**  
- **Worst case:** `O(n²)` – For each character as the center, expansion can take up to `n/2` steps in both directions.  
- **Best case:** `O(n)` – When no expansions occur beyond one step (all characters are different).  

**Space Complexity:**  
- `O(1)` – Uses constant extra space for pointers/counters only.
---
## 🖥️ Code Implementation

```python
class Solution:
    def countPS(self, s):
        n = len(s)
        count = 0
        
        def expand(l, r):
            nonlocal count
            while l >= 0 and r < n and s[l] == s[r]:
                if r - l + 1 >= 2:
                    count += 1
                l -= 1
                r += 1
        
        for center in range(n):
            expand(center, center)       # Odd length
            expand(center, center + 1)   # Even length
        
        return count
```
---

### 📌 Applications

- **Text Analysis:** Detecting repeated patterns or palindromic sequences in natural language processing.  
- **DNA Sequencing:** Identifying reverse-complement sequences in bioinformatics.  
- **Data Compression:** Finding symmetrical patterns for optimized encoding.  
- **Cryptography:** Detecting symmetric patterns in cipher texts for cryptanalysis.  
- **Search Engines:** Pattern-based substring detection for fast queries.  
- **Competitive Programming:** Common subproblem in string manipulation and dynamic programming challenges.
---
### 🏷️ Tags
`#Palindrome`, `#StringProcessing`, `#DynamicProgramming`, `#TwoPointer`, `#SubstringSearch`, `#PatternMatching`, `#InterviewPrep`, `#HardProblems`

