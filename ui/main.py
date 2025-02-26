from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
import sys

class AimbotUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("YOLO Aimbot 控制面板")
        self.setGeometry(100, 100, 300, 200)

        self.start_btn = QPushButton("啟動 Aimbot", self)
        self.stop_btn = QPushButton("停止 Aimbot", self)

        layout = QVBoxLayout()
        layout.addWidget(self.start_btn)
        layout.addWidget(self.stop_btn)
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AimbotUI()
    window.show()
    sys.exit(app.exec_())

