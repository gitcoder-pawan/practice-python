
def facsum(n) :
    if(n == 1):
       return 1
    result = 0
    i=2
    while(i*i<=n) :
        # print(f'{i} times {result}')
        if (n % i == 0) :
            if (i == (n/i)) :
                result = result + i
            else :
                result = result + (i + n//i)
        i+=1
    return result+n+1
        
def maxsubsetsum(arr):
    for i in arr:
        print(facsum(i))

n =int(input())
arr=[int(input()) for i in range(n)]
maxsubsetsum(arr)
