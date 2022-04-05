# https://programmers.co.kr/learn/courses/30/lessons/12910

def solution(arr, divisor):
    answer = []
    for i in range(len(arr)):
        if i != (len(arr)):
            if arr[i]%divisor==0:
                answer.append(arr[i])
            continue
        if i == (len(arr)):
            break
    if len(answer)==0:
        answer.append(-1)
    answer.sort()
    return answer

print(solution([5, 9, 7, 10],5))
a = []
print(len(a))