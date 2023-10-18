def solution(rows, columns, queries):
    result = []
    arr = [[i+(columns*j) for i in range(1, columns+1)] for j in range(rows)]
    
    for query in queries:
        num, value = [], []
        a,b,c,d = query[0], query[1], query[2], query[3]
        
        for i in range(b, d+1):
            num.append([a, i])
            value.append(arr[a-1][i-1])
        for i in range(a+1, c+1):
            num.append([i, d])
            value.append(arr[i-1][d-1])
        for i in range(d-1, b, -1):
            num.append([c, i])
            value.append(arr[c-1][i-1])
        for i in range(c, a, -1):
            num.append([i, b])
            value.append(arr[i-1][b-1])
        result.append(min(value))
        
        for i, v in enumerate(num):
            arr[v[0]-1][v[1]-1] = value[(i-1)%len(value)]
            
    return result