def solution(s, n):
    s = list(s)
    for i in range(len(s)):
        if s[i].isupper():
            s[i] = chr((ord(s[i]) - ord('A') + n) % 26 + ord('A'))
        elif s[i].islower():
            s[i] = chr((ord(s[i]) - ord('a') + n) % 26 + ord('a'))

    return "".join(s)
    
# 실패한 코드
# def solution(s, n):
#     answer = ''
#     s_list = list(s)
#     blank_list = []
#     for i in range(len(s_list)):
#         if s_list[i] == ' ':
#             blank_list.append(s_list[i])
#         else:
#             blank_list.append(ord(s_list[i]))
#     for x in range(len(s_lsit)):
#         if s_list
#     return answer
print(solution(12))


print(solution(14))