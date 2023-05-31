
# 💡 **Question 1**

# A permutation perm of n + 1 integers of all the integers in the range [0, n] can be represented as a string s of length n where:

# - s[i] == 'I' if perm[i] < perm[i + 1], and
# - s[i] == 'D' if perm[i] > perm[i + 1].

# Given a string s, reconstruct the permutation perm and return it. If there are multiple valid permutations perm, return **any of them**.

# **Example 1:**

# **Input:** s = "IDID"

# **Output:**

# [0,4,1,3,2]



s = "IDID"
def permutation(s):
    l = 0
    r = len(s)
    ans = []
    for i in s:
        if i =='I':
            ans.append(l)
            l += 1
        if i == 'D':
            ans.append(r)
            r -= 1 

    ans.append(l)

    print(ans)
    
# permutation(s)


# 💡 **Question 2**

# You are given an m x n integer matrix matrix with the following two properties:

# - Each row is sorted in non-decreasing order.
# - The first integer of each row is greater than the last integer of the previous row.

# Given an integer target, return true *if* target *is in* matrix *or* false *otherwise*.

# You must write a solution in O(log(m * n)) time complexity.


class Solution:
  def searchMatrix(self, matrix, target):
    if not matrix:
      return False

    m = len(matrix)
    n = len(matrix[0])
    l = 0
    r = m * n

    while l < r:
      mid = (l + r) // 2
    #   print(mid)
      i = mid // n
      j = mid % n
      
    #   print(i,j)
      
      if matrix[i][j] == target:
        return True
      elif matrix[i][j] < target:
        l = mid + 1
      else:
        r = mid

    return False



matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
s = Solution()
# print(s.searchMatrix( matrix, target))


# 💡 **Question 3**

# Given an array of integers arr, return *true if and only if it is a valid mountain array*.

# Recall that arr is a mountain array if and only if:

# - arr.length >= 3
# - There exists some i with 0 < i < arr.length - 1 such that:
#     - arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
#     - arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

arr = [0,2,3,4,5,2,1,0]

def check_mountain_array(arr):
    i = len(arr)-2

    while i >= 0:
        if arr[i] > arr[i+1]:
            i -= 1
        else:
            break 

    # print(i)
    for i in range(i):
        if arr[i] < arr[i+1]:
            print(True)
        else:
            print(False)


check_mountain_array(arr)




# 💡 **Question 4**

# Given a binary array nums, return *the maximum length of a contiguous subarray with an equal number of* 0 *and* 1.

# **Example 1:**

# **Input:** nums = [0,1]

# **Output:** 2

# **Explanation:**

# [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.


nums = [0, 1, 0]
def findMaxLength( nums):
    ans = 0
    prefix = 0
    prefixToIndex = {0: -1}

    for i, num in enumerate(nums):
      prefix += 1 if num else -1
    #   print(prefix)
    #   print(i,prefixToIndex.setdefault(prefix, i),i - prefixToIndex.setdefault(prefix, i))
      ans = max(ans, i - prefixToIndex.setdefault(prefix, i))

    print(ans)


findMaxLength(nums)




# 💡 **Question 5**

# The **product sum** of two equal-length arrays a and b is equal to the sum of a[i] * b[i] for all 0 <= i < a.length (**0-indexed**).

# - For example, if a = [1,2,3,4] and b = [5,2,3,1], the **product sum** would be 1*5 + 2*2 + 3*3 + 4*1 = 22.

# Given two arrays nums1 and nums2 of length n, return *the **minimum product sum** if you are allowed to **rearrange** the **order** of the elements in* nums1.

# **Example 1:**

# **Input:** nums1 = [5,3,4,2], nums2 = [4,2,2,5]

# **Output:** 40

# **Explanation:**

# We can rearrange nums1 to become [3,5,4,2]. The product sum of [3,5,4,2] and [4,2,2,5] is 3*4 + 5*2 + 4*2 + 2*5 = 40.


nums1 = [1,2,3,4]
nums2 = [5,2,3,1]
def product_sum(nums1,nums2):
    nums = list(zip(nums1,nums2))
    ans = 0
    # print(nums)
    for i,j in nums:
        # print(i,j, '--> ',i*j)
        ans += i*j
        
    print(ans)

# product_sum(nums1,nums2)




# 💡 **Question 6**

# An integer array original is transformed into a **doubled** array changed by appending **twice the value** of every element in original, and then randomly **shuffling** the resulting array.

# Given an array changed, return original *if* changed *is a **doubled** array. If* changed *is not a **doubled** array, return an empty array. The elements in* original *may be returned in **any** order*.

# **Example 1:**

# **Input:** changed = [1,3,4,2,6,8]

# **Output:** [1,3,4]

# **Explanation:** One possible original array could be [1,3,4]:

# - Twice the value of 1 is 1 * 2 = 2.
# - Twice the value of 3 is 3 * 2 = 6.
# - Twice the value of 4 is 4 * 2 = 8.

# Other original arrays could be [4,3,1] or [3,1,4].


changed = [1,3,4,2,6,8]
def orginal_array(changed):
  ans = []
  # sorted(changed)
  for i in range(changed.index(changed[0]*2)):
    ans.append(changed[i])


  print(ans)
  
orginal_array(changed)





# 💡 **Question 8**

# Given two [sparse matrices](https://en.wikipedia.org/wiki/Sparse_matrix) mat1 of size m x k and mat2 of size k x n, return the result of mat1 x mat2. You may assume that multiplication is always possible.

# **Example 1:**

# **Input:** mat1 = [[1,0,0],[-1,0,3]], mat2 = [[7,0,0],[0,0,0],[0,0,1]]

# **Output:**

# [[7,0,0],[-7,0,3]]



class Solution:
  def multiply(self, mat1, mat2):
    m = len(mat1)
    n = len(mat2)
    l = len(mat2[0])
    ans = [[0] * l for _ in range(m)]

    for i in range(m):
      for j in range(l):
        for k in range(n):
          ans[i][j] += mat1[i][k] * mat2[k][j]

    return ans

# mat1 = [[1,0,0],[-1,0,3]]
# mat2 = [[7,0,0],[0,0,0],[0,0,1]]


# m = len(mat1)
# n = len(mat2)
# l = len(mat2[0])

# ans = [[0] * l for _ in range(m)]

# for i in range(m):
#     for j in range(l):
#         for k in range(n):
#             ans[i][j] += mat1[i][k] * mat2[k][j]

# print(ans)