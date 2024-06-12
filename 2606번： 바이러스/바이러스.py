#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2606                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: sujjong456 <boj.kr/u/sujjong456>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2606                           #+#        #+#      #+#     #
#    Solved: 2024/06/12 18:13:21 by sujjong456    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
from collections import deque


N = int(input())  
T = int(input())  


lst = [[] for _ in range(N+1)]
for _ in range(T):
    a, b = map(int, input().split())
    lst[a].append(b)
    lst[b].append(a)


def bfs(start):
    visited = [False] * (N + 1)  
    queue = deque([start]) 
    visited[start] = True 
    count = 0 
    
    while queue: 
        node = queue.popleft() 
        for neighbor in lst[node]:  
            if not visited[neighbor]:  
                visited[neighbor] = True  
                queue.append(neighbor)  
                count += 1  
    return count  


result = bfs(1)
print(result)

