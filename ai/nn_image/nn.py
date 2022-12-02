import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#read data and nn parameters
kuva = pd.read_csv('kuva4.csv',header=None).values.tolist()
w1 = pd.read_csv('w1.csv',header=None).values.tolist()
w2 = pd.read_csv('w2.csv',header=None).values.tolist()
b1 = pd.read_csv('b1.csv',header=None).values.tolist()
b2 = pd.read_csv('b2.csv',header=None).values.tolist()

#show input data
plt.figure(1)
plt.imshow(np.asarray(kuva).reshape(28,28))
plt.show()

def doNeuro(w1, w2, b1, b2, data):
	#do first layer
	layer1 = []
	for i in range(len(w1)):
		tmp = 0.0
		#dot product
		for ii in range(len(data)):
			tmp += data[ii][0] * w1[i][ii]
		#do sigmoid
		if tmp < 0:
			tmp = 0
		layer1.append(tmp)
	#add bias
	for i in range(len(b1)):
		layer1[i] = layer1[i] + b1[i][0]
	
	#repeate for layer2
	layer2 = []
	for i in range(len(w2)):
		tmp = 0.0
		#dot product
		for ii in range(len(layer1)):
			tmp += layer1[ii] * w2[i][ii]
		#do sigmoid
		if tmp < 0:
			tmp = 0
		layer2.append(tmp)
	#add bias
	for i in range(len(b2)):
		layer2[i] = layer2[i] + b2[i][0]

	return layer2

print(doNeuro(w1, w2, b1, b2, kuva))
print("if index 4 has highest number then this works")