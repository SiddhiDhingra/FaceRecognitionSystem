from PyQt5.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QLabel,
    QPushButton
)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt


class CustomMessage(QDialog):

    def __init__(self, title, message):
        super().__init__()

        self.setWindowTitle(title)

        self.setFixedSize(420, 220)

        layout = QVBoxLayout()

        layout.setSpacing(20)
        layout.setContentsMargins(25, 25, 25, 25)

        label = QLabel(message)

        label.setAlignment(Qt.AlignCenter)

        label.setWordWrap(True)

        label.setFont(QFont("Segoe UI", 13))

        button = QPushButton("OK")

        button.setFixedSize(120, 40)

        button.setFont(QFont("Segoe UI", 11, QFont.Bold))

        button.clicked.connect(self.accept)

        layout.addWidget(label)

        layout.addWidget(button, alignment=Qt.AlignCenter)

        self.setLayout(layout)

        self.setStyleSheet("""
        QDialog{
            background:white;
            border-radius:15px;
        }

        QLabel{
            color:#222;
        }

        QPushButton{
            background:#1976D2;
            color:white;
            border:none;
            border-radius:10px;
        }

        QPushButton:hover{
            background:#1565C0;
        }
        """)