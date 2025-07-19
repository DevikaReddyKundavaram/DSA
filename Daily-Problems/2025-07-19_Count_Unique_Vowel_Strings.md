# 💡 Count Unique Vowel Strings

## Problem Statement
You are given a lowercase string `s`. Determine the total number of distinct strings that can be formed using the following rules:

1. Identify all **unique vowels** (a, e, i, o, u) present in the string.
2. For each distinct vowel, choose exactly **one occurrence** from `s`.
3. Generate all possible **permutations** of the selected vowels. Each unique arrangement counts as a distinct string.

Return the **total number of such distinct strings**.

---

## 🔍 Examples

### Example 1
**Input:**  
`s = "aeiou"`  
**Output:**  
`120`  

---

### Example 2
**Input:**  
`s = "ae"`  
**Output:**  
`2`  

---

### Example 3
**Input:**  
`s = "aacidf"`  
**Output:**  
`4`  

---

## 🚀 Approach

1. Collect the **indices of each vowel occurrence**.
2. For each vowel, count how many choices exist.
3. Multiply the number of choices for all vowels.
4. Multiply by the factorial of the number of unique vowels.

---
## 📊 Time & Space Complexity

### 🕒 Time Complexity

| Step                              | Complexity |
|-----------------------------------|------------|
| Iterating over string `s`          | O(n)       |
| Collecting positions of vowels     | O(n)       |
| Calculating factorial (max 5!)     | O(1)       |
| Multiplying choices for permutations | O(1)    |
| **Total Time Complexity**          | **O(n)**   |

---

### 🗃️ Space Complexity

| Usage                                          | Space   |
|------------------------------------------------|---------|
| Storing positions of vowels (in worst case)    | O(n)    |
| Storing unique vowels (fixed max 5 vowels)     | O(1)    |
| **Total Space Complexity**                     | **O(n)** |
## ✅ Python Solution
---
```python
from math import factorial
from collections import defaultdict

class Solution:
    def vowelCount(self, s):
        vowels = 'aeiou'
        pos_map = defaultdict(list)

        for idx, char in enumerate(s):
            if char in vowels:
                pos_map[char].append(idx)

        unique_vowels = list(pos_map.keys())
        if not unique_vowels:
            return 0

        choices = [len(pos_map[vowel]) for vowel in unique_vowels]

        total_combinations = 1
        for c in choices:
            total_combinations *= c

        permutations = factorial(len(unique_vowels))

        return total_combinations * permutations
```
---
## 🎯 Applications

### ✅ String Combinatorics
- This problem is a practical example of how permutations and combinations can be applied to strings, especially when selections are constrained.

### ✅ Interview Preparation
- Helps to strengthen concepts related to:
  - Set theory
  - Counting principles (Product Rule, Permutations)
  - String traversal and mapping techniques.

### ✅ Competitive Programming
- Questions like this appear often in coding contests to test understanding of strings, sets, and permutations.

### ✅ Natural Language Processing (NLP)
- Identifying unique patterns of vowels or sounds can be useful in tasks like:
  - Phonetic analysis
  - Syllable pattern recognition
  - Language modeling

### ✅ Software Applications
- Can be used as a subproblem in software where generating valid permutations of constrained inputs (like vowels, keys, sounds) is required.
- Examples: Puzzle games, AI chatbots, educational tools for language learning.
- ---
## 🏷️ Tags

- Strings
- Combinatorics
- Permutations
- Vowels
- Counting Principle
- Set Operations
- Mathematical Logic
- Interview Question
- Competitive Programming
- Python Implementation
  
