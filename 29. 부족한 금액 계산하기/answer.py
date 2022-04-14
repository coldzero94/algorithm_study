# https://programmers.co.kr/learn/courses/30/lessons/82612

def solution(price, money, count):
    
    new_price = 0
    for i in range(1,count+1):
        new_price += price*i
    if money >= new_price:
        answer = 0
    else:
        answer = new_price - money

    return answer

print(solution(3,20,4))
