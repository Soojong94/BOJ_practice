#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1010                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: sujjong456 <boj.kr/u/sujjong456>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1010                           #+#        #+#      #+#     #
#    Solved: 2024/05/06 10:38:55 by sujjong456    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import math

num = int(input())

for i in range(num):
    M, N = map(int, input().split())
    deno = math.factorial(M) * math.factorial(N - M)
    print(int(math.factorial(N) / deno))
