n,h,x=map(int,input().rstrip().split())
print(n+h+x)
t=list(map(int,input().rstrip().split()))
print(t[0]+t[1])
count=0
if x==h:
    print("yes")
else:
    for i in range(n):
        if t[i] + x == h:
            count = count + 1
    if count == 0:
        print("NO")
    else:
        print("YES")