import numpy as np
from keras.layers import *
from keras.models import *
from keras.utils import *
from sklearn.preprocessing import *
import seaborn as sns

# from keras.datasets import cifar10
from keras.utils.np_utils import to_categorical



def make_h5(mem_id):

    X_train = np.load("train/{}/x_train.npy".format(mem_id))
    Y_train = np.load("train/{}/y_train.npy".format(mem_id))
    
    # X_train = X_train/255.0
    Y_train = to_categorical(Y_train)
    
        
    model = tf.keras.models.Sequential([
        tf.keras.layers.Flatten(input_shape=(478, 3)),
        tf.keras.layers.Dense(512, activation=tf.nn.relu),
        tf.keras.layers.Dense(2, activation=tf.nn.softmax)
    ])
            
    
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    
    
    model.fit(X_train, Y_train,epochs=30)
    
    model.summary()
    model.save("train/{}/{}_face.h5".format(mem_id, mem_id))


    
if __name__ == '__main__':
        make_h5("dohee") # 폴더이름




