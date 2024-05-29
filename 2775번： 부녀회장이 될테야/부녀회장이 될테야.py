#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2775                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: sujjong456 <boj.kr/u/sujjong456>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2775                           #+#        #+#      #+#     #
#    Solved: 2024/05/29 17:45:49 by sujjong456    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

# k 층 n 호 -> k-1 층 n호까지의 합
# n호까지의 합 = (k-1)[0] + ... + (k-1)[n-1]
# (k-2)[0] + (k-2)[1] + (k-2)[n-1]

import sys

def input():
    return sys.stdin.readline()

memo = {}

def people(k, n):
    
    if (k, n) in memo:
        return memo[(k, n)]
    
    cnt = 0
    if k == 0:
        return n
    elif n == 1:
        return 1
    else:
        for i in range(1, n + 1):
            cnt += people(k - 1, i)
        

        memo[(k, n)] = cnt
        return cnt

T = int(input())
for i in range(T):
    k = int(input())
    n = int(input())
    print(people(k, n))
