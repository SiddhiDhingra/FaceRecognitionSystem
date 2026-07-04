from PyQt5.QtWidgets import QApplication
from gui import FaceRecognitionGUI
import sys

app = QApplication(sys.argv)

window = FaceRecognitionGUI()
window.show()

sys.exit(app.exec_())