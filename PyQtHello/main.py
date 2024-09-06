import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QWidget()
    label = QLabel('Hello, PyQt!', window)
    label.move(50, 50)
    window.setGeometry(300, 300, 300, 200)
    window.show()
    sys.exit(app.exec_())