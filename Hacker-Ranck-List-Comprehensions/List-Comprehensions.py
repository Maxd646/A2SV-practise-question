if __name__ == '__main__':
    
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    result= [[i,j,k] for k in range(z+1) for j in range(y+1) for i in range(x+1)]
    newnew=[]
    for num in result:
        if sum(num)!=n:
            newnew.append(num)
    print(sorted(newnew))
        