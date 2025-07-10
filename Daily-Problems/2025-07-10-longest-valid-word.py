# 🔠 Problem: Longest Valid Word (All Prefixes Present)

**Platform:** GeeksForGeeks  
**Date Solved:** 10 July 2025  

---

## 📜 Problem Statement

Given an array of strings `words[]`, find the **longest word** such that **every prefix** of that word is also present in the array.

> If multiple such words have the same length, return the **lexicographically smallest** one.

---

## 📥 Input & Output

### Example 1:
Input: ["p", "pr", "pro", "probl", "problem", "pros", "process", "processor"]
Output: pros

### Example 2:
Input: ["ab", "a", "abc", "abd"]
Output: abc


---

## 💡 Approach & Intuition

To solve the problem efficiently:
1. **Sort the words lexicographically**.
2. Maintain a set of valid words that can be built character-by-character.
3. For each word:
   - If length is 1, or
   - If its prefix (`word[:-1]`) is in the set,
   - Then it's a valid word. Add it to the set.
4. Track the longest such valid word.

This ensures:
- Lexicographically smaller words come first due to sorting.
- Only those with complete valid prefixes are considered.

---

## 🧠 Algorithm & Data Structures

- **Sorting** (for lexicographical order)
- **Set** (to quickly check prefixes)
- **Greedy approach** (build only when prefix exists)

---

## ⏱️ Complexity

| Metric         | Value                     |
|----------------|---------------------------|
| Time Complexity| O(n * m)                  |
| Space Complexity| O(n * m) (due to set)     |

Where:
- `n = number of words`
- `m = average length of a word`

---

## 🧪 Dry Run

Input: `["a", "ab", "abc", "abd"]`  
Sorted: `["a", "ab", "abc", "abd"]`

| Word | Prefix Exists? | Add to Set | Current Best |
|------|----------------|------------|--------------|
| a    | -              | ✅         | a            |
| ab   | a              | ✅         | ab           |
| abc  | ab             | ✅         | abc          |
| abd  | ab             | ✅         | abc (smaller than abd) |

Final Answer: `abc`

---

## 🧑‍💻 Code (Python)

```python
class Solution:
    def longestString(self, words):
        words.sort()
        valid = set()
        ans = ""
        for word in words:
            if len(word) == 1 or word[:-1] in valid:
                valid.add(word)
                if len(word) > len(ans):
                    ans = word
        return ans


🏷️ Tags
#Greedy #Set #Prefix #Sorting #Lexicographical #StringHandling
