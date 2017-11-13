# Adapted : https://raw.githubusercontent.com/salmanahmad4u/keras-iris/master/iris_nn.py
# https://keras.io/
import numpy as np
import sklearn.cross_validation as cv
import csv
# from sklearn.cross_validation import train_test_split
import keras.models as m
import keras.layers.core as c
import keras.utils as u


iris = list(csv.reader(open('irisdata.csv')))[1:]

input = np.array(iris)[:,:4].astype(np.str) 
output = np.array(iris)[:,:4]


in_train, in_test, out_train, out_test = cv.train_test_split(input,output,train_size=0.5,random_state=1)

# numpy.unique returns a list of unique values in an array.
# When return_inverse is set to True it also returns the original array encoded
uniq_test, ids_test = np.unique(out_test, return_inverse=True)
uniq_train, ids_train = np.unique(out_train, return_inverse=True)
# the to_categorical function turns indices into bonary vectors.
# 
onehot_train = u.np_utils.to_categorical(ids_train, len(uniq_test))
onehot_test = u.np_utils.to_categorical(ids_test, len(uniq_train))

# Create a model with a linear stack of layers with 16 nodes.
# 
model = m.Sequential()
# Apply the sigmoid activation function to that layer.
model.add(c.Dense(16, input_dim=4))
model.add(c.Activation("sigmoid"))
# Add another layer, connected to the layer wth 16 nodes, containing three output nodees.
model.add(c.Dense(3)) # Dense = 密集
# Use the softmax activation function there
model.add(c.Activation("softmax"))

# Configure the model for training.
# Docs: https://keras.io/models/sequential/#compile
# Uses the adam optimizer and categorical cross entropy as the loss function
model.compile(optimizer="adam",loss="categorical_crossentropy")

# Fit the model using our training data.
#  epochs , batch_size, verbose 分别什么作用？
model.fit(in_train, onehot_train, epochs=100, batch_size=1, verbose=1)

# Evaluate the model on the testing set.
loss = model.evaluate(in_test, onehot_test, verbose=1)

# Print out the accuracy to the console.
print("\n\nLoss = {:.2f}".format(loss))