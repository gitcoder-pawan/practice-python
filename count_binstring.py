def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)

# count binary string starting and ending with 1
def count_bin(n):
    count = 0
    for i in n:
        if i == '1':
            count += 1
    return fact(count)//(fact(count-2)*2)

# print binary string starting and ending with 1
def binarystring(string):
    indexlist = []
    for i in range(len(string)):
        if string[i] == '1':
            indexlist.append(i)
    binstrlist = []
    for i in range(len(indexlist)):
        for j in range(i+1,len(indexlist)):
            binstrlist.append( string[indexlist[i]:indexlist[j]+1])
    return binstrlist

n=input()
print(f"binary substrings are {sorted(binarystring(n),key=len)}")
print(f"binary substring count is {count_bin(n)}")

