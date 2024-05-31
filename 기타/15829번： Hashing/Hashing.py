#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 15829                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: sujjong456 <boj.kr/u/sujjong456>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/15829                          #+#        #+#      #+#     #
#    Solved: 2024/05/30 19:38:59 by sujjong456    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

L = int(input())
letter = input()
letters = []

for char in letter:
    letters.append(char)


def ascii(letter):
    ascii = ord(f"{letter}")
    ascii_hash = ascii - 96
    return ascii_hash


mod = 1234567891


answer = 0

for i in range(len(letters)):
    answer = (answer + ascii(letters[i]) * (31**i)) % mod


print(answer)
