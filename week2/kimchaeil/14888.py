#14888번 문제 (연산자 끼워넣기)
#백트래킹 DFS(깊이우선탐색)를 이용하였다

import sys

maximum = -1e9 #결과의 최소값이 -10억(-1e9)
minimum = 1e9 #결과의 최대값이 10억(1e9)

def DFS(depth, result, plus, minus, multiply,devide):
    if depth == N:
        global maximum,minimum
        maximum = max(result,maximum)
        minimum = min(result,minimum)
        return
    if plus:DFS(depth+1,result+A[depth],plus-1,minus,multiply,devide)
    if minus:DFS(depth+1,result-A[depth],plus,minus-1,multiply,devide)
    if multiply:DFS(depth+1,result*A[depth],plus,minus,multiply-1,devide)
    if devide:DFS(depth+1,int(result/A[depth]),plus,minus,multiply,devide-1)
    #int(A/B)와 A//B는 음수/양수 or 양수/음수일때 결과의 차이가 있음
    #int()는 소수점을 버리고 //는 소수점을 내리기 때문(ex. int(-1/2) = int(-0.5) = 0, -1//2 = floor(-0.5) = -1)
    #이 문제는 C++14 기준이므로 int(A/B)를 사용

input = sys.stdin.readline

N = int(input()) #수열 A의 길이
A = list(map(int, input().split())) #수열 A
operator = list(map(int, input().split())) #연산자 개수(+,-,*,/ 순서)

DFS(1,A[0],operator[0],operator[1],operator[2],operator[3])
print(maximum) #최대값 출력
print(minimum) #최소값 출력