#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1874                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: sujjong456 <boj.kr/u/sujjong456>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1874                           #+#        #+#      #+#     #
#    Solved: 2024/06/01 11:13:34 by sujjong456    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
from collections import deque

n = int(input())

numbers = [i for i in range(1, n + 1)]

order = []

for i in range(n):
    order.append(int(input()))

que = deque()

print(numbers, order)
