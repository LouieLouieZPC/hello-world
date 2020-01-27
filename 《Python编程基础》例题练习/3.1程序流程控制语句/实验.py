for i in range(0,3):
    for j in range(0,3):
        break
print(i,j) 



for i in range(0,3):
    if i<1:
        for j in range(0,3):
            if j>1:
                print(i,j)