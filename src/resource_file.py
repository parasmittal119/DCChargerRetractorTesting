import getpass
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QPushButton, QVBoxLayout, QLabel


class FileDialogExample(QWidget):
    def __init__(self):
        super().__init__()

        # self.initUI()

    def initUI(self):
        self.setWindowTitle('File Dialog Example')

        layout = QVBoxLayout()

        self.label = QLabel('Selected File: No file selected')
        layout.addWidget(self.label)


        button = QPushButton('Open File Dialog', self)
        layout.addWidget(button)

        self.setLayout(layout)

    def showDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_dialog = QFileDialog()
        file_dialog.setOptions(options)
        account_user = getpass.getuser()
        fileName, _ = file_dialog.getOpenFileName(self, 'Open Database File', r'\\SLICE\\Data_Share_Temp', 'Database Files (*.db *.sqlite *.sqlite3);;All Files (*)')
        if fileName:
            # Display the selected file location and name
            with open(f"C:/Users/{account_user}/AppData/Local/retractorDBLocation/source.txt", "w") as file:
                file.write(fileName)
            file.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = FileDialogExample()
    ex.show()
    sys.exit(app.exec_())