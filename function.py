# def add(x,y):
#     return x+y
# a=int(input("enter first number : "))
# b= int(input("enter second number : "))
# print("sum of number is", add(a,b))

# def odd_even(n):
#     if n%2==0:
#         return "even"
#     else:
#         return "odd"
# x=int(input("enter your number : "))
# print(odd_even(x))

# def is_even(n):
#     if n%2==0:
#         return True
# x=int(input("enter your number : "))
# print("your number is ",is_even(x))


"""fibonacci series
def fibonacci(n):
    a=0
    b=1
    if n==1:
        print(a)
    elif n==2:
        print(a,b)
    else:
        print(a,b,end=" ")
        for i in range(n-2):
            c=a+b
            a=b
            b=c
            print(b,end=" ")
n=int(input("enter mo upto which you want series : "))
x=fibonacci(n)
print("fibonacci series is", x)"""
"""greater no
def greater(a,b):
    if a>b:
        print(a)
    print(b)
x=int(input("enter first number : " ))
y=int(input("enter second number: " ))
print(greater(x,y))"""
"""greatest no
def greater(a,b):
    if a>b:
        return a
    return b
def greatest(a,b,c):
    d=greater(a,b)
    return greater(d,c)
x=int(input("enter first number : " ))
y=int(input("enter second number: " ))
z=int(input("enter third number : " ))
print(f"greatest number is : {greatest(x,y,z)}")"""
#     *args

"""def add(*args):
    print(type(n))
    sum=1
    for i in args:
        sum =sum*int(i)
    return sum
n=input("enter").split()
print(add())"""
"""def itspower(num,*args):
    if args:
        return [i**num for i in args]
    else:
        return "enter value in the args"
num=int(input ("enter power "))
n=int(input ("enter range"))

list1=[i for i in range(1,n+1)]
print(itspower(num,*list1))"""
# def kw(**kwrgs):
#     for k,v in kwrgs.items():
#         print(f"{k}:{v}")
# kw(n="pawan",age=20)
# kw()
# kw(** {"n":30})
# def all_parameter(num,*args,num1="default",**kwrgs):
#     print(num,args,num1,kwrgs)
# x=30
# all_parameter("pawan",1,2,3,4,5,6,num1=40,n="a",age=30)
# #pawan (1, 2, 3, 4, 5, 6) 40 {'n': 'a', 'age': 30} ---> i want this in first case
# # pawan (1, 2, 3, 4, 5, 6) default {'num1':40,'n': 'a', 'age': 30}---> in 2nd cse
"""def rev(list,**kwargs):
    if kwargs.get('reverse_str')=="True":
        return [i[::-1].title() for i in list]
    else:
        return [i.title() for i in list]
n=int(input("enter no of names: "))
list=[input(f"name{i+1}: ") for i in range(n)]
print(rev(list))
print(rev(list,reverse_str="True"))"""
# add=lambda a,b:a+b
# print(add("a","b"))
# sum=0
# x=lambda a:a if i%2==0 else 0
# for i in range(10):
#     sum+=x(i)
# print(sum)
# def counter(name,value):
#     # if value in name:
#     for pos,val in enumerate(name):
#         if val == value:
#                 return f"{value}: {pos}"
#     return "entered value not found"
# n=int(input("enter no of names: "))
# name=[input(f"enter name{i+1}: ") for i in range(n)]
# value=input("enter value to be searched: ")
# print(counter(name,value))
# numb=[1,2,3,4,5]
# def pow(n):
#     def numb(x):
#         return x**n
#     return numb
# square=pow(2)
# print(square(5))
# def fun(func,l):
#     return [func(i) for i in l]
# list=[i for i in range(10)]
# print(fun(lambda a:a**2,list),end=" ")
# n=int(input("ennter no"))
# l=[1,2,3,4,5]

# my_map=list(map(lambda a:a**2 ,l))
# print(my_map)
# even=list(filter(lambda a : a if a%2==0 else None, [i for i in range(n)]))
# print(even)
# l1=list(zip([i for i in range(20) if i%2==0],[i for i in range(20) if i%2!=0]))
# d1=dict(zip([i for i in range(20) if i%2==0],[i for i in range(20) if i%2!=0]))
# print(d1)
# l1,l2=zip(*l1)
# print(l1,l2)
# d3,d2=[],[]
# for k,v in d1.items():
#     d3.append(k)
#     d2.append(v)
# print(d3,d2)
"""def check_all(*args):
    if all([type(arg)==int for arg in args]):
        for i in args:
            print(i)
    else:
        print("enter valid data type")
check_all(1,2,3,4)
check_all(1,"w",3)"""
"""def check_any(*args):
    if any([type(arg)==int for arg in args]):
        for i in args:
            print(i,end=" ")
check_any(1,2,3,4)
print()
check_any(1,2,"w",4.0)"""
"""l1=[{"name":"pawan", "age":20,"score":70.5},{"name":"dhawan", "age":30,"score":60.5},{"name":"Rawan", "age":10,"score":80.5}]
l2={
    "student1":{"name":"pawan", "age":20,"score":70.5},
    "student2":{"name":"dhawan", "age":30,"score":60.5},
    "student3":{"name":"Rawan", "age":10,"score":80.5}
    }
# max
print((max(l1,key= lambda a:a.get("score"))))
print(l2[(max(l2,key= lambda keys:l2[keys]["score"]))])

# sorted
print(sorted(l1, key= lambda d:d["score"]))
print(sorted(l1, key= lambda d:d["score"], reverse=True))
print(list(l2[i] for i in sorted(l2, key= lambda keys:l2[keys]["score"])))"""
# docstring
"""def add(*args):
    '''this function add all the arguments passed in the function'''
    if all([type(i)==int for i in args]):
        sum=0
        for i in args:
            sum+=i
        return sum
    return "enter valid arguments"
print(add.__doc__)
print(add.__name__)"""




