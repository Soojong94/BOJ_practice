#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 10866                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: sujjong456 <boj.kr/u/sujjong456>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/10866                          #+#        #+#      #+#     #
#    Solved: 2024/05/25 13:46:17 by sujjong456    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

from collections import deque
import sys


def input():
    return sys.stdin.readline()


N = int(input())
que = deque()

for i in range(N):
    letters = list(input().split())
    command = letters[0]

    if command == "push_front":
        que.appendleft(letters[1])
    elif command == "push_back":
        que.append(letters[1])
    elif command == "pop_front":
        if que:
            print(que.popleft())
        else:
            print(-1)
    elif command == "pop_back":
        if que:
            print(que.pop())
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
