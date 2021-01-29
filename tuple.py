tup_=[1,2,3,[6,5,4]]
tup2=()
# print(sum(tup_))
tup_=tuple(tup_)
# print(tup_)
# tuple unpackig
# tup2=1,2,3,4
# print(tup2)
# n1,n2,n3,n4=tup2
# print(n1,n2,n3,n4)
tup_[3][1]=1
# print(tup_)
def fun(a,b):
    add=a+b
    mul=a*b
    sub=a-b
    return add,mul,sub
print(fun(2,3))
