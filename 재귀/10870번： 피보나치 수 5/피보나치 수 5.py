#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 10870                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: sujjong456 <boj.kr/u/sujjong456>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/10870                          #+#        #+#      #+#     #
#    Solved: 2024/05/09 11:14:36 by sujjong456    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

<<<<<<< HEAD
N = int(input())
=======
N = int(input()) = int(input())
>>>>>>> b8c4f224c398a0c5955439acb8d2cb4383852471
num0 = 0
num1 = 1
answer_num = 1

if N == 0:
    print(0)
elif N == 1:
    print(1)

elif N >= 2:

    for i in range(1, N):
        answer_num = num0 + num1
        num0 = num1
        num1 = answer_num

    print(answer_num)
<<<<<<< HEAD
=======
num0 = 0
num1 = 1
answer_num = 1

if N == 0:
    print(0)
elif N == 1:
    print(1)

elif N >= 2:

    for i in range(1, N):
        answer_num = num0 + num1
        num0 = num1
        num1 = answer_num

    print(answer_num)
>>>>>>> b8c4f224c398a0c5955439acb8d2cb4383852471
