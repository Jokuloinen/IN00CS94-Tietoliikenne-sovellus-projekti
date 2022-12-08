import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#logfile
data = pd.read_csv("putty.log", header=None)
datav = np.reshape(data.to_numpy(), (-1, 3))
datac = datav.transpose()


#plot rawdata
plt.figure(1)
plt.subplot(1,1,1, projection='3d')
plt.plot(datac[0], datac[1], datac[2], 'o')
plt.show()


#find min max for all axises
minX = np.min(datac[0])
maxX = np.max(datac[0])
minY = np.min(datac[1])
maxY = np.max(datac[1])
minZ = np.min(datac[2])
maxZ = np.max(datac[2])
print(minX, maxX, minY, maxY, minZ, maxZ)
#create array and fill it with random start values based on data
dataKc = np.empty([3, 4])
dataKc[0] = np.random.randint(minX, maxX, 4)
dataKc[1] = np.random.randint(minY, maxY, 4)
dataKc[2] = np.random.randint(minZ, maxZ, 4)
dataKv = dataKc.transpose()
print(dataKv)



#loop like 10 times: more = more accurate
for i in range(10):
	print("iteration:", i)
	print("point0", dataKv[0])
	print("point1", dataKv[1])
	print("point2", dataKv[2])
	print("point3", dataKv[3])
	#make array that contains what k is the closest to a vector
	count = np.zeros(4)			#how many numbers added to cumSum
	cumSum = np.zeros((4, 3))		#gets x,y,z from point added to it "cumulative sum"
	for point in datav:
		distances = np.zeros(4)		#distance from Kv
		for ii in range(4):
			distances[ii]=np.linalg.norm(point-dataKv[ii])
		#select correct point for distance
		count[distances.argmin()] = count[distances.argmin()] + 1
		cumSum[distances.argmin()] = point + cumSum[distances.argmin()]
	#print(count, cumSum)
	
	#update the k values
	for ii in range(4):
		if count[ii] > 0:
			dataKv[ii] = cumSum[ii]/count[ii]
		else:
			dataKv[ii] = np.empty(3)
			dataKv[ii][0] = np.random.randint(minX, maxX, 1)
			dataKv[ii][1] = np.random.randint(minY, maxY, 1)
			dataKv[ii][2] = np.random.randint(minZ, maxZ, 1)





#pretty plotting of the data


#create new array that has points and their closest associated array
pgs = np.empty((int(datac.size/3), 4))
for i in range(int(datav.size/3)):
	distances = np.zeros(4)
	for ii in range(4):
		distances[ii]=np.linalg.norm(datav[i]-dataKv[ii])
	pgs[i][0] = datav[i][0]
	pgs[i][1] = datav[i][1]
	pgs[i][2] = datav[i][2]
	pgs[i][3] = distances.argmin()


#create pointgroups for each classification
g0 = pgs[(pgs[:, 3] == 0), :].transpose()
g1 = pgs[(pgs[:, 3] == 1), :].transpose()
g2 = pgs[(pgs[:, 3] == 2), :].transpose()
g3 = pgs[(pgs[:, 3] == 3), :].transpose()


#print/plot value
plt.figure(1)
plt.subplot(1,1,1, projection='3d')
#plot "centroid" points
plt.plot(dataKv.transpose()[0], dataKv.transpose()[1], dataKv.transpose()[2], 'o')
#plot all point groups and give them custom color
plt.plot(g0[0], g0[1], g0[2], 'o')
plt.plot(g1[0], g1[1], g1[2], 'o')
plt.plot(g2[0], g2[1], g2[2], 'o')
plt.plot(g3[0], g3[1], g3[2], 'o')
plt.show()