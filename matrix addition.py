#Addition of two matrices
X=[[5,2],
  [3,5]]
Y=[[4,6],
  [3,6]]
sum=[[0,0],
    [0,0]]
for i in range(len(X)):
   for j in range(len(X[0])):
       sum[i][j]=X[i][j]+Y[i][j]
print(sum)  # in array form
for k in sum:
    print(k) #in matrix form
                  
       
