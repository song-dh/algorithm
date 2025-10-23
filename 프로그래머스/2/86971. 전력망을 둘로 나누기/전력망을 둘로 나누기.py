def solution(n, wires):
    tree = {}
    answer = n

    for wire in wires:
        tree.setdefault(wire[0], []).append(wire[1])
        tree.setdefault(wire[1], []).append(wire[0])
    
    for wire in wires:
        treeA = set([wire[0]])
        leftNode = list(tree[wire[0]])
        leftNode.remove(wire[1])
        while len(leftNode) != 0:
            tmp = leftNode.pop(0)  
            if not tmp in treeA:
                treeA.add(tmp)
                leftNode = leftNode + tree[tmp]
        answer = min(answer, abs(n - len(treeA)*2))
        
    return answer
            
            
        
        