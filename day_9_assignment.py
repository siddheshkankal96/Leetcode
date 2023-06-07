# <aside>
# 💡 **Question 1**

# Given an integer `n`, return *`true` if it is a power of two. Otherwise, return `false`*.

# An integer `n` is a power of two, if there exists an integer `x` such that `n == 2x`.

# **Example 1:**
# Input: n = 1 

# Output: true

# **Example 2:**
# Input: n = 16 

# Output: true

# **Example 3:**
# Input: n = 3 

# Output: false

# </aside>


def powerOf2(n):
    if n<=0:
        return False
    if n==1:
        return True
    return powerOf2(n//2) if n%2==0 else False

# print(powerOf2(16))


    
# <aside>
# 💡 **Question 2**

# Given a number n, find the sum of the first natural numbers.

# **Example 1:**

# Input: n = 3 

# Output: 6

# **Example 2:**

# Input  : 5 

# Output : 15

# </aside>

def sumOfNaturalNums(n):
    if n==1:
        return 1
    return n + sumOfNaturalNums(n-1)

# print(sumOfNaturalNums(3))



# <aside>
# 💡 **Question 3**

# ****Given a positive integer, N. Find the factorial of N. 

# **Example 1:**

# Input: N = 5 

# Output: 120

# **Example 2:**

# Input: N = 4

# Output: 24

# </aside>



def Factorial(n):
    if n==1:
        return 1
    return n * Factorial(n-1)

# print(Factorial(4))

# <aside>
# 💡 **Question 4**

# Given a number N and a power P, the task is to find the exponent of this number raised to the given power, i.e. N^P.

# **Example 1 :** 

# Input: N = 5, P = 2

# Output: 25

# **Example 2 :**
# Input: N = 2, P = 5

# Output: 32

# </aside>


def power(n,p):
    if p == 0:
        return 1
    if p == 1:
        return n
    return n * power(n,p-1)

print(power(5,2))

# <aside>
# 💡 **Question 5**

# Given an array of integers **arr**, the task is to find maximum element of that array using recursion.

# **Example 1:**

# Input: arr = {1, 4, 3, -5, -4, 8, 6};
# Output: 8

# **Example 2:**

# Input: arr = {1, 4, 45, 6, 10, -8};
# Output: 45

# </aside>


arr = [1, 4, 3, -5]

def findMaxRec(A, n):
     
    if (n == 1):
        return A[0]
    return max(A[n - 1], findMaxRec(A, n - 1))



# print(findMaxRec(arr, len(arr)))


                
                
                
# <aside>
# 💡 **Question 6**

# Given first term (a), common difference (d) and a integer N of the Arithmetic Progression series, the task is to find Nth term of the series.

# **Example 1:**

# Input : a = 2 d = 1 N = 5
# Output : 6
# The 5th term of the series is : 6

# **Example 2:**

# Input : a = 5 d = 2 N = 10
# Output : 23
# The 10th term of the series is : 23

# </aside>



a = 2
d = 1 
N = 5

def series(a,d,n):
    if n==1:
        return 1
    return d + series(a,d,n-1)

# print(series(a,d,N))



    


# <aside>
# 💡 **Question 7**

# Given a string S, the task is to write a program to print all permutations of a given string.

# **Example 1:**

# ***Input:***

# *S = “ABC”*

# ***Output:***

# *“ABC”, “ACB”, “BAC”, “BCA”, “CBA”, “CAB”*

# **Example 2:**

# ***Input:***

# *S = “XY”*

# ***Output:***

# *“XY”, “YX”*

# </aside>

def permute(a, l, r):
    if l == r:
        print((''.join(a)),end = ' ')
    else:
        for i in range(l, r):
            # print(a[l], a[i])
            a[l], a[i] = a[i], a[l]
            # print(a[l], a[i])
            permute(a, l+1, r)
            # print(a[l], a[i])
            a[l], a[i] = a[i], a[l]  # backtrack
            # print(a[l], a[i])
 
 
# Driver code
string = "AB"
n = len(string)
a = list(string)
 
# Function call
# permute(a, 0, n)
 

# <aside>
# 💡 **Question 8**

# Given an array, find a product of all array elements.

# **Example 1:**

# Input  : arr[] = {1, 2, 3, 4, 5}
# Output : 120
# **Example 2:**

# Input  : arr[] = {1, 6, 3}
# Output : 18

# </aside>
a = [1,2,3,4,5]

def mul(a,n):
    if n==1:
        return a[0]
    return a[n-1] * mul(a,n-1)


        

# print(mul(a,len(a)))