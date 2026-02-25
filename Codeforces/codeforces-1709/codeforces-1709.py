#  1709
# Platform: Codeforces

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    ans = []

    for i in range(n):
        for j in range(n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                ans.append([1, j + 1])

    for i in range(n):
        for j in range(n - i - 1):
            if b[j] > b[j + 1]:
                b[j], b[j + 1] = b[j + 1], b[j]
                ans.append([2, j + 1])
              
    for i in range(n):
        if a[i] > b[i]:
            temp = a[i]
            a[i] = b[i]
            b[i] = temp
            ans.append([3, i + 1])
          
    print(len(ans))
    for j in ans:
        print(*j)
