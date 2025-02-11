'''
a = 10
b = 20

print(a * b)
print(a / b)
print(a // b)
print(a % b)

print(-10//3) # 向下取整

# += -= *= /=  %=  //=
# /0 %0 程序直接崩溃

s = 0
s = s + 1
print(s)
s = s + 2
print(s)

# 表达式
x = 2 + 3
y = (x + 1.0) * 5

print(x , y)

s =-12.9
a = float(s)
b = int(s)
print(s,a,b) #小数点后面直接抹掉

s2 = "the value is " + str(b)
print(s2)
'''

# 输入
# s1 = input()

'''
a , b = map(int, input().split())
print(a+b)
'''

a=1
b=2
c=3
# 输出
print(a,b,c)
print(a,end=' ')
print(b,end='！')
print(c)

x=1.29089
y=100.000
print("x = "+ str(round(x,3)))
print("y = %.3f" % (x*y) )
