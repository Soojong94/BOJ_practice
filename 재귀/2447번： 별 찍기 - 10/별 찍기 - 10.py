#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2447                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: sujjong456 <boj.kr/u/sujjong456>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2447                           #+#        #+#      #+#     #
#    Solved: 2024/05/14 10:01:04 by sujjong456    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

# 가운데 정사각형의 크기 = N // 3 * N // 3
# 둘러싼 패턴의 크기 N // 3
# N 이 1일때 별 생성 lst 로 담아서 join 출력
# i 에는 N = 3 일 때의 패턴이 담김

N = int(input())


def star(N):
    if N == 1:
        return ["*"]

    stars = star(N // 3)
    lst = []

    for i in stars:
        lst.append(i * 3)
    for i in stars:
        lst.append(i + " " * (N // 3) + i)
    for i in stars:
        lst.append(i * 3)

    return lst


print("\n".join(star(N)))
