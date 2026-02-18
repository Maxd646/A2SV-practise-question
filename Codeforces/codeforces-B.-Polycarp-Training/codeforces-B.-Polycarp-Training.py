# B. Polycarp Training
# Platform: Codeforces

count= 0
n= int(input())
arra= list(map(int, input().split()))
arra.sort()
summ=0
for j in range(len(arra)):
    if arra[j]>summ:
        summ+=1
        count+=1
print(count)
