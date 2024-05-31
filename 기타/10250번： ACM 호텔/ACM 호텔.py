#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 10250                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: sujjong456 <boj.kr/u/sujjong456>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/10250                          #+#        #+#      #+#     #
#    Solved: 2024/05/19 19:38:00 by sujjong456    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

T = int(input())

for i in range(T):
    H, W, N = map(int, input().split())
    num1 = N % H
    num2 = N // H + 1
    if num1 == 0:
        num1 = H
        num2 -= 1

    if num2 >= 10:
        print(str(num1) + str(num2))
    else:
        print(str(num1) + "0" + str(num2))
