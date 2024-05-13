#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 4779                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: sujjong456 <boj.kr/u/sujjong456>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/4779                           #+#        #+#      #+#     #
#    Solved: 2024/05/13 11:02:48 by sujjong456    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #


# 0 과 1로 치환해서 리스트를 구한 다음 for문으로 0일 시에는 공백 출력, 1일 시에는 '-' 출력


def cantor_set(N):
    if N == 0:
        return "-"
    else:
        prev_set = cantor_set(N - 1)
        return prev_set + " " * len(prev_set) + prev_set


def generate_cantor_set(N):
    set_length = 3**N
    cantor_string = cantor_set(N)
    return cantor_string[:set_length]


nums = []

while True:
    try:
        num = input()
        nums.append(int(num))
    except:
        break

for i in nums:
    print(generate_cantor_set(i))
