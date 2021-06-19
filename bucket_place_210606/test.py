import sys
import re
input = sys.stdin.readline

str_ = input()
only_num = re.findall("\d+", str_)
only_str = re.findall("[a-zA-Z]+", str_)

new_str_list=[]
zero_list=[]

for i in range(len(only_num)):
    if only_num[i] == '0':
        new_str_list += only_str[i]
        zero_list.append(only_str[i])
    else:
        new_str_list += only_str[i] * int(only_num[i])

count={}

for i in new_str_list:
    if i in zero_list:
        count[i]=0
    else:
        try: count[i] += 1
        except: count[i]=1

result = ''

for key, value in count.items():
    result += (key + str(value))
print(result)