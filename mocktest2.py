# Given a non-negative integer x, return the square root of x rounded down to the nearest integer.
# The returned integer should be non-negative as well. You must not use any built-in exponent function or operator. 

#  Example 1:
# Input: x = 4 Output: 2 Explanation: The square root of 4 is 2, so we return 2.
# Example 2:

# Input: x = 8 Output: 2 Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.
# Constraints:

# 0 <= x <= 2^31 - 1

# import math
# def square_root(x):
#     if (x == None) :
#         return
#     return int(math.sqrt(x))

# print(square_root(8))


# def square_root(x):
#     if (x == None) or x < 0:
#         return
#     return int(x ** 0.5)

# print(square_root(8))


# def square_root(x):
#     l = 0
#     r = 9
#     while l < r:
#         mid = (l+r)//2

        
#         mid_square = mid ** 2
        
#         if mid_square == x:
#             return mid
        
#         elif mid_square > x:
#             r = mid -1
        
#         else:
#             l = mid + 1
    
    
# print(square_root(4))


# formula for this is as 
# We can consider (√x-√x)2  = 0.
# Replacing one of the √x‘s with y, then the equation becomes (y-√x)2 => y2 – 2y√x + x = 0
# √x = (y2 + x) / 2y
# √x = (y + x/y) / 2


def findSqrt(x):
  if x < 2:
    return x
   
  y = x
  z = (y + (x/y)) / 2
  print(y,z)

  while abs(y - z) >= 0.1:
    y = z
    z = (y + (x/y)) / 2
   
  return int(z)
     
    



# -------------------------------------------------------------------------------------------

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
 
 
# Helper function to print a given linked list
def printList(head):
 
    ptr = head
    while ptr:
        print(ptr.data, end=' —> ')
        ptr = ptr.next
 
    print('None')

def reverse(head):
    if head == None:
        return None
    current = head
    next = None
    prev = None
    count = 0
  
        # Reverse first k nodes of the linked list
    while(current is not None):
        next = current.next
        current.next = prev
        prev = current
        current = next
            
    return prev


def addTwoList(l1,l2):
    
    summ = 0
    carry = 0
    temp = None
    head = None
    while (carry or l1!= None and l2!= None ):
        summ = carry
        if l1 is not None:
            summ += int(l1.data)
            l1 = l1.next
        if l2 is not None:
            summ += int(l2.data)
            l2 = l2.next        
        
        node = Node(summ % 10)
        # print(node.data)
        carry = summ //10
    
        if temp == None:
            head = temp = node
        else:
            temp.next = node
            temp = temp.next
            
    return head

if __name__ == '__main__':
    l1 = [2,4,3]
    l2 = [5,6,4]
 
 
    # construct a linked list
    head1 = None
    for i in reversed(range(len(l1))):
        head1 = Node(l1[i], head1)
    # printList(head1)
    
    head2 = None
    for j in reversed(range(len(l2))):
        head2 = Node(l2[j], head2)
        
    # printList(head2)

    head2  = reverse(head2)
    printList(head2)
    head1 = reverse(head1)
    printList(head1)
    
    head = reverse(addTwoList(head1,head2))
    
    printList(head)
