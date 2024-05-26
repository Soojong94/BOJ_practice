#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1676                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: sujjong456 <boj.kr/u/sujjong456>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1676                           #+#        #+#      #+#     #
#    Solved: 2024/05/26 12:16:44 by sujjong456    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import math

n = int(input())
fac_num = str(math.factorial(n))
cnt = 0


for char in reversed(fac_num):
    if char == '0':
        cnt += 1
    else:
        break

print(cnt)

      
