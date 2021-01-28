"""winning_number= 25
guessed_number= int(input("enter a number between 0 to 1000 : "))
if guessed_number< 0 or guessed_number>1000:
    print("enter a valid number")
if guessed_number==winning_number :
    print("you win")
if  guessed_number >=0 and guessed_number<=1000:
    if guessed_number< winning_number :
        print("too low")
    else :
        print("too high")
"""
"""name = input("enter name start with 'a' or 'A' : ")
age = int(input("enter your age : "))
if (name[0]== 'a' or name[0]== 'A') and age>=10 :
    print("you can watch movie")
else:
    print("sorry! , you cant watch movie")"""
"""name, char = input("enter name and char : ").split()
if char in name :
    print("character you is present ")
else:
    print("not present ")"""
"""name= input ("enter your name : ")
if name:
    print("string is not empty")
else:
    print("please enter valid name")"""

"""i=1
while i<=10 :
    print("hello world ")
    i=i+1"""
"""i=1
sum =0
while i<=20 :
    sum = sum + i
    i+=1
print(sum)"""
"""n= int(input("enter a number upto which you want sum : "))
sum =0
i=1
if n>0 :
    while i<=n :
        sum =sum + i
        i= i+1
    print(f"your sum is : {sum}")
else :
    print(" please enter a valid number")"""
"""n = input("enter a number having more than one digit : ")
i = 0 
sum = 0
if len(n)>1 :
    while i<len(n) :
        sum = sum + int(n[i])
        i= i+1
    print(f"sum of digit is : {sum}")
else :
    print("please enter a valid number")"""
"""name= input("enter your name : ")
i=0
temp =""
while i<len(name) :
    if name[i] not in temp :
        print(f"{name[i]} : {name.count(name[i])}")
    temp = temp+name[i]
    i=i+1"""
"""numb = input("enter any number greater than one digits : ")
sum=0
if len(numb)>1:
        for i in range(len(numb)):
            sum=sum+ int(numb[i])
        print(f"sum of digits : {sum}")
else:
        print("please enter a number greater than one digit")"""
"""n=int(input("please enter a number up to which youwant sum : "))
sum=0
if n>=0:
    for i in range (1,n+1):
        sum =sum + i
    print(f"sum of digits is : {sum}")
else:
    print("please enter a valid number")"""
"""name= input("ENTER your name : ")
temp =""
for i in range (1,len(name)):
    if name[i] not in temp :
        print(f"{name[i]}: {name.count(name[i])}")
    temp=temp+name[i]"""
"""import random
num=random.randint(0,100)
guess= 1
numu=int(input("enter any number between 0 to 99 :"))
while True:
    if numu==num:
        print(f"you win. your guessed number in {guess} times ")
        break
    else:
        if numu>num:
            print("too high")
        else:
            print("too low")
        guess+=1
        numu= int(input("guess a number : "))"""
# for i in range (1,10):
#     print(i)
"""name=input("enter your name : ")
total=0
for i in name:
    total+=int(i)
print(total)"""
"""st1=input("enter your strting : ")
n=len(st1)
for i in range(0,n,2):
    print(str(i) + ' : ' +st1[i],end=" | " )"""
"""st1=input("enter your strting : ")
n=len(st1)
for i in range(n-1,-1,-2):
    print(str(i) + ' : ' +st1[i] )"""
nane=input("enter your string")
# for i in range(0,len(name) )







