def solution(n, computers):
    networks = []
    soloNetworks = []
    for i in range(n):
        tmp = set()
        for j in range(n):
            if computers[i][j] == 1:
                tmp.update([i, j])
        if len(tmp) == 1:
            soloNetworks.append(tmp)
        else:
            networks.append(tmp)
    for i in range(len(networks)-1, -1, -1):
        for j in range(len(networks) - 1, -1, -1):
            if i!=j and networks[i] & networks[j]:
                networks[i] = networks[i] | networks[j]
                networks.pop(j)
                break
    return len(networks) + len(soloNetworks)
    