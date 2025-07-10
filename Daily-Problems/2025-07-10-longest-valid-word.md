# 🔠 Problem: Longest Word With All Prefixes Present 

**Platform:** GeeksForGeeks  
**Date Solved:** 10 July 2025  
**Difficulty:** Medium  

---

## 📜 Problem Statement

Given an array of strings `words[]`, return the **longest word** such that **every prefix** of that word is also present in the array.

- If multiple answers exist, return the **lexicographically smallest** one.


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
```
---

## 💡 Approach: Using Trie (Prefix Tree)

A **Trie** is perfect here because:
- It allows efficient **prefix traversal**.
- You can check whether each **prefix of a word is itself a word**.

### 🔄 Steps:
1. **Insert** all words into the Trie.
2. For each word:
   - Traverse it in the Trie.
   - Check if **each prefix node is marked as a complete word**.
3. Track the **longest** valid word, and **break ties** using lexicographic order.

---

## 🧠 Algorithm & Data Structures

| Concept        | Used For                        |
|----------------|----------------------------------|
| **Trie**       | Efficient storage of word prefixes |
| **Greedy**     | Picking longest, then lex smallest |
| **DFS/Path Check** | Verifying valid prefixes |


## ✅ Time Complexity

- **Insertion:** O(N × L)  
- **Prefix Check:** O(N × L)  
- **Total:** `O(N × L)`
---
## 🧑‍💻 Python Code (Trie Implementation)

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class Solution:
    def insert(self, word, root):
        node = root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_word = True

    def check_all_prefixes(self, word, root):
        node = root
        for ch in word:
            node = node.children.get(ch)
            if not node or not node.is_word:
                return False
        return True

    def longestString(self, words):
        root = TrieNode()
        for word in words:
            self.insert(word, root)

        longest = ""
        for word in words:
            if self.check_all_prefixes(word, root):
                if len(word) > len(longest) or (len(word) == len(longest) and word < longest):
                    longest = word
        return longest
```
---

## 📌 Applications

| # | Application Area              | Real-World Example |
|---|-------------------------------|--------------------|
| 1 | Auto-complete systems         | Google, IDEs       |
| 2 | Word-building games           | Scrabble, Wordle   |
| 3 | Language learning             | Duolingo, Memrise  |
| 4 | Role-based security           | Admin roles, APIs  |
| 5 | File system path validation   | Linux, Web Servers |
| 6 | NLP subword token validation  | Transformers, BERT |
| 7 | Build system dependency check | CMake, Makefiles   |

---

🏷️ Tags
#Trie #String #PrefixCheck #Greedy #GFG #LexicographicalOrder #DSA

