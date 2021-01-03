from PyQt5 import QtWidgets
from schema import Ui_MainWindow
import sys
from operations import *

class CalculatorWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    first_number = None
    second_number = None
    operation = None
    is_second_digit = False

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(Ui_MainWindow)
        self.setupUi(self)


        self.pushButton_zero.clicked.connect(self.digit_pressed)
        self.pushButton_1.clicked.connect(self.digit_pressed)
        self.pushButton_2.clicked.connect(self.digit_pressed)
        self.pushButton_3.clicked.connect(self.digit_pressed)
        self.pushButton_4.clicked.connect(self.digit_pressed)
        self.pushButton_5.clicked.connect(self.digit_pressed)
        self.pushButton_6.clicked.connect(self.digit_pressed)
        self.pushButton_7.clicked.connect(self.digit_pressed)
        self.pushButton_8.clicked.connect(self.digit_pressed)
        self.pushButton_9.clicked.connect(self.digit_pressed)
        self.pushButton_dot.clicked.connect(self.decimal_pressed)

        self.pushButton_plus.clicked.connect(self.binary_operation_pressed)
        self.pushButton_minus.clicked.connect(self.binary_operation_pressed)
        self.pushButton_multiply.clicked.connect(self.binary_operation_pressed)
        self.pushButton_divide.clicked.connect(self.binary_operation_pressed)

        self.pushButton_equal.clicked.connect(self.equal_pressed)
        self.pushButton_clear.clicked.connect(self.clear_pressed)


    def digit_pressed(self):
        button = self.sender()

        if (self.operation and not self.is_second_digit):
            new_label = format(float(button.text()), '.15g')
            self.is_second_digit = True
        else:
            if ('.' in self.label.text()) and (button.text() == '0'):
                new_label = format(self.label.text() + button.text(), '.15')
            else:
                new_label = format(float(self.label.text() + button.text()), '.15g')

        self.label.setText(new_label)

    def decimal_pressed(self):
        if '.' in self.label.text():
            pass

        else:
            self.label.setText(self.label.text() + '.')

    def binary_operation_pressed(self):
        button = self.sender()

        self.first_number = float(self.label.text())

        self.operation = button.text()

    def equal_pressed(self):
        self.second_number = float(self.label.text())

        result = calculate(entry=f'{self.first_number}{self.operation}{self.second_number}')

        new_label = format(result, '.15g')

        self.label.setText(new_label)

        self.is_second_digit = False

    def clear_pressed(self):
        self.first_number = None
        self.second_number = None
        self.operation = None
        self.is_second_digit = False

        self.label.setText("0")