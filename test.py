from types import resolve_bases


a=eval(input())
b=eval(input())
c=eval(input())


################ Begin  ###########

c=a%b

while c != 0:
    a=b
    b=c
    c=a%b
result=b


################## End ##############


print(result)
