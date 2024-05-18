#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 8958                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: sujjong456 <boj.kr/u/sujjong456>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/8958                           #+#        #+#      #+#     #
#    Solved: 2024/05/18 21:15:06 by sujjong456    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

N = int(input())

for i in range(N):
    cnt = 0
    answer = 0
    letter = input()
    for j in range(len(letter)):
        if letter[j] == "O":
            cnt += 1
            answer += cnt
        else:
            cnt = 0
    print(answer)
