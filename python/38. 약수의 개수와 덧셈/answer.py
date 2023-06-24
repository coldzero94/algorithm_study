#https://programmers.co.kr/learn/courses/30/lessons/77884
def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        now_count = 0
        for j in range(1, i+1):
            if i % j == 0:		
                now_count +=1
        
        if now_count % 2 == 0:
            answer += i
        else:
            answer -= i
            
    return answer

# def solution(left, right):
#     common_list = []
#     answer = 0
#     for i in range(left,right+1):
#         for x in range(1,i+1):
#             if i%x == 0:
#                 common_list.append(x)
#                 if common_list
                
#     return answer

print(solution(13,17))