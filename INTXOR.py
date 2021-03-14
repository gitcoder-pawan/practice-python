def bin2dec(n):
    return bin(n).replace("0b", "")
t=input()
for i in range(int(t)):
    n = input()
    n = int(n)
    d = len(bin2dec(n))
    a = 2 ** (d - 1) - 1
    b = a ^ n
    print(a * b)

