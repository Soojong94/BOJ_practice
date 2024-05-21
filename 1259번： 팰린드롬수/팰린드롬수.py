#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1259                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: sujjong456 <boj.kr/u/sujjong456>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1259                           #+#        #+#      #+#     #
#    Solved: 2024/05/21 08:49:32 by sujjong456    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

while True:
    N = input()
    if N == "0":
        break

    isCheck = True

    for i in range(len(N) // 2):
        if N[i] != N[-i - 1]:
            isCheck = False
            break

    if isCheck:
        print("yes")
    else:
        print("no")
