import pandas as pd
from sklearn.metrics import confusion_matrix

data = pd.read_csv("performance.csv")#.values.tolist()

#print(data.real, data.predict)


print("k-means")
print(confusion_matrix(data.x, data.y))
print("NeuralNet")
print(confusion_matrix(data.x, data.z))
print("DecisionTree")
print(confusion_matrix(data.x, data.w))
