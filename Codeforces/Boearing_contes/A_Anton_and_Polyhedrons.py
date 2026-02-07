n= int(input())
summ=0
for _ in range(n):
    t= input().strip()
    if t=="Tetrahedron":
        summ+=4
    elif t=="Cube":
        summ+=6
    elif t=="Octahedron":
        summ+=8
    elif t=="Dodecahedron":
        summ+=12
    elif t=="Icosahedron":
        summ+=20
print(summ)


    
    

