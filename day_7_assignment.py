
# 💡 **Question 1**

# Given two strings s and t, *determine if they are isomorphic*.

# Two strings s and t are isomorphic if the characters in s can be replaced to get t.

# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

# **Example 1:**

# **Input:** s = "egg", t = "add"

# **Output:** true

s = "egg"
t = "add"
def is_isomorphic(s,t):
    print(list(map(s.index,s))==list(map(t.index,t)))   

is_isomorphic(s,t)

# 💡 **Question 2**

# Given a string num which represents an integer, return true *if* num *is a **strobogrammatic number***.

# A **strobogrammatic number** is a number that looks the same when rotated 180 degrees (looked at upside down).

# **Example 1:**

# **Input:** num = "69"

# **Output:**

# true


class Solution:
  def isStrobogrammatic(self, num: str) -> bool:
    rotated = ['0', '1', 'x', 'x', 'x',
               'x', '9', 'x', '8', '6']
    l = 0
    r = len(num) - 1

    while l <= r:
      if num[l] != rotated[ord(num[r]) - ord('0')]:
        return False
      l += 1
      r -= 1

    return True





# 💡 **Question 3**

# Given two non-negative integers, num1 and num2 represented as string, return *the sum of* num1 *and* num2 *as a string*.

# You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You must also not convert the inputs to integers directly.

# **Example 1:**

# **Input:** num1 = "11", num2 = "123"

# **Output:**

# "134"



num1 = "11"
num2 = "123"

i = len(num1) - 1
j = len(num2) - 1
carry = 0
ans = []

while i>=0 or j>=0 or carry:
    if i >= 0:
        carry += int(num1[i])
    if j >= 0:
        carry += int(num2[j])
    ans.append(str(carry % 10))
    carry = carry // 10
    
    i -= 1
    j -= 1
    
print(''.join(ans[::-1]))
        
    
    
    
    
# 💡 **Question 4**

# Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

# **Example 1:**

# **Input:** s = "Let's take LeetCode contest"

# **Output:** "s'teL ekat edoCteeL tsetnoc"


s = "Let's take LeetCode contest"
print(' '.join([i[::-1] for i in s.split()]))





# 💡 **Question 5**

# Given a string s and an integer k, reverse the first k characters for every 2k characters counting from the start of the string.

# If there are fewer than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and leave the other as original.

# **Example 1:**

# **Input:** s = "abcdefg", k = 2

# **Output:**

# "bacdfeg"


s = "abcdefg"
k = 2


class Solution:
  def reverseStr(self, s: str, k: int) -> str:
    return s[:k][::-1] + s[k:2 * k] + self.reverseStr(s[2 * k:], k) if s else ""


# print(s)
# print(s[:k][::-1],s[k:2 * k])


# 💡 **Question 6**

# Given two strings s and goal, return true *if and only if* s *can become* goal *after some number of **shifts** on* s.

# A **shift** on s consists of moving the leftmost character of s to the rightmost position.

# - For example, if s = "abcde", then it will be "bcdea" after one shift.

# **Example 1:**

# **Input:** s = "abcde", goal = "cdeab"

# **Output:**

# true


def rotateString(self, A: str, B: str) -> bool:
        return len(A) == len(B) and B in A + A

# s = "abcde"
# goal = "cdeab"
# print(len(s) == len(goal) and (s+s).find(goal)> 0)

# 💡 **Question 7**

# Given two strings s and t, return true *if they are equal when both are typed into empty text editors*. '#' means a backspace character.

# Note that after backspacing an empty text, the text will continue empty.

# **Example 1:**

# **Input:** s = "ab#c", t = "ad#c"

# **Output:** true

# **Explanation:**

# Both s and t become "ac".

s = "ab##"
t = "c#d#"

class Solution:
  def backspaceCompare(self, s, t) -> bool:
    def backspace(s):
      stack = []
      for c in s:
        if c != '#':
          stack.append(c)
        elif stack:
          stack.pop()
      return stack

    return backspace(s) == backspace(t)


