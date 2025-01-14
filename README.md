# 🚗💤 Driver Drowsiness Detection Using YOLOv8  

## 📝 Overview  

This project implements a **Driver Drowsiness Detection System** using **YOLOv8**. The system helps improve road safety by detecting signs of drowsiness in drivers in real time and providing alerts.  

---

## ✨ Features  

- 📂 **Custom Dataset Integration**: Uses a dataset tailored for detecting drowsiness in drivers.  
- ⚡ **YOLOv8**: Leverages YOLOv8 for fast and accurate object detection.  
- 🎥 **Real-Time Detection**: Processes live video streams using OpenCV for instant feedback.  
- ☁️ **Google Colab Support**: Includes scripts for easy training and testing on Google Colab.  
- 🚀 **Portable and Flexible**: Easily adaptable to different hardware setups.  

---

## 📊 Dataset and Preprocessing  

The dataset was prepared using **Roboflow** and labeled for driver states (e.g., drowsy, alert).  

### Steps:  
1. Download the dataset via the Roboflow API.  
2. Convert the dataset into YOLOv8 format.  
3. Split the data into training and validation sets.  

---

## 🏋️‍♂️ Training the Model  

Training was performed on Google Colab using the following steps:  

1. **📦 Installing Dependencies**: Required libraries (`ultralytics`, `roboflow`) were installed.  
2. **📚 Fine-Tuning YOLOv8**: Pretrained weights (`yolov8n.pt`) were fine-tuned on the custom dataset with the following configuration:  
   - 🖼️ Image Size: 640x640  
   - 🔄 Epochs: 100  
3. **💾 Saving Weights**: Best model weights were saved for real-time detection.  

---

## 🎥 Real-Time Detection  

Real-time detection is achieved using **OpenCV**. Key functionalities include:  
- 🖼️ Capturing live video input from a webcam.  
- 🤖 Performing model inference on each frame.  
- 🔲 Displaying results with bounding boxes on the video stream.  

---

## 🚀 How to Use  

### 1️⃣ Clone the Repository  
```bash
git clone https://github.com/your-username/driver-drowsiness-detection.git  
cd driver-drowsiness-detection  
