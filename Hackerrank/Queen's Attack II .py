sys.setrecursionlimit(1000000) # dfs loop out of time limit
def queensAttack(n, k, r_q, c_q, obstacles):
    # Write your code here
    obs = set() #obstacles
    visit = set() # answer

    for i, j in obstacles:
        obs.add((i, j))
    
    if n == 1:
        return 0
    
    def dfs(r, c, a, b):
        if (r+a, c+b) not in obs and 0<(r+a)<=n and 0<(c+b)<=n:
            visit.add((r+a, c+b))
            dfs(r+a, c+b, a, b)
        
    dfs(r_q, c_q, 1, 1)
    dfs(r_q, c_q, 1, -1)
    dfs(r_q, c_q, -1, 1)
    dfs(r_q, c_q, -1, -1)
    dfs(r_q, c_q, 1, 0)
    dfs(r_q, c_q, 0, 1)
    dfs(r_q, c_q, -1, 0)
    dfs(r_q, c_q, 0, -1)

    res = len(visit)

    return res
        
 
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    r_q = int(second_multiple_input[0])

    c_q = int(second_multiple_input[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    fptr.write(str(result) + '\n')

    fptr.close()
