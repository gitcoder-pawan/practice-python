n=int(input("enter no of tests: "))
l=[]
for i in range(n):
    nh=int(input(f"enter no of stick holders for test{i+1}: "))
    hs=input("enter height of sticks comma seprated: ").split()
    hs=[int(i) for i in hs]
    h=list(set(hs))
    for i in h:
        if i==0:
            h.remove(i)
    l.append(len(h))
for i in range(len(l)):
    print(f"min operation required for test{i+1} is : {l[i]}")