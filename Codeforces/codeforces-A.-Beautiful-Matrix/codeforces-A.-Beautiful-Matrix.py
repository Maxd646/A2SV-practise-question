# A. Beautiful Matrix
# Platform: Codeforces
t= list(map(int, input().split()))
t1= list(map(int, input().split()))
t2=list(map(int, input().split()))
t3= list(map(int, input().split()))
t4= list(map(int, input().split()))
marix= [t, t1, t2, t3, t4]
found= False
for i in range(5):
    for j in range(5):
        if marix[i][j] == 1:
            found= True
            print(abs(i-2)+abs(j-2))
            break
    if found:
        break
