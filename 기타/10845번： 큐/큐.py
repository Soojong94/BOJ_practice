#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 10845                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: sujjong456 <boj.kr/u/sujjong456>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/10845                          #+#        #+#      #+#     #
#    Solved: 2024/05/24 09:01:21 by sujjong456    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
from collections import deque
import sys


def input():
    return sys.stdin.readline()


que = deque()

N = int(input())
for i in range(N):
    words = list(input().split())
    command = words[0]
    if command == "push":
        que.append(words[1])
    elif command == "pop":
        if que:
            print(que.popleft())
        else:
            print(-1)
    elif command == "size":
        print(len(que))
    elif command == "empty":
        if que:
            print(0)
        else:
            print(1)
    elif command == "front":
        if que:
            print(que[0])
        else:
            print(-1)
    elif command == "back":
        if que:
            print(que[-1])
        else:
            print(-1)
