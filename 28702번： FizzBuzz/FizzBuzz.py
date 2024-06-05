#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 28702                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: sujjong456 <boj.kr/u/sujjong456>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/28702                          #+#        #+#      #+#     #
#    Solved: 2024/06/05 23:20:55 by sujjong456    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
lst = []

for i in range(3):
    value = input()
    try:
        lst.append(int(value))
    except ValueError:
        lst.append(value)

index = -1

for j in range(3):
    if isinstance(lst[j], int):
        index = j
        break

if index == 0:
    answer = lst[index] + 3

elif index == 1:
    answer = lst[index] + 2

else:
    answer = lst[index] + 1


if answer % 15 == 0:
    print("FizzBuzz")
elif answer % 5 == 0:
    print("Buzz")
elif answer % 3 == 0:
    print("Fizz")
else:
    print(answer)
