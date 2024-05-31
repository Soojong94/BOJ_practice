#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1966                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: sujjong456 <boj.kr/u/sujjong456>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1966                           #+#        #+#      #+#     #
#    Solved: 2024/05/31 09:01:41 by sujjong456    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

from collections import deque
import sys


def input():
    return sys.stdin.readline()


T = int(input())  # 테스트케이스 개수

for i in range(T):
    n, m = map(int, input().split())  # n - 문서의 개수 / m - 찾을 문서의 위치
    importance = list(map(int, input().split()))  # importance - 중요도
    que = deque((j, importance[j]) for j in range(n))

    # 중요도가 높은 게 있으면 먼저 출력

    count = 0

    while que:
        currentNumber = que.popleft()  # 일단 que 에서 꺼낸 후에 비교해보기
        if any(currentNumber[1] < q[1] for q in que):
            que.append(currentNumber)  # 중요도가 더 높은 게 없을 시에만 else 로 넘어감
        else:
            count += 1  # 순서 + 1
            if currentNumber[0] == m:  # m의 위치와 일치하면 출력
                print(count)
                break
