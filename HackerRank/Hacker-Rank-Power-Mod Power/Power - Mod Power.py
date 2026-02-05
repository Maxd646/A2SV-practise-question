if __name__ == '__main__':
    
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    result= [[i,j,k] for k in range(z) for j in range(y) for i in range(x)]
    newnew=[]
    print(result)
    for num in result:
        if sum(num)<n:
            newnew.append(num)
    print(newnew)
        