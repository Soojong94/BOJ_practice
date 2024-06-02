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

numbers = deque(range(1, n + 1))
order = deque(int(input()) for _ in range(n))

que = deque()
plus_minus = []

# 오름차순으로 큐에 넣고, order에 주어진 순서대로 수열을 만들 수 있는지 확인해야 함


for i in order:
    while True:
        if que and que[-1] == i:
            que.pop()
            plus_minus.append("-")
            break
        elif numbers:
            que.append(numbers.popleft())
            plus_minus.append("+")
        else:
            print("NO")
            exit()

print("\n".join(plus_minus))
