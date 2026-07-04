import sqlite3
from PyQt5.QtWidgets import (
    QWidget,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
    QLabel,
    QHeaderView
)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class ViewWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Registered Persons")
        self.setFixedSize(750, 450)

        layout = QVBoxLayout()
        title = QLabel("📋 Registered Persons")

        title.setAlignment(Qt.AlignCenter)
        title.setFont(QFont("Segoe UI", 18, QFont.Bold))
        title.setStyleSheet("color:#0D47A1; margin-bottom:10px;")

        layout.addWidget(title)

        self.table = QTableWidget()
        self.message = QLabel()

        self.message.setAlignment(Qt.AlignCenter)

        self.message.setFont(QFont("Segoe UI", 18, QFont.Bold))

        self.message.setStyleSheet("color:gray;")
        self.table.setAlternatingRowColors(True)

        self.table.setEditTriggers(QTableWidget.NoEditTriggers)

        self.table.horizontalHeader().setStretchLastSection(True)

        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.table.setFont(QFont("Segoe UI", 12))

        self.table.verticalHeader().setVisible(False)

        self.table.setSelectionBehavior(QTableWidget.SelectRows)
        self.table.verticalHeader().setDefaultSectionSize(50)
        layout.addWidget(self.table)

        layout.addWidget(self.message)

        self.message.hide()


        self.setLayout(layout)
        self.setStyleSheet("""
        QWidget{
            background-color:#F4F6F9;
        }

        QTableWidget{
            background:white;
            alternate-background-color:#EEF5FF;
            gridline-color:#D6E4F0;
            border:1px solid #B0BEC5;
            font-size:12px;
        }

        QHeaderView::section{
            background-color:#1976D2;
            color:white;
            font-weight:bold;
            font-size:13px;
            padding:10px;
        }
        """)

        self.load_data()

    def load_data(self):

        conn = sqlite3.connect("database/faces.db")
        cursor = conn.cursor()

        cursor.execute("SELECT id, name, image_path FROM persons")

        records = cursor.fetchall()
        if len(records) == 0:
            self.table.hide()

            self.message.setText(
                "📂\n\nNo Registered Faces Found\n\nPlease register a face first."
            )

            self.message.show()

            conn.close()
            return
        self.message.hide()
        self.table.show()

        self.table.setRowCount(len(records))
        self.table.setColumnCount(3)

        self.table.setHorizontalHeaderLabels(
            ["ID", "Name", "Image Path"]
        )
        header = self.table.horizontalHeader()

        header.setFont(QFont("Segoe UI", 12, QFont.Bold))

        for row, record in enumerate(records):

            for column, value in enumerate(record):
                item = QTableWidgetItem(str(value))

                item.setFont(QFont("Segoe UI", 12))

                self.table.setItem(
                    row,
                    column,
                    item
                )

        conn.close()