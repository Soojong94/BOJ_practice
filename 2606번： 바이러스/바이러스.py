#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2606                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: sujjong456 <boj.kr/u/sujjong456>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2606                           #+#        #+#      #+#     #
#    Solved: 2024/06/12 18:13:21 by sujjong456    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

T = int(input())
link = [[] for _ in range(T)]

for i in range(T):
    link[i] = list(map(int, input().split()))

number = []

for i in range(T):
    if 1 in link[i]:
        number.append(link[i][0])
        number.append(link[i][1])

for j in number:
    if j in link[i]:
        number.append(link[i][0])
        number.append(link[i][1])
