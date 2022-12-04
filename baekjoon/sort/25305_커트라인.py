def sort(data):
    for stand in range(len(data)-1):
        lowest = stand
        for index in range(stand, len(data)):
            if data[lowest] > data[index]:
                lowest = index
        data[stand], data[lowest] = data[lowest], data[stand]
    
    return data

num, k = map(int, input().split())
a = []
a = list(map(int, input().split(" ")))

print(sort(a)[len(a)-k])