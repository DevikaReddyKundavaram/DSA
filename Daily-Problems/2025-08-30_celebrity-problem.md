# 🎭 The Celebrity Problem

## 📌 Problem Statement
A celebrity is a person who is known to all but does not know anyone at a party.  
We are given a square matrix `mat[][]` of size `n x n` representing the people at the party:  

- `mat[i][j] = 1` → person `i` knows person `j`  
- `mat[i][j] = 0` → person `i` does not know person `j`  

A celebrity is a person **who is known by everyone** but **does not know anyone**.  

We need to return the **index of the celebrity** if one exists, else return `-1`.

---

## ✨ Examples
```text
Example 1:
Input: mat = [[1, 1, 0],[0, 1, 0],[0, 1, 1]]
Output: 1
Explanation: Person 0 and 2 know person 1, and person 1 knows no one. Hence, celebrity = 1.

Example 2:
Input: mat = [[1, 1],[1, 1]]
Output: -1
Explanation: Both know each other → no celebrity exists.

Example 3:  
Input: mat = [[1]]
Output: 0
Explanation: Only one person is present → that person is the celebrity.
```
---

## 📝 Constraints
- `1 ≤ mat.size() ≤ 1000`  
- `0 ≤ mat[i][j] ≤ 1`  
- `mat[i][i] = 1`  

---

## 💡 Approach
1. Start with two pointers `i = 0`, `j = n-1`.  
2. If `i` knows `j`, then `i` **cannot** be a celebrity → move `i++`.  
3. Else `j` cannot be a celebrity → move `j--`.  
4. After this elimination process, only one candidate remains.  
5. Verify candidate:  
   - Candidate knows **no one**.  
   - Everyone knows the candidate.  

---
## ⏱️ Complexities

- **Time Complexity:**  
  - Finding candidate → **O(n)**  
  - Verifying candidate → **O(n)**  
  - **Total = O(n)**  

- **Space Complexity:**  
  - Only a few variables used → **O(1)**
---

## ✅ Python Code
```python
class Solution:
    def celebrity(self, mat):
        n = len(mat)
        i, j = 0, n - 1
        
        # Step 1: Find potential candidate
        while i < j:
            if mat[i][j] == 1:
                i += 1  # i knows j → i not celebrity
            else:
                j -= 1  # i does not know j → j not celebrity
        
        candidate = i
        
        # Step 2: Verify candidate
        for k in range(n):
            if k != candidate:
                if mat[candidate][k] == 1 or mat[k][candidate] == 0:
                    return -1
        return candidate
```
---
## 🚀 Applications of The Celebrity Problem

- **Social Networks** → Identify influencers or people with high visibility who don’t follow others back.  
- **Graph Theory** → Models a node with **in-degree = n-1** and **out-degree = 0**.  
- **Event Management** → In a large gathering, helps in identifying the chief guest or key figure.  
- **Database Systems** → Used in dependency resolution where one entity is referenced by all but doesn’t reference others.  
- **Organizational Hierarchy** → Helps in detecting the ultimate boss (everyone knows them, but they don’t know subordinates).  
- **Interview Question Classic** → Tests candidate’s problem-solving using **2-pointer elimination** or **stack-based approaches**.

---
## 🏷️ Tags

`#Matrix` `#Graph` `#Stack` `#TwoPointers` `#EliminationTechnique` `#Medium`









