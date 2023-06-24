# https://velog.io/@qmasem/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-3%EC%A7%84%EB%B2%95-%EB%92%A4%EC%A7%91%EA%B8%B0-Python
def solution(n):
    answer = ''

    while n > 0:			
        n, re = divmod(n,3)	# n을 3으로 나눈 몫과 나머지
        answer += str(re)
    return int(answer, 3)