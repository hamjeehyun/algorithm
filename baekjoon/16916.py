

S=input()
P=input()

s_index=0
p_index=0

while s_index < len(S)-1 and p_index < len(P)-1:
    
    if S[s_index] == P[p_index]:
        s_index += 1
        p_index += 1
    else:
        s_index += 1
        p_index =0

if p_index == len(P)-1:
    print("1")
else:
    print("0")