#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 11050                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: sujjong456 <boj.kr/u/sujjong456>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/11050                          #+#        #+#      #+#     #
#    Solved: 2024/05/06 10:25:27 by sujjong456    ###          ###   ##.kr     #
#                                                                              #
#  *************************************************************************  #

# ** 이항계수 정리
# 서로 다른 n개의 항목에서 k 개의 항목을 선택하는 경우의 수
# 식 정리
# n! / k!(n-k)!
# factorial 은 math 에 함수가 있음 #

import math

N, K = map(int, input().split())
deno = math.factorial(K) * math.factorial(N - K)

print(int(math.factorial(N) / deno))
