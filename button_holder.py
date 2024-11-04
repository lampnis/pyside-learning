from PySide6.QtWidgets import QMainWindow, QPushButton

# Subclass QMainWindow to customize your applications main window
class ButtonHolder(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Dollars game!!!")
        button = QPushButton("+1 $")
        self.button = button
        # set our button as the central widget!!
        self.setCentralWidget(button)