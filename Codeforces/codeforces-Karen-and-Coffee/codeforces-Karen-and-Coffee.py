# Karen and Coffee
# Platform: Codeforces
a , b , c = list(map(int, input().split()))
r= 200005
arr = [0] *r
for _ in range(a):
    x , y = list(map(int , input().split()))
    arr[x] += 1
    arr[y + 1]-= 1
for i in range(1 , r):
    arr[i] += arr[i - 1]
f = [0] * r
for t in range(r):
    if arr[t] >= b :
        f[t] += 1
for t in range(1 , r):
    f[t] +=f[t - 1]
for g in range(c):
    x, y = list(map(int , input().split()))
    print(f[y] - f[x - 1])
    
