# n,k=map(int,input().split())
# count=0
# for i in range(n):
#     t=input()
#     t=int(t)
#     if t%k==0:
#         count=count+1
# print(count)


# cook your dish here
def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n - 1)


t = input()
t = int(t)
for i in range(t):
    n = input()
    n = int(n)
    print(fact(n))

