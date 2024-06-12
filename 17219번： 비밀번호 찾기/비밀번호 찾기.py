#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 17219                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: sujjong456 <boj.kr/u/sujjong456>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/17219                          #+#        #+#      #+#     #
#    Solved: 2024/06/12 22:55:59 by sujjong456    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
N, M = map(int, input().split())
lst = dict()

for _ in range(N):
    site, password = map(str, input().split())
    lst[site] = password

for _ in range(M):
    site = input()
    print(lst[site])

