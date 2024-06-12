#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 11399                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: sujjong456 <boj.kr/u/sujjong456>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/11399                          #+#        #+#      #+#     #
#    Solved: 2024/06/11 19:06:43 by sujjong456    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

# N = int(input())
# times = list(map(int, input().split()))

# times.sort()

# sums = [0] * N
# sums[0] = times[0]

# for i in range(1, N):
#     sums[i] = sums[i - 1] + times[i]

# print(sum(sums))


#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 9184                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: sujjong456 <boj.kr/u/sujjong456>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/9184                          #+#        #+#      #+#     #
#    Solved: 2024/06/11 19:06:43 by sujjong456    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

while True :
    a,b,c = map(int,input().split())
    if a == -1 and b == -1 and c == -1 :
        break
    elif a <= 0 or b <= 0 or c <= 0 :
        print(f"w({a}, {b}, {c}) = 1")
    elif a > 20 or b > 20 or c > 20 :
        