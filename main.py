

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
    
    
# rhombus shape

n = 5
# In this for loop we are creating two parallel triangles filled with nothing but spaces as they decrease from 5 until 1, the stars works in a similiar way but they are instead increasing from 1 to 5 to create a hill shaped pattern 
for i in range(n):
    for j in range(i, n):
        
    # this loop creates the spaces that decrease from 5 to 1 spaces on both sides
        print(" ",end="  ")
    
    # this creates the first triangle that increases from 1 to 5 facing left
    for j in range(i):
        print("*",end="  ")
        
    # this creates the second triangle that increases from 1 to 5 facing right
    for j in range(i + 1):
        print("*",end="  ")
    print()
    
    
# In this for loop we are creating two parallel triangles filled with nothing but spaces as they increase from 1 until 5, the stars works in a similiar way but they are instead decreasing from 5 to 1 to create a reverse hill shaped pattern below the hill shaped pattern we made above

for i in range(n):
    
    # this loop creates the spaces that increase from 1 to 5 spaces on both sides
    for j in range(i + 1):
        print(" ",end="  ")
        
    # this creates the first triangle that decreases from 5 to 1 facing left
    for j in range(i, n - 1):
        print("*",end="  ")
        
    # this creates the second triangle that decreases from 5 to 1 facing tight
    for j in range(i, n):
        print("*",end="  ")
    print()
    
# another shape

for i in range(n-1):
    for j in range(i, n):
        print(" ",end="  ")
    
    
    for j in range(i):
        print("*",end="  ")
    print()
    
for i in range(n):
    for j in range(i + 1):
        print(" ",end="  ")
    
    
    for j in range(i, n - 1):
        print("*",end="  ")
    print()
    
# same shape but other side

for i in range(n-1):
    
    for j in range(i):
        print("*",end="  ")
        
    for j in range(i, n):
        print(" ",end="  ")
    print()
    
for i in range(n):
    
    for j in range(i, n - 1):
        print("*",end="  ")
        
    for j in range(i + 1):
        print(" ",end="  ")
    print()
    
# we swapped the for loop which was responsible for drawing the star right angle triangle and the space right angle triangle to create an opposite reversed verion of the code we made prior so it faced right instead of left.