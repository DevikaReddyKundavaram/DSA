# 🔠 Problem: Longest Word With All Prefixes Present (Trie Approach)

**Platform:** GeeksForGeeks  
**Date Solved:** 10 July 2025  
**Difficulty:** Medium  

---

## 📜 Problem Statement

Given an array of strings `words[]`, return the **longest word** such that **every prefix** of that word is also present in the array.

- If multiple answers exist, return the **lexicographically smallest** one.

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

💼 Applications of Trie (In Real-World)
Application→Description
🔍 Auto-complete Engines	→Typing “pro” → suggestions like “program”, “process”, etc.
📚 Dictionary Word Lookup	→Faster word search, with support for prefix-based logic.
🔐 IP Routing (Network Tries)→	Used in longest prefix match for IP addresses (e.g. routers, firewalls).
🧠 Spell Checker	→Detects wrong spellings and suggests possible corrections using prefix paths.
🧠 Word Games / Boggle Solver→	Efficiently verifies valid words in board games using prefix pruning.

🏷️ Tags
#Trie #String #PrefixCheck #Greedy #GFG #LexicographicalOrder #DSA

