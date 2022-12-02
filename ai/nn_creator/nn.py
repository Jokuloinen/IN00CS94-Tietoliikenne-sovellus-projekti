
import pandas as pd
import numpy as np
from tensorflow import keras
from tensorflow.keras import layers


num_classes = 6
input_shape = (3)

#load data
alldata = pd.read_csv("data.csv", header=None).to_numpy()	#read data
np.random.shuffle(alldata)					#shuffel data
splitdata = np.array_split(alldata, 10)				#split array

#large arrays training data
traindata = np.concatenate((splitdata[1], splitdata[2], splitdata[3], splitdata[4], splitdata[5], splitdata[6], splitdata[7], splitdata[8], splitdata[9]))
evaldata = np.concatenate((splitdata[0], splitdata[5]))

#train and test vectors/points
x_train = traindata.transpose()[0:3].transpose().astype("float32")
x_test = evaldata.transpose()[0:3].transpose().astype("float32")
print(x_test.shape, x_train.shape)

#train and test answers
y_train = traindata.transpose()[3].transpose().astype("float32")
y_test = evaldata.transpose()[3].transpose().astype("float32")
print(y_test.shape, y_train.shape)

#smth binary smth
y_train = keras.utils.to_categorical(y_train, num_classes)
print("ytrain", y_train)
y_test = keras.utils.to_categorical(y_test, num_classes)

#define model
model = keras.Sequential(
    [
        keras.Input(shape=input_shape, name="inputl"),
        #layers.Dense(6, activation='relu'),
        #layers.Dense(12, activation='relu'),
        #layers.Dropout(0.5),
        layers.Dense(num_classes, activation="softmax", name="outputl"),
    ]
)
model.summary()

batch_size = 64
epochs = 2048

#compile and train model
model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])
model.fit(x_train, y_train, batch_size=batch_size, epochs=epochs, validation_split=0.1)


score = model.evaluate(x_test, y_test, verbose=0)
print("Test loss:", score[0])
print("Test accuracy:", score[1])


pred_y = model.predict(x_test)
rped_y = np.round(pred_y, 0).astype(int)

print(pred_y.astype(int), pred_y.shape, pred_y[0].shape)
print(y_test.astype(int), y_test.shape, y_test[0].shape)
print(rped_y[0:15], "\t", y_test[0:15])

failed_lst = []
for i in range(0, rped_y.shape[0]):
  pushval = 0
  for ii in range(6):
    if rped_y[i, ii] != y_test[i, ii]:
      pushval += 1
  if pushval != 0:
    failed_lst.append(i)

print("failed test on following input indecies:\n", failed_lst)
print(len(failed_lst), "\n", y_test.shape)

# firstlayer by name
for layer in model.layers:
    print(layer.name, layer)
    print("\tweight", layer.weights)
    print("\tbiasses", layer.bias.numpy())