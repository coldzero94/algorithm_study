
   
# 하샤드 수

## 문제 설명

양의 정수 x가 하샤드 수이려면 x의 자릿수의 합으로 x가 나누어져야 합니다. 예를 들어 18의 자릿수 합은 1+8=9이고, 18은 9로 나누어 떨어지므로 18은 하샤드 수입니다. 자연수 x를 입력받아 x가 하샤드 수인지 아닌지 검사하는 함수, solution을 완성해주세요.

## 제한 조건

- x는 1 이상, 10000 이하인 정수입니다.
## 입출력 예

|arr|return|
|----|----|
|10|True|
|12|True|
|11|False|
|13|False|
----

## 문제 접근 로그
1. 문자열로 변환시킨뒤 슬라이싱하고
2. 다시 정수로 바꿔서 더해주는 방식으로 해결하였다.
3. 

## 추가 공부가 필요한 사항
1. 코드 간소화

## 문제 url
https://programmers.co.kr/learn/courses/30/lessons/12947?language=python3