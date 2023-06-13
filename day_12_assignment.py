



# class Solution:
#     def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         if(head.next==None):
#             return None
#         slow=head
#         fast=head.next
#         while(fast.next and fast.next.next):
#             slow=slow.next
#             fast=fast.next.next
#         slow.next=slow.next.next
#         return head




# 2

# def detectAndRemoveLoop(head): 
#       if head is None:
#           return
#       if head.next is None:
#           return
#       slow_p = head
#       fast_p = head
          
#       while(slow_p and fast_p and fast_p.next):
#           slow_p = slow_p.next
#           fast_p = fast_p.next.next
 
#           # If slow_p and fast_p meet at some point then
#           # there is a loop
#           if slow_p == fast_p:
#               return True
        # return False 
# 3


# def findNthFromEnd(n):
#     node1 = head
#     node2 = head
#     count = 0
       
# 	        while (node1 != None):
# 	            if (count == (n)): 
# 	                break
# 	            count += 1
# 	            node1 = node1.next
	         
# 	        if (count == (n)):

# 	            while (node1 != None):
# 	                node1 = node1.next
# 	                node2 = node2.next
	            
# 	            return node2.value
      
#         else:
# 	        System.out.println("\nError: The length of the list is less than "  + n);
#             return -1;


# 4
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow,fast = head,head
            
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next 
            
            # middle is slow
            
        prev = slow
        slow = slow.next
        prev.next = None
         
            
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow 
            slow = temp
            
        fast = head 
        slow  = prev 
            
        while slow:
            if slow.val != fast.val:
                return False
            fast = fast.next
            slow = slow.next 
        return True


# 5

# Input:
# N = 3
# value[] = {1,3,4}
# X = 2
# Output:1
# s         f
# 1 -> 3 -> 4



 
# def detectAndRemoveLoop(self): 
#       if self.head is None:
#           return
#       if self.head.next is None:
#           return
#       slow_p = self.head
#       fast_p = self.head
          
#       while(slow_p and fast_p and fast_p.next):
#           slow_p = slow_p.next
#           fast_p = fast_p.next.next
 
#           # If slow_p and fast_p meet at some point then
#           # there is a loop
#           if slow_p == fast_p:
#             slow_p = self.head
#               # Finding the beginning of the loop
#             while (slow_p.next != fast_p.next):
#               slow_p = slow_p.next
#               fast_p = fast_p.next
 
#                 # Sinc fast.next is the looping point
#             fast_p.next = None  # Remove loop     
   


# 6

# class Solution:
#     def deleteNodes(self, head: ListNode, m: int, n: int) -> ListNode:
#         pre = head
#         while pre:
#             for _ in range(m - 1):
#                 if pre:
#                     pre = pre.next
#             if pre is None:
#                 return head
#             cur = pre
#             for _ in range(n):
#                 if cur:
#                     cur = cur.next
#             pre.next = None if cur is None else cur.next
#             pre = pre.next
#         return head
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    






    





