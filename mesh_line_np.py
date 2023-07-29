import cv2
import numpy as np
import mediapipe as mp


def meshnp(imgsrc):
    IMAGE_FILE = imgsrc
    mp_face_mesh = mp.solutions.face_mesh

    with mp_face_mesh.FaceMesh(
            static_image_mode=True,
            max_num_faces=1,
            refine_landmarks=True,
            min_detection_confidence=0.5) as face_mesh:

        image = cv2.imread(IMAGE_FILE)
        results = face_mesh.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

        if not results.multi_face_landmarks:
            exit()
        face_landmarks = results.multi_face_landmarks[0]
        coordinate = []
        
        for landmark in face_landmarks.landmark:
            coordinate.append((landmark.x, landmark.y, landmark.z))
        
        # print(coordinate)
        # print(len(coordinate))
        # print(np.array(coordinate))
        
    return coordinate


    
if __name__ == '__main__':
    meshnp('cha.jpg')

