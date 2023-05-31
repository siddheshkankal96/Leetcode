# # Assignment Questions 4

# 💡 **Question 1**
# Given three integer arrays arr1, arr2 and arr3 **sorted** in **strictly increasing** order, return a sorted array of **only** the integers that appeared in **all** three arrays.

# **Example 1:**

# Input: arr1 = [1,2,3,4,5], arr2 = [1,2,5,7,9], arr3 = [1,3,4,5,8]

# Output: [1,5]

# **Explanation:** Only 1 and 5 appeared in the three arrays.

arr1 = [1,2,3,4,5]
arr2 = [1,2,5,7,9]
arr3 = [1,3,4,5,8]

def appeared_in_3_arrays(arr1,arr2,arr3):
    ans  = []
    for i in arr1:
        if i in arr2 and i in arr3:
            ans.append(i)

    print(ans)        
    
# appeared_in_3_arrays(arr1,arr2,arr3)
# 💡 **Question 2**

# Given two **0-indexed** integer arrays nums1 and nums2, return *a list* answer *of size* 2 *where:*

# - answer[0] *is a list of all **distinct** integers in* nums1 *which are **not** present in* nums2*.*
# - answer[1] *is a list of all **distinct** integers in* nums2 *which are **not** present in* nums1.

# **Note** that the integers in the lists may be returned in **any** order.

# **Example 1:**

# **Input:** nums1 = [1,2,3], nums2 = [2,4,6]

# **Output:** [[1,3],[4,6]]

# **Explanation:**

# For nums1, nums1[1] = 2 is present at index 0 of nums2, whereas nums1[0] = 1 and nums1[2] = 3 are not present in nums2. Therefore, answer[0] = [1,3].

# For nums2, nums2[0] = 2 is present at index 1 of nums1, whereas nums2[1] = 4 and nums2[2] = 6 are not present in nums2. Therefore, answer[1] = [4,6].

nums1 = [1,2,3]
nums2 = [2,4,6]

# **Output:** [[1,3],[4,6]]
# ans = []
# temp= []
# for i in nums1:
#     if i not in nums2:
#         temp.append(i)

# ans.append(temp)
# temp = []
# for i in nums2:
#     if i not in nums1:
#         temp.append(i)
# ans.append(temp)

# print(ans)


class Solution:
  def findDifference(self, nums1, nums2):
    set1 = set(nums1)
    set2 = set(nums2)
    return [set1 - set2, set2 - set1]



# 💡 **Question 3**
# Given a 2D integer array matrix, return *the **transpose** of* matrix.

# The **transpose** of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.

# **Example 1:**

# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]

# Output: [[1,4,7],[2,5,8],[3,6,9]]

matrix = [[1,2,3],[4,5,6],[7,8,9]]

ans = []
for i in range(len(matrix[0])):
    temp = []
    for j in range(len(matrix)):
        temp.append(matrix[j][i])
    ans.append(temp)
print(ans)
    
    
# 💡 **Question 4**
# Given an integer array nums of 2n integers, group these integers into n pairs (a1, b1), (a2, b2), ..., (an, bn) such that the sum of min(ai, bi) for all i is **maximized**. Return *the maximized sum*.

# **Example 1:**

# Input: nums = [1,4,3,2]

# Output: 4

# **Explanation:** All possible pairings (ignoring the ordering of elements) are:

# 1. (1, 4), (2, 3) -> min(1, 4) + min(2, 3) = 1 + 2 = 3

# 2. (1, 3), (2, 4) -> min(1, 3) + min(2, 4) = 1 + 2 = 3

# 3. (1, 2), (3, 4) -> min(1, 2) + min(3, 4) = 1 + 3 = 4

# So the maximum possible sum is 4.

def maximum_possible(nums):
    nums = [1,4,3,2]
    sum = 0
    for i,n in enumerate(nums):
        if i%2==0:
            sum+=n 
            
    print(sum)
        
# 💡 **Question 5**
# You have n coins and you want to build a staircase with these coins. The staircase consists of k rows where the ith row has exactly i coins. The last row of the staircase **may be** incomplete.

# Given the integer n, return *the number of **complete rows** of the staircase you will build*.

# **Example 1:**

# []()

# ![v2.jpg](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/4bd91cfa-d2b1-47b3-8197-a72e8dcfff4b/v2.jpg)

# **Input:** n = 5

# **Output:** 2

# **Explanation:** Because the 3rd row is incomplete, we return 2.
n = 8

l = 1
r = n 
res = 0
# 1 2 3 4 5
while l<r:
    mid = (l + r)//2 
    coins = (mid / 2) * (mid+1)
    if coins > n:
        r -=  1
    else:
        l += 1
        res = max(res,mid)              
    
print(res)


# 💡 **Question 6**
# Given an integer array nums sorted in **non-decreasing** order, return *an array of **the squares of each number** sorted in non-decreasing order*.

# **Example 1:**

# Input: nums = [-4,-1,0,3,10]

# Output: [0,1,9,16,100]



# **Explanation:** After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100]



nums = [-4,-1,0,3,10]

ans = sorted([i**2 for i in nums])
# ans.sort()
# print(ans)



class Solution:
  def sortedSquares(self, nums):
    n = len(nums)
    l = 0
    r = n - 1
    ans = [0] * n

    while n:
      n -= 1
      if abs(nums[l]) > abs(nums[r]):
        ans[n] = nums[l] * nums[l]
        l += 1
      else:
        ans[n] = nums[r] * nums[r]
        r -= 1

    return ans






# 💡 **Question 7**
# You are given an m x n matrix M initialized with all 0's and an array of operations ops, where ops[i] = [ai, bi] means M[x][y] should be incremented by one for all 0 <= x < ai and 0 <= y < bi.

# Count and return *the number of maximum integers in the matrix after performing all the operations*

# **Example 1:**

# **Input:** m = 3, n = 3, ops = [[2,2],[3,3]]

# **Output:** 4

# **Explanation:** The maximum integer in M is 2, and there are four of it in M. So return 4.



m = 3
n = 3
ops = [[2,2],[3,3]]

# arr = [[0]*m]*n 
# arr = [[0,0,0],[0,0,0],[0,0,0]]

def solution_7(ops,m,n):
    arr = [[0 for _ in range(m)] for _ in range(n)]
    # print(arr)

    for x in range(len(ops)):
        for i in range(ops[x][0]):
            for j in range(ops[x][1]):
                # print(i,j)
                # print(arr[i][j])
                arr[i][j] = arr[i][j]+1
                # print(arr[i][j])

    # print(arr)

    ar = [ j for i in arr for j in i]
    # print(max(ar))
    print(ar.count(max(ar)))


# solution_7(ops,m,n)

ops = [[2,2],[3,3]]
class Solution:
  def maxCount(self, m, n, ops):
    minY = m
    minX = n

    for y, x in ops:
      minY = min(minY, y)
      minX = min(minX, x)

    return minX * minY

# 💡 **Question 8**

# Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].

# *Return the array in the form* [x1,y1,x2,y2,...,xn,yn].

# **Example 1:**

# **Input:** nums = [2,5,1,3,4,7], n = 3

# **Output:** [2,3,5,4,1,7]

# **Explanation:** Since x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 then the answer is [2,3,5,4,1,7].




nums = [2,5,1,3,4,7]
n = 3
def solution(nums,n):
    ans = []
    for i in range(len(nums)-n):
        ans.append(nums[i])
        ans.append(nums[i+n])
        
    print(ans)
    
# solution(nums,n)
