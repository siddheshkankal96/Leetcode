# # 496. Next Greater Element I 👍

# <aside>
# 💡 **Question 1**

# Given an array **arr[ ]** of size **N** having elements, the task is to find the next greater element for each element of the array in order of their appearance in the array.Next greater element of an element in the array is the nearest element on the right which is greater than the current element.If there does not exist next greater of current element, then next greater element for current element is -1. For example, next greater of the last element is always -1.
# Input:
# N = 4, arr[] = [1 3 2 4]
# Output:
# 3 4 4 -1
# Explanation:
# In the array, the next larger element
# to 1 is 3 , 3 is 4 , 2 is 4 and for 4 ?
# since it doesn't exist, it is -1.

# Input:
# N = 5, arr[] [6 8 0 1 3]
# Output:
# 8 -1 1 3 -1
# Explanation:
# In the array, the next larger element to
# 6 is 8, for 8 there is no larger elements
# hence it is -1, for 0 it is 1 , for 1 it
# is 3 and then for 3 there is no larger
# element on right and hence -1.
# </aside>


# input = [2, 7, 3, 5, 4, 6, 8]

def next_Greater_Element(input):
    
    if not input:
        return
    
    for i in range(len(input)):
        next = -1
        for j in range(i+1,len(input)):
            if input[j] > input[i]:
                next = input[j]
                break
                
        print(next,end = ' ')
                
        
# next_Greater_Element(input) 


input = [2, 7, 3, 5, 4, 6, 8]

def next_Greater_Element2(arr,n):
    ans = [-1] * n
    stack = []
    def peek(stack):
        return stack[-1]
    def pop(stack):
        stack.pop()
    def push(stack,val):
        stack.append(val)
    def isEmpty(stack):
        if len(stack) ==0:
            return True
        else:
            return False  
    

    push(stack,arr[0])
    for i in range(1,len(arr)):
        while not isEmpty(stack) and peek(stack) <=  arr[i]:
            pop(stack)
            ans[i-1] = arr[i]
            while not isEmpty(stack) and peek(stack) <=  arr[i]:
                pop(stack)
                ans[i-2] = arr[i]
            break
        push(stack,arr[i])
        print(stack)
    
    print(ans) 
            
# next_Greater_Element2([6, 8, 0, 1, 3],len([6,8, 0, 1, 3]))
# 8 -1 1 3 -1

# next_Greater_Element2([1,3,2,4],len([1,3,2,4]))

# 3 4 4 -1


from collections import deque

input = [1,3,2,4]
def findNextGreaterElements(input):
    if not input:
        return
    result = [-1] * len(input)
    s = deque()
    
    for i in range(len(input)): 
        while s and input[s[-1]] < input[i]:
            result[s[-1]] = input[i]
            s.pop()
 
        s.append(i)
        print(s)
 
    print(result)
    
    
# findNextGreaterElements(input)







# <aside>
# 💡 **Question 2**

# Given an array **a** of integers of length **n**, find the nearest smaller number for every element such that the smaller element is on left side.If no small element present on the left print -1.
# Input: n = 3
# a = {1, 6, 2}
# Output: -1 1 1
# Explaination: There is no number at the
# left of 1. Smaller number than 6 and 2 is 1.

# Input: n = 6
# a = {1, 5, 0, 3, 4, 5}
# Output: -1 1 -1 0 3 4
# Explaination: Upto 3 it is easy to see
# the smaller numbers. But for 4 the smaller
# numbers are 1, 0 and 3. But among them 3
# is closest. Similary for 5 it is 4.

# </aside>
# Find the previous smaller element for every array element
def findPrevSmaller(arr):
 
    # base case
    if not arr:
        return
 
    # do for each element
    for i in range(len(arr)):
        # keep track of the previous smaller element for element `arr[i]`
        prev = -1
        # process elements on the left of the element `arr[i]`
        for j in reversed(range(0, i)):
            # break the inner loop at the first smaller element on the
            # left of the element `arr[i]`
            if arr[j] < arr[i]:
                prev = arr[j]
                break
 
        print(prev, end=' ')
 


def findPrevSmaller(arr):
 
    # base case
    if not arr:
        return
 
    # create an empty stack
    s = deque()
 
    # do for each element
    for i in range(len(arr)):
        # loop till stack is empty
        while s:
            # If the stack's top element is less than the current element,
            # it is the previous smaller element
            if s[-1] < arr[i]:
                print(s[-1], end=' ')
                break
            # remove the stack's top element is less if it is greater or equal
            # to the current element
            else:
                s.pop()
 
        # If the stack becomes empty, all elements to the left
        # of the current element are greater
        if not s:
            print(-1, end=' ')
 
        # push current element into the stack
        s.append(arr[i])
 


# <aside>
# 💡 **Question 4**

# You are given a stack **St**. You have to reverse the stack using recursion.
# Input:St = {3,2,1,7,6}
# Output:{6,7,1,2,3}

# Input:St = {4,3,9,6}
# Output:{6,9,3,4}
# </aside>

from collections import deque
 
 
def insertAtBottom(s, item):
 
    if not s:
        s.append(item)
        return
    top = s.pop()
    insertAtBottom(s, item)
    s.append(top) 
 
def insertAtBottom2(s, item):
    s.append(item)
    for _ in range(len(s) - 1):
        s.append(s.popleft())
    
    
def reverseStack(s):
    if not s:
        return
    item = s.pop()
    reverseStack(s)

    insertAtBottom2(s, item)
 

 
# s = deque(range(1, 5))
# print('Original stack is', s)
# reverseStack(s)
# print('Reversed stack is', s)
   
# <aside>
# 💡 **Question 5**

# You are given a string **S**, the task is to reverse the string using stack.
# Input: S="GeeksforGeeks"
# Output: skeeGrofskeeG

# </aside>

s="GeeksforGeeks"

q  = deque()

def reverse(q,s):
    for i in s:
        q.append(i)
        for _ in range(len(q)-1):
            q.append(q.popleft())
    print(''.join(q))
    
reverse(q,s)


def reverse2(s):
    stack = deque(s)
    return ''.join([stack.pop() for _ in range(len(s))])
    
# print( reverse2(s))




# <aside>
# 💡 **Question 6**

# Given string **S** representing a postfix expression, the task is to evaluate the expression and find the final value. Operators will only include the basic arithmetic operators like ***, /, + and -**.
# Input: S = "231*+9-"
# Output: -4
# Explanation:
# After solving the given expression,
# we have -4 as result.

# Input: S = "123+*8-"
# Output: -3
# Explanation:
# After solving the given postfix
# expression, we have -3 as result.

# </aside>

def evelauate_postfix(expr):
    if not expr:
        return -1

    stack = deque()
    for i in expr:
        if i.isdigit():
            stack.append(int(i))
        else:
            y = stack.pop()
            x = stack.pop()
            if i == '+':
                stack.append(x + y)
            if i == '-':
                stack.append(x - y)
            if i == '*':
                stack.append(x * y)
            if i == '/':
                stack.append(x // y)
                
    return stack.pop()


# print(evelauate_postfix("123+*8-"))


# <aside>
# 💡 **Question 7**

# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

# Implement the `MinStack` class:

# - `MinStack()` initializes the stack object.
# - `void push(int val)` pushes the element `val` onto the stack.
# - `void pop()` removes the element on the top of the stack.
# - `int top()` gets the top element of the stack.
# - `int getMin()` retrieves the minimum element in the stack.

# You must implement a solution with `O(1)` time complexity for each function.

# **Example 1:**
# Input
# ["MinStack","push","push","push","getMin","pop","top","getMin"]
# [[],[-2],[0],[-3],[],[],[],[]]

# Output
# [null,null,null,null,-3,null,0,-2]

# Explanation
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin(); // return -3
# minStack.pop();
# minStack.top();    // return 0
# minStack.getMin(); // return -2
# </aside>


# <aside>
# 💡 **Question 8**

# Given `n` non-negative integers representing an elevation map where the width of each bar is `1`, compute how much water it can trap after raining.

# **Example 1:**

# </aside>

# Function to find the amount of water that can be trapped within
# a given set of bars in linear time and constant space
def trap(heights):
 
    # maintain two pointers left and right, pointing to the leftmost and
    # rightmost index of the input list
    (left, right) = (0, len(heights) - 1)
    water = 0
 
    maxLeft = heights[left]
    maxRight = heights[right]
 
    while left < right:
        if heights[left] <= heights[right]:
            left = left + 1
            maxLeft = max(maxLeft, heights[left])
            water += (maxLeft - heights[left])
        else:
            right = right - 1
            maxRight = max(maxRight, heights[right])
            water += (maxRight - heights[right])
 
    return water

# a = [1,2]
# print(a[-1][1])