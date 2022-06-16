test1 = [[1,3,5],[2,4,1],[1,5,7]]
test2 = [[3,3,4],[2,4,1],[3,5,4]]

z= len(test1)

t = len(test1[z-1])

for i in range(0,z):
    for j in range(0,t):
        test1[i][j] += test2[i][j]
        
print(test1)