# 👤 Face Recognition System

A desktop-based Face Recognition System developed using **Python**, **OpenCV**, **face_recognition**, **PyQt5**, and **SQLite**. The application allows users to register faces, recognize previously registered faces in real-time, view registered records, and delete registered faces through a user-friendly graphical interface.

## ✨ Features

- 📸 Register a new face using the webcam
- 🧑‍💻 Recognize registered faces in real time
- 🗄️ Store person details in an SQLite database
- 🔒 Prevent duplicate face registration
- 📋 View all registered persons
- 🗑️ Delete registered faces
- 💬 Professional custom pop-up dialogs
- 🎨 Modern and attractive PyQt5 GUI
- 📊 Displays recognition status and number of detected faces

## 🛠 Technologies Used

- Python
- OpenCV
- face_recognition
- PyQt5
- SQLite
- NumPy

## 📁 Project Structure

FaceRecognitionSystem/
│
├── database/
├── encodings/
├── images/
├── custom_message.py
├── database.py
├── delete_face.py
├── gui.py
├── main.py
├── name_dialog.py
├── recognizer.py
├── register.py
├── view_window.py
├── requirements.txt
├── README.md
└── .gitignore

## 🚀 Installation

1. Clone the repository

```bash
git clone https://github.com/SiddhiDhingra/FaceRecognitionSystem.git
```

2. Open the project folder

```bash
cd FaceRecognitionSystem
```

3. Install the required packages

```bash
pip install -r requirements.txt
```

4. Run the application

```bash
python main.py
```

## 📖 How to Use

1. Click **Register New Face**.
2. Press **S** to capture your face.
3. Enter the person's name.
4. Click **Recognize Face** to identify registered users.
5. Click **View Registered Faces** to view all records.
6. Click **Delete Registered Face** to remove a registered person.

## 📸 Screenshots

Add screenshots of:
- Main GUI
- Face Registration
- Face Recognition
- Registered Persons Window


## 🔮 Future Enhancements

- Multiple face registration
- Attendance management
- Face recognition with confidence score
- User login authentication
- Cloud database integration


## 👩‍💻 Developed By

**Siddhi Dhingra**

## 📄 License

This project is developed for educational purposes.
