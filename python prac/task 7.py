list = [-5, 2, 10, -24, 15, -6, -52, 24, -37, 13, -2, -7, -11]

for i in range(13):
 if list[i] < 0:
    list[i] = abs(list[i])
    
print(list)

