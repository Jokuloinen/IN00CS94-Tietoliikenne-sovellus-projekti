import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#read data and nn parameters
pisteet = pd.read_csv('points.csv',header=None).values.tolist()
w1 = list(pd.read_csv('w1.csv',header=None).to_numpy().transpose())
#w2 = pd.read_csv('w2.csv',header=None).values.tolist()
b1 = pd.read_csv('b1.csv',header=None).values.tolist()
#b2 = pd.read_csv('b2.csv',header=None).values.tolist()

#show input data
plt.figure(1)
plt.subplot(1,1,1, projection='3d')
plt.plot(pisteet[0], pisteet[1], pisteet[2], pisteet[3], pisteet[4], pisteet[5], 'o')
plt.show()


def doNeuro(w1, b1, data):
	#do first layer
	layer1 = []
	for i in range(len(w1)):
		tmp = 0.0
		#dot product
		for ii in range(len(data)):
			tmp += data[ii] * w1[i][ii]
		#do sigmoid
		if tmp < 0:
			tmp = 0
		layer1.append(tmp)
	#add bias
	for i in range(len(b1)):
		layer1[i] = layer1[i] + b1[i][0]

	return layer1

for i in range(len(pisteet)):
	print(doNeuro(w1, b1, pisteet[i]))
	print("if index", i%6, "has highest value then this works")