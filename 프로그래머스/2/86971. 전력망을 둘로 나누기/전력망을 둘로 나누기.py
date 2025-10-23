def solution(n, wires):
    tree = {}
    
    for wire in wires:
        tree.setdefault(wire[0], []).append(wire[1])
        tree.setdefault(wire[1], []).append(wire[0])
    answer = n
    for wire in wires:
        a = set([wire[0]])
        b = list(tree[wire[0]])
        b.remove(wire[1])
        while len(b) != 0:
            tmp = b.pop(0)  
            if not tmp in a:
                a.add(tmp)
                b = b + tree[tmp]
        answer = min(answer, abs(n-len(a)-len(a)))
        
    return answer

def dfs(tree, wires, wire):
    print(tree, wires, wire)
    a = set([wire[0]])
    b = list(tree[wire[0]])
    b.remove(wire[1])
    while len(b) != 0:
        tmp = b.pop(0)  
        if not tmp in a:
            a.add(tmp)
            b = b + tree[tmp]
    return len(a)
            
            
        
        