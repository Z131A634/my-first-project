# 斐波那契（while）


# for  range使用
"""
for i in range(0,10): #左闭右开
    print(i, end=' ')

print()

s = 0
for i in range(1,101):
    s += i ** 3

print(s)
"""

n = int(input())

is_prime = True
for i in range(2,n):
    if n % i == 0:
        is_prime = False
        break

if is_prime:
    print("yes")
else:
    print("no")

