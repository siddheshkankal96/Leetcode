# Assignment Questions 3 
# 💡
# Question 1
# Given an integer array nums of length n and an integer target, find three integers
# in nums such that the sum is closest to the target.
# Return the sum of the three integers.

# You may assume that each input would have exactly one solution.

# Example 1:
# Input: nums = [-1,2,1,-4], target = 1
# Output: 2

# Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
# 💡

class Solution:
  def threeSumClosest(self, nums, target: int) -> int:
    ans = nums[0] + nums[1] + nums[2]

    nums.sort()

    for i in range(len(nums) - 2):
      if i > 0 and nums[i] == nums[i - 1]:
        continue
      l = i + 1
      r = len(nums) - 1
      while l < r:
        summ = nums[i] + nums[l] + nums[r]
        if summ == target:
          return summ
        if abs(summ - target) < abs(ans - target):
          ans = summ
        if summ < target:
          l += 1
        else:
          r -= 1

    return ans




# Question 2
# Given an array nums of n integers, return an array of all the unique quadruplets
# [nums[a], nums[b], nums[c], nums[d]] such that:
#            ● 0 <= a, b, c, d < n
#            ● a, b, c, and d are distinct.
#            ● nums[a] + nums[b] + nums[c] + nums[d] == target

# You may return the answer in any order.

# Example 1:
# Input: nums = [1,0,-1,0,-2,2], target = 0
# Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]



class Solution:
  def fourSum(self, nums, target: int):
    ans = []

    def nSum(l, r, target, n, path, ans):
        if r - l + 1 < n or n < 2 or target < nums[l] * n or target > nums[r] * n:
            return
        if n == 2:
            while l < r:
                summ = nums[l] + nums[r]
                if summ == target:
                    ans.append(path + [nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                elif summ < target:
                    l += 1
                else:
                    r -= 1
            return

        for i in range(l, r + 1):
            if i > l and nums[i] == nums[i - 1]:
                continue

        nSum(i + 1, r, target - nums[i], n - 1, path + [nums[i]], ans)

    nums.sort()
    nSum(0, len(nums) - 1, target, 4, [], ans)
    return ans




# Question 3
# A permutation of an array of integers is an arrangement of its members into a
# sequence or linear order.

# For example, for arr = [1,2,3], the following are all the permutations of arr:
# [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].

# The next permutation of an array of integers is the next lexicographically greater
# permutation of its integer. More formally, if all the permutations of the array are
# sorted in one container according to their lexicographical order, then the next
# permutation of that array is the permutation that follows it in the sorted container.


class Solution:
  def nextPermutation(self, nums) -> None:
    n = len(nums)

    # From back to front, find the first num < nums[i + 1]
    i = n - 2
    while i >= 0:
      if nums[i] < nums[i + 1]:
        break
      i -= 1

    # From back to front, find the first num > nums[i], swap it with nums[i]
    if i >= 0:
      for j in range(n - 1, i, -1):
        if nums[j] > nums[i]:
          nums[i], nums[j] = nums[j], nums[i]
          break

    def reverse(nums, l: int, r: int) -> None:
      while l < r:
        nums[l], nums[r] = nums[r], nums[l]
        l += 1
        r -= 1

    # Reverse nums[i + 1..n - 1]
    reverse(nums, i + 1, len(nums) - 1)
    
    
    
# 💡
# Question 4
# Given a sorted array of distinct integers and a target value, return the index if the
# target is found. If not, return the index where it would be if it were inserted in
# order.

# You must write an algorithm with O(log n) runtime complexity.

# Example 1:
# Input: nums = [1,3,5,6], target = 5
# Output: 2


nums = [1,3,5,6]
target = 4

l = 0
r = len(nums)-1

while l < r:
    mid = (l + r) //2
    if nums[mid] == target:
        print(mid)
        break
    elif nums[mid] < target:
        l += 1
    else:
        r -= 1
        
    if l==r:
        print(l)
        

# Question 5
# You are given a large integer represented as an integer array digits, where each
# digits[i] is the ith digit of the integer. The digits are ordered from most significant
# to least significant in left-to-right order. The large integer does not contain any
# leading 0's.

# Increment the large integer by one and return the resulting array of digits.

# Example 1:
# Input: digits = [1,2,3]
# Output: [1,2,4]

digits = [1,2,3]

# print(list(map(int,list(str(int(''.join(list(map(str,digits))))+1)))))

# 💡
# Question 6
# Given a non-empty array of integers nums, every element appears twice except
# for one. Find that single one.

# You must implement a solution with a linear runtime complexity and use only
# constant extra space.

# Example 1:
# Input: nums = [2,2,1]
# Output: 1
# 💡

nums = [2,2,1]

class solution():
    def single_one(nums):
        nums_count = {i:nums.count(i) for i in  nums}
        # print(nums_count)

        for i,j in nums_count.items():
            if j ==1:
                print(i)
    
    
    
# Question 7
# You are given an inclusive range [lower, upper] and a sorted unique integer array
# nums, where all elements are within the inclusive range.

# A number x is considered missing if x is in the range [lower, upper] and x is not in
# nums.

# Return the shortest sorted list of ranges that exactly covers all the missing
# numbers. That is, no element of nums is included in any of the ranges, and each
# missing number is covered by one of the ranges.

# Example 1:
# Input: nums = [0,1,3,50,75], lower = 0, upper = 99
# Output: [[2,2],[4,49],[51,74],[76,99]]

# Explanation: The ranges are:
# [2,2]
# [4,49]
# [51,74]
# [76,99]
# 💡
nums = [0,1,3,50,75]
lower = 0
upper = 99

class Solution:
  def findMissingRanges(self, nums, lower: int, upper: int):
    def getRange(lo: int, hi: int) -> str:
      if lo == hi:
        return [lo,hi]
      return [lo,hi]

    if not nums:
      return [getRange(lower, upper)]

    ans = []

    if nums[0] > lower:
      ans.append(getRange(lower, nums[0] - 1))

    for prev, curr in zip(nums, nums[1:]):
      if curr > prev + 1:
        ans.append(getRange(prev + 1, curr - 1))

    if nums[-1] < upper:
      ans.append(getRange(nums[-1] + 1, upper))

    return ans

s = Solution()
print(s.findMissingRanges(nums, lower, upper))

# Question 8
# Given an array of meeting time intervals where intervals[i] = [starti, endi],
# determine if a person could attend all meetings.

# Example 1:
# Input: intervals = [[0,30],[5,10],[15,20]]
# Output: false


intervals = [[0,30],[5,10],[15,20]]

class solution:
    def ableto_attend_meeting(self,intervals):
        ans = True
        for i in range(len(intervals)-1):
            # print(intervals[i][1] , intervals[i+1][0])
            if intervals[i][1] < intervals[i+1][0]:
                ans &= True
                
            else:
                ans &= False 
                
        return ans
    
s = solution()
print(s.ableto_attend_meeting(intervals))