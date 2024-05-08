#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2108                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: sujjong456 <boj.kr/u/sujjong456>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2108                           #+#        #+#      #+#     #
#    Solved: 2024/05/08 11:09:18 by sujjong456    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys


def input():
    return sys.stdin.readline()


N = int(input())
nums = list(int(input()) for _ in range(N))
nums.sort()

print(round(sum(nums) / N))
print(nums[N // 2])

nums_dict = {i: 0 for i in nums}
for num in nums:
    nums_dict[num] += 1

max_num = max(nums_dict.values())
max_nums = []

for key, value in nums_dict.items():
    if value == max_num:
        max_key = key
        max_nums.append(key)

if len(max_nums) > 1:
    print(max_nums[1])
else:
    print(max_nums[0])

print(nums[-1] - nums[0])
