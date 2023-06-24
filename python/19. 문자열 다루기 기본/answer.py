def solution(s):
    if (len(s) == 4 or len(s) == 6) and s.isdigit():
        return True

    else:
        return False

# def solution(s):
#     answer = True
#     s_list = list(s)
#     for i in range(len(s_list)):
#         if not s_list[i].isdigit():
#             return False
#         return True
#     return answer
