# <aside>
# 💡 **Question 1**

# Given a non-negative integer `x`, return *the square root of* `x` *rounded down to the nearest integer*. The returned integer should be **non-negative** as well.

# You **must not use** any built-in exponent function or operator.

# - For example, do not use `pow(x, 0.5)` in c++ or `x ** 0.5` in python.

# Input: x = 4
# Output: 2
# Explanation: The square root of 4 is 2, so we return 2.

# Input: x = 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.

# </aside>


class Solution:
  def mySqrt(self,x):
    l = 1
    r = x + 1

    while l < r:
        mid = (l + r) // 2
        if (mid > x // mid):
            r = mid
        else:
            l = mid + 1
    

   
    return l - 1


def mySqrt(x):
    l = 1
    r = x + 1

    while l < r:
        mid = (l + r) // 2
        if (mid > x // mid):
            r = mid
        else:
            l = mid + 1
    

   
    return l - 1



# print(mySqrt(4))









# <aside>
# 💡 **Question 2**

# A peak element is an element that is strictly greater than its neighbors.

# Given a **0-indexed** integer array `nums`, find a peak element, and return its index. If the array contains multiple peaks, return the index to **any of the peaks**.

# You may imagine that `nums[-1] = nums[n] = -∞`. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.

# You must write an algorithm that runs in `O(log n)` time.

# **Example 1:**

# Input: nums = [1,2,3,1]
# Output: 2
# Explanation: 3 is a peak element and your function should return the index number 2.

# Example 2:

# Input: nums = [1,2,1,3,5,6,4]
# Output: 5
# Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.
# </aside>



        
nums = [1,3,2]

l = 0
r = len(nums) - 1

while l < r:
    m = (l + r) // 2
    # print(l,r,m,'-',nums[m-1],nums[m],nums[m+1])
    if nums[m] >= nums[m + 1]:
        r = m
    else:
        l = m + 1

# print(l)





# <aside>
# 💡 **Question 3**

# ****

# Given an array `nums` containing `n` distinct numbers in the range `[0, n]`, return *the only number in the range that is missing from the array.*

# **Example 1:**
# Input: nums = [3,0,1]
# Output: 2
# Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.

# Example 2:
# Input: nums = [0,1]
# Output: 2
# Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.

# Example 3:
# Input: nums = [9,6,4,2,3,5,7,0,1]
# Output: 8
# Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.

# </aside>


# nums = [3,0,1]

# n = len(set(nums))

# for i in range(0,n+1):
#     if i not in nums:
#         print(i)



# nums = [9,6,4,2,3,5,7,0,1]
# l = 0
# r = len(nums)
# nums.sort() #013
# while l<r:
#     mid = (l + r) // 2
    
#     if nums[mid] == mid:
#         l = mid + 1
#     else:
#         r = mid
    
# print(l)

# <aside>
# 💡 **Question 4**

# Given an array of integers `nums` containing `n + 1` integers where each integer is in the range `[1, n]` inclusive.

# There is only **one repeated number** in `nums`, return *this repeated number*.

# You must solve the problem **without** modifying the array `nums` and uses only constant extra space.

# **Example 1:**
# Input: nums = [1,3,4,2,2]
# Output: 2

# Example 2:
# Input: nums = [3,1,3,4,2]
# Output: 3
# </aside>        



# nums = [3,1,3,4,2]

# l = 0
# r = len(nums)
# nums.sort()
# #1 2 3 3 4
# while l < r:
#     mid = (l+r)//2
#     # print(mid)
#     if nums[mid] == mid:
#         print(nums[mid])
#         break
#     elif nums[mid] > mid:
#         l = mid 
#     else:
#         r = mid-1



# <aside>
# 💡 **Question 5**

# Given two integer arrays `nums1` and `nums2`, return *an array of their intersection*. Each element in the result must be **unique** and you may return the result in **any order**.

# **Example 1:**
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2]

# Example 2:
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [9,4]
# Explanation: [4,9] is also accepted.

# </aside>

nums1 = [4,9,5]
# nums1.sort()
nums2 = [9,4,9,8,4]
nums2.sort()

# print(list(set(nums1).intersection(set(nums2))))


# def binarySearch(arr,n,target):
#     l = 0
#     r = n 
#     while l <= r:
#         mid = (l+r)//2
#         # print(arr[mid],target)
#         if arr[mid] == target:
#             return (mid)
            
#         elif arr[mid] < target:
#             l = mid+1
#         else:
#             r = mid-1
#     return -1

# # binarySearch(nums1,len(nums),5) 
# def arrayIntersection(arr1,arr2):
#     intersection = set() 
#     m = len(arr1)
#     n = len(arr2)
    
#     for i in range(m):
#         if binarySearch(arr2,n,arr1[i]) != -1:
#             intersection.add(arr1[i])
#     return intersection 

            
# print(arrayIntersection(nums1,nums2))
            



# <aside>
# 💡 **Question 6**

# Suppose an array of length `n` sorted in ascending order is **rotated** between `1` and `n` times. For example, the array `nums = [0,1,2,4,5,6,7]` might become:

# - `[4,5,6,7,0,1,2]` if it was rotated `4` times.
# - `[0,1,2,4,5,6,7]` if it was rotated `7` times.

# Notice that **rotating** an array `[a[0], a[1], a[2], ..., a[n-1]]` 1 time results in the array `[a[n-1], a[0], a[1], a[2], ..., a[n-2]]`.

# Given the sorted rotated array `nums` of **unique** elements, return *the minimum element of this array*.

# You must write an algorithm that runs in `O(log n) time.`

# **Example 1:**
# Input: nums = [3,4,5,1,2]
# Output: 1
# Explanation: The original array was [1,2,3,4,5] rotated 3 times.

# Input: nums = [4,5,6,7,0,1,2]
# Output: 0
# Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.
# </aside>



# l = [4,5,6,0,1,2,3]

# def findMin(nums) -> int:
#     l = 0
#     r = len(nums) - 1

#     while l < r:
#       m = (l + r) // 2
#       print(l,r,m,'--',nums[m] , nums[r])
#       if nums[m] < nums[r]:
#         r = m
#       else:
#         l = m + 1

#     return nums[l]

# print(findMin(l))

# <aside>
# 💡 **Question 7**

# Given an array of integers `nums` sorted in non-decreasing order, find the starting and ending position of a given `target` value.

# If `target` is not found in the array, return `[-1, -1]`.

# You must write an algorithm with `O(log n)` runtime complexity.

# **Example 1:**
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]

# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]



# </aside>

# nums = [5,7,7,8,8,10]
# target = 8

# def find_target(nums):
#     l = 0
#     r = len(nums)-1
#     ans = []
#     while l <= r:
#         mid = (l+r)//2
#         if nums[mid] == target:
#             ans.append(mid)
#             r = mid-1
            
#         elif nums[mid] < target:
#             #         print(mid,l,r)
#             l = mid+1
#         else:
#             r = mid-1
    
#     # print(l,r)    
#     if l>r and ans == []:
#         ans.append(-1)
#         ans.append(-1)
            
#     return sorted(ans)
        
# print(find_target(nums))
        

# import bisect



# l =[1,2,2,4,5,6]
# print(bisect.bisect_left(l,3))

# print(bisect.bisect_right(l,2)-1)

# class Solution:
#   def searchRange(self, nums, target):
#     l = bisect_left(nums, target)
#     if l == len(nums) or nums[l] != target:
#       return -1, -1
#     r = bisect_right(nums, target) - 1
#     return l, r


# <aside>
# 💡 **Question 8**

# Given two integer arrays `nums1` and `nums2`, return *an array of their intersection*. 
# Each element in the result must appear as many times as it shows in both arrays and you may return the result in **any order**.
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]

# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [4,9]
# Explanation: [9,4] is also accepted.
# </aside>


def binarySearch(arr,n,target):
    l = 0
    r = n 
    while l <= r:
        mid = (l+r)//2
        # print(arr[mid],target)
        if arr[mid] == target:
            return (mid)
            
        elif arr[mid] < target:
            l = mid+1
        else:
            r = mid-1
    return -1

# binarySearch(nums1,len(nums),5) 
def arrayIntersection(arr1,arr2):
    intersection = [] 
    m = len(arr1)
    n = len(arr2)
    
    for i in range(m):
        if binarySearch(arr2,n,arr1[i]) != -1:
            intersection.append(arr1[i])
    return intersection 


nums1 = [1,2,2,1]
nums2 = [2,2]
            
# print(arrayIntersection(nums1,nums2))
            



