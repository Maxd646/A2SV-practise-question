for _ in range(int(input())):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = int(input())
    stack =[]
    found =False
    for i in range(len(a)):
        if not stack:
            stack.append(min(a[i], b-a[i]))
        else:
            if a[i] == stack[-1]:
                stack.append(a[i])
            elif a[i]<stack[-1] and stack[-1]>b-a[i]:
                print("NO")
                found =True
                break
            elif a[i]>=stack[-1] and b-a[i]>=stack[-1]:
                stack.append(min(a[i], b-a[i]))
            else:
                stack.append(max(a[i], b-a[i]))
    if not found:
        print("YES")