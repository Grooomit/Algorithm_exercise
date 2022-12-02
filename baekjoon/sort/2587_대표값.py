def middle(data):
    data.sort()
    return sum(data)//len(data)

def avg(data):
    data.sort()
    return data[len(data)//2]


a = []
for i in range(5):
    a.append(int(input()))

print(middle(a))
print(avg(a))