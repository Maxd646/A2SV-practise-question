for _ in range(int(input())):
    n = int(input())
    graph = [input().strip() for _ in range(n)]
    
    deg = [0]*n
    
    for i in range(n):
        for j in range(i+1, n):
            if graph[i][j] == '1':
                deg[min(i,j)] += 1
            else:
                deg[max(i,j)] += 1
                
    perm = [0]*n
    
    for u in range(n):
        pos = n - deg[u]
        perm[pos-1] = u+1
    
    print(*perm)