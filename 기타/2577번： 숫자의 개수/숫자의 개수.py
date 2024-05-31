#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2577                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: sujjong456 <boj.kr/u/sujjong456>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2577                           #+#        #+#      #+#     #
#    Solved: 2024/05/16 11:19:07 by sujjong456    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

A = int(input())
B = int(input())
C = int(input())

answer = A * B * C

nums = {i: 0 for i in range(10)}

for i in str(answer):
    nums[int(i)] += 1

for i in range(10):
    print(nums[i])
