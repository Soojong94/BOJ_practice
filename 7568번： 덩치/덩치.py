#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 7568                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: sujjong456 <boj.kr/u/sujjong456>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/7568                           #+#        #+#      #+#     #
#    Solved: 2024/05/27 09:45:21 by sujjong456    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

# 
import sys

def input() :
  return sys.stdin.readline()

N = int(input())
people = []

for i in range(1 , N+1) :
  p, q = map(int, input().split())
  people.append([i, p, q, 1])

for i in range(N) :
  rank = 1
  for j in range(N):
    if i != j and people[i][1] < people[j][1] and people[i][2] < people[j][2] :
      rank += 1
  people[i][3] = rank

people.sort(key=lambda x : x[0])

for i in range(N) :
  print(people[i][3], end = ' ')


