num = int(input())
stack = []
a = []
for i in range(num):
    q = input().split(" ")
    if q[0] == "1":
        stack.append(q[1])
        
    elif q[0] == "2":
        if not a:
            while len(stack) != 0:
                a.append(stack.pop())
        a.pop()
            
    elif q[0] == "3":
        if not a:
            while len(stack) != 0:
                a.append(stack.pop())
        print(a[-1])
        
