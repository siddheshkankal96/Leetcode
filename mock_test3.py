#Stack using list
stack = [] 

#Function to print top element of stack
def top(stack):
  if stack != []:
    print(stack[-1]  + " is top element")
  else:
    print("Stack Empty!!!")

#Function to print size of stack
def size(stack):
  print("Size of stack is " + str(len(stack)))

#Function to check if a stack is empty
def empty(stack):
  if stack == []:
    print("True")
  else:
    print("False")

# append() function is used to push element in the stack 
stack.append('a') 
stack.append('b') 
stack.append('c')

size(stack)

print(stack) 

top(stack)

# pop() function to pop element from stack in LIFO order 
print(stack.pop() + " is popped")

print(stack) 

empty(stack)

print(stack.pop() + " is popped")
print(stack.pop() + " is popped")

print(stack) 

empty(stack)




# Implement Queue using List(Functions)
q=[]
def Enqueue():
    if len(q)==size: # check wether the stack is full or not
        print("Queue is Full!!!!")
    else:
        element=input("Enter the element:")
        q.append(element)
        print(element,"is added to the Queue!")
def dequeue():
    if not q:# or if len(stack)==0
        print("Queue is Empty!!!")
    else:
        e=q.pop(0)
        print("element removed!!:",e)
def display():
    print(q)
    size=int(input("Enter the size of Queue:"))
    while True:
        print("Select the Operation:1.Add 2.Delete 3. Display 4. Quit")
        choice=int(input())
        if choice==1:
            Enqueue()
        elif choice==2:
            dequeue()
        elif choice==3:
            display()
        elif choice==4:
            break
        else:
            print("Invalid Option!!!")
            
            
            
