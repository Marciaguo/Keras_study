from __future__ import print_function

import numpy as np
np.random.seed(1337)


from keras.datasets import mnist
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation
from keras.optimizers import RMSprop
from keras.utils import np_utils
from keras.optimizers import SGD

# ����batch�Ĵ�С
batch_size = 128
# �������ĸ���
nb_classes = 10
# ���õ����Ĵ���
nb_epoch = 20

# keras�е�mnist���ݼ��Ѿ������ֳ���60,000��ѵ������10,000�����Լ�����ʽ�������¸�ʽ���ü���
(X_train, y_train), (X_test, y_test) = mnist.load_data()

# X_trainԭ����һ��60000*28*28����ά����������ת��Ϊ60000*784�Ķ�ά����
X_train = X_train.reshape(60000, 784)
# X_testԭ����һ��10000*28*28����ά����������ת��Ϊ10000*784�Ķ�ά����
X_test = X_test.reshape(10000, 784)
# ��X_train, X_test�����ݸ�ʽתΪfloat32�洢
X_train = X_train.astype('float32')
X_test = X_test.astype('float32')
# ��һ��
X_train /= 255
X_test /= 255
# ��ӡ��ѵ�����Ͳ��Լ�����Ϣ
print(X_train.shape[0], 'train samples')
print(X_test.shape[0], 'test samples')



Y_train = np_utils.to_categorical(y_train, nb_classes)
Y_test = np_utils.to_categorical(y_test, nb_classes)

# ����˳����ģ��
model1 = Sequential()

model1.add(Dense(256, activation='relu', input_dim=784))
model1.add(Dropout(0.2))
model1.add(Dense(256, activation='relu'))
model1.add(Dropout(0.2))
model1.add(Dense(10, activation='softmax'))
sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
model1.compile(loss='categorical_crossentropy',
              optimizer=sgd,
              metrics=['accuracy'])

history1 = model1.fit(X_train, Y_train,
                    batch_size = batch_size,
                    epochs = nb_epoch,
                    verbose = 2,
                    validation_data = (X_test, Y_test))

model2 = Sequential()

model2.add(Dense(256, activation='relu', input_dim=784))

model2.add(Dense(256, activation='relu'))

model2.add(Dense(10, activation='softmax'))
sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
model2.compile(loss='categorical_crossentropy',
              optimizer=sgd,
              metrics=['accuracy'])

history2 = model2.fit(X_train, Y_train,
                    batch_size = batch_size,
                    epochs = nb_epoch,
                    verbose = 2,
                    validation_data = (X_test, Y_test))
model3 = Sequential()

model3.add(Dense(256, activation='relu', input_dim=784))

model3.add(Dense(10, activation='softmax'))
sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
model3.compile(loss='categorical_crossentropy',
              optimizer=sgd,
              metrics=['accuracy'])

history3 = model3.fit(X_train, Y_train,
                    batch_size = batch_size,
                    epochs = nb_epoch,
                    verbose = 2,
                    validation_data = (X_test, Y_test))


import matplotlib.pyplot as plt
# list all data in history
print(history.history.keys())
# summarize history for accuracy
plt.plot(history1.history['acc'])
plt.plot(history1.history['val_acc'])
plt.title('model1 accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()
plt.plot(history2.history['acc'])
plt.plot(history2.history['val_acc'])
plt.title('model2 accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()
plt.plot(history3.history['acc'])
plt.plot(history3.history['val_acc'])
plt.title('model3 accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()
plt.plot(history1.history['val_acc'])
plt.plot(history2.history['val_acc'])
plt.plot(history3.history['val_acc'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['model1', 'model2', 'model3'], loc='upper left')
plt.show()



# summarize history for loss
plt.plot(history1.history['loss'])
plt.plot(history1.history['val_loss'])
plt.title('model1 loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()
plt.plot(history2.history['loss'])
plt.plot(history2.history['val_loss'])
plt.title('model2 loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()
plt.plot(history3.history['loss'])
plt.plot(history3.history['val_loss'])
plt.title('model3 loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()