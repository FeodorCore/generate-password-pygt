import sys
import random
import string
from PyQt5 import QtCore, QtGui, QtWidgets
from pattern_2 import Ui_MainWindow

class PasswordGenerator(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setup_initial_values()

        self.connect_signals()

        self.original_text = self.ui.pushButton_2.text()
        self.original_icon = self.ui.pushButton_2.icon()

    def setup_initial_values(self):
        self.ui.horizontalSlider.setMinimum(4)
        self.ui.horizontalSlider.setMaximum(100)
        self.ui.horizontalSlider.setValue(4)

        self.ui.checkBox_4.setChecked(True)
        self.ui.checkBox_3.setChecked(True)
        self.ui.checkBox_2.setChecked(True)

        self.update_length_display()

    def connect_signals(self):
        self.ui.pushButton.clicked.connect(self.generate_password)

        self.ui.pushButton_2.clicked.connect(self.copy_to_clipboard)

        self.ui.horizontalSlider.valueChanged.connect(self.update_length_display)

    def update_length_display(self):
        length = self.ui.horizontalSlider.value()
        self.ui.label_3.setText(f"Количество символов: {length}")

    def generate_password(self):
        length = self.ui.horizontalSlider.value()

        characters = ""

        if self.ui.checkBox_2.isChecked():
            characters += string.digits

        if self.ui.checkBox.isChecked():
            characters += "!@#$%^&*()_+-=[]{}|;:,.<>?"

        if self.ui.checkBox_4.isChecked():
            characters += string.ascii_lowercase

        if self.ui.checkBox_3.isChecked():
            characters += string.ascii_uppercase

        if not characters:
            self.ui.lineEdit.setText("Выберите хотя бы один тип символов")
            return

        password = ''.join(random.choice(characters) for i in range(length))

        self.ui.lineEdit.setText(password)

    def copy_to_clipboard(self):
        password = self.ui.lineEdit.text()
        if password:
            clipboard = QtWidgets.QApplication.clipboard()
            clipboard.setText(password)

            self.ui.pushButton_2.setText("✓")
            self.ui.pushButton_2.setIcon(QtGui.QIcon())

            QtCore.QTimer.singleShot(200, lambda: self.restore_copy_button(self.original_text, self.original_icon))
        else:
            self.ui.lineEdit.setText("Сначала сгенерируйте пароль")

    def restore_copy_button(self, text, icon):
        self.ui.pushButton_2.setText(text)
        self.ui.pushButton_2.setIcon(icon)


def main():
    app = QtWidgets.QApplication(sys.argv)

    app.setStyle('Fusion')

    window = PasswordGenerator()
    window.setWindowTitle("Генератор паролей")
    window.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()