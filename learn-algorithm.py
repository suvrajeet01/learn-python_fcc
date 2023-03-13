def iterative_funcions(n):
    fact = 1
    for i in range(2, n + 1):
        fact *= i
    return fact

print(iterative_funcions(5))


def recur_factorial(n):
    if n == 1:
        return n
    else:
        temp = recur_factorial(n-1)
        temp = temp * n
    return temp

print(recur_factorial(5))


def recur_fact(m):
    if m == 1: return m
    else: return m * recur_fact(m-1)

print(recur_fact(5))














def permute(string, pocket=""):
    if len(string) == 0:
        print(pocket)
    else:
        for i in range(len(string)):
            letter = string[i]
            front = string[0:i]
            back = string[i+1:]
            together = front + back
            permute(together, letter+pocket)
        
print(permute("ABC", ""))




from math import factorial

def permutations(str):
    for p in range(factorial(len(str))):
        print(''.join(str))
        i = len(str) - 1
        while i > 0 and str[i-1] > str[i]:
            i -= 1
        str[i:] = reversed(str[i:])
        if i > 0:
            q = i
            while str[i-1] > str[q]:
                q += 1
            temp = str[i-1]
            str[i-1] = str[q]
            str[q] = temp
s = 'abc'
s = list(s)
permutations(s)









# def search(arr, target):
#     for i in range(len(arr)):
        
#         if arr[i] == target:
#             return i

# arr = [2,5,8,9,10,16,22]
# target = 10

# print(search(arr, target))



# def binary_itr(arr, start, end, target):
#         while start <= end:
#             mid = (start + end)//2
#             if arr[mid] < target:
#                 start = mid + 1
            
#             elif arr[mid] > target:
#                 start = mid - 1

#             else:
#                 return mid
#         return start
        


# arr = [2,5,8,9,10,16,22]
# target = 10

# result = binary_itr(arr, 0, len(arr) - 1, target)

# if result != 1:
#     print('element is present at index %d'%result)
# else:
#     print('element is not present in array')













# def binary_recur(arr, start, end, target):
#         if start <= end:
#             mid = start + end - 1 //2
#             if arr[mid] < target:
#                 binary_recur(arr, mid+1, end, target)
            
#             elif arr[mid] > target:
#                 binary_recur(arr, start, mid - 1, target)

#             else:
#                 return mid
#         else:
#             return -1


# arr = [2,5,8,9,10,16,22]
# target = 10

# result = binary_recur(arr, 0, len(arr)-1, target)

# if result != 1:
#     print('element is present at index %d', str(result))
# else:
#     print('element is not present in array')





























def bubble_optimized(A):
    iterations = 0
    for i in range(len(A)):
        for j in range(len(A) -i -1):
            iterations += 1
            if A[j] > A[j+1]:
                A[j] ,A[j+1] = A[j+1], A[j]
    return A, iterations


A = [9,8,7,6,5,4,3,2,1]
print(bubble_optimized(A))



def swap(A, i, j):
    temp= A[i]
    A[i] = A[j]
    A[j] = temp
def bubble_sort_un_op(A):
    iterations = 0

    for i in A:
        for j in range(len(A) - 1):
            iterations +=1
            if A[j] >= A[j+1]:
                swap(A, j, j+1)
    return A, iterations


A = [9,8,7,6,5,4,3,2,1]
print(bubble_sort_un_op(A))
















def insert_sort(a):
    for j in range(1, len(a)):
        key = a[j]
        i = j - 1
        while i >= 0 and a[i] > key:
            a[i+1] = a[i]
            i -= 1
        a[i+1] = key
    return a

a = [5,2,4,6,1,3]
print(insert_sort(a))































class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def traversal(self):
        first = self.head
        while first:
            print(first.data)
            first = first.next

    def insert_new_header(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node


    def search(self, x):
        temp = self.head
        while temp is not None:
            if temp.data == x:
                return True
            temp = temp.next
        else:
            return False

    def delete_node(self, data):
        temp = self.head
        while temp is not None:
            if temp.data == data:
                break
            prev = temp
            temp = temp.next
        prev.next = temp.next

    
    def delete_tail(self):
        temp = self.head
        while temp.next.next is None:
            temp = temp.next
        temp.next = None

family = LinkedList()
family.head = Node('bob')
wife = Node('amy')
first_kid = Node('max')
second_kid = Node('jenna')

family.head.next = wife
wife.next = first_kid
first_kid.next = second_kid

family.traversal()
family.insert_new_header('dave')
family.traversal()
print(family.search('bob'))
family.delete_node('amy')
family.traversal()
family.delete_tail()
family.traversal()
















































a = [-5, -23, 5, 0, 23, -6, 23, 67]
c = []

while a:
    minimum = a[0]
    for x in a:
        if x < minimum:
            minimum = x
    c.append(minimum)
    a.remove(minimum)

print(c)





def merging(left, right):
    c=[]
    while min(len(left), len(right)) > 0:
        if left[0] > right[0]:
            insert = right.pop()
            c.append(insert)
        elif left[0] <= right[0]:
            insert = left.pop()
            c.append(insert)
    if len(left) > 0:
        for i in left:
            c.append(i)
    if len(right) > 0:
        for i in right:
            c.append(i)
    return c

left = [2,5,6,10]
right = [3,4,12,20]

print(merging(left, right))



def sortArray(a):
    if len(a) <= 0:
        return a
    middle = len(a)//2
    left = sorted(a[:middle])
    right = sorted(a[middle:])
    merged = []
    while left and right:
        if left[0] <= right[0]:
            merged.append(left.pop(0))
        else:
            merged.append(right.pop(0))
    merged.extend(right if right else left)
    return merged

print(sortArray(a))




class Solution(object):
    def sortArray(self, nums):
        mid = len(nums)//2
        left = sorted(nums[:mid])
        right = sorted(nums[mid:])
        c=[]
        while min(len(left), len(right)) > 0:
            if left[0] > right[0]:
                insert = right.pop()
                c.append(insert)
            elif left[0] <= right[0]:
                insert = left.pop(0)
                c.append(insert)
        if len(left) > 0:
            for i in left:
                c.append(i)
        if len(right) > 0 :
            for i in right:
                c.append(i)
        return c


nums = [5,2,3,1]
numss = [5, 1, 1, 0, 2, 6]
print(sortArray(nums))
print(sortArray(numss))