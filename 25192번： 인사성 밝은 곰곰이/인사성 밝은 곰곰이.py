#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 25192                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: sujjong456 <boj.kr/u/sujjong456>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/25192                          #+#        #+#      #+#     #
#    Solved: 2024/05/08 09:01:42 by sujjong456    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #


N = int(input())
str_lst = []
cnt = 0

for _ in range(N):
    str_lst.append(input())

for i in range(len(str_lst)):
    if str_lst[i] == "ENTER":
        str_lst_set = set()
        j = i + 1
        while j < len(str_lst) and str_lst[j] != "ENTER":
            str_lst_set.add(str_lst[j])
            j += 1
        cnt += len(str_lst_set)
print(cnt)


# ENTER를 기준으로 split 해서 set 에 담고 count 하는 방법도 가능
# -> 이렇게 하면 for문 하나 줄어듬
