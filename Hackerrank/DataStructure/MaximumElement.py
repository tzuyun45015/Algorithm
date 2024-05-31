# stack
def getMax(operations):
    # Write your code here
    stack = []
    maxstack = []
    res = []
    
    for i in operations:
        op = i.split()
        if op[0] == "1":
            val = int(op[1])
            stack.append(val)
            if maxstack == []:
                maxstack.append(val)
            else:
                val = max(val,maxstack[-1])
                maxstack.append(val)   
        
        elif op[0] == "2":
            stack.pop()
            maxstack.pop()
        
        elif op[0] == "3":
            res.append(maxstack[-1])
    return res
