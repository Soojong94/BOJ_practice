#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 18111                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: sujjong456 <boj.kr/u/sujjong456>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/18111                          #+#        #+#      #+#     #
#    Solved: 2024/06/03 08:51:28 by sujjong456    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys

input = sys.stdin.readline

N, M, B = map(int, input().split())

place = []
sum_num = 0

for i in range(N):
    nums = list(map(int, input().split()))
    place.append(nums)
    sum_num += sum(nums)

max_num = (sum_num + B) // (N * M)
min_num = min(min(row) for row in place)

best_time = float("inf")
best_height = 0

# 최대 높이에서 최저 높이까지 반복
for height in range(min_num, max_num + 1):
    add_blocks = 0
    remove_blocks = 0

    for i in range(N):
        for j in range(M):
            if place[i][j] < height:
                add_blocks += height - place[i][j]
            else:
                remove_blocks += place[i][j] - height

    if remove_blocks + B >= add_blocks:
        time = remove_blocks * 2 + add_blocks
        if time <= best_time:
            best_time = time
            best_height = height

print(best_time, best_height)
