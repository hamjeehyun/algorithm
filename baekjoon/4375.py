while True:
    try:
        n=int(input())
        arr=[0]*n

        for i in range(n):
            M=(arr[i]*10+1)%n
            if M==0:
                print(i+1)
                break
            arr[i+1] = (arr[i]*10+1)%n
    except:
        break