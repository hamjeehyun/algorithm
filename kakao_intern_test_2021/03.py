def solution(n, k, cmd):
    arr=['O']*n
    del_list=[]
    index=0

    while index < len(cmd):  
        print('k', k)
        print(cmd[index])
        
        if cmd[index][0]=='D':
            # X 가 있으면 건너뛰기
            
            dis = 0 # 이동한 거리
            i=0 # 실제 이동한 거리

            # 한칸씩 이동 할 때마다 X인지 확인
            while True:
                # 이동한 거리 = 이동할 거리
                if dis == int(cmd[index][-1]):
                    break

                i += 1
                if arr[k+i] == 'O':
                    dis += 1
            k += i
            index+=1
            
        elif cmd[index][0]=='U':
            # X 가 있으면 건너뛰기
            dis = 0 # 이동한 거리
            i=0 # 실제 이동한 거리

            # 한칸씩 이동 할 때마다 X인지 확인
            while True:
                # 이동한 거리 = 이동할 거리
                if dis == int(cmd[index][-1]):
                    break

                i += 1
                
                if arr[k-i] == 'O':
                    dis += 1

            k -= i
            index+=1

        elif cmd[index][0]=='C':
            arr[k]='X'
            del_list.append(k)
            index+=1

            if 'O' in arr:
                while True:
                    if k == n-1:
                        k -= 1
                        if arr[k]=='O':
                            break
                
                    else:
                        k += 1
                        if arr[k]=='O':
                            break

        elif cmd[index][0]=='Z':
            undo_index=del_list.pop()
            arr[undo_index]='O'
            index+=1
        
        print('arr', arr)
        print("----------")

    print(''.join(arr))
            
    answer = ''
    return answer

solution(5, 0, ["C", "C", "C", "C", "C"])