import numpy as np
import math 
import random
import matplotlib.pyplot as plt
import numpy as np

#Calculation of the Majian game in night market

###############################
# 01 # 02 # 03 # 04 # 05 # 06 #
###############################
# 07 # 08 # 09 # 10 # 11 # 12 #
###############################
# 13 # 14 # 15 # 16 # 17 # 18 #
###############################
# 19 # 20 # 21 # 22 # 23 # 24 #
###############################
# 25 # 26 # 27 # 28 # 29 # 30 #
###############################
# 31 # 32 # 33 # 34 # 35 # 36 #
###############################

# Rule
# Majian-Bingo GAME
# There are 36 patterns on the table.
# Randomly get the 15 ones and do the bingo game.

box,row,column,cross1,cross2=[],[],[],[],[]
# box : save the data in all test
# row : save the data in the rows
# column : save the data in the columns
# cross1 : means the line (1,8,15,22,29,36)
# cross2 : means the line (6,11,16,21,26,31)
f=[0,0,0,0,0,0]
g=[0,0,0,0,0,0]
x,m,n1,n2,n3,n4=0,0,0,0,0,0
successful_number=[]

for j in range(0,100):# the number of test
    n,count=0,0
    #Add new space to save the data
    box.append([])
    column.append([[],[],[],[],[],[]])
    row.append([[],[],[],[],[],[]])
    cross2.append([])
    cross1.append([])
    #######################
    while (count < 15):
        x=random.randint(1,36)
        #Confirm if there are some same elements.
        if (x in box[j]):
            continue
        #classify the element gotten
        else:
            box[j].append(x)
            column[j][(x-1)%6].append(x)
            row[j][(x-1)/6].append(x)
            if(x%5==1 and x!=1 and x!=36):
                cross2[j].append(x)
            if(x%7==1):
                cross1[j].append(x)
            count=count+1
    #######################
    #Count the number of sucessful line.
    for i in range(0,6):
        # column
        if (len(column[j][i])==6):
            n1=n1+1
            f[i]=f[i]+1
            n=n+1
        # row
        if (len(row[j][i])==6):
            n2=n2+1
            g[i]=g[i]+1
            n=n+1

    if (len(cross2[j])==6):
        #cross2
        n3=n3+1
        n=n+1

    if (len(cross1[j])==6):
        #cross1
        n4=n4+1
        n=n+1

    if (n!=0):
        m=m+1
        box[j].sort()
        successful_number.append(j)

print "The line success are ",n1+n2+n3+n4
print "The total success are ",m
print "row:",g,"column:",f,"cross:",n3,n4

#Plot#
t1 = np.arange(-0.5, 6.5, 1.0)
for i in successful_number:
    plt.figure()
    for j in range(0,15):
        plt.scatter((box[i][j]-1)/6, (box[i][j]-1)%6,100.0)
    for ww in t1:
        plt.plot(t1, t1*0.0 + ww)
    for ww in t1:
        plt.plot(t1*0.0 + ww, t1)
    plt.show()
