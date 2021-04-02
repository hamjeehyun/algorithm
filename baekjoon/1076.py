value=["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]

a=value.index(input())
b=value.index(input())
c=value.index(input())

result=int(str(a)+str(b)) * (10**c)
print(result)