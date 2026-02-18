# #fibonacci series
# class Solution:
#     def fib(self, n: int) -> int:
#         if n == 0:
#             return 0
#         if n == 1:
#             return 1
#         a, b = 0, 1
#         for _ in range(2, n + 1):
#             a, b = b, a + b
#         return b
    
# def fibonacci(n):
#     a, b = 0, 1
#     for _ in range(n):
#         print(a, end=" ")
#         a, b = b, a + b
# fibonacci(10)    

# class Solution:
#     def tribonacci(self, n: int) -> int:
#         if n == 0:
#             return 0
#         if n == 1 or n == 2:
#             return 1
        
#         a, b, c = 0, 1, 1
        
#         for _ in range(3, n + 1):
#             a, b, c = b, c, a + b + c
        
#         return c


# #LIST
# #list indices
# #list slicing
# #list method
# #list operators
# #mapping


# #list
# list=[1,3,45,2,6]
# print(list[4])

# #list slicing makes a new data
# #syntax [start index: end index]

# print(list[1:4])
# print(list[:4])

# #list operatorn (concatenation +)(repetition *)(membership (in,not-in)) (comparison)

# a=[1,2,3]
# b=[4,5,6]
# print(a+b)

# print(a*3)

# fruits=["hi","hello","bye"]
# print("hi"in fruits)

# one=[1,2,3]
# two=[1,3,4]
# print(one==two)
# print(one<two)

# #EX

# a=[1,2,3,4,5]
# b=[2,4,5,6,8]

# print(a[3])
# print(a[:3],b[1:])
# print(a+b)
# print(a*2,b*3)
# print(a>b)

#list methods (append) (insert) (extend) (remove) (pop) (index) (count) (sort)

# num=[1,2,3]
# num.append(4)
# print(num)

# num.insert(3,5)
# print(num)

# a=[1,2]
# b=[3,4]
# a.extend(b)
# print(a)

# num.remove(2)
# print(num)

# num.pop(1)
# print(num)

# num.clear()
# print(num)

# num=[1,2,40,5]
# print(num.index(2))
# num[2]

# print(num.count(2))

# a=[4,6,8,1,0]
# a.sort()
# print(a)
# a.sort(reverse=True)
# print(a)

# b=a.copy()
# print()

#map(), filter and list()-->functional programming-->iterates

# num=[1,2,3,4]
# result=list(lambda x:x*2,num)
# print(result)


# def func(x):
#     return x*2
# result=list(map(func,num))
# print(result)

# one=[1,2,3,4,5,6,7,8,9]
# two=list(filter(lambda x:x%2==0,one))
# print(two)

#reduce-->convert into a single value
# from functools import reduce
# num=[1,2,3,4,5]
# result=reduce(lambda a,b:a+b,num)
# print(result)

# num=[1,2,3,4,5,6,7,8]
# odd=list(filter(lambda x:x%2!=0, num))
# even=list(filter(lambda x:x%2==0, num))
# print(even)
# print(odd) 

# #palindrome slicing
# word=input("enter a word:")
# if word==word[::-1]:
#     print("palindrome")
# else:
#     print("not a palindrome")
    
# #without slicing

# word=input("enter a word:")
# rev=" "
# for ch in word:
#     rev=ch+rev
# if word==word[::-1]:
#     print("palindrome")
# else:
#     print("not a palindrome")
    
num=int(input("enter num:"))
ori=num
rev=0
while num>0:
    digit=num%10
    rev=rev*10+digit
    num=num
print(rev)
if ori==rev:
    print("palindrome")
else:
    print("not a palindrome")
