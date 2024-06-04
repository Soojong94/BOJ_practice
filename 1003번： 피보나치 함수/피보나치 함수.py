#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1003                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: sujjong456 <boj.kr/u/sujjong456>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1003                           #+#        #+#      #+#     #
#    Solved: 2024/06/04 08:57:01 by sujjong456    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #


import sys

input = sys.stdin.readline


def fibonacci(n, memo):
    if n in memo:
        return memo[n]

    if n == 0:
        memo[0] = (1, 0)
        return memo[0]
    elif n == 1:
        memo[1] = (0, 1)
        return memo[1]
    else:
        a = fibonacci(n - 1, memo)
        b = fibonacci(n - 2, memo)
        memo[n] = (a[0] + b[0], a[1] + b[1])
        return memo[n]


T = int(input())
for i in range(T):
    n = int(input())
    memo = {}
    cnt0, cnt1 = fibonacci(n, memo)
    print(cnt0, cnt1)
