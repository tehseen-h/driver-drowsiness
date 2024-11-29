# -*- coding: utf-8 -*-
"""DD-New-18-Nov-2024

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/117YZgTKG_5Z1RSZL3kQofzlkF8RA5_Tk

#Downloading the dataset to colab
"""

# Commented out IPython magic to ensure Python compatibility.
# %%capture
# !pip install roboflow
# 
# from roboflow import Roboflow
# rf = Roboflow(api_key="xASvrfOl0QmZenRAZDB1")
# project = rf.workspace("augmented-startups").project("drowsiness-detection-cntmz")
# dataset = project.version(2).download("yolov8", location = "/content/datasets")

"""#Importing Yolov8 and training our Model


"""

# Commented out IPython magic to ensure Python compatibility.
# %%capture
# !pip install ultralytics

from ultralytics import YOLO

# Load a model
model = YOLO('yolov8n.pt')  # load a pretrained model (recommended for training)
# Train the model
results = model.train(data="/content/drive/MyDrive/Projects/project-dd/datasets/data.yaml", epochs=100, imgsz=640)

"""#***Copying the runs file to our google drive***"""

import locale
print(locale.getpreferredencoding())
import locale
def getpreferredencoding(do_setlocale = True):
  return "UTF-8"
locale.getpreferredencoding = getpreferredencoding

!cp -r /content/runs /content/drive/MyDrive/Projects/project-dd/

"""Load our trained file to YOLO model"""

# Commented out IPython magic to ensure Python compatibility.
# %%capture
# !pip install ultralytics
# from ultralytics import YOLO
# 
# model = YOLO('/content/drive/MyDrive/Projects/project-dd/runs/detect/train2/weights/best.pt')

"""Using OpenCV Run our model for live detection"""

import cv2
from ultralytics import YOLO

model = YOLO(r'C:\Users\Ghalib\Downloads\Driver-Drowsiness\best.pt')  # Use raw string to avoid unicode errors

# Initialize the webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open video device.")
else:
    print("Press 'q' to quit.")

try:
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        if not ret:
            print("Failed to grab frame")
            break

        # Perform detection
        results = model(frame)

        # Check if results are returned as a list
        if isinstance(results, list):
            # Render results on the frame
            frame = results[0].plot()  # Or use results[0].render() depending on the library

        # Display the resulting frame
        cv2.imshow('YOLO Live Detection', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
finally:
    # When everything is done, release the capture
    cap.release()
    cv2.destroyAllWindows()