#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1065                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: sujjong456 <boj.kr/u/sujjong456>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1065                           #+#        #+#      #+#     #
#    Solved: 2024/05/17 12:40:25 by sujjong456    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

N = int(input())
cnt = 0

if N <= 99:
    cnt = N

else:
    cnt = 99
    for i in range(100, N + 1):
        str_N = str(i)
        if len(str_N) == 3:
            a1 = int(str_N[0]) - int(str_N[1])
            a2 = int(str_N[1]) - int(str_N[2])
            if a1 == a2:
                cnt += 1

print(cnt)
