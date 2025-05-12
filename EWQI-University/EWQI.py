import numpy as np

# Original Hydrochemical Data Matrix (24 samples × 13 parameters)
# Columns: EC, pH, Turbidity, Alkalinity, Bicarbonate, Calcium, Chloride, Magnesium, Potassium, Sodium, Sulphate, Nitrate, TDS
x = np.array([
    # Sample 1 to 24 (rows)
    [687, 7.36, 30, 262, 262, 57, 28, 39, 3.9, 24, 64, 0.24, 378],       # Sample 1
    [1013, 7.25, 3.56, 482, 482, 49, 36, 19, 2.8, 170, 33, 0.05, 608],    # Sample 2
    [411, 7.30, 16, 202, 202, 45, 10, 27, 0.8, 4, 22, 0.09, 142],         # Sample 3
    [304, 7.60, 7.73, 122, 122, 41, 12, 12, 0.6, 7, 25, 0.67, 167],       # Sample 4
    [459, 7.40, 3.77, 202, 202, 45, 14, 22, 2.6, 23, 25, 0.09, 252],      # Sample 5
    [588, 7.22, 10.76, 272, 272, 65, 10, 19, 1.1, 38, 32, 0.03, 323],     # Sample 6
    [546, 7.27, 2.56, 232, 232, 65, 12, 10, 2.4, 31, 25, 0.36, 300],      # Sample 7
    [623, 7.42, 13.25, 262, 262, 73, 24, 5, 2.7, 52, 16, 0.51, 343],      # Sample 8
    [566, 7.45, 7.15, 222, 222, 61, 14, 5, 4.7, 49, 35, 0.25, 311],       # Sample 9
    [546, 7.37, 18.09, 182, 182, 65, 20, 15, 3.4, 21, 37, 5.33, 300],     # Sample 10
    [566, 7.27, 9.89, 242, 242, 81, 12, 15, 1.2, 10, 20, 0.98, 311],      # Sample 11
    [280, 7.43, 3.63, 102, 102, 45, 12, 7, 1.2, 7, 20, 0.98, 154],        # Sample 12
    [839, 7.39, 19.5, 352, 352, 105, 26, 39, 2.2, 20, 59, 0.44, 461],     # Sample 13
    [656, 7.34, 19.39, 232, 232, 61, 12, 19, 2.7, 21, 31, 0.22, 361],     # Sample 14
    [564, 7.91, 0.0001, 232, 232, 89, 12, 12, 1.5, 7, 27, 0.17, 310],      # Sample 15 (BDL = Below Detection Limit)
    [413, 7.42, 0.0001, 162, 162, 49, 12, 12, 2.8, 15, 29, 0.49, 227],     # Sample 16 (BDL)
    [724, 7.33, 14.55, 302, 302, 73, 16, 29, 2.7, 32, 59, 1.69, 398],     # Sample 17
    [621, 7.06, 10.57, 202, 202, 101, 16, 5, 3.3, 16, 8, 0.63, 342],      # Sample 18
    [619, 7.18, 0.0001, 252, 252, 89, 12, 15, 3.2, 10, 26, 3.09, 340],     # Sample 19 (BDL)
    [600, 7.35, 3.85, 222, 222, 61, 12, 19, 8.8, 29, 68, 0.18, 330],      # Sample 20
    [256, 7.60, 2.79, 82, 82, 41, 12, 2, 1.3, 6, 27, 0.35, 141],          # Sample 21
    [648, 7.28, 17.29, 282, 282, 65, 16, 36, 2.3, 7, 24, 0.12, 356],      # Sample 22
    [413, 7.44, 24.55, 172, 172, 41, 12, 19, 2.4, 10, 24, 0.11, 227],     # Sample 23
    [905, 7.34, 2.75, 222, 222, 101, 60, 32, 3.6, 29, 128, 4.42, 498]     # Sample 24
])



#calculating necessary things for calculating probabilities (like min, max etc.)

# 1. getting all 13 columns from the matrix
c1=x[:,0]
c2=x[:,1]
c3=x[:,2]
c4=x[:,3]
c5=x[:,4]
c6=x[:,5]
c7=x[:,6]
c8=x[:,7]
c9=x[:,8]
c10=x[:,9]
c11=x[:,10]
c12=x[:,11]
c13=x[:,12]

# 2. calculating max of each column
max_c1=np.max(c1)
max_c2=np.max(c2)
max_c3=np.max(c3)
max_c4=np.max(c4)
max_c5=np.max(c5)
max_c6=np.max(c6)
max_c7=np.max(c7)
max_c8=np.max(c8)
max_c9=np.max(c9)
max_c10=np.max(c10)
max_c11=np.max(c11)
max_c12=np.max(c12)
max_c13=np.max(c13)


# 3. calculating min of each column
min_c1=np.min(c1)
min_c2=np.min(c2)
min_c3=np.min(c3)
min_c4=np.min(c4)
min_c5=np.min(c5)
min_c6=np.min(c6)
min_c7=np.min(c7)
min_c8=np.min(c8)
min_c9=np.min(c9)
min_c10=np.min(c10)
min_c11=np.min(c11)
min_c12=np.min(c12)
min_c13=np.min(c13)

#calculating entries of prbability matrix (only benificial ones)


# sample 1 all 13 parameters
y_00=((x[0,0] -min_c1)/(max_c1-min_c1))+ 0.0001
y_01=((x[0,1] -min_c2)/(max_c2-min_c2))+ 0.0001
y_02=((x[0,2] -min_c3)/(max_c3-min_c3))+ 0.0001
y_03=((x[0,3] -min_c4)/(max_c4-min_c4))+ 0.0001
y_04=((x[0,4] -min_c5)/(max_c5-min_c5))+ 0.0001
y_05=((x[0,5] -min_c6)/(max_c6-min_c6))+ 0.0001
y_06=((x[0,6] -min_c7)/(max_c7-min_c7))+ 0.0001
y_07=((x[0,7] -min_c8)/(max_c8-min_c8))+ 0.0001
y_08=((x[0,8] -min_c9)/(max_c9-min_c9))+ 0.0001
y_09=((x[0,9] -min_c10)/(max_c10-min_c10))+ 0.0001
y_10=((x[0,10] -min_c11)/(max_c11-min_c11))+ 0.0001
y_11=((x[0,11] -min_c12)/(max_c12-min_c12))+ 0.0001
y_12=((x[0,12] -min_c13)/(max_c13-min_c13))+ 0.0001





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



