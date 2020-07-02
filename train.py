import os 
from PIL import Image
import numpy as np
import cv2
import pickle
import dlib
def trainning(name_folder):
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    image_dir = os.path.join(BASE_DIR,"Database\Dataset\ " + name_folder)

    detector = dlib.get_frontal_face_detector()
    recognizer = cv2.face.LBPHFaceRecognizer_create()

    vitriID = 0
    TenID = {}
    x_train = []
    y_labels = []

    for root, dirs, files in os.walk(image_dir):
        for file in files:
            if file.endswith("png") or file.endswith("jpg"):
                path = os.path.join(root,file)
                label = os.path.basename(root).replace(" ", "-").lower()
                print(label, path)
                if not label in TenID:
                    TenID[label] = vitriID
                    vitriID +=1
                id_ = TenID[label]

                pil_image = Image.open(path).convert("L")
                image_array = np.array(pil_image,"uint8")
                print(image_array)
                faces = detector(image_array)
                
                for face in faces:

                    x1 = face.left()
                    y1 = face.top()
                    x2 = face.right()
                    y2 = face.bottom()

                    roi = image_array[y1:y2,x1:x2]
                    x_train.append(roi)
                    y_labels.append(id_)


    with open("labels.pickle", 'wb') as f:
        pickle.dump(TenID, f)

    recognizer.train(x_train, np.array(y_labels))
    a = name_folder + ".yml"
    print(a)
    recognizer.save(a)
 

