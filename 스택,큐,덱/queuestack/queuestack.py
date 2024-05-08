# 스택일 경우, last in first out -> 들어간 숫자 그대로 pop
# queue일 경우, 새로운 숫자 들어감 -> 기존 숫자 pop
# 스택일 경우에는 생각 안해도 됨. 1입력받으면 숫자를 queue 에 추가 하고, M만큼 appendleft 한 뒤에 pop()해서 출력

import sys
from collections import deque


def input():
    return sys.stdin.readline()


N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
M = int(input())
C = list(map(int, input().split()))

q = deque()

for i in range(N):
    if A[i] == 0:
        q.append(B[i])

for j in range(M):
    q.appendleft(C[j])
    print(q.pop(), end=" ")
