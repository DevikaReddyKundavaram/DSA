# 🔐 Decode the String  

---

## 📝 Problem Statement  
Given an encoded string `s`, decode it by expanding the pattern `k[substring]`, where the substring inside brackets is written `k` times.  

- `k` is always a positive integer.  
- The encoded string contains only lowercase English alphabets.  
- The length of the decoded string will not exceed `10^5`.  

---

## 📌 Examples  
```text
Example 1:  
Input: s = 3[b2[ca]]
Output: bcacabcacabcaca
Explanation:
Inner substring 2[ca] → caca.
Becomes 3[bcaca] → bcacabcacabcaca.


Example 2:  
Input: s = 3[ab]
Output: ababab
Explanation: Substring "ab" is repeated 3 times → "ababab".
```
---

## ✅ Constraints  
- `1 ≤ |s| ≤ 10^5`  
- `1 ≤ k`  

---

## ⚡ Algorithm  
1. Use two stacks:  
   - One for numbers (`count_stack`)  
   - One for characters (`string_stack`)  
2. Traverse the string `s`:  
   - If a digit → compute full number and push to `count_stack`.  
   - If `[` → push current string to `string_stack` and reset temp string.  
   - If `]` → pop count and previous string, repeat the substring, and append back.  
   - Else → keep adding normal characters.  
3. At the end, the stack will hold the decoded string.  

---
## ⏱️ Time and Space Complexity  

- **Time Complexity:** `O(n)`  
  Each character in the string is processed once, and substring concatenation is handled efficiently.  

- **Space Complexity:** `O(n)`  
  Extra space is used for stacks and temporary substrings.  
---

## 💻 Code (Python3)

```python
class Solution:
    def decodedString(self, s: str) -> str:
        count_stack = []
        string_stack = []
        curr_str = ""
        curr_num = 0
        
        for ch in s:
            if ch.isdigit():
                curr_num = curr_num * 10 + int(ch)  # handle multi-digit numbers
            elif ch == '[':
                count_stack.append(curr_num)
                string_stack.append(curr_str)
                curr_str = ""
                curr_num = 0
            elif ch == ']':
                repeat_times = count_stack.pop()
                prev_str = string_stack.pop()
                curr_str = prev_str + curr_str * repeat_times
            else:
                curr_str += ch
        
        return curr_str
```
---
## 🌍 Applications  

- **Data Compression & Expansion** → Used in decompressing encoded data formats.  
- **Compiler Design** → Parsing and expanding nested grammar expressions.  
- **Text Editors** → Implementing macros or repeat patterns in strings.  
- **Encoding/Decoding in Networks** → Handling structured or compressed message formats.  
- **Problem Solving & Competitive Programming** → Common string decoding pattern for nested expressions.  
---
## 🏷️ Tags  

`#String` `#Stack` `#Decoding` `#NestedPatterns` `#Parsing`  

