# Cutting Binary String 🔥

---

## Problem Statement 📄
You are given a binary string `s` consisting only of characters `'0'` and `'1'`.  
Split this string into the **minimum number of non-empty substrings** such that:  
✅ Each substring represents a **power of 5** in decimal.  
✅ No substring should have **leading zeros**.

If it's impossible to split, return `-1`.

---

## 🔥 Dry Run Example

### Input: `s = "101101101"`

Binary indexes:

### Step-by-step:

| i  | Substring `s[j:i]` | Decimal | Power of 5? | dp[i] Update |
|----|---------------------|---------|-------------|-------------|
| 1  | `1`                 | 1       | ✅           | `dp[1] = 1` |
| 3  | `101`               | 5       | ✅           | `dp[3] = 1` |
| 6  | `101` (3-6)         | 5       | ✅           | `dp[6] = dp[3] + 1 = 2` |
| 9  | `101` (6-9)         | 5       | ✅           | `dp[9] = dp[6] + 1 = 3` |

Final `dp = [0, 1, inf, 1, inf, inf, 2, inf, inf, 3]`  
Answer: `3`

---

## ⏳ Time & Space Complexities

| Type   | Complexity |
|--------|------------|
| **Time Complexity**   | `O(n^2)`  |
| **Reason:** For each `i`, we check all substrings `s[j:i]`. Each substring takes O(1) for `is_power_of_five`. |
| **Space Complexity**  | `O(n)`    |
| **Reason:** DP array of size `n+1` to store minimum cuts. |

---


## 👨‍💻 Code (Python)

```python
class Solution:
    def cuts(self, s):
        n = len(s)
        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        def is_power_of_five(sub):
            if not sub or sub[0] == '0':
                return False
            num = int(sub, 2)
            if num == 0:
                return False
            while num % 5 == 0:
                num //= 5
            return num == 1

        for i in range(1, n + 1):
            for j in range(i):
                if is_power_of_five(s[j:i]):
                    dp[i] = min(dp[i], dp[j] + 1)

        return dp[n] if dp[n] != float('inf') else -1
```


## 🚀 Applications

✅ **Binary String Problems:**  
This problem strengthens your understanding of how to split binary strings optimally based on mathematical properties.

✅ **Bit Manipulation:**  
This problem relates to binary-to-decimal conversion and checking numerical properties (power of 5).

✅ **Dynamic Programming:**  
Classic example of using prefix-based `dp[i]` to track minimal partitions.

✅ **Mathematical String Validation:**  
Useful in validating substrings representing specific patterns (powers of numbers).

✅ **Competitive Programming:**  
Teaches efficient substring checks + optimization via DP for coding interviews.

## 🔖 Tags

- Dynamic Programming (DP)
- Binary Strings
- Substring Problems
- Bit Manipulation
- Number Theory (Powers of 5)
- String Processing
- Mathematical Validation
- Competitive Programming
