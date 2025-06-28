# Human Movement Detection using OpenCV

This is a Python-based project that detects human movement in a pre-recorded video using OpenCV's background subtraction technique.

## 📹 Overview

The script processes each frame of a video, applies background subtraction, detects contours (moving objects), and draws bounding boxes around them to highlight motion.

## 🧠 Features

* Loads and plays a local video file
* Detects moving objects using MOG2 background subtraction
* Draws bounding boxes on detected motion areas
* Displays both the processed frame and foreground mask in real-time
* Exits the program on pressing the `q` key

## 🛠️ Technologies Used

* Python
* OpenCV


### Install dependencies:

```bash
pip install opencv-python
```

## 📁 Project Structure

```
human_movement_detection/
│
├── main.py         # Main Python script for movement detection
├── README.md       # Project documentation
└── .gitignore      # To ignore large files like videos
```

## 🚀 How to Run the Project

1. **Clone the Repository**

```bash
git clone https://github.com/your-username/human_movement_detection.git
cd human_movement_detection
```

2. **Add your video**

   * Place your video (e.g. `samplevdo.mp4`) in the project directory.
   * Update the path in `main.py` if needed:

     ```python
     video = cv2.VideoCapture("samplevdo.mp4")
     ```

3. **Run the Python Script**

```bash
python main.py
```

4. **Exit**

   * Press `q` to quit the video window.



## 📷 Output Example

* Bounding boxes drawn around moving objects
* Real-time display of processed video and foreground mask

