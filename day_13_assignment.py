# 1

# def newList(root1, root2):
 
#     ptr1 = root1
#     ptr2 = root2
     
#     root = None
#     while (ptr1 != None) :
#         temp = Node(0)
#         temp.next = None
 
#         # Compare for greater node
#         if (ptr1.val < ptr2.val):
#             temp.val = ptr2.val
#         else:
#             temp.val = ptr1.val
 
#         if (root == None):
#             root = temp
#         else :
#             ptr = root
#             while (ptr.next != None):
#                 ptr = ptr.next
 
#             ptr.next = temp
         
#         ptr1 = ptr1.next
#         ptr2 = ptr2.next
     
#     return root

# 2

# def removeDuplicates(head):
 
#     # do nothing if the list is empty
#     if head is None:
#         return None
 
#     current = head
 
#     # compare the current node with the next node
#     while current.next:
#         if current.data == current.next.data:
#             nextNext = current.next.next
#             current.next = nextNext
#         else:
#             current = current.next        # only advance if no deletion
 
#     return head

# 3
# def reverse(head, k):
        
#         if head == None:
#           return None
#         current = head
#         next = None
#         prev = None
#         count = 0
  
#         # Reverse first k nodes of the linked list
#         while(current is not None and count < k):
#             next = current.next
#             current.next = prev
#             prev = current
#             current = next
#             count += 1
  
#         if next is not None:
#             head.next = reverse(next, k)
  
#         # prev is new head of the input list
#         return prev


def reverseInGroups(head, k):
 
    # base case
    if head is None:
        return None
 
    # start with the current node
    current = head
 
    # reverse next `k` nodes
    prev = None
    count = 0
 
    # iterate through the list and move/insert each node
    # in front of the result list (like a push of the node)
    while current and count < k:
        count = count + 1
        # tricky: note the next node
        next = current.next
        # move the current node onto the result
        current.next = prev
        # update the previous pointer to the current node
        prev = current
        # move to the next node in the list
        current = next
 
    # recur for remaining nodes
    head.next = reverseInGroups(current, k)
 
    # it is important to return the previous node (to link every group of `k` nodes)
    return prev



# A Linked List Node
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
 
 
# Remove duplicates from a sorted list
def removeDuplicates(head):
 
    # do nothing if the list is empty
    if head is None:
        return None
 
    current = head
 
    # compare the current node with the next node
    while current.next:
        if current.data == current.next.data:
            nextNext = current.next.next
            current.next = nextNext
        else:
            current = current.next        # only advance if no deletion
 
    return head
 
def reverse(head, k):
        
        if head == None:
          return None
        current = head
        next = None
        prev = None
        count = 0
  
        # Reverse first k nodes of the linked list
        while(current is not None and count < k):
            next = current.next
            current.next = prev
            prev = current
            current = next
            count += 1
  
        if next is not None:
            head.next = reverse(next, k)
  
        # prev is new head of the input list
        return prev
    
def deleteLast(head, x):
  
    temp = head
    ptr = None
      
    while (temp != None): 
          
        # If found key, update
        if (temp.data == x):
            ptr = temp     
              
        temp = temp.next
      
    # If the last occurrence is the last node
    if (ptr != None and ptr.next == None): 
        temp = head
        while (temp.next != ptr):
            temp = temp.next
              
        temp.next = None
      
    # If it is not the last node
    if (ptr != None and ptr.next != None): 
        ptr.data = ptr.next.data
        temp = ptr.next
        ptr.next = ptr.next.next
          
    return head

if __name__ == '__main__':
 
    # input keys
    # keys = [1, 2, 2, 2, 3, 4, 4, 5]
    keys = [1,2,3,4,2,5]
 
    # construct a linked list
    head = None
    for i in reversed(range(len(keys))):
        head = Node(keys[i], head)
 
    # head = removeDuplicates(head)
    printList(head)
    # head = reverse(head,2)
    
    # head  = deleteLast(head,2)
 
    # print linked list
    printList(head)
    
    
    
    
# 1       2       3       4

# 2       1      4     3   


# 4
# def reverse(curr, k):
 
#     # maintain a `prev` pointer
#     prev = None
 
#     # traverse the list and reverse first `k` nodes
#     while curr and k > 0:
#         k = k - 1
 
#         # tricky: note the next node
#         next = curr.next
 
#         # fix the `curr` node
#         curr.next = prev
 
#         # advance the two pointers
#         prev = curr
#         curr = next
 
#     # return node at the front
#     return prev, curr
 
 
# # Function to skip `k` nodes in a given linked list.
# def skipKNodes(curr, k):
 
#     prev = None
#     while curr and k > 0:
#         k = k - 1
#         prev = curr
#         curr = curr.next
 
#     return prev, curr
 
 
# # Recursive function to reverse every alternate group of `k` nodes
# # in a linked list
# def reverseAlternatingKNodes(head, k):
 
#     prev = None
#     curr = head
 
#     # traverse the whole list
#     while curr:
 
#         # curr would be the last node in the reversed sublist
#         last = curr
 
#         # reverse next `k` nodes and get their head
#         front, curr = reverse(curr, k)
 
#         # update head pointer after first `reverse()` call
#         if prev is None:
#             head = front
 
#         # for subsequent calls to `reverse()`, link the reversed sublist
#         # with the rest of the list
#         else:
#             prev.next = front
 
#         # link the last node with the current node
#         last.next = curr
 
#         # skip next `k` nodes
#         prev, curr = skipKNodes(curr, k)
 
#     # return head node
#     return head



# 5
# def deleteLast(head, x):
  
#     temp = head
#     ptr = None
      
#     while (temp != None): 
          
#         # If found key, update
#         if (temp.data == x):
#             ptr = temp     
              
#         temp = temp.next
      
#     # If the last occurrence is the last node
#     if (ptr != None and ptr.next == None): 
#         temp = head
#         while (temp.next != ptr):
#             temp = temp.next
              
#         temp.next = None
      
#     # If it is not the last node
#     if (ptr != None and ptr.next != None): 
#         ptr.data = ptr.next.data
#         temp = ptr.next
#         ptr.next = ptr.next.next
          
#     return head


# 6
# class Solution:
#     def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
#         if list1 == None:
#             return list2
#         if list2 == None:
#             return list1 

#         if list1.val <= list2.val:
#             list1.next = self.mergeTwoLists(list1.next,list2)
#             return list1
#         else:
#             list2.next = self.mergeTwoLists(list1,list2.next)
#             return list2
        
