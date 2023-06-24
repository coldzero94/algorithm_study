def solution(n, lost, reserve):
    set_reserve = set(reserve)-set(lost)
    set_lost = set(lost)-set(reserve)
    for i in set_reserve:
        if i-1 in set_lost:
            set_lost.remove(i-1)
        elif i+1 in set_lost:
            set_lost.remove(i+1)
    return n-len(set_lost)
# def solution(n, lost, reserve):
#     count_num = 0
#     del_list = []
#     for i in range(len(lost)):
#         for l in range(len(reserve)):
#             if lost[i]+1 == reserve[l]:
#                 del_list.append(lost[i])
#     for x in range(len(del_list)):
#         lost.remove(del_list[x])
#     answer = n - len(lost)
    
#     return answer

print(solution(4,[3],[2]))