from keras.utils.np_utils import to_categorical

import keras
import cv2
import numpy as np
from FACE_LOGIN3.face.mesh_line_np import meshnp

def predict(mem_id):
    img = meshnp('mem_image/{}/login.jpg'.format(mem_id))
    resize_img = np.reshape(img,(1,478,3))
    model = keras.models.load_model("train/{}/{}_face.h5".format(mem_id, mem_id))
    predictions = model.predict(resize_img)
    
    print(resize_img)
    print(predictions[0])
    print(np.argmax(predictions[0]))
    
    return np.argmax(predictions[0])

if __name__ == '__main__':
    predict("dohee")




