def componentsInGraph(gb):
    # Write your code here
    n = len(gb) * 2
    adj = { i:[] for i in range(n+1)}
    for n1, n2 in gb:
        adj[n1].append(n2)
        adj[n2].append(n1)
        
        
    def dfs(i):
        visited[i] = True
        count = 1
        for j in adj[i]:
            if visited[j] == False:
                count += dfs(j)
        return count
        
    visited = [False] * (n+1)
    smallest = float('inf')
    biggest = 0
      
    for i in range(1,n+1):  
        if visited[i] == False :
            count = dfs(i)   
            if count >= 2:
                smallest = min(smallest, count)
            biggest = max(biggest, count)
    
    if smallest == float('inf'):
        smallest = biggest

    return [smallest, biggest]
