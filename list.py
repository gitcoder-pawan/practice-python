# list1=['p','pawan','pawan kumar', 5, 5.5]
# print(list1)
# list1[2]= 'kumar'
# list2=list1
# print(list1)
# print(list2)
# list1[2:]=5, 'shekhar'
# print(list1)
# list1[0:5:2]=[3,'p']
# list1[1:5]=1,2,3,4,6
# print(list1)
# list1[::2]=1,2,3
# print(list1)
# alpha=['c','a','d','b','pawan','kumar']
# beta=[1,2,1.2,3,4,5.0,2.5]
# alpha.append(2,"d")
# alpha.insert(1,"d")
# gama=beta+alpha
# alpha.append(beta)
# alpha.extend(beta)
# beta.extend(alpha)
# print(alpha)
# print(beta)
# print(alpha.count('a'))
# alpha.sort()
# print(alpha)
# beta.sort()
# print(beta)
# print(sorted(alpha))
# print(alpha)
# print(sorted(beta))
# print(beta)
# a=['a','b','c']
# b=[1,2,3,4]
# b=a.copy()
# print(b)
# b=a.sort()
# a.reverse()
# b=a.reverse()
# b=len(a)
# print(a)
# print(b)
# list1=['a','b','c']
# list2=['b','a','c']
# list3=['a','b','c']
# print(list1==list3)
# string1,string2,string3,string4= input("enter your all string : ").split(",")
# list1=[string1,string2,string3,string4]
# print(list1)
# list1=["this","is","my","string"]
# new_string=" ".join(list1)
# print(new_string)
# name="my name is pawan"
# list1=name.split(" ")
# print(list1)
# string2=" ".join(list1)
# print(string2)
# def reve(l):
#     li=[]
#     t=l.pop()
#     li.append(t)
#     print(li)
# list1=[1,2,3,4,5]
# reve(list1)

#
# numb=input("enter 4 digit your numb")
# list1=[]
# for i in numb:
#     list1.append(int(i))
# print(list1)
# print(rev(list1))



# n=int(input("enter element in the list: "))

# def square(list):
#     return [i**2 for i in list]
# # n=int(input("enter no of element in the list: "))
# print(square([i for i in range(1,n+1)]))

# def reverse(list):
#     return [list[-i] for i in range(1,len(list)+1)]
# # n=int(input("ente no of element in the list :"))
# print(reverse([i for i in range(n)]))

# def st_rev(list):
#         return [i[::-1] for i in list]
# print (f"enter {n} element")
# print(st_rev([input(f"enter {i+1} element for reversing: ") for i in range(n)]))

# def odd_even(list):
#     x,y,l=[],[],[]
#     for i in list:
#         if i%2==0:
#             x.append(i)
#         else:
#             y.append(i)
#     l.append(x)
#     l.append(y)
#     return l
# print(odd_even([i for i in range(n**2)]))

# def common(list1,list2):
#     return[i for i in list1 for j in list2 if i==j]
# n1=int(input("enter no of element in list 1: "))
# n2=int(input("enter no of element in list 2: "))
# print(common([input(f"enter list{n1}'s {i} no's : ") for i in range(1,n1+1)],[input(f"enter list {n2}'s {i} no's: ") for i in range(1,n2+1)]))


# def lt(list):
#     count=0
#     lst=[]
#     for i in list:
#         if type(i) == type(lst):
#             count+=1
#     return count
# n=int(input("enter no of element: "))
# list=[]
# for i in range(n):
#     inp=[]
#     if i%2==0:
#         print(f"enter list{i + 1} element : ")
#         for j in range(i+1):
#             inp.append(input(f"{j+1} element ="))
#         list.append(inp)
#     else:
#         list.append(i)
# print(list)
# print("no of list element "
#       lt(lis
# from array import *
# l=array('i',[1,2,3,4])
# for i in range(len(l)):
#     print(l[i],end=" ")

#decorator
"""def add(*args):
    sum=0
    for i in args:
        sum+=i
    return sum
a=add
# print(a(1,3,4,5))
def add(*args):
    def mul():
        mul=1
        for i in args:
            mul*=i
        return mul
    return mul
m=add(1,2,3,4,5)
# print(m())

def sum(fun,*args):
    s=0
    for i in args:
        s+=fun(i)
    return int(s)
# print(sum(lambda a:a**2,1,2,3,4,5,6))"""
"""def decorator_func(any_func):
    def wrapper_func():
        print("this is awesome")
        return any_func()
    return wrapper_func
@decorator_func
def func1():
    print("this is function 1")
func1()
from functools import wraps
def decorator_func(any_func):
    def wrapper_func(*args,**kwargs):
        '''this is wrapper function'''
        print("this is awesome")
        return any_func(*args,**kwargs)
    return wrapper_func
@decorator_func
def func1(*args,**kwargs):
    '''this is function one'''
    sum=0
    for i in args:
        sum+=i
    return sum
print(func1(1,2,3,4,5))
print(func1.__doc__)"""
#generator
def gen(n):
    for i in range(1,n+1):
        yield i**2
n=gen(10)
for i in gen(10):
    print(i)
print(list((i**2 for i in range(10))))








