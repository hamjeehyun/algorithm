str_=input()
str_upper = str_.upper()
str_arr = {}

for s in str_upper:
    if s in str_arr:
        continue
    else:
        str_arr[s] = 0

for s in str_upper:
    str_arr[s] += 1

str_max = [k for k, v in str_arr.items() if max(str_arr.values()) == v]

if len(str_max) > 1:
    print("?")
else:
    print(str_max[0])