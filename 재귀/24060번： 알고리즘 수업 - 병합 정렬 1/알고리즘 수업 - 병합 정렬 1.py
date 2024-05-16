#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 24060                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: sujjong456 <boj.kr/u/sujjong456>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/24060                          #+#        #+#      #+#     #
#    Solved: 2024/05/12 11:59:57 by sujjong456    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #


def merge_sort(A, start, end):
    if start < end:
        mid = (start + end) // 2
        merge_sort(A, start, mid)
        merge_sort(A, mid + 1, end)
        merge(A, start, mid, end)


def merge(A, start, mid, end):
    global cnt, answer
    tmp = [0] * (end - start + 1)
    i, j, k = start, mid + 1, 0

    while i <= mid and j <= end:
        if A[i] <= A[j]:
            tmp[k] = A[i]
            k += 1
            i += 1
        else:
            tmp[k] = A[j]
            k += 1
            j += 1

    while i <= mid:
        tmp[k] = A[i]
        k += 1
        i += 1

    while j <= end:
        tmp[k] = A[j]
        k += 1
        j += 1

    i, k = start, 0
    while i <= end:
        A[i] = tmp[k]
        cnt += 1
        if cnt == K:
            answer = A[i]
            break
        i += 1
        k += 1


A, K = map(int, input().split())
lst = list(map(int, input().split()))
cnt = 0
answer = -1
merge_sort(lst, 0, A - 1)
print(answer)
