def solution(s):
    # answer = True
    s_list = list(s)
    for i in range(len(s_list)):
        if not s_list[i].isdigit():
            return False
        return True
    # return answer