def solution(new_id):
    idList = []
    for s in new_id:
        if s.islower() or s.isdigit() or s == '-' or s == '_':
            idList.append(s)
        elif s.isupper():
            idList.append(s.lower())
        elif s == ".":
            if idList and idList[-1] != '.':
                idList.append(s)
        else:
            continue
        if len(idList) == 15:
            break
            
    while idList and idList[-1] == '.':
        idList.pop()
        
    if not idList:
        idList.append('a')
    
    while len(idList) < 3:
        idList.append(idList[len(idList)-1])
        
    return ''.join(idList)