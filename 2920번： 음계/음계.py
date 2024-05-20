#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2920                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: sujjong456 <boj.kr/u/sujjong456>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2920                           #+#        #+#      #+#     #
#    Solved: 2024/05/18 21:31:51 by sujjong456    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #


def is_ascending(nums, index=0):
    if index == len(nums) - 1:
        return True
    if nums[index] >= nums[index + 1]:
        return False
    return is_ascending(nums, index + 1)


def is_descending(nums, index=0):
    if index == len(nums) - 1:
        return True
    if nums[index] <= nums[index + 1]:
        return False
    return is_descending(nums, index + 1)


nums = list(map(int, input().split()))

if is_ascending(nums):
    print("ascending")
elif is_descending(nums):
    print("descending")
else:
    print("mixed")
