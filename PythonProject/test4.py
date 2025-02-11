"""
year = int(input())

if(year % 100 == 0):
    if(year % 400 == 0):
        print("yes")
    else:print("no")
else:
    if(year % 4 == 0):
        print("no")

a, b = map(int, input().split())

if(a > b):
    max_value = a
else:
    max_value = b
print(max_value)
"""
# max_value = a if a > b else b

"""
status = int(input())

match status:
    case 400:
        print("Bad request")
    case 404:
        print("Not found")
    case 418 | 420 | 422 | 400:
        print("I'm a teapot")
    case _:
        print("Something's wrong with the internet")
"""


