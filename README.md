🚗💤 Driver Drowsiness Detection Using YOLOv8
📝 Overview
This project implements a Driver Drowsiness Detection System using YOLOv8. The system helps improve road safety by detecting signs of drowsiness in drivers in real time and providing alerts.

✨ Features
📂 Custom Dataset Integration: Uses a dataset tailored for detecting drowsiness in drivers.
⚡ YOLOv8: Leverages YOLOv8 for fast and accurate object detection.
🎥 Real-Time Detection: Processes live video streams using OpenCV for instant feedback.
☁️ Google Colab Support: Includes scripts for easy training and testing on Google Colab.
🚀 Portable and Flexible: Easily adaptable to different hardware setups.
📊 Dataset and Preprocessing
The dataset was prepared using Roboflow and labeled for driver states (e.g., drowsy, alert).

Steps:
1️⃣ Download the dataset via the Roboflow API.
2️⃣ Convert the dataset into YOLOv8 format.
3️⃣ Split the data into training and validation sets.

🏋️‍♂️ Training the Model
Training was performed on Google Colab using the following steps:

📦 Installing Dependencies: Required libraries (ultralytics, roboflow) were installed.
📚 Fine-Tuning YOLOv8: Pretrained weights (yolov8n.pt) were fine-tuned on the custom dataset with the following configuration:
🖼️ Image Size: 640x640
🔄 Epochs: 100
💾 Saving Weights: Best model weights were saved for real-time detection.
🎥 Real-Time Detection
Real-time detection is achieved using OpenCV. Key functionalities include:

🖼️ Capturing live video input from a webcam.
🤖 Performing model inference on each frame.
🔲 Displaying results with bounding boxes on the video stream.
🚀 How to Use
1️⃣ Clone the Repository
bash
Copy code
git clone https://github.com/tehseen-h/driver-drowsiness.git  
cd driver-drowsiness-detection  
2️⃣ Install Dependencies
Make sure Python is installed, then install required packages:

bash
Copy code
pip install -r requirements.txt  
3️⃣ Run Real-Time Detection
Connect a webcam and execute the detection script:

bash
Copy code
python detect_drowsiness.py  
📂 Code Highlights
🧠 Training YOLOv8
python
Copy code
from ultralytics import YOLO  

# Load a pretrained YOLOv8 model  
model = YOLO('yolov8n.pt')  

# Train the model on the custom dataset  
results = model.train(data='/path/to/data.yaml', epochs=100, imgsz=640)  
🎥 Real-Time Detection
python
Copy code
import cv2  
from ultralytics import YOLO  

model = YOLO('path/to/best.pt')  # Load trained model weights  

cap = cv2.VideoCapture(0)  # Initialize webcam  

while True:  
    ret, frame = cap.read()  
    if not ret:  
        break  

    # Perform detection  
    results = model(frame)  

    # Display results  
    frame = results[0].plot()  
    cv2.imshow('Driver Drowsiness Detection', frame)  

    if cv2.waitKey(1) & 0xFF == ord('q'):  
        break  

cap.release()  
cv2.destroyAllWindows()  
📈 Results
✅ Accuracy: Achieved high accuracy in detecting driver drowsiness.
⚡ Performance: Real-time detection with minimal latency.
🔮 Future Improvements
🔊 Add audio/visual alerts for detected drowsiness.
🤖 Optimize the system for embedded devices like Raspberry Pi.
🛠️ Extend functionality to analyze other driver behaviors.
🤝 Contributing
Contributions are welcome! Feel free to submit a pull request or open an issue to suggest improvements.

