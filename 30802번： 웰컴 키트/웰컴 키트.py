#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 30802                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: sujjong456 <boj.kr/u/sujjong456>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/30802                          #+#        #+#      #+#     #
#    Solved: 2024/06/05 22:53:54 by sujjong456    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import math

N = int(input())
clothes = list(map(int, input().split()))
T, P = map(int, input().split())

cnt = 0

for i in clothes:
    cnt += math.ceil(i / T)

print(cnt)
print(N // P, N % P)
