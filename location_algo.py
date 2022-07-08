from math import cosh
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# READING THE DATA OF THE 1ST VIDEO
data = pd.read_csv("C:\Users\Sepideh\Desktop\MS\CSE 535\posenet_nodejs_setup-master\videos\GESTURE_PRACTICE_Falah_1656657435473_bluetooth\bluetooth\key_points.csv")

rWX = data.iloc[:,33].values
rWY = data.iloc[:,34].values
nX = data.iloc[:,3].values
nY = data.iloc[:,4].values
lShX = data.iloc[:,18].values
rShX = data.iloc[:,21].values
hY = data.iloc[:,37].values

# normalizing the values of the right wrist X and right wrist Y coordinates
rWXN = (rWX - nX) / (np.abs(lShX - rShX))
rWYN = (rWY - nY) / (np.abs(nY - hY))
plt.plot(rWXN[10:len(rWXN)+1],rWYN[10:len(rWYN)+1])

# READING THE DATA OF THE 2ND VIDEO
data = pd.read_csv("C:\Users\Sepideh\Desktop\MS\CSE 535\posenet_nodejs_setup-master\videos\GESTURE_PRACTICE_Falah_1656653232972_ACPower\ACPower\key_points.csv")

rWX2 = data.iloc[:,33].values
rWY2 = data.iloc[:,34].values
nX2 = data.iloc[:,3].values
nY2 = data.iloc[:,4].values
lShX2 = data.iloc[:,18].values
rShX2 = data.iloc[:,21].values
hY2 = data.iloc[:,37].values

# normalizing the values of the right wrist X and right wrist Y coordinates
rWXN2 = (rWX2 - nX2) / (np.abs(lShX2 - rShX2))
rWYN2 = (rWY2 - nY2) / (np.abs(nY2 - hY2))
plt.plot(rWXN2[10:len(rWXN2)+1],rWYN2[10:len(rWYN2)+1])

# READING THE DATA OF THE 3rD VIDEO
data = pd.read_csv("C:\Users\Sepideh\Desktop\MS\CSE 535\posenet_nodejs_setup-master\videos\GESTURE_PRACTICE_Falah_1656653982419_Authentication\Authentication\key_points.csv")

rWX3 = data.iloc[:,33].values
rWY3 = data.iloc[:,34].values
nX3 = data.iloc[:,3].values
nY3 = data.iloc[:,4].values
lShX3 = data.iloc[:,18].values
rShX3 = data.iloc[:,21].values
hY3 = data.iloc[:,37].values

# normalizing the values of the right wrist X and right wrist Y coordinates
rWXN3 = (rWX3 - nX3) / (np.abs(lShX3 - rShX3))
rWYN3 = (rWY3 - nY3) / (np.abs(nY3 - hY3))
plt.plot(rWXN3[10:len(rWXN3)+1],rWYN3[10:len(rWYN3)+1])


# READING THE DATA OF THE 4th VIDEO
data = pd.read_csv("C:\Users\Sepideh\Desktop\MS\CSE 535\posenet_nodejs_setup-master\videos\GESTURE_PRACTICE_Falah_1656654444825_Domain\Domain\key_points.csv")

rWX4 = data.iloc[:,33].values
rWY4 = data.iloc[:,34].values
nX4 = data.iloc[:,3].values
nY4 = data.iloc[:,4].values
lShX4 = data.iloc[:,18].values
rShX4 = data.iloc[:,21].values
hY4 = data.iloc[:,37].values

# normalizing the values of the right wrist X and right wrist Y coordinates
rWXN4 = (rWX4 - nX4) / (np.abs(lShX4 - rShX4))
rWYN4 = (rWY4 - nY4) / (np.abs(nY4 - hY4))
plt.plot(rWXN4[10:len(rWXN4)+1],rWYN4[10:len(rWYN4)+1])

# Trajectories 
tA1 = rWXN**2 + rWYN**2
tA2 = rWXN2**2 + rWYN2**2
tA3 = rWXN3**2 + rWYN3**2
tA4 = rWXN4**2 + rWYN4**2

def cosine_similarity(a,b):
    return dot(a,b) / ( (dot(a,a) **.5) * (dot(b,b) ** .5) )
 
def dot(A,B): 
    return (sum(a*b for a,b in zip(A,B)))

cos12 = cosine_similarity(tA1,tA2)
cos13 = cosine_similarity(tA1,tA3)
cos14 = cosine_similarity(tA1,tA4)
cos23 = cosine_similarity(tA2,tA3)
cos24 = cosine_similarity(tA2,tA4)
cos34 = cosine_similarity(tA3,tA4)


print(cos12)
print(cos13)
print(cos14)
print(cos23)
print(cos24)
print(cos34)