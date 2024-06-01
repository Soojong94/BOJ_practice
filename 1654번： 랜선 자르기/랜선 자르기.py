#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1654                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: sujjong456 <boj.kr/u/sujjong456>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1654                           #+#        #+#      #+#     #
#    Solved: 2024/06/01 10:39:44 by sujjong456    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

# 가지고 있는 랜선의 개수 = K
# 만들어야 하는 랜선의 개수 = N
# 최대 길이로, N개의 랜선을 만들어야 함

import sys


def input():
    return sys.stdin.readline()


K, N = map(int, input().split())

numbers = []

for i in range(K):
    numbers.append(int(input()))

# 입력된 수 중 가장 작은 수를 기준으로 나눠보고 개수가 N 과 일치하는지 확인
# 일치하지 않는다면 나누는 수를 올리거나 낮추기

start, end = 1, max(numbers)

result = 0
while start <= end:
    mid = (start + end) // 2
    cnt = sum(number // mid for number in numbers)

    if cnt >= N:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)
