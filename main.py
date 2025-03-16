# Lesson 1: Intro

# from PySide6.QtWidgets import QApplication, QWidget
# import sys
# app = QApplication(sys.argv)
# window = QWidget()
# window.show()
# app.exec()
# Lesson 2: separating in the classes!!!

# from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

# import sys
# app = QApplication(sys.argv)

# window = QMainWindow()
# window.setWindowTitle("Our first MainWindow App!")

# button = QPushButton()
# button.setText("Ok")

# window.setCentralWidget(button)

# window.show()
# app.exec()

#  can separate the previous messy global scope code into clases, for example:

# import sys
# from PySide6.QtWidgets import QApplication, QPushButton, QMainWindow

# # Subclass QMainWindow to customize your applications main window
# class ButtonHolder(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Button Holder app")
#         button = QPushButton("Press me!")
#         # set our button as the central widget!!
#         self.setCentralWidget(button)

# app = QApplication(sys.argv)
# window = ButtonHolder()
# window.show()
# app.exec()

# We can also save the whole button class in a different file and then import
# from there!!!

# import sys
# from PySide6.QtWidgets import QApplication
# from button_holder import ButtonHolder

# app = QApplication(sys.argv)
# window = ButtonHolder()
# window.show()
# app.exec()

# Lesson 3: Signals and Slots !!

# import sys
# from PySide6.QtWidgets import QApplication
# from button_holder import ButtonHolder

# balance = 1
# def button_clicked(data): #checks if button is clicked/unclicked
#     global balance
#     balance += 1
#     print(f"Current Balance: ${balance}.00 USD", data)

# app = QApplication(sys.argv)
# window = ButtonHolder()
# window.button.clicked.connect(button_clicked)
# window.button.setCheckable(True)
# window.show()
# app.exec()

# QtCore and QSlider

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QSlider


def respond_to_slider(data):
    print(f"Slider moved to: {data}")


app = QApplication()
slider = QSlider(Qt.Horizontal)
slider.setMinimum(1)
slider.setMaximum(100)
slider.setValue(25)

slider.valueChanged.connect(respond_to_slider)
slider.show()
app.exec()
