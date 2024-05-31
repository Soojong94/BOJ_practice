#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 10828                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: sujjong456 <boj.kr/u/sujjong456>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/10828                          #+#        #+#      #+#     #
#    Solved: 2024/05/23 08:56:19 by sujjong456    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
from collections import deque
import sys


def input():
    return sys.stdin.readline()


N = int(input())
nums = deque()

for i in range(N):
    order = list(input().split())
    if order[0] == "push":
        nums.append(order[1])
    elif order[0] == "pop":
        if nums:
            print(nums.pop())
        else:
            print(-1)
    elif order[0] == "size":
        print(len(nums))
    elif order[0] == "empty":
        if nums:
            print(0)
        else:
            print(1)
    elif order[0] == "top":
        if nums:
            print(nums[-1])
        else:
            print(-1)
