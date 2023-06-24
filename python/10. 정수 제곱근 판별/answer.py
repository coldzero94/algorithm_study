def solution(n):
    answer = 0
    for i in range(2,n):
        if n%i**2 == 0:
            answer+=(i+1)**2
        else:
            answer+=-1
    return answer

print(solution(121))