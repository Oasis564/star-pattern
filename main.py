

row = 10

for i in range(1, row+1):
    for j in range(i):
        print("*", end=" ")
    print()
    
for i in range(1, row+1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
    
name = "Osaeid"

for i in range(0, 7):
    for j in range(0, i):
        print(name[j], end=" ")
    print()
    
length = len(name)

for i in range(length):
    for j in range(length-1-i, 0, -1):
        print(end="  ")
    for k in range(i+1, 0, -1):
        print(name[k-1], end=" ")
    print()