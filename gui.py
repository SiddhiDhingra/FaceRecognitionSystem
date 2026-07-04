from register import RegisterFace
from recognizer import FaceRecognizer
from view_window import ViewWindow
from delete_face import delete_person
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QFrame
from custom_message import CustomMessage
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QPushButton,
    QLabel,
    QVBoxLayout,
    QInputDialog,

)
import sys


class FaceRecognitionGUI(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Face Recognition System")

        self.setFixedSize(700, 650)

        layout = QVBoxLayout()

        layout.setSpacing(20)
        layout.setContentsMargins(40, 30, 40, 30)

        title = QLabel("👤 Face Recognition System")
        title.setAlignment(Qt.AlignCenter)
        title.setFont(QFont("Segoe UI", 24, QFont.Bold))
        title.setStyleSheet("color:#0D47A1;")

        subtitle = QLabel("Secure • Fast • Smart")
        subtitle.setAlignment(Qt.AlignCenter)
        subtitle.setFont(QFont("Segoe UI", 11))
        subtitle.setStyleSheet("color:gray; margin-bottom:15px;")

        layout.addWidget(title)
        layout.addWidget(subtitle)
        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        line.setStyleSheet("color:#1976D2;")
        layout.addWidget(line)







        self.register_btn = QPushButton("📸 Register New Face")
        layout.addWidget(self.register_btn, alignment=Qt.AlignCenter)

        self.recognize_btn = QPushButton("🔍 Recognize Face")
        layout.addWidget(self.recognize_btn, alignment=Qt.AlignCenter)

        self.view_btn = QPushButton("📋 View Registered Faces")
        layout.addWidget(self.view_btn, alignment=Qt.AlignCenter)

        self.delete_btn = QPushButton("🗑 Delete Registered Face")
        layout.addWidget(self.delete_btn, alignment=Qt.AlignCenter)
        layout.addSpacing(15)

        self.exit_btn = QPushButton("🚪 Exit")
        self.exit_btn.setObjectName("exitButton")
        layout.addWidget(self.exit_btn, alignment=Qt.AlignCenter)



        self.register_btn.setFixedSize(350, 50)
        self.recognize_btn.setFixedSize(350, 50)
        self.view_btn.setFixedSize(350, 50)
        self.delete_btn.setFixedSize(350, 50)
        self.exit_btn.setFixedSize(350, 50)

        self.register_btn.clicked.connect(self.register_face)
        self.recognize_btn.clicked.connect(self.recognize_face)
        self.view_btn.clicked.connect(self.show_registered_faces)
        self.delete_btn.clicked.connect(self.delete_face)
        self.exit_btn.clicked.connect(self.close)

        self.setStyleSheet("""
        QWidget{
            background-color:#F4F6F9;
        }

        QLabel{
            color:#0D47A1;
        }

        QPushButton{
            background-color:#1976D2;
            color:white;
            border:none;
            border-radius:15px;
            padding:12px;
            font-size:15px;
            font-weight:bold;
        }

        QPushButton:hover{
            background-color:#1565C0;
            border:2px solid #64B5F6;
        }

        QPushButton:pressed{
            background-color:#0D47A1;
        }

        QPushButton#exitButton{
            background-color:#D32F2F;
        }

        QPushButton#exitButton:hover{
            background-color:#B71C1C;
        }

        QPushButton#exitButton:pressed{
            background-color:#8B0000;
        }
        """)
        footer = QLabel("Version 1.0 | Developed by Siddhi Dhingra")
        footer.setAlignment(Qt.AlignCenter)
        footer.setFont(QFont("Segoe UI", 9))
        footer.setStyleSheet("color:gray;")
        layout.addWidget(footer)

        self.setLayout(layout)

    def show_message(self, title, message):

        popup = CustomMessage(title, message)

        popup.exec_()

    def register_face(self):

        obj = RegisterFace()

        result = obj.open_camera()

        if result == "success":

            recognizer = FaceRecognizer()
            recognizer.create_encodings()

            self.show_message(
                "Success",
                "Face registered successfully!"

            )

        elif result == "duplicate":

            self.show_message(
                "Duplicate Face",
                "This face is already registered!"

            )

        elif result == "no_face":

            self.show_message(
                "No Face Detected",
                "No face was detected. Please try again."

            )

        elif result == "camera_error":

            self.show_message(
                "Camera Error",
                "Unable to open the camera."

            )



    def recognize_face(self):
        obj = FaceRecognizer()
        obj.recognize_faces()

    def show_registered_faces(self):
        self.view_window = ViewWindow()
        self.view_window.show()

    def delete_face(self):

        name, ok = QInputDialog.getText(
            self,
            "Delete Person",
            "Enter Person Name:"
        )

        if ok and name:

            success = delete_person(name)

            if success:
                self.show_message(
                    "Success",
                    "Person deleted successfully!",

                )
            else:
                self.show_message(
                    "Error",
                    "Person not found!",

                )
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FaceRecognitionGUI()
    window.show()
    sys.exit(app.exec_())