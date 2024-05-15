#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 11729                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: sujjong456 <boj.kr/u/sujjong456>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/11729                          #+#        #+#      #+#     #
#    Solved: 2024/05/14 12:36:09 by sujjong456    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

# 실행하면 cnt += 1 / 실행 과정 print
# 3개의 장대 <> 기존 숫자보다 큰 숫자는 리스트에 들어올 수 없는 조건식
# 장대는 dictionary key 값으로 1,2,3 // value 로 list 생성하고 움직이도록 설정

# 단순하게 value에 접근하는 변수를 3개 만들어서 각각 어떤 식으로 진행되는지 적어보기

# n-1 개의 원판을 2번 장대로 옮기고 그걸다시 3번으로 옮기면 됨
# 이동횟수는 2**N-1

N = int(input())


def move(N, start, end, assist):
    if N == 1:
        print(start, end)
        return
    else:
        move(N - 1, start, assist, end)
        print(start, end)
        move(N - 1, assist, end, start)


print(2**N - 1)
move(N, 1, 3, 2)
