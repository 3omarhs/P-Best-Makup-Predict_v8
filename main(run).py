import os
import sys

import face_recognition
import cv2
import numpy as np
import pickle
import tkinter as tk
from tkinter import filedialog

from subCode_files.capture import Capture
from subCode_files.inputImageButtons import IIbuttons
from subCode_files.readData import imagesData, allA, b
from subCode_files.runtypeButtons import RTbuttons

# current_run = 'train'
current_run = 'run'
# input_image = 'filePicker'
input_image = 'camShot'
mode_selected = 0   # select which mode to start run with..
# mode_selected = 1
tolerance=0.85  #un-accuracy "error" percentage
encoding_images_path = 'encoded images files'
images_path_F = 'photos/womens/'        # Train From path
images_path = ''
Female_list = []


MODEL_MEAN_VALUES = (78.4263377603, 87.7689143744, 114.895847746)
padding = 20

image = 'photos/test/img.png'






class SimpleFacerec:
    def __init__(self):
        self.known_face_encodings_f = []
        self.known_face_names_f = []
        self.frame_resizing = 0.25


    def load_encoding_images(self, images_path, category):
        print(f'{category} Images Encoding:')
        if current_run == 'train':
            for img_path in images_path:
                img = cv2.imread(img_path)  # read and show image
                rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # convert image to another color space, There are more than 150 color-space
                basename = os.path.basename(img_path)
                (filename, ext) = os.path.splitext(basename)  # split colored/multi-channel image into separate single-channel images
                filename = img_path
                try:
                    img_encoding = face_recognition.face_encodings(rgb_img)[0]  #return the 128-dimension face encoding for each face
                except:
                    1
                self.known_face_encodings_f.append(img_encoding)
                self.known_face_names_f.append(filename)
            with open(f'{encoding_images_path}/{category}_encoding.txt', "wb") as fp:  # Pickling
                pickle.dump(self.known_face_encodings_f, fp)

            with open(f'{encoding_images_path}/{category}_names.txt', "wb") as fp:  # Pickling
                pickle.dump(self.known_face_names_f, fp)
            self.known_face_encodings_f = []
            self.known_face_names_f = []
            with open(f'{encoding_images_path}/{category}_encoding.txt', "rb") as fp:  # Unpickling
                self.known_face_encodings_f = pickle.load(fp)
            with open(f'{encoding_images_path}/{category}_names.txt', "rb") as fp:  # Unpickling
                self.known_face_names_f = pickle.load(fp)
            print(f"{category} Encoding images loaded")

        else:
            with open(f'{encoding_images_path}/{category}_encoding.txt', "rb") as fp:  # Unpickling
                self.known_face_encodings_f = pickle.load(fp)
            with open(f'{encoding_images_path}/{category}_names.txt', "rb") as fp:  # Unpickling
                self.known_face_names_f = pickle.load(fp)
            print(f"{category} Encoding images loaded")

    def detect_known_faces(self, frame):
        small_frame = cv2.resize(frame, (0, 0), fx=self.frame_resizing, fy=self.frame_resizing)  # to change photo size
        rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)  # convert image to another color space, There are more than 150 color-space
        face_locations = face_recognition.face_locations(rgb_small_frame)  # bounding boxes of human faces
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)  # return the 128-dimension face encoding for each face
        face_names = []
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(self.known_face_encodings_f, face_encoding, tolerance=tolerance)  # Compare faces to see if they match
            name = "Can`t Detect"
            face_distances = face_recognition.face_distance(self.known_face_encodings_f, face_encoding)  # get distance (un-similarity) for each comparison face
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = self.known_face_names_f[best_match_index]
            else:
                print('unknown detected!!')
            if len(face_names) < 2:
                face_names.append(name)
        face_locations = np.array(face_locations)
        face_locations = face_locations / self.frame_resizing
        return face_locations.astype(int), face_names


def main_GUI():
    logo = cv2.imread('photos/ZUJ.png', cv2.IMREAD_UNCHANGED)
    logo = cv2.resize(logo, (250, 250), interpolation=cv2.INTER_AREA)
    img = cv2.imread(image, cv2.IMREAD_UNCHANGED)
    Bg = cv2.imread('photos/img.png', cv2.IMREAD_UNCHANGED)
    Bg = cv2.resize(Bg, (1000, 700), interpolation=cv2.INTER_AREA)
    face_locations, face_names = sfr.detect_known_faces(img)
    try:
        for face_loc, name in zip(face_locations, face_names):
            y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]
            cv2.putText(img, str(os.path.dirname(name).split('/')[-1].split('\\')[-1]), (x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 200), 2)  # to add text into an image
            cv2.putText(Bg, "Virtual cosmetics recommender system", (25, 55), cv2.FONT_HERSHEY_DUPLEX, 1.1, (50, 50, 50), 2)  # to add text into an image
            cv2.putText(Bg, "The best cosmetic product for you is:", (25, 130), cv2.FONT_HERSHEY_DUPLEX, 0.7, (200, 0, 0), 2)  # to add text into an image
            cv2.putText(Bg, "Before:", (600, 410), cv2.FONT_HERSHEY_DUPLEX, 0.7, (10, 10, 10), 2)  # to add text into an image
            cv2.putText(Bg, "After:", (800, 410), cv2.FONT_HERSHEY_DUPLEX, 0.7, (10, 10, 10), 2)  # to add text into an image
            cv2.putText(Bg, "And here is a picture of the", (600, 300), cv2.FONT_HERSHEY_DUPLEX, 0.7, (0, 0, 0), 2)  # to add text into an image
            cv2.putText(Bg, "person who looks like you the", (600, 330), cv2.FONT_HERSHEY_DUPLEX, 0.7, (0, 0, 0), 2)  # to add text into an image
            cv2.putText(Bg, "most use this product:", (600, 360), cv2.FONT_HERSHEY_DUPLEX, 0.7, (0, 0, 0), 2)  # to add text into an image
            name = name.split('/')[0]+'\\'+name.split('/')[-1]
            collectedPath = ''
            for i in range(len(name.split('\\'))-1):
                collectedPath += name.split('\\')[i]+"\\"
            aft_ImgName = cv2.imread(name.replace('\\','/'), cv2.IMREAD_UNCHANGED)
            bef_ImgName = cv2.imread(name.replace('after', 'before').replace('\\','/'), cv2.IMREAD_UNCHANGED)
            aft_ImgName = cv2.resize(aft_ImgName, (120, 240), interpolation=cv2.INTER_AREA)
            bef_ImgName = cv2.resize(bef_ImgName, (120, 240), interpolation=cv2.INTER_AREA)
            brand = collectedPath[:]+'brand.jpg'
            brand = brand.replace('\\','/')
            brImg = cv2.imread(brand, cv2.IMREAD_UNCHANGED)
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 0, 200), 3)  # draw rectangle on photo “usually used for face boundaries”

            h, w, o = img.shape
            if h < 250 or w < 250:
                resized = cv2.resize(img, (w * 2, h * 2), interpolation=cv2.INTER_AREA)
            elif h < 400 or w < 400:
                frame = img
            else:
                resized = cv2.resize(img, (int(w / 2), int(h / 2)), interpolation=cv2.INTER_AREA)

        Bg[0:0+250, 750:750+250] = logo[:, :, 0:3]
        try: Bg[150:150+130, 50:50+375] = brImg
        except: Bg[150:150+130, 50:50+375, 2] = brImg
        try: Bg[350:350+int(h), 120:120+int(w)] = resized[:,:,:3]
        except:
            try: Bg[350:350+int(h*2), 120:120+int(w*2)] = resized[:,:,:3]
            except: Bg[350:350+int(h/2), 120:120+int(w/2)] = resized[:,:,:3]
        Bg[420:420+240, 600:600+120] = bef_ImgName
        Bg[420:420+240, 800:800+120] = aft_ImgName
    except:
        Bg = cv2.imread('photos/img.png', cv2.IMREAD_UNCHANGED)
        Bg = cv2.resize(Bg, (1000, 700), interpolation=cv2.INTER_AREA)
        cv2.putText(Bg, "Sorry Try another image in which the face becomes clearer!", (40, 250), cv2.FONT_HERSHEY_DUPLEX, 0.9, (0, 0, 0),2)  # to add text into an image
        img = cv2.resize(img, (int(img.shape[1]/2), int(img.shape[0]/2) ), interpolation=cv2.INTER_AREA)
        cv2.putText(img, "Unknown!", (int(img.shape[0]/2), 25), cv2.FONT_HERSHEY_DUPLEX, 0.6, (0, 0, 200),1)  # to add text into an image
        Bg[int(350-(img.shape[0]/2)*0.25):int(350-(img.shape[0]/2)*0.25)+int(240), int(500-img.shape[1]/2):int(500-img.shape[1]/2)+int(320)] = img

    cv2.imshow("3omar.hs Detection..", Bg)  # read and show image
    cv2.waitKey(0)  # read and show image
    cv2.destroyAllWindows()


val = RTbuttons.getbuttonPressed()
print(val)
if val == 1:
    current_run = 'train'
elif val == 2:
    current_run = 'run'
else:
    sys.exit(1)

val1 = IIbuttons.getbuttonPressed()
print(val1)
if val1 == 1:
    input_image = 'camShot'
elif val1 == 2:
    input_image = 'filePicker'
else:
    sys.exit(1)
if input_image == 'filePicker':
    tk.Tk().withdraw()
    image = filedialog.askopenfilename()
elif input_image == 'camShot':
    image = Capture.Image()
imagesData()
sfr = SimpleFacerec()
for i in range(len(list(b))):
    sfr.load_encoding_images(allA, list(b)[i])
try:
    main_GUI()
except: 1