import psutil
import time
from PySide6 import QtWidgets, QtCore
from PySide6.QtGui import QIcon


class SystemMonitor(QtCore.QThread):
    system_info = QtCore.Signal(list)

    def run(self):
        while True:
            time.sleep(0.5)
            self.system_info.emit(psutil.cpu_percent(percpu=True))


class SystemWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUi()

    def initUi(self) -> None:
        self.system_value = QtWidgets.QProgressBar()
        self.system_value.setRange(0, 100)
        self.system_value.setOrientation(QtCore.Qt.Orientation.Vertical)
        self.system_value.setSizePolicy(
            QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)

        self.system_label = QtWidgets.QLabel()

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.system_value)
        layout.addWidget(self.system_label)

        self.setLayout(layout)

    def setValue(self, value: int) -> None:
        self.system_value.setValue(value)

    def setText(self, text: str) -> None:
        self.system_label.setText(text)


class CPU_Core_Monitor(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.initUI()
        self.initThreads()

    def initUI(self) -> None:
        self.setWindowTitle("мониторинг системы")
        self.setWindowIcon(QIcon('icon.png'))
        layout = QtWidgets.QHBoxLayout()

        for _ in range(psutil.cpu_count()):
            layout.addWidget(SystemWidget(self))

        self.setLayout(layout)

    def initThreads(self) -> None:
        self.systemMonitor = SystemMonitor()
        self.systemMonitor.start()
        self.systemMonitor.system_info.connect(self.updateSystemWidget)

    def updateSystemWidget(self, cpu_percent_list: list) -> None:
        layout = self.layout()

        for cpu_count in range(layout.count()):
            widget_link = layout.itemAt(cpu_count).widget()

            widget_link.setValue(cpu_percent_list[cpu_count])
            widget_link.setText(f"CPU №{cpu_count + 1} - {cpu_percent_list[cpu_count]}%")


if __name__ == '__main__':
    app = QtWidgets.QApplication()

    win = CPU_Core_Monitor()
    win.show()

    app.exec()
