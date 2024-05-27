#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 7568                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: sujjong456 <boj.kr/u/sujjong456>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/7568                           #+#        #+#      #+#     #
#    Solved: 2024/05/27 09:45:21 by sujjong456    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

N = int(input())
people = []
cnt = 0



for i in range(N) :
  p, q = map(int, input().split())
  people.append([p,q])
  
people_sorted = sorted(people, key=lambda x : (x[0], x[1]))