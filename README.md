# Face Detection using OpenCV (Python)

## 📌 Project Description

This project is a real-time Face Detection application built using Python and OpenCV. It uses the webcam to detect human faces and draws a rectangle around each detected face while displaying the face number on the screen.

The application uses OpenCV's pre-trained Haar Cascade Classifier for frontal face detection.

---

## 🚀 Features

- Real-time face detection using webcam
- Detects multiple faces simultaneously
- Draws a green rectangle around each detected face
- Displays face numbers (Face 1, Face 2, ...)
- Shows the total number of detected faces in the console
- Exit the application by pressing the **ESC** key

---

## 🛠️ Technologies Used

- Python 3.x
- OpenCV (cv2)
- NumPy

---

## 📂 Project Structure

```
Face-Detection/
│
├── facedet.py
├── haarcascade_frontalface_default.xml
├── README.md
```

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/Face-Detection.git
```

### 2. Move into the project folder

```bash
cd Face-Detection
```

### 3. Install the required packages

```bash
pip install opencv-python numpy
```

---

## ▶️ Run the Project

Execute the following command:

```bash
python facedet.py
```

Your webcam will open and begin detecting faces.

Press **ESC** to close the application.

---

## 📖 How It Works

1. Opens the webcam.
2. Captures each video frame.
3. Converts the frame to grayscale.
4. Uses the Haar Cascade classifier to detect faces.
5. Draws a rectangle around every detected face.
6. Labels each detected face with its face number.
7. Displays the processed video in real time.

---

## 📸 Sample Output

- Green rectangle around each face.
- Labels such as:
  - Face 1
  - Face 2
  - Face 3
- Number of detected faces printed in the terminal.

---

## 📚 Future Improvements

- Save detected faces as images
- Face recognition using LBPH or Deep Learning
- Face attendance system
- Emotion detection
- Age and gender prediction
- Face mask detection

---

## 👨‍💻 Author

**Mohamed Shafi**

B.Tech Artificial Intelligence & Machine Learning Student

---

## 📄 License

This project is for educational and learning purposes.
