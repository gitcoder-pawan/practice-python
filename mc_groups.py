t=input()
t=int(t)

for i in range(t):
    count = 0
    s=input().split('0')
    for i in range(len(s)):
        if '1' in s[i]:
            count=count+1
    print(count)


