#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 24416                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: sujjong456 <boj.kr/u/sujjong456>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/24416                          #+#        #+#      #+#     #
#    Solved: 2024/06/09 15:46:00 by sujjong456    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #


def fib(n):
    if n == 1 or n == 2:
        return 1, 1
    else:
        fib1, cnt1 = fib(n - 1)  
        fib2, cnt2 = fib(n - 2)  
        return fib1 + fib2, cnt1 + cnt2 


def fibonacci(n):
    if n == 1 or n == 2:
        return 1, 0 
    f = [0] * (n + 1)
    f[1], f[2] = 1, 1
    count = 0  
    for i in range(3, n + 1):
        f[i] = f[i - 1] + f[i - 2]
        count += 1  
    return f[n], count
  
N =  int(input())

print(fib(N)[1], fibonacci(N)[1])

#------------------------------------

# n = int(input())
# dp = [0] * 41
# dp[1] = 1
# dp[2] = 1
# cnt = 0

# for i in range(3, n+1):
#     dp[i] = dp[i-1] + dp[i-2]
#     cnt += 1

# print(dp[n], cnt)




