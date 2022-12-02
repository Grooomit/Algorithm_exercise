def sort(data):
    for stand in range(len(data) - 1):
        lowest = stand
        for index in range(stand+1, len(data)):
            if data[lowest] > data[index]:
                lowest = index
        data[stand], data[lowest] = data[lowest], data[stand]
    return data


a = int(input())
b = []

for i in range(a):
    b.append(int(input()))

print(*sort(b), sep='\n')