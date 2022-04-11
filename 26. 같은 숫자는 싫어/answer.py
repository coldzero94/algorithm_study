# https://programmers.co.kr/learn/courses/30/lessons/12906

def solution(arr):
    answer = []
    answer.append(arr[0])
    
    for i in range(1, len(arr)):  
        if arr[i-1] != arr[i]:
          answer.append(arr[i])

    return answer

# 틀린답
# def solution(arr):
#     answer = []
#     check_num = len(arr)-2
#     last_num = len(arr)-1
#     for i in range(len(arr)):
#         if i == (len(arr)-1):
#             break
#         if arr[i] != arr[i+1]:
#             answer.append(arr[i])
#     if arr[check_num] != arr[last_num]:
#         answer.append(arr[last_num])
#     if arr[check_num-1] != arr[check_num]:
#         answer.append(arr[check_num])
#     return answer

print(solution([1,1,1,5,5,1,1,9]))
