def solution(ss):
    arr=['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'] 
    s=list(ss) 
    answer = []
    index=0
    
    while index < len(s):
        # isdigit->숫자면 true
        if s[index].isdigit():
            answer.append(s[index])
            index+=1
            
        else:
            if ss[index:index+len('zero')]=='zero':
                answer.append('0')
                index += len('zero')
            
            elif ss[index:index+len('one')]=='one':
                answer.append('1')
                index += len('one')
                
            elif ss[index:index+len('two')]=='two':
                answer.append('2')
                index += len('two')
            
            elif ss[index:index+len('three')]=='three':
                answer.append('3')
                index += len('three')
            
            elif ss[index:index+len('four')]=='four':
                answer.append('4')
                index += len('four')
            
            elif ss[index:index+len('five')]=='five':
                answer.append('5')
                index += len('five')
                
            elif ss[index:index+len('six')]=='six':
                answer.append('6')
                index += len('six')
                
            elif ss[index:index+len('seven')]=='seven':
                answer.append('7')
                index += len('seven')
                
            elif ss[index:index+len('eight')]=='eight':
                answer.append('8')
                index += len('eight')
                
            elif ss[index:index+len('nine')]=='nine':
                answer.append('9')
                index += len('nine')

    result=int("".join(answer))
    print(result)
    return result

s=input()
solution(s)