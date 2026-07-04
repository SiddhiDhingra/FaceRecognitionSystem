from PyQt5.QtWidgets import (
    QDialog,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout
)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt


class NameDialog(QDialog):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Register New Face")
        self.setFixedSize(420, 220)

        layout = QVBoxLayout()

        title = QLabel("👤 Register New Face")
        title.setAlignment(Qt.AlignCenter)
        title.setFont(QFont("Segoe UI", 16, QFont.Bold))

        label = QLabel("Enter Person Name")
        label.setFont(QFont("Segoe UI", 11))

        self.name_edit = QLineEdit()
        self.name_edit.setPlaceholderText("Example: Siddhi")

        ok_btn = QPushButton("Save")
        cancel_btn = QPushButton("Cancel")

        ok_btn.clicked.connect(self.accept)
        cancel_btn.clicked.connect(self.reject)

        button_layout = QHBoxLayout()
        button_layout.addWidget(cancel_btn)
        button_layout.addWidget(ok_btn)

        layout.addWidget(title)
        layout.addSpacing(10)
        layout.addWidget(label)
        layout.addWidget(self.name_edit)
        layout.addStretch()
        layout.addLayout(button_layout)

        self.setLayout(layout)

        self.setStyleSheet("""
        QDialog{
            background:#F4F6F9;
        }

        QLabel{
            color:#0D47A1;
        }

        QLineEdit{
            padding:8px;
            font-size:12px;
            border:2px solid #1976D2;
            border-radius:8px;
        }

        QPushButton{
            background:#1976D2;
            color:white;
            border:none;
            border-radius:8px;
            padding:8px;
            font-weight:bold;
        }

        QPushButton:hover{
            background:#1565C0;
        }
        """)