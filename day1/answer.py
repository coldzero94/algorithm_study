def solution(x, n):
    answer = []
    if n == 0:
        return answer
    
    for i in range(1,n+1):
        answer.append(i*x)
    
    return answer