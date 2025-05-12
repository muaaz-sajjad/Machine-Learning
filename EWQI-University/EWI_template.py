import numpy as np
x = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

#calculating necessary things for calculating probabilities (like min, max etc.)
c1=x[:,0]
c2=x[:,1]
c3=x[:,2]
max_c1=np.max(c1)
max_c2=np.max(c2)
max_c3=np.max(c3)
min_c1=np.min(c1)
min_c2=np.min(c2)
min_c3=np.min(c3)

#calculating entries of prbability matrix (only benificial ones)

y_00=((x[0,0] -min_c1)/(max_c1-min_c1))+ 0.0001
y_01=((x[0,1] -min_c2)/(max_c2-min_c2))+ 0.0001
y_02=((x[0,2] -min_c3)/(max_c3-min_c3))+ 0.0001

y_10=((x[1,0] -min_c1)/(max_c1-min_c1))+ 0.0001
y_11=((x[1,1] -min_c2)/(max_c2-min_c2))+ 0.0001
y_12=((x[1,2] -min_c3)/(max_c3-min_c3))+ 0.0001

y_20=((x[2,0] -min_c1)/(max_c1-min_c1))+ 0.0001
y_21=((x[2,1] -min_c2)/(max_c2-min_c2))+ 0.0001
y_22=((x[2,2] -min_c3)/(max_c3-min_c3))+ 0.0001

y=np.array([
    [y_00,y_01, y_02],
    [y_10,y_11,y_12],
    [y_20,y_21,y_22]
])
# calculating sum of coloumns of prbability matrix
sum_c1 = y_00+y_01+y_02
sum_c2 = y_10+y_11+y_12
sum_c3 = y_20+y_21+y_22

print("sum of coloumns of prbability matrix: ")
print(f"coloum-1: {sum_c1}  coloumn-2: {sum_c2}  coloumn-3{sum_c3}")

#calculating probabilities
p00 = y[0,0]/sum_c1
p01 = y[0,1]/sum_c2
p02 = y[0,2]/sum_c3

p10 = y[1,0]/sum_c1
p11 = y[1,1]/sum_c2
p12 = y[1,2]/sum_c3

p20 = y[2,0]/sum_c1
p21 = y[2,1]/sum_c2
p22 = y[2,2]/sum_c3

p = np.array([
    [p00, p01, p02],
    [p10, p11, p12],
    [p20, p21, p22]
])

print(f"probability matrix: {p}")

# calculating entropy for each coloumn
no_of_rows = 3
k = 1/np.log(no_of_rows)

# coloumn 1
e1 = -k * (
    p[0,0]*np.log(p[0,0])+
    p[0,1]*np.log(p[0,1])+
    p[0,2]*np.log(p[0,2]) 
      )



