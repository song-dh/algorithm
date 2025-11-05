def solution(tickets):
    global answer
    global ticketMap
    answer = []
    tickets.sort()
    ticketMap = {}
    for index, ticket in enumerate(tickets):
        ticketMap.setdefault(ticket[0], []).append([index, ticket[1]])
    
    visit = [0 for _ in range(len(tickets))]
    dfs(visit, ["ICN"]) 
    print(tickets, ticketMap, answer, visit)
    return answer

def dfs(visit, root):
    global answer
    for i in ticketMap.get(root[len(root)-1], []):
        if visit[i[0]] == 1:
            continue
        visit[i[0]] = 1
        root.append(i[1])
        if len(root) == len(visit) + 1:
            answer = root[:]
            return
        dfs(visit, root)
        if answer:
            break
        root.pop()
        visit[i[0]] = 0