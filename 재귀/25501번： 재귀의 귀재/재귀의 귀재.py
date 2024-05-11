#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 25501                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: sujjong456 <boj.kr/u/sujjong456>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/25501                          #+#        #+#      #+#     #
#    Solved: 2024/05/11 20:53:18 by sujjong456    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #


def recursion(s, l, r, cnt):
    if l >= r:
        return 1, cnt
    elif s[l] != s[r]:
        return 0, cnt
    else:
        cnt += 1
        return recursion(s, l + 1, r - 1, cnt)


def isPalindrome(s):
    return recursion(s, 0, len(s) - 1, 1)


T = int(input())
for i in range(T):
    word = input().rstrip()
    print(isPalindrome(word)[0], isPalindrome(word)[1])
