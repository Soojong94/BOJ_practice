#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 26069                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: sujjong456 <boj.kr/u/sujjong456>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/26069                          #+#        #+#      #+#     #
#    Solved: 2024/05/08 09:59:16 by sujjong456    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

N = int(input())
person_set = set(["ChongChong"])

for i in range(N):
    a, b = input().split()

    if a in person_set:
        person_set.add(b)
    if b in person_set:
        person_set.add(a)

print(len(person_set))
