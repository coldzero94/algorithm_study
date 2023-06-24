#https://programmers.co.kr/learn/courses/30/lessons/42889

def solution(N, stages):
    People = len(stages)
    faillist = {}
    for i in range(1, N + 1):
        if People != 0:
            faillist[i] = stages.count(i) / People
            People -= stages.count(i)
        else:
            faillist[i] = 0

    return sorted(faillist, key=lambda i: faillist[i], reverse=True)