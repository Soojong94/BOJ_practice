#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2475                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: sujjong456 <boj.kr/u/sujjong456>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2475                           #+#        #+#      #+#     #
#    Solved: 2024/05/20 13:34:00 by sujjong456    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

nums = list(map(int, input().split()))
answer = 0

for i in nums:
    answer += i**2

print(answer % 10)
