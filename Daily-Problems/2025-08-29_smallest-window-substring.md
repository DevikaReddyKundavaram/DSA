# 📝 Problem: Smallest Window Containing All Characters
---

## 📌 Problem Statement  
Given two strings `s` and `p`. Find the smallest substring in `s` consisting of all the characters (including duplicates) of the string `p`. Return empty string in case no such substring is present.  
If multiple substrings of the same length exist, return the one with the least starting index.  

---

## 🔑 Examples 
```text
Example1:
Input: s = "timetopractice", p = "toc"
Output: "toprac"

Example2:
Input: s = "zoomlazapzo", p = "oza"  
Output: "apzo" 

Example3:
Input: s = "zoom", p = "zooe"
Output: ""
```
---

## 💡 Approach  
- Use **sliding window** with two pointers.  
- Maintain character frequency of `p` using a counter.  
- Expand right pointer until all characters are covered.  
- Shrink from left to minimize the window.  
- Track smallest valid window.  

---
## ⏱️ Complexity Analysis  

- **Time Complexity:** `O(|s| + |p|)`  
- **Space Complexity:** `O(|p|)`  
---

## 🧑‍💻 Code (Python)

```python
from collections import Counter

class Solution:
    def smallestWindow(self, s, p):
        need = Counter(p)
        missing = len(p)
        left = start = end = 0

        for right, ch in enumerate(s, 1):
            if need[ch] > 0:
                missing -= 1
            need[ch] -= 1

            if missing == 0:
                while left < right and need[s[left]] < 0:
                    need[s[left]] += 1
                    left += 1
                if end == 0 or right - left < end - start:
                    start, end = left, right
                need[s[left]] += 1
                missing += 1
                left += 1

        return s[start:end]
```
---

## 🌍 Applications  

- 🔍 Used in **search engines** to find relevant passages containing required keywords.  
- 🧬 Helpful in **bioinformatics** for pattern matching in DNA/protein sequences.  
- 📊 Applied in **data mining** and **information retrieval** to detect smallest spans containing query terms.  
- 🛒 Useful in **recommendation systems** for matching required features within minimal context.  
---
## 🏷️ Tags  

`#Strings` `#Hashing` `#SlidingWindow` `#TwoPointers` `#Hard`  
