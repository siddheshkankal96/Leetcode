# Question 1
# Given an integer array nums of 2n integers, group these integers into n pairs (a1, b1), (a2, b2),
# ..., (an, bn) such that the sum of min(ai, bi) for all i is maximized. Return the maximized sum.
# Example 1:
# Input: nums = [1,4,3,2]
# Output: 4
# Explanation: All possible pairings (ignoring the ordering of elements) are:
# 1. (1, 4), (2, 3) -> min(1, 4) + min(2, 3) = 1 + 2 = 3
# 2. (1, 3), (2, 4) -> min(1, 3) + min(2, 4) = 1 + 2 = 3
# 3. (1, 2), (3, 4) -> min(1, 2) + min(3, 4) = 1 + 3 = 4
# So the maximum possible sum is 4


# nums = [1,4,3,2]
# all_comb = []
# for i in range(len(nums)-1):
#     for j in range(i+1,len(nums)):
#         all_comb.append((nums[i],nums[j]))


# print(all_comb)   
# unique_pair = []
# unique_pair_comb = []
# for pair in all_comb:
#     if len(unique_pair) == 0:
#         unique_pair.append(pair)
#         all_comb.remove(pair)
#     else:
#         i,j = pair 
#         x,y = unique_pair[0]
#         if i!=x and i!=y and j!=x and j!=y:
#             unique_pair.append(pair)
#             all_comb.remove(pair)
            
            
            
# print(unique_pair)
# unique_pair_comb.append(unique_pair)

# print(unique_pair_comb)    

# print(all_comb)


nums = [1,5,3,4]

class solution:
    def maximum_possible_sum(self,nums):
        
        max_sum = 0
        nums.sort()

        for i,n in enumerate(nums):
            if i%2==0:
                max_sum += n 
                
        print(max_sum)

s = solution()
s.maximum_possible_sum(nums)


# Question 2
# Alice has n candies, where the ith candy is of type candyType[i]. Alice noticed that she started
# to gain weight, so she visited a doctor.
# The doctor advised Alice to only eat n / 2 of the candies she has (n is always even). Alice
# likes her candies very much, and she wants to eat the maximum number of different types of
# candies while still following the doctor's advice.
# Given the integer array candyType of length n, return the maximum number of different types
# of candies she can eat if she only eats n / 2 of them.
# Example 1:
# Input: candyType = [1,1,2,2,3,3]
# Output: 3
# Explanation: Alice can only eat 6 / 2 = 3 candies. Since there are only 3 types, she can eat one
# of each type.


class Solution:
  def distributeCandies(self, candies):
    return min(len(candies) // 2, len(set(candies)))




# Question 3
# We define a harmonious array as an array where the difference between its maximum value
# and its minimum value is exactly 1.
# Given an integer array nums, return the length of its longest harmonious subsequence
# among all its possible subsequences.
# A subsequence of an array is a sequence that can be derived from the array by deleting some
# or no elements without changing the order of the remaining elements.
# Example 1:
# Input: nums = [1,3,2,2,5,2,3,7]
# Output: 5
# Explanation: The longest harmonious subsequence is [3,2,2,2,3].


# import collections

# nums = [1,3,2,2,5,2,3,7]
# count = collections.Counter(nums)
# print(count)

class Solution:
  def findLHS(self, nums):
    ans = 0
    count = {i:nums.count(i) for i in nums}

    for i,j in count.items():
        if i+1 in count:
            ans = max(ans, j + count[i+1])

    return ans

# nums = [1,3,2,2,5,2,3,7]
# count = {i:nums.count(i) for i in nums}
# ans = 0
# for i,j in count.items():
#     if i+1 in count:
#         ans = max(ans, j + count[i+1])
        
# print(ans) 



# Question 4
# You have a long flowerbed in which some of the plots are planted, and some are not.
# However, flowers cannot be planted in adjacent plots.
# Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means
# not empty, and an integer n, return true if n new flowers can be planted in the flowerbed
# without violating the no-adjacent-flowers rule and false otherwise.
# Example 1:
# Input: flowerbed = [1,0,1,0,1],n = 1
# Output: true

flowerbed = [1,0,0,0,1]
n = 1
class Solution_4:
    def flowerbed_planted(self,flowerbed,n):
        count = 0
        for i in range(0,len(flowerbed),2):
            # print(flowerbed[i])
            if flowerbed[i] == 0:
                count+=1
        
        print(count==n)
    
    
s = Solution_4()
s.flowerbed_planted(flowerbed,n)


# Question 5
# Given an integer array nums, find three numbers whose product is maximum and return the
# maximum product.
# Example 1:
# Input: nums = [1,2,3]
# Output: 6

# nums = [1,2,3,3]

class solution_5:
    def maximum_product(self,nums):
        
        ans = 0
        for i in range(len(nums)-2):
            # print(nums[i] ,nums[i+1],nums[i+2])
            product = nums[i] *nums[i+1]*nums[i+2]
            # print(product)
            ans = max(ans,product)
            
            
        print(ans)


# Question 6
# Given an array of integers nums which is sorted in ascending order, and an integer target,
# write a function to search target in nums. If target exists, then return its index. Otherwise,
# return -1.
# You must write an algorithm with O(log n) runtime complexity.
# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4

# nums = [-1,0,3,5,9,12]
# target = 9
class solution_6:
    def search(self,nums,target):
        l = 0
        r = len(nums)-1
        mid = (l + r)//2               

        while l < r:
            # print(target == nums[mid])
            if target == nums[mid]:
                print(mid)
                break
            elif target > nums[mid]:
                l+=1
                mid = (l + r)//2 
            else:
                r-=1
                mid = (l + r)//2 
                                                                                          



# Question 7
# An array is monotonic if it is either monotone increasing or monotone decreasing.
# An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]. An array nums is
# monotone decreasing if for all i <= j, nums[i] >= nums[j].
# Given an integer array nums, return true if the given array is monotonic, or false otherwise.
# Example 1:
# Input: nums = [1,2,2,3]
# Output: true


# nums = [1,2,2,3]

# increasing = True
# decreasing = True

# for i in range(1,len(nums)):
#     increasing &= nums[i-1] <= nums[i]
#     decreasing &= nums[i - 1] >= nums[i]
    
# print(increasing | decreasing)
    
class Solution:
  def isMonotonic(self, nums: List[int]) -> bool:
    increasing = True
    decreasing = True

    for i in range(1, len(nums)):
      increasing &= nums[i - 1] <= nums[i]
      decreasing &= nums[i - 1] >= nums[i]

    return increasing or decreasing  


# Question 8
# You are given an integer array nums and an integer k.
# In one operation, you can choose any index i where 0 <= i < nums.length and change nums[i]
# to nums[i] + x where x is an integer from the range [-k, k]. You can apply this operation at
# most once for each index i.
# The score of nums is the difference between the maximum and minimum elements in nums.
# Return the minimum score of nums after applying the mentioned operation at most once for
# each index in it.
# Example 1:
# Input: nums = [1], k = 0
# Output: 0
# Explanation: The score is max(nums) - min(nums) = 1 - 1 = 0.


class Solution:
  def smallestRangeI(self, nums: List[int], k: int) -> int:
    return max(0, max(nums) - min(nums) - 2 * k)
