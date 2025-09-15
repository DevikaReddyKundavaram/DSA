# 📚 String Stack

---

## 📖 Problem Statement
You are given two strings `pat` and `tar` consisting of lowercase English characters.  
You can construct a new string `s` by performing one of the following operations for each character in `pat`:

1. Append the character `pat[i]` to the string `s`.  
2. Delete the last character of `s` (if `s` is empty, do nothing).  

After processing all characters of `pat`, determine whether it is possible to make `s == tar`.

---

## 🔎 Examples
```text
Example 1
Input: pat = "geuaek", tar = "geek" Output: true Explanation:
Append 'g','e','u' → s = "geu"
Delete 'a' → s = "ge"
Append 'e','k' → s = "geek"

Example 2
Input: pat = "agiffghd", tar = "gfg" Output: true Explanation:
Append 'g','i' → "gi"
Delete 'f' → "g"
Append 'f','g','h' → "gfgh"
Delete 'd' → "gfg"

Example 3
Input: pat = "ufahs", tar = "aus" Output: false
```
---

## 📝 Algorithm
1. Start from the **end of `pat` and `tar`**.  
2. Maintain a pointer `j` for `tar` and a `skip` counter.  
3. Traverse `pat` backwards:
   - If `skip > 0`, ignore current char and decrement `skip`.  
   - Else if `pat[i] == tar[j]`, match both and move left.  
   - Else, increment `skip` (the char will be deleted in forward traversal).  
4. If `j < 0` after the traversal, return **True**, else **False**.  

---
## 📊 Complexities

- **Time Complexity:** O(n)  
  We traverse the string `pat` once (where n = length of `pat`).  

- **Space Complexity:** O(1)  
  Only a few pointers (`i`, `j`) and a counter (`skip`) are used. No extra data structures.
---

## 🖥️ Code (Python)

```python
class Solution:
    def stringStack(self, pat: str, tar: str) -> bool:
        # quick fail case
        if len(tar) > len(pat):
            return False

        i = len(pat) - 1
        j = len(tar) - 1
        skip = 0

        while i >= 0:
            if skip > 0:
                skip -= 1
                i -= 1
            elif j >= 0 and pat[i] == tar[j]:
                i -= 1
                j -= 1
            else:
                skip += 1
                i -= 1

        return j < 0
```
---
## Applications of Hash Tables

1. **Databases**  
   - Indexing for fast retrieval of records  
   - Hash-based joins  

2. **Compilers & Interpreters**  
   - Symbol table management (variables, functions, classes)  

3. **Caching**  
   - Storing recently accessed data (e.g., browser cache, DNS cache)  

4. **Cryptography & Security**  
   - Hashing for digital signatures, password storage, integrity checks  

5. **Networking**  
   - Routing tables  
   - IP lookup and MAC address resolution  

6. **File Systems**  
   - Directory structures and quick file lookups  

7. **Search Engines**  
   - Storing word-to-document mappings (inverted index)  

8. **Data Deduplication**  
   - Detecting duplicates in large datasets  

9. **Load Balancing**  
   - Consistent hashing for distributed systems  

10. **Games & AI**  
   - Storing game states, transposition tables in chess engines
---
## Tags

- `#HashTable`
- `#DataStructures`
- `#Algorithms`
- `#ComputerScience`
- `#InterviewPrep`
- `#Coding`
- `#Python`
- `#Applications`
