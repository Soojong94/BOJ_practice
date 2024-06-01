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

numbers = deque()
order = deque()
que = deque()


for i in range(1, n + 1):
    numbers.append(i)


for i in range(n):
    order.append(int(input()))


plus_minus = []

# 오름차순으로 큐에 넣고, order에 주어진 순서대로 수열을 만들 수 있는지 확인해야 함

print(numbers, order)

while True:
    for i in order:
        if que:
            if que[-1] == i:
                que.pop()
                plus_minus.append("-")
            else:
                que.append(numbers.popleft())
                plus_minus.append("+")
        else:
            que.append(numbers.popleft())
            plus_minus.append("+")
