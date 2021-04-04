n=int(input())
vals=list(map(int, input().split()))
add, sub, mul, div=map(int, input().split())

min_, max_=1e9, -1e9

def calculate(index, val, add, sub, mul, div):
    global min_, max_
    if index==n:
        min_=min(val, min_)
        max_=max(val, max_)
        return
    else:
        if add:
            calculate(index+1, val+vals[index], add-1, sub, mul, div)
        if sub:
            calculate(index+1, val-vals[index], add, sub-1, mul, div)
        if mul:
            calculate(index+1, val*vals[index], add, sub, mul-1, div)
        if div:
            calculate(index+1, int(val/vals[index]), add, sub, mul, div-1)
    
calculate(1, vals[0], add, sub, mul, div)
print(max_)
print(min_)