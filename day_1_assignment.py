
# Assignment 1 Questions - Arrays | DSA

'''
💡 **Q1.** Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

**Example:**
Input: nums = [2,7,11,15], target = 9
Output0 [0,1]

**Explanation:** Because nums[0] + nums[1] == 9, we return [0, 1][
'''

# approach is two sum problem 


# nums = [2,7,11,15]
# target = 9


# class solution:
#     def two_sum(self,nums,target):
#         l , r = 0,len(nums)-1

#         # print(l,r)
#         while l < r:
#             sum = nums[l] + nums[r]
#             if sum == target:
#                 # print ([l,r])
#                 return [l,r]
#                 l += 1
#                 r -= 1
#             elif sum < target:
#                 l += 1
#             else:
#                 r -= 1



# s = solution()

# print(s.two_sum(nums,target))

 

'''
💡 **Q2.** Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

- Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
- Return k.

**Example :**
Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_*,_*]

**Explanation:** Your function should return k = 2, with the first two elements of nums being 2. It does not matter what you leave beyond the returned k (hence they are underscores)[

'''


nums = [3,2,2,3]
val = 3
ans = []
for num in nums:
    if num != val:
        ans.append(num)
 
# print(len(ans))        



# class Solution:
#     def removeElement(self, nums, val) -> int:
#         ans = []
#         for num in nums:
#             if num != val:
#                 ans.append(num)
        
#         print((ans))
        

# s= Solution()
# s.removeElement(nums, val)      



# class Solution:
#   def removeElement(self, nums, val) -> int:
#     i = 0

#     for num in nums:
#       if num != val:
#         nums[i] = num
#         i += 1

#     return i



'''
💡 **Q3.** Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

**Example 1:**
Input: nums = [1,3,5,6], target = 5

Output: 2


'''
# nums = [1,3,5,6]
# target = 6

# l=0 
# r = len(nums)-1
# mid = (l + r)//2

# # print(l,r,mid)

# while l<=r:
#     if nums[mid] == target:
#         print(mid)
#         break 
#     elif nums[mid]< target:
#         l+=1
#         mid = (l + r)//2
#     else:
#         r -=1
#         mid = (l + r)//2


# class Solution(object):
#     def searchInsert(self, nums, target):

#         start = 0
#         end = len(nums) - 1
        
#         # Traverse an array
#         while (start <= end):
            
#             mid = (start + end)//2
             
#             # if target value found.
#             if nums[mid] == target:
#                 return mid
            
#             # If target value is greater then mid elements's value
#             elif target > nums[mid]:
#                 start +=  1
#                 mid = (start + end)//2
                
#             # otherwise target value is less, 
#             else:
#                 end -= 1
#                 mid = (start + end)//2
#         # Return the insertion position
#         return end+1    #### if target not found    

# s =  Solution()
# print(s.searchInsert(nums, 2))

        



'''
💡 **Q4.** You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

**Example 1:**
Input: digits = [1,2,3]
Output: [1,2,4]

**Explanation:** The array represents the integer 123.

Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].

'''


# digits = [1,2,3]

# digit = ''.join(list(map(str,digits)))
# digit = list(map(int,list(str(int(digit) +1))))
# print(digit)


# class Solution:
#     def plusOne(self, digits: List[int]) -> List[int]:
#         return list(map(int,list(str(int(''.join(list(map(str,digits)))) +1))))
    
    
# class Solution:
#     def plusOne(self, digits: List[int]) -> List[int]:
#         num = ''
#         for i in digits:
#             num+=str(i)
#         num = str((int(num)+1))
#         return (list(map(int,list(num))))


'''
💡 **Q5.** You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

**Example 1:**
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]

**Explanation:** The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

'''


nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

# class Solution:
#     def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        
#         """
#         Do not return anything, modify nums1 in-place instead.
#         """
#         nums1[m:m+n] = nums2
#         nums1.sort()
# #         return nums1

# i = m-1
# j = n-1
# k = m+n -1

# while j>=0:
#     if nums1[i]>=nums2[j]:
#         nums1[k] = nums1[i]
        
#         i-=1
#         k-=1
#     else:
#         nums1[k] = nums2[j]
#         j-=1
#         k-=1
        
# print(nums1)






'''
💡 **Q6.** Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

**Example 1:**
Input: nums = [1,2,3,1]

Output: true

'''

nums = [1,2,3,1]

nums_count = {i:nums.count(i) for i in nums}

ans = any([k>1 for i,k in nums_count.items()])
# print(ans)

'''
💡 **Q7.** Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the nonzero elements.

Note that you must do this in-place without making a copy of the array.

**Example 1:**
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
'''
nums = [0,1,0,3,12]
# zeros = [num for num in nums if num==0]
# ans = [num for num in nums if num!=0]
# ans.extend(zeros)
# nums.clear()
# nums  = ans
# print(nums)


# class Solution:
#   def moveZeroes(self, nums: List[int]) -> None:
#     j = 0
#     for num in nums:
#       if num != 0:
#         nums[j] = num
#         j += 1

#     for i in range(j, len(nums)):
#       nums[i] = 0
      
i = 0
for num in nums:
    if num != 0:
        nums[i] = num 
        i += 1

for j in range(i,len(nums)):
    nums[j] = 0
    
# print(nums)
        
        
'''
💡 **Q8.** You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.

You are given an integer array nums representing the data status of this set after the error.

Find the number that occurs twice and the number that is missing and return them in the form of an array.

**Example 1:**
Input: nums = [1,2,2,4]
Output: [2,3]

'''


nums = [1,2,2,4]

nums_count = {i:nums.count(i) for i in nums if nums.count(i) > 1}
ans = []
for i in nums_count.keys():
    ans.append(i)
    ans.append(i+1)
    
# print(ans)




