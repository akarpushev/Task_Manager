from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QTextEdit
import psutil


class HdMonitor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 800, 600)

        self.initUI()

    def initUI(self):
        self.main_widget = QWidget(self)
        self.setCentralWidget(self.main_widget)
        self.layout = QVBoxLayout(self.main_widget)

        self.layout = QTextEdit(self.main_widget)
        self.layout.setGeometry(100, 100, 500, 300)

        self.layout.setText(f"количество HD: {len(psutil.disk_partitions())}\n\n"
                            f"{psutil.disk_partitions()}\n\n")


if __name__ == "__main__":
    app = QApplication()
    window = HdMonitor()
    window.show()
    app.exec()
