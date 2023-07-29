import os
import cv2
import numpy as np
from FACE_LOGIN3.face.mesh_line_np import meshnp

def pic2num(mem_id):
    arr_y = []
    arr_path = []
    
    x_np = np.array([])
    y_np = None
    
    default_dirs = os.listdir("default_image/")
    user_dirs = os.listdir("mem_image/{}".format(mem_id))

    
    for d in default_dirs:
        default_path_sub = "default_image/" + d
    
        arr_path.append(default_path_sub)
        arr_y.append(0)    


    for d in user_dirs:
        user_path_sub = "mem_image/{}/".format(mem_id) + d
    
        arr_path.append(user_path_sub)
        arr_y.append(1)
    
    
    for idx,y in enumerate(arr_y):
        img = meshnp(arr_path[idx])
        x_np = np.append(x_np, img)
        
        
    
    
    x_np = np.reshape(x_np,(len(arr_path),478,3))
    y_np = np.array(arr_y)  
    
    np.save("train/{}/x_train".format(mem_id),x_np)
    np.save("train/{}/y_train".format(mem_id),y_np)
    
    print("x_np : ",x_np.shape,x_np)
    print("y_np : ",y_np)
    
    print(len(arr_path))
    print(len(y_np))
    
    
if __name__ == '__main__':
        pic2num("1") # 폴더이름
