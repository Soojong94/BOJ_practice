#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2579                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: sujjong456 <boj.kr/u/sujjong456>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2579                           #+#        #+#      #+#     #
#    Solved: 2024/06/08 19:59:40 by sujjong456    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

N = int(input())
floor_lst = []

for i in range(N):
    floor_lst.append(int(input()))

def make_max(lst=[]) :
    if len(lst) == 0:
        return 0
    elif len(lst) == 1:
        return lst[0]
    elif len(lst) == 2:
        return lst[0] + lst[1]

    dp = [0] * len(lst)
    dp[0] = lst[0]
    dp[1] = lst[0] + lst[1]
    dp[2] = max(lst[0] + lst[2], lst[1] + lst[2])
    
    
    # 최종 경우의 수는 두개밖에 없음(두칸 올라오던지 / 한칸 올라오던지  : 이 경우에는 세칸 밑도 구해줘야 함-이 경우보다 큰 값은 없기 때문에 결국 두개만 비교하면 됨)
    for i in range(3, len(lst)):
        dp[i] = max(dp[i-2] + lst[i], dp[i-3] + lst[i-1] + lst[i])

    return dp[-1]

print(make_max(floor_lst))