#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 18110                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: sujjong456 <boj.kr/u/sujjong456>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/18110                          #+#        #+#      #+#     #
#    Solved: 2024/05/28 09:05:40 by sujjong456    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
n = int(input())

score = []

for i in range(n):
    score.append(int(input()))

score.sort()


def roundUp(num):
    if (num - int(num)) >= 0.5:
        return int(num) + 1
    else:
        return int(num)


cut = roundUp(n * 0.15)
sum_num = sum(score[cut : n - cut])

if sum_num == 0:
    print(0)
else:

    print(roundUp(sum_num / (n - (2 * cut))))
