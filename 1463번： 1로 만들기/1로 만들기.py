#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1463                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: sujjong456 <boj.kr/u/sujjong456>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1463                           #+#        #+#      #+#     #
#    Solved: 2024/06/07 17:20:35 by sujjong456    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #


def makeOne(N):
    if N == 1:
        return 0
    cnt = 1
    if N % 3 == 0:
        return cnt + makeOne(N // 3)
    elif N % 2 == 0:
        return cnt + makeOne(N // 2)
    else:
        return cnt + makeOne(N - 1)


print(makeOne(int(input())))
