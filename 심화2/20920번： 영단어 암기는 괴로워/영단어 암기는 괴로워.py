#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 20920                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: sujjong456 <boj.kr/u/sujjong456>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/20920                          #+#        #+#      #+#     #
#    Solved: 2024/05/08 16:31:31 by sujjong456    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys


def input():
    return sys.stdin.readline()


# 입력 받기
N, M = map(int, input().split())

# 단어와 빈도를 저장할 딕셔너리(시간 줄이기 위한 코드)
word_count = {}

# 단어의 빈도를 계산
words = []
for _ in range(N):
    word = input().rstrip()
    if len(word) >= M:
        words.append(word)
        word_count[word] = (
            word_count.get(word, 0) + 1
        )  # 초기값 0으로 설정하고 등장할 때마다 +1

# 중복된 단어 제거하고 빈도, 길이, 알파벳 순으로 정렬
sorted_words = sorted(set(words), key=lambda x: (-word_count[x], -len(x), x))

# 출력
for i, word in enumerate(sorted_words):
    if i == len(sorted_words) - 1:
        print(word, end="")
    else:
        print(word)
