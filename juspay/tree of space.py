def lock(name):
    ind = nodes.index(name) + 1 
    c1 = ind * 2  
    c2 = ind * 2 + 1  
    if status[name] == 'lock' or status[name] == 'fail':
        return 'false'
    else:
        p = ind // 2 
        status[nodes[p - 1]] = 'fail'
        status[name] = 'lock'
        return 'true'
def unlock(name):
    if status[name] == 'lock':
        status[name] = 'unlock'
        return 'true'
    else:
        return 'false'
def upgrade(name):
    ind = nodes.index(name) + 1  
    c1 = ind * 2  
    c2 = ind * 2 + 1  
    if c1 in range(1, n + 1) and c2 in range(1, n + 1):
        if status[nodes[c1 - 1]] == 'lock' and status[nodes[c2 - 1]] == 'lock':
            status[nodes[c1 - 1]] = 'unlock'
            status[nodes[c2 - 1]] = 'unlock'
            status[nodes[ind - 1]] = 'lock'
            return 'true'
        else:
            return 'false'
    else:
        return 'false'
def precompute(queries):
    d = []
    for j in queries:
        i = j.split()
        d.append(i[1])  
        d.append(int(i[0]))  
    status = {}
    for j in range(0, len(d) - 1, 2):
        status[d[j]] = 'unlock' 
    return status, d
def operation(name, code):
    result = 'false'
    if code == 1:
        result = lock(name)
    elif code == 2:
        result = unlock(name)
    elif code == 3:
        result = upgrade(name)
    return result
if __name__ == '__main__':
    n = int(input())
    apis = int(input())  
    nodes = list(map(str, input().split())) 
    queries = [input() for _ in range(apis)] 
    status, d = precompute(queries)
    for j in range(0, len(d) - 1, 2):
        print(operation(d[j], d[j + 1]), end=' ')