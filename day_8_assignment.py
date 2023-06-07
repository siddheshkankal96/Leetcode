
# 💡 **Question 1**

# Given two strings s1 and s2, return *the lowest **ASCII** sum of deleted characters to make two strings equal*.

# **Example 1:**

# **Input:** s1 = "sea", s2 = "eat"

# **Output:** 231

# **Explanation:** Deleting "s" from "sea" adds the ASCII value of "s" (115) to the sum.

# Deleting "t" from "eat" adds 116 to the sum.

# At the end, both strings are equal, and 115 + 116 = 231 is the minimum sum possible to achieve this.





# 💡 **Question 2**

# Given a string s containing only three types of characters: '(', ')' and '*', return true *if* s *is **valid***.

# The following rules define a **valid** string:

# - Any left parenthesis '(' must have a corresponding right parenthesis ')'.
# - Any right parenthesis ')' must have a corresponding left parenthesis '('.
# - Left parenthesis '(' must go before the corresponding right parenthesis ')'.
# - '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".

# **Example 1:**

# **Input:** s = "()"

# **Output:**

# true


s = "()"

ans  = 0
for i in s:
    if i == '(':
        ans += 1 
    elif i == '*':
        if ans > 0:
            ans -= 1
    else:
        if ans > 0:
            ans -= 1
# print(ans == 0)





# 💡 **Question 3**

# Given two strings word1 and word2, return *the minimum number of **steps** required to make* word1 *and* word2 *the same*.

# In one **step**, you can delete exactly one character in either string.

# **Example 1:**

# **Input:** word1 = "sea", word2 = "eat"

# **Output:** 2

# **Explanation:** You need one step to make "sea" to "ea" and another step to make "eat" to "ea".



class Solution:
  def minDistance(self, word1: str, word2: str) -> int:
    m = len(word1)
    n = len(word2)
    dp = [0] * (n + 1)

    for j in range(n + 1):
      dp[j] = j

    for i in range(1, m + 1):
      newDp = [i] + [0] * n
      for j in range(1, n + 1):
        if word1[i - 1] == word2[j - 1]:
          newDp[j] = dp[j - 1]
        else:
          newDp[j] = min(newDp[j - 1], dp[j]) + 1
      dp = newDp

    return dp[n]


word1 = "sea"
word2 = "eat"


def minDistance( word1: str, word2: str) -> int:
        
        len1, len2 = len(word1), len(word2)
        dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]

        for l1 in range(len1):
            for l2 in range(len2):
                print(word1[l1], word2[l2], word1[l1] == word2[l2])
                if word1[l1] == word2[l2]:
                    dp[l1+1][l2+1] = dp[l1][l2] + 1
                    print(dp)
                else:
                    dp[l1+1][l2+1] = max(dp[l1][l2+1], dp[l1+1][l2])
                    print(dp)


        longest_subsequence_len = dp[-1][-1]
        # The extra characters will be the ones not in longest common sunsequence 
        return len1 + len2 - 2 * longest_subsequence_len


# print(minDistance(word1, word2))




# 💡 **Question 4**

# You need to construct a binary tree from a string consisting of parenthesis and integers.

# The whole input represents a binary tree. It contains an integer followed by zero, one or two pairs of parenthesis. The integer represents the root's value and a pair of parenthesis contains a child binary tree with the same structure.
# You always start to construct the **left** child node of the parent first if it exists.



s = "4(2(3)(1))(6(5))"
# s = "1"

# n = len(s)
# i= 0
# stack = []

# while i<n:
#     if s[i] == '-':
#         i+=1
#         num = 0
#         while i<n and s[i].isdigit():
#             num = num * 10 + int(s[i])
#             i+= 1
#         stack.append(num)
#         i-=1 
#     elif s[i].isdigit():
#         # print("inside elif 1")
#         num = 0
#         while i<n and s[i].isdigit():
#             num = num * 10 + int(s[i])
#             i+= 1
#         stack.append(num)
#         i-=1
#     elif s[i] == ')':
        
#         curNode = stack.pop()
#         if stack:
#             parent = stack[-1]
#             if not parent.left:
#                 parent.left = curNode 
#             else:
#                 parent.right = curNode 
                

#     i+=1

    # print(stack)
    
    
    
    
# 💡 **Question 5**

# Given an array of characters chars, compress it using the following algorithm:

# Begin with an empty string s. For each group of **consecutive repeating characters** in chars:

# - If the group's length is 1, append the character to s.
# - Otherwise, append the character followed by the group's length.

# The compressed string s **should not be returned separately**, but instead, be stored **in the input character array chars**. Note that group lengths that are 10 or longer will be split into multiple characters in chars.

# After you are done **modifying the input array,** return *the new length of the array*.

# You must write an algorithm that uses only constant extra space.

# **Example 1:**

# **Input:** chars = ["a","a","b","b","c","c","c"]

# **Output:** Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]

# **Explanation:**

# The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".

chars = ["a","a","b","b","c","c","c","d"]
chars_count = {c:chars.count(c) for c in chars}

# print(chars_count)
ans = ""
for i,j in chars_count.items():
    if j==1:
        ans += i
    else: ans +=  i +str(j)

# print(ans)



s = "rat"
t = "car"

# s_count = {i:s.count(i) for i in s}
# for i in t:
#     s_count[i] -=1
#     if s_count[i] < 0:
#         print(False)


# print(True)





# 💡 **Question 7**

# Given an encoded string, return its decoded string.

# The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

# You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].

# The test cases are generated so that the length of the output will never exceed 105.

# **Example 1:**

# **Input:** s = "3[a]2[bc]"

# **Output:** "aaabcbc"



class Solution:
  def decodeString(self, s: str) -> str:
    stack = []  # (prevStr, repeatCount)
    currStr = ''
    currNum = 0

    for c in s:
      if c.isdigit():
        currNum = currNum * 10 + int(c)
      else:
        if c == '[':
          stack.append((currStr, currNum))
          currStr = ''
          currNum = 0
        elif c == ']':
          prevStr, num = stack.pop()
          currStr = prevStr + num * currStr
        else:
          currStr += c

    return currStr




def decodeString(s: str) -> str:
    stack = []  # (prevStr, repeatCount)
    currStr = ''
    currNum = 0

    for c in s:
      if c.isdigit():
        currNum = currNum * 10 + int(c)
      else:
        if c == '[':
          stack.append((currStr, currNum))
          print(stack)
          currStr = ''
          currNum = 0
        elif c == ']':
          prevStr, num = stack.pop()
          currStr = prevStr + num * currStr
        else:
          currStr += c

    return currStr




# s = "3[aA]2[b]"

# print(decodeString(s))


# 💡 **Question 8**

# Given two strings s and goal, return true *if you can swap two letters in* s *so the result is equal to* goal*, otherwise, return* false*.*

# Swapping letters is defined as taking two indices i and j (0-indexed) such that i != j and swapping the characters at s[i] and s[j].

# - For example, swapping at indices 0 and 2 in "abcd" results in "cbad".

# **Example 1:**

# **Input:** s = "ab", goal = "ba"

# **Output:** true

# **Explanation:** You can swap s[0] = 'a' and s[1] = 'b' to get "ba", which is equal to goal.

s = "ab"
goal = "aa"

def buddyStrings(s,goal):
    if len(s) != len(goal):
        return False
    
    if s == goal and len(set(s)) < len(goal):
      return True
  
    s =list(s)
    s[0],s[1] = s[1],s[0]
    s = ''.join(s)
    print(s==goal)
# print(''.join(s))




# Swapping_letters(s,goal)


class Solution:
  def buddyStrings(self, A: str, B: str) -> bool:
    if len(A) != len(B):
      return False
    if A == B and len(set(A)) < len(A):
      return True

    diff = [(a, b) for a, b in zip(A, B) if a != b]

    return len(diff) == 2 and diff[0] == diff[1][::-1]
