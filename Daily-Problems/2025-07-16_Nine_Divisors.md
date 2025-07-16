# 🔢 Nine Divisors Problem

## 📝 Problem Statement
Given a positive integer `n`, count the numbers less than or equal to `n` which have **exactly 9 divisors**.

---

## 📥 Input:
- A single integer `n` where `1 ≤ n ≤ 10^9`.

## 📤 Output:
- Return the count of numbers ≤ `n` having **exactly 9 divisors**.

---

## 📊 Example

### Input:
n=100
### Output:
2

### Explanation:
The numbers are `36` and `100` which have exactly `9` divisors.

---

## 🚀 Algorithm / Approach

### 🔑 Key Insight:
The number of divisors for a number `N = p1^e1 * p2^e2 * ... * pk^ek` is:

We need this count to be **exactly 9**.

### ✅ Ways to achieve 9:
- **Case 1:** `9 = 9 x 1` → Number of the form `p^8`
- **Case 2:** `9 = 3 x 3` → Number of the form `p1^2 * p2^2` where `p1` and `p2` are distinct primes.

---

## 💡 Steps:
1. Generate all primes up to `sqrt(n)` using **Sieve of Eratosthenes**.
2. Count numbers of the form `p^8` such that `p^8 ≤ n`.
3. Count numbers of the form `p1^2 * p2^2` such that `p1 ≠ p2` and `p1^2 * p2^2 ≤ n`.

---

## ⏳ Time & Space Complexity

### Time Complexity:
- Sieve of Eratosthenes: `O(n^0.5 log log n)`
- Checking pairs: `O(k^2)` where `k` is the number of primes up to `sqrt(n)`.
- Overall: Approximately `O(sqrt(n))`

### Space Complexity:
- Storing primes: `O(sqrt(n))`

---

## 🐍 Python Solution
```python
import math
class Solution:
    def countNumbers(self, n):
        # Sieve of Eratosthenes to find primes up to sqrt(n)
        limit = int(n ** 0.5) + 1
        sieve = [True] * limit
        sieve[0] = sieve[1] = False
        
        for i in range(2, int(limit ** 0.5) + 1):
            if sieve[i]:
                for j in range(i * i, limit, i):
                    sieve[j] = False
        
        primes = [i for i in range(2, limit) if sieve[i]]

        count = 0
        
        # Count numbers of the form p^8
        for p in primes:
            if p ** 8 <= n:
                count += 1
        
        # Count numbers of the form p1^2 * p2^2
        length = len(primes)
        for i in range(length):
            for j in range(i + 1, length):
                if primes[i] ** 2 * primes[j] ** 2 <= n:
                    count += 1
                else:
                    break
        
        return count
```
## 🎯 Applications

- ✅ **Competitive Programming:** Helps solve problems related to factors, primes, and divisor counts in contests.
- ✅ **Number Theory:** Useful in problems involving prime factorization, properties of divisors, and mathematical proofs.
- ✅ **Cryptography:** Some cryptographic algorithms rely on properties of numbers with specific factor structures (e.g., RSA with large primes).
- ✅ **Mathematical Modeling:** Certain mathematical problems or simulations require identifying numbers with exact numbers of divisors.
- ✅ **Algorithm Design:** Teaches optimization techniques using number theory and prime sieves.
- ✅ **Interview Preparation:** Strong example for understanding prime-based constraints and combinations of factors.
- ✅ **Data Science (Theoretical):** Insight into factors and divisors can help in data encoding/compression theories.


## 🏷️ Tags

`#Mathematics`  
`#NumberTheory`  
`#PrimeNumbers`  
`#Divisors`  
`#SieveOfEratosthenes`  
`#CompetitiveProgramming`  
`#ProblemSolving`  
`#AlgorithmicThinking`
