#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 4153                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: sujjong456 <boj.kr/u/sujjong456>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/4153                           #+#        #+#      #+#     #
#    Solved: 2024/05/20 13:41:00 by sujjong456    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #


while True:
    num_list = []
    num1, num2, num3 = map(int, (input().split()))
    if num1 == num2 == num3 == 0:
        break
    else:
        num_list.append(num1)
        num_list.append(num2)
        num_list.append(num3)
        num_list.sort()

        if num_list[2] ** 2 == num_list[0] ** 2 + num_list[1] ** 2:
            print("right")
        else:
            print("wrong")
