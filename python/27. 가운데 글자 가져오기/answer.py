# https://programmers.co.kr/learn/courses/30/lessons/12903

def solution(s):
    center = int(len(s)/2)
    if len(s) % 2 != 0:
        return s[center]
    else:
        return s[center-1:center+1]

# 틀린답
# import statistics
# def solution(s):
#     answer = []
    
#     if len(s)%2 == 0:
#         return statistics.median(list(s))
#         # return answer.append(s[len(s)//2]), answer.append(s[(len(s)//2-1)])
#     else:
#         return statistics.median(list(s))
#     return answer