#https://programmers.co.kr/learn/courses/30/lessons/68644
def solution(numbers):
    answer = set()
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            answer.add(numbers[i] + numbers[j])
    answer = list(answer)
    answer.sort()
    return answer
# def solution(numbers):
#     answer = []
#     for i in range(len(numbers)):
#         for x in range(len(numbers)-1):
#             answer.append(numbers[i] + numbers[x+1])
#     answer = sorted(list(set(answer)))
#     return answer

print(solution([5, 0, 2, 7]))