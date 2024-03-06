import datetime
import time

from PyQt5 import QtCore, QtGui, QtWidgets
from database_file import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import os
import platform



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1932, 1000)  # 1932, 1000
        self.frame = QtWidgets.QFrame(MainWindow)
        self.frame.setGeometry(QtCore.QRect(10, 10, 750, 1000))  # 1911, 980
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.Report_Search = QtWidgets.QFrame(self.frame)
        self.Report_Search.setGeometry(QtCore.QRect(10, 20, 741, 961))
        self.Report_Search.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Report_Search.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Report_Search.setObjectName("Report_Search")

        self.Report_Search_Box = QtWidgets.QGroupBox(self.Report_Search)

        self.Report_Search_Box.setGeometry(250, 330, 300, 300)

        # self.Report_Search_Box.setGeometry(QtCore.QRect(0, 10, 741, 941))
        self.Report_Search_Box.setStyleSheet(
            "color: white ; background-color: #376888 ;border: 3px solid white; border-radius: 30px;")
        self.Report_Search_Box.setTitle("")
        self.Report_Search_Box.setObjectName("Report_Search_Box")

        self.closeButton = QtWidgets.QPushButton(self.Report_Search)
        self.closeButton.setGeometry(QRect(655, 55, 50, 30))
        self.closeButton.setText("X")
        font = QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.closeButton.setFont(font)
        self.closeButton.setStyleSheet("QPushButton{background-color: qlineargradient(spread:pad, x1:0.142045, y1:0.148, x2:1, y2:1, stop:0 rgba(255, 0, 0, 255), stop:0.704545 rgba(144, 0, 0, 255));"
                                       "border:rgba(170,0,250,255);border-radius:15px;}"
                                       "\n\n\n"
                                       "QPushButton::hover{background-color: qlineargradient(spread:pad, x1:0.142045, y1:0.148, x2:1, y2:1, stop:0 rgba(255, 0, 0, 255), stop:0.704545 rgba(144, 0, 0, 255));"
                                       "border:rgba(170,0,250,255);border-radius:15px;}\n\n\n"
                                       "QPushButton::pressed{padding-top:10px;padding-up:5px;background-color: qlineargradient(spread:pad, x1:0.142045, y1:0.148, x2:1, y2:1, stop:0 rgba(255, 0, 0, 255), "
                                       "stop:0.704545 rgba(144, 0, 0, 255));}")
        self.closeButton.clicked.connect(self.closeFunction)
        self.start_time_label = QtWidgets.QLabel(self.Report_Search_Box)
        self.start_time_label.setGeometry(QtCore.QRect(20, 120, 301, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.start_time_label.setFont(font)
        self.start_time_label.setStyleSheet("color: white ; ;border: 3px solid  #7194ab; border-radius: 20px;\n"
                                            "background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(55, 104, 136, 255), stop:0.615819 rgba(179, 198, 210, 255), stop:0.99 rgba(179, 198, 210, 255) stop:1 rgba(255, 255, 255, 255));")
        self.start_time_label.setObjectName("start_time_label")

        self.End_dateEdit = QtWidgets.QDateEdit(self.Report_Search_Box)
        self.End_dateEdit.setGeometry(QtCore.QRect(480, 120, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.End_dateEdit.setFont(font)
        self.End_dateEdit.setStyleSheet("color: white ; ;border: none; border-radius: 20px;background-color: rgba(0,0,0,0);")
        self.End_dateEdit.setWrapping(False)
        self.End_dateEdit.setFrame(False)
        self.End_dateEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.End_dateEdit.setReadOnly(False)
        self.End_dateEdit.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.End_dateEdit.setKeyboardTracking(True)
        self.End_dateEdit.setCalendarPopup(True)
        self.End_dateEdit.setObjectName("End_dateEdit")
        self.End_dateEdit.setDate(QDate(datetime.datetime.now().date().year, datetime.datetime.now().date().month, datetime.datetime.now().date().day))

        self.End_time_label = QtWidgets.QLabel(self.Report_Search_Box)
        self.End_time_label.setGeometry(QtCore.QRect(370, 120, 301, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.End_time_label.setFont(font)
        self.End_time_label.setStyleSheet("color: white ; ;border: 3px solid  #7194ab; border-radius: 20px;\n"
                                          "background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(55, 104, 136, 255), stop:0.615819 rgba(179, 198, 210, 255), stop:0.99 rgba(179, 198, 210, 255) stop:1 rgba(255, 255, 255, 255));")
        self.End_time_label.setObjectName("End_time_label")

        self.Start_dateEdit = QtWidgets.QDateEdit(self.Report_Search_Box)
        self.Start_dateEdit.setGeometry(QtCore.QRect(160, 120, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.Start_dateEdit.setFont(font)
        self.Start_dateEdit.setStyleSheet("color: white ; ;border: none; border-radius: 20px;\n"
                                          "background-color: rgba(0,0,0,0);")
        self.Start_dateEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.Start_dateEdit.setCalendarPopup(True)
        self.Start_dateEdit.setObjectName("Start_dateEdit")
        self.Start_dateEdit.setDate(QDate(2024, 1, 1))

        self.lineEdit = QtWidgets.QLineEdit(self.Report_Search_Box)
        self.lineEdit.setGeometry(QtCore.QRect(200, 190, 331, 40))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("QLineEdit{color: white ; background-color:rgba(0,0,0,0); border:none; border-radius:20px;}")
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")

        self.Part_Num_label = QtWidgets.QLabel(self.Report_Search_Box)
        self.Part_Num_label.setGeometry(QtCore.QRect(20, 190, 511, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Part_Num_label.setFont(font)
        self.Part_Num_label.setStyleSheet("color: white ; ;border: 3px solid  #7194ab; border-radius: 20px;\n"
                                          "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(55, 104, 136, 255), stop:0.615819 rgba(179, 198, 210, 255), stop:0.99 rgba(179, 198, 210, 255) stop:1 rgba(255, 255, 255, 255));")
        self.Part_Num_label.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.Part_Num_label.setObjectName("Part_Num_label")

        self.Serial_Num_label = QtWidgets.QLabel(self.Report_Search_Box)
        self.Serial_Num_label.setGeometry(QtCore.QRect(320, 120, 291, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Serial_Num_label.setFont(font)
        self.Serial_Num_label.setStyleSheet("color: white ; ;border: 3px solid  #7194ab; border-radius: 20px;\n"
                                            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(55, 104, 136, 255), stop:0.615819 rgba(179, 198, 210, 255), stop:1 rgba(255, 255, 255, 255));")
        self.Serial_Num_label.setObjectName("Serial_Num_label")
        self.Serial_Num_label.hide()

        self.Serial_Num_textEdit = QtWidgets.QLineEdit(self.Report_Search_Box)
        self.Serial_Num_textEdit.setGeometry(QtCore.QRect(480, 120, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setCapitalization(True)
        font.setBold(True)
        font.setPointSize(10)
        self.Serial_Num_textEdit.setFont(font)
        self.Serial_Num_textEdit.setStyleSheet("color: white ; ;border: 3px solid  #7194ab; border-radius: 20px;\n"
                                               "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(55, 104, 136, 255), stop:0.615819 rgba(55, 104, 136, 255), stop:1 rgba(55, 104, 136, 255));")
        self.Serial_Num_textEdit.setObjectName("Serial_Num_textEdit")
        self.Serial_Num_textEdit.hide()

        self.Report_Table = QtWidgets.QTableWidget(self.Report_Search_Box)
        self.Report_Table.setGeometry(QtCore.QRect(10, 260, 721, 671))
        self.Report_Table.setStyleSheet("color: Black ; background-color: #0d4977 ;border: none; border-radius: 30px;")
        self.Report_Table.setObjectName("Report_Table")
        self.Report_Table.setAutoScrollMargin(20)
        self.Report_Table.setAlternatingRowColors(True)
        self.Report_Table.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.Report_Table.setGridStyle(QtCore.Qt.NoPen)
        self.Report_Table.setRowCount(0)
        self.Report_Table.setColumnCount(6)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.Report_Table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.Report_Table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.Report_Table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.Report_Table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.Report_Table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.Report_Table.setHorizontalHeaderItem(5, item)
        self.Report_Table.horizontalHeader().setVisible(True)
        self.Report_Table.horizontalHeader().setCascadingSectionResizes(True)
        self.Report_Table.horizontalHeader().setHighlightSections(True)
        self.Report_Table.horizontalHeader().setMinimumSectionSize(100)
        self.Report_Table.horizontalHeader().setSortIndicatorShown(True)
        # self.Report_Table.horizontalHeaderItem(1).setSizeHint(QSize(10,50))
        # self.Report_Table.horizontalHeader().setAlternatingRowColors(False)
        self.Report_Table.horizontalHeader().setStretchLastSection(True)
        self.Report_Table.verticalHeader().setVisible(True)
        self.Report_Table.verticalHeader().setCascadingSectionResizes(True)
        self.Report_Table.verticalHeader().setDefaultSectionSize(50)
        # self.Report_Table.verticalHeader().setHighlightSections(True)
        self.Report_Table.verticalHeader().setSortIndicatorShown(True)
        # self.Report_Table.verticalHeader().setStretchLastSection(True)
        self.Report_Table.verticalHeader().setVisible(False)
        # self.Report_Table.verticalHeader().setAlternatingRowColors(False)
        self.Report_Table.setAlternatingRowColors(True)
        header_style = "QHeaderView::section {border:1px solid black; border-radius: 5px; background-color: #dddddd; }"
        self.Report_Table.horizontalHeader().setStyleSheet(header_style)

        """SIZE"""
        header = self.Report_Table.horizontalHeader()
        header.resizeSection(0, 10)
        # header.setSectionResizeMode(1, QtWidgets.QHeaderView.Fixed)
        header.resizeSection(1, 210)
        # header.setSectionResizeMode(2, QtWidgets.QHeaderView.Fixed)
        header.resizeSection(2, 90)
        header.resizeSection(3, 85)
        header.resizeSection(4, 85)
        header.resizeSection(5, 60)

        self.Part_Num_label.raise_()
        self.End_time_label.raise_()
        self.start_time_label.raise_()
        self.End_dateEdit.raise_()
        self.Start_dateEdit.raise_()
        self.lineEdit.raise_()
        self.Serial_Num_label.raise_()
        self.Serial_Num_textEdit.raise_()
        self.Report_Table.raise_()

        self.Out_Card = QtWidgets.QFrame(self.frame)
        self.Out_Card.setGeometry(QtCore.QRect(720, 60, 1181, 881))
        self.Out_Card.setAutoFillBackground(False)
        self.Out_Card.setStyleSheet(
            "background-color: rgba(55,122,136,150); border:2px; border-top-right-radius:40px;border-bottom-right-radius:40px;\n"
            "")
        self.Out_Card.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Out_Card.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Out_Card.setObjectName("Out_Card")

        self.Card_05 = QtWidgets.QGroupBox(self.Out_Card)
        self.Card_05.setGeometry(QtCore.QRect(420, 480, 341, 391))
        self.Card_05.setStyleSheet(
            "color: white ; background-color: #0d4977 ;border: 3px solid white; border-radius: 30px;")
        self.Card_05.setTitle("")
        self.Card_05.setObjectName("Card_05")

        self.IMAGE_56 = QtWidgets.QLabel(self.Card_05)
        self.IMAGE_56.setGeometry(QtCore.QRect(270, 320, 50, 50))
        self.IMAGE_56.setMaximumSize(QtCore.QSize(50, 50))
        self.IMAGE_56.setStyleSheet("border:none;\n"
                                    "background-color: rgba(0, 0, 0, 0\n"
                                    ");")
        self.IMAGE_56.setText("")
        self.IMAGE_56.setPixmap(QtGui.QPixmap("D:/Work/F1/ATE SOFTWARES/MBO testing/images/icons_335318.svg"))
        self.IMAGE_56.setScaledContents(True)
        self.IMAGE_56.setAlignment(QtCore.Qt.AlignCenter)
        self.IMAGE_56.setObjectName("IMAGE_56")

        self.FAULTED_RESERVED = QtWidgets.QLabel(self.Card_05)
        self.FAULTED_RESERVED.setGeometry(QtCore.QRect(20, 320, 300, 50))
        self.FAULTED_RESERVED.setMaximumSize(QtCore.QSize(413, 50))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.FAULTED_RESERVED.setFont(font)
        self.FAULTED_RESERVED.setStyleSheet("color: white ; ;border: 3px solid  #7194ab; border-radius: 20px;\n"
                                            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(55, 104, 136, 255), stop:0.307692 rgba(107, 143, 167, 255), stop:0.542125 rgba(153, 178, 195, 255), stop:0.754579 rgba(179, 198, 210, 255), stop:1 rgba(255, 255, 255, 255));")
        self.FAULTED_RESERVED.setObjectName("FAULTED_RESERVED")

        self.FAULTED_IDLE = QtWidgets.QLabel(self.Card_05)
        self.FAULTED_IDLE.setGeometry(QtCore.QRect(20, 20, 300, 50))
        self.FAULTED_IDLE.setMaximumSize(QtCore.QSize(413, 50))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.FAULTED_IDLE.setFont(font)
        self.FAULTED_IDLE.setStyleSheet("color: white ; ;border: 3px solid  #7194ab; border-radius: 20px;\n"
                                        "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(55, 104, 136, 255), stop:0.307692 rgba(107, 143, 167, 255), stop:0.542125 rgba(153, 178, 195, 255), stop:0.754579 rgba(179, 198, 210, 255), stop:1 rgba(255, 255, 255, 255));")
        self.FAULTED_IDLE.setObjectName("FAULTED_IDLE")

        self.IMAGE_53 = QtWidgets.QLabel(self.Card_05)
        self.IMAGE_53.setGeometry(QtCore.QRect(270, 140, 50, 50))
        self.IMAGE_53.setMaximumSize(QtCore.QSize(50, 50))
        self.IMAGE_53.setStyleSheet("border:none;\n"
                                    "background-color: rgba(0, 0, 0, 0\n"
                                    ");")
        self.IMAGE_53.setText("")
        self.IMAGE_53.setPixmap(QtGui.QPixmap("D:/Work/F1/ATE SOFTWARES/MBO testing/images/icons_335318.svg"))
        self.IMAGE_53.setScaledContents(True)
        self.IMAGE_53.setAlignment(QtCore.Qt.AlignCenter)
        self.IMAGE_53.setObjectName("IMAGE_53")

        self.IMAGE_52 = QtWidgets.QLabel(self.Card_05)
        self.IMAGE_52.setGeometry(QtCore.QRect(270, 80, 50, 50))
        self.IMAGE_52.setMaximumSize(QtCore.QSize(50, 50))
        self.IMAGE_52.setStyleSheet("border:none;\n"
                                    "background-color: rgba(0, 0, 0, 0\n"
                                    ");")
        self.IMAGE_52.setText("")
        self.IMAGE_52.setPixmap(QtGui.QPixmap("D:/Work/F1/ATE SOFTWARES/MBO testing/images/icons_335318.svg"))
        self.IMAGE_52.setScaledContents(True)
        self.IMAGE_52.setAlignment(QtCore.Qt.AlignCenter)
        self.IMAGE_52.setObjectName("IMAGE_52")

        self.FAULTED_CHARGING = QtWidgets.QLabel(self.Card_05)
        self.FAULTED_CHARGING.setGeometry(QtCore.QRect(20, 140, 300, 50))
        self.FAULTED_CHARGING.setMaximumSize(QtCore.QSize(413, 50))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.FAULTED_CHARGING.setFont(font)
        self.FAULTED_CHARGING.setStyleSheet("color: white ; ;border: 3px solid  #7194ab; border-radius: 20px;\n"
                                            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(55, 104, 136, 255), stop:0.307692 rgba(107, 143, 167, 255), stop:0.542125 rgba(153, 178, 195, 255), stop:0.754579 rgba(179, 198, 210, 255), stop:1 rgba(255, 255, 255, 255));")
        self.FAULTED_CHARGING.setObjectName("FAULTED_CHARGING")

        self.FAULTED_PREPARING = QtWidgets.QLabel(self.Card_05)
        self.FAULTED_PREPARING.setGeometry(QtCore.QRect(20, 80, 300, 50))
        self.FAULTED_PREPARING.setMaximumSize(QtCore.QSize(413, 50))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.FAULTED_PREPARING.setFont(font)
        self.FAULTED_PREPARING.setStyleSheet("color: white ; ;border: 3px solid  #7194ab; border-radius: 20px;\n"
                                             "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(55, 104, 136, 255), stop:0.307692 rgba(107, 143, 167, 255), stop:0.542125 rgba(153, 178, 195, 255), stop:0.754579 rgba(179, 198, 210, 255), stop:1 rgba(255, 255, 255, 255));")
        self.FAULTED_PREPARING.setObjectName("FAULTED_PREPARING")

        self.FAULTED_FAULTED = QtWidgets.QLabel(self.Card_05)
        self.FAULTED_FAULTED.setGeometry(QtCore.QRect(20, 260, 300, 50))
        self.FAULTED_FAULTED.setMaximumSize(QtCore.QSize(413, 50))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.FAULTED_FAULTED.setFont(font)
        self.FAULTED_FAULTED.setStyleSheet("color: white ; ;border: 3px solid  #7194ab; border-radius: 20px;\n"
                                           "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(55, 104, 136, 255), stop:0.307692 rgba(107, 143, 167, 255), stop:0.542125 rgba(153, 178, 195, 255), stop:0.754579 rgba(179, 198, 210, 255), stop:1 rgba(255, 255, 255, 255));")
        self.FAULTED_FAULTED.setObjectName("FAULTED_FAULTED")

        self.IMAGE_54 = QtWidgets.QLabel(self.Card_05)
        self.IMAGE_54.setGeometry(QtCore.QRect(270, 200, 50, 50))
        self.IMAGE_54.setMaximumSize(QtCore.QSize(50, 50))
        self.IMAGE_54.setStyleSheet("border:none;\n"
                                    "background-color: rgba(0, 0, 0, 0\n"
                                    ");")
        self.IMAGE_54.setText("")
        self.IMAGE_54.setPixmap(QtGui.QPixmap("D:/Work/F1/ATE SOFTWARES/MBO testing/images/icons_335318.svg"))
        self.IMAGE_54.setScaledContents(True)
        self.IMAGE_54.setAlignment(QtCore.Qt.AlignCenter)
        self.IMAGE_54.setObjectName("IMAGE_54")

        self.FAULTED_FINISHING = QtWidgets.QLabel(self.Card_05)
        self.FAULTED_FINISHING.setGeometry(QtCore.QRect(20, 200, 300, 50))
        self.FAULTED_FINISHING.setMaximumSize(QtCore.QSize(413, 50))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.FAULTED_FINISHING.setFont(font)
        self.FAULTED_FINISHING.setStyleSheet("color: white ; ;border: 3px solid  #7194ab; border-radius: 20px;\n"
                                             "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(55, 104, 136, 255), stop:0.307692 rgba(107, 143, 167, 255), stop:0.542125 rgba(153, 178, 195, 255), stop:0.754579 rgba(179, 198, 210, 255), stop:1 rgba(255, 255, 255, 255));")
        self.FAULTED_FINISHING.setObjectName("FAULTED_FINISHING")

        self.IMAGE_55 = QtWidgets.QLabel(self.Card_05)
        self.IMAGE_55.setGeometry(QtCore.QRect(270, 260, 50, 50))
        self.IMAGE_55.setMaximumSize(QtCore.QSize(50, 50))
        self.IMAGE_55.setStyleSheet("border:none;\n"
                                    "background-color: rgba(0, 0, 0, 0\n"
                                    ");")
        self.IMAGE_55.setText("")
        self.IMAGE_55.setPixmap(QtGui.QPixmap("D:/Work/F1/ATE SOFTWARES/MBO testing/images/icons_335318.svg"))
        self.IMAGE_55.setScaledContents(True)
        self.IMAGE_55.setAlignment(QtCore.Qt.AlignCenter)
        self.IMAGE_55.setObjectName("IMAGE_55")

        self.IMAGE_51 = QtWidgets.QLabel(self.Card_05)
        self.IMAGE_51.setGeometry(QtCore.QRect(270, 20, 50, 50))
        self.IMAGE_51.setMaximumSize(QtCore.QSize(50, 50))
        self.IMAGE_51.setStyleSheet("border:none;\n"
                                    "background-color: rgba(0, 0, 0, 0\n"
                                    ");")
        self.IMAGE_51.setText("")
        self.IMAGE_51.setPixmap(QtGui.QPixmap("D:/Work/F1/ATE SOFTWARES/MBO testing/images/icons_335318.svg"))
        self.IMAGE_51.setScaledContents(True)
        self.IMAGE_51.setAlignment(QtCore.Qt.AlignCenter)
        self.IMAGE_51.setObjectName("IMAGE_51")
        self.FAULTED_RESERVED.raise_()
        self.FAULTED_IDLE.raise_()
        self.FAULTED_CHARGING.raise_()
        self.FAULTED_PREPARING.raise_()
        self.FAULTED_FAULTED.raise_()
        self.FAULTED_FINISHING.raise_()
        self.IMAGE_55.raise_()
        self.IMAGE_51.raise_()
        self.IMAGE_54.raise_()
        self.IMAGE_52.raise_()
        self.IMAGE_56.raise_()
        self.IMAGE_53.raise_()

        self.Card_06 = QtWidgets.QGroupBox(self.Out_Card)
        self.Card_06.setGeometry(QtCore.QRect(800, 480, 341, 391))
        self.Card_06.setStyleSheet(
            "color: white ; background-color: #0d4977 ;border: 3px solid white; border-radius: 30px;")
        self.Card_06.setTitle("")
        self.Card_06.setObjectName("Card_06")

        self.RESERVED_RESERVED = QtWidgets.QLabel(self.Card_06)
        self.RESERVED_RESERVED.setGeometry(QtCore.QRect(20, 320, 300, 50))
        self.RESERVED_RESERVED.setMaximumSize(QtCore.QSize(413, 50))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.RESERVED_RESERVED.setFont(font)
        self.RESERVED_RESERVED.setStyleSheet("color: white ; ;border: 3px solid  #7194ab; border-radius: 20px;\n"
                                             "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(55, 104, 136, 255), stop:0.307692 rgba(107, 143, 167, 255), stop:0.542125 rgba(153, 178, 195, 255), stop:0.754579 rgba(179, 198, 210, 255), stop:1 rgba(255, 255, 255, 255));")
        self.RESERVED_RESERVED.setObjectName("RESERVED_RESERVED")

        self.RESERVED_IDLE = QtWidgets.QLabel(self.Card_06)
        self.RESERVED_IDLE.setGeometry(QtCore.QRect(20, 20, 300, 50))
        self.RESERVED_IDLE.setMaximumSize(QtCore.QSize(413, 50))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.RESERVED_IDLE.setFont(font)
        self.RESERVED_IDLE.setStyleSheet("color: white ; ;border: 3px solid  #7194ab; border-radius: 20px;\n"
                                         "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(55, 104, 136, 255), stop:0.307692 rgba(107, 143, 167, 255), stop:0.542125 rgba(153, 178, 195, 255), stop:0.754579 rgba(179, 198, 210, 255), stop:1 rgba(255, 255, 255, 255));")
        self.RESERVED_IDLE.setObjectName("RESERVED_IDLE")

        self.RESERVED_CHARGING = QtWidgets.QLabel(self.Card_06)
        self.RESERVED_CHARGING.setGeometry(QtCore.QRect(20, 140, 300, 50))
        self.RESERVED_CHARGING.setMaximumSize(QtCore.QSize(413, 50))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.RESERVED_CHARGING.setFont(font)
        self.RESERVED_CHARGING.setStyleSheet("color: white ; ;border: 3px solid  #7194ab; border-radius: 20px;\n"
                                             "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(55, 104, 136, 255), stop:0.307692 rgba(107, 143, 167, 255), stop:0.542125 rgba(153, 178, 195, 255), stop:0.754579 rgba(179, 198, 210, 255), stop:1 rgba(255, 255, 255, 255));")
        self.RESERVED_CHARGING.setObjectName("RESERVED_CHARGING")

        self.RESERVED_PREPARING = QtWidgets.QLabel(self.Card_06)
        self.RESERVED_PREPARING.setGeometry(QtCore.QRect(20, 80, 300, 50))
        self.RESERVED_PREPARING.setMaximumSize(QtCore.QSize(413, 50))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.RESERVED_PREPARING.setFont(font)
        self.RESERVED_PREPARING.setStyleSheet("color: white ; ;border: 3px solid  #7194ab; border-radius: 20px;\n"
                                              "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(55, 104, 136, 255), stop:0.307692 rgba(107, 143, 167, 255), stop:0.542125 rgba(153, 178, 195, 255), stop:0.754579 rgba(179, 198, 210, 255), stop:1 rgba(255, 255, 255, 255));")
        self.RESERVED_PREPARING.setObjectName("RESERVED_PREPARING")

        self.RESERVED_FAULTED = QtWidgets.QLabel(self.Card_06)
        self.RESERVED_FAULTED.setGeometry(QtCore.QRect(20, 260, 300, 50))
        self.RESERVED_FAULTED.setMaximumSize(QtCore.QSize(413, 50))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.RESERVED_FAULTED.setFont(font)
        self.RESERVED_FAULTED.setStyleSheet("color: white ; ;border: 3px solid  #7194ab; border-radius: 20px;\n"
                                            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(55, 104, 136, 255), stop:0.307692 rgba(107, 143, 167, 255), stop:0.542125 rgba(153, 178, 195, 255), stop:0.754579 rgba(179, 198, 210, 255), stop:1 rgba(255, 255, 255, 255));")
        self.RESERVED_FAULTED.setObjectName("RESERVED_FAULTED")

        self.RESERVED_FINISHING = QtWidgets.QLabel(self.Card_06)
        self.RESERVED_FINISHING.setGeometry(QtCore.QRect(20, 200, 300, 50))
        self.RESERVED_FINISHING.setMaximumSize(QtCore.QSize(413, 50))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.RESERVED_FINISHING.setFont(font)
        self.RESERVED_FINISHING.setStyleSheet("color: white ; ;border: 3px solid  #7194ab; border-radius: 20px;\n"
                                              "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(55, 104, 136, 255), stop:0.307692 rgba(107, 143, 167, 255), stop:0.542125 rgba(153, 178, 195, 255), stop:0.754579 rgba(179, 198, 210, 255), stop:1 rgba(255, 255, 255, 255));")
        self.RESERVED_FINISHING.setObjectName("RESERVED_FINISHING")

        self.IMAGE_66 = QtWidgets.QLabel(self.Card_06)
        self.IMAGE_66.setGeometry(QtCore.QRect(270, 320, 50, 50))
        self.IMAGE_66.setMaximumSize(QtCore.QSize(50, 50))
        self.IMAGE_66.setStyleSheet("border:none;\n"
                                    "background-color: rgba(0, 0, 0, 0\n"
                                    ");")
        self.IMAGE_66.setText("")
        self.IMAGE_66.setPixmap(QtGui.QPixmap("D:/Work/F1/ATE SOFTWARES/MBO testing/images/icons_335318.svg"))
        self.IMAGE_66.setScaledContents(True)
        self.IMAGE_66.setAlignment(QtCore.Qt.AlignCenter)
        self.IMAGE_66.setObjectName("IMAGE_66")

        self.IMAGE_62 = QtWidgets.QLabel(self.Card_06)
        self.IMAGE_62.setGeometry(QtCore.QRect(270, 80, 50, 50))
        self.IMAGE_62.setMaximumSize(QtCore.QSize(50, 50))
        self.IMAGE_62.setStyleSheet("border:none;\n"
                                    "background-color: rgba(0, 0, 0, 0\n"
                                    ");")
        self.IMAGE_62.setText("")
        self.IMAGE_62.setPixmap(QtGui.QPixmap("D:/Work/F1/ATE SOFTWARES/MBO testing/images/icons_335318.svg"))
        self.IMAGE_62.setScaledContents(True)
        self.IMAGE_62.setAlignment(QtCore.Qt.AlignCenter)
        self.IMAGE_62.setObjectName("IMAGE_62")

        self.IMAGE_63 = QtWidgets.QLabel(self.Card_06)
        self.IMAGE_63.setGeometry(QtCore.QRect(270, 140, 50, 50))
        self.IMAGE_63.setMaximumSize(QtCore.QSize(50, 50))
        self.IMAGE_63.setStyleSheet("border:none;\n"
                                    "background-color: rgba(0, 0, 0, 0\n"
                                    ");")
        self.IMAGE_63.setText("")
        self.IMAGE_63.setPixmap(QtGui.QPixmap("D:/Work/F1/ATE SOFTWARES/MBO testing/images/icons_335318.svg"))
        self.IMAGE_63.setScaledContents(True)
        self.IMAGE_63.setAlignment(QtCore.Qt.AlignCenter)
        self.IMAGE_63.setObjectName("IMAGE_63")

        self.IMAGE_64 = QtWidgets.QLabel(self.Card_06)
        self.IMAGE_64.setGeometry(QtCore.QRect(270, 200, 50, 50))
        self.IMAGE_64.setMaximumSize(QtCore.QSize(50, 50))
        self.IMAGE_64.setStyleSheet("border:none;\n"
                                    "background-color: rgba(0, 0, 0, 0\n"
                                    ");")
        self.IMAGE_64.setText("")
        self.IMAGE_64.setPixmap(QtGui.QPixmap("D:/Work/F1/ATE SOFTWARES/MBO testing/images/icons_335318.svg"))
        self.IMAGE_64.setScaledContents(True)
        self.IMAGE_64.setAlignment(QtCore.Qt.AlignCenter)
        self.IMAGE_64.setObjectName("IMAGE_64")

        self.IMAGE_65 = QtWidgets.QLabel(self.Card_06)
        self.IMAGE_65.setGeometry(QtCore.QRect(270, 260, 50, 50))
        self.IMAGE_65.setMaximumSize(QtCore.QSize(50, 50))
        self.IMAGE_65.setStyleSheet("border:none;\n"
                                    "background-color: rgba(0, 0, 0, 0\n"
                                    ");")
        self.IMAGE_65.setText("")
        self.IMAGE_65.setPixmap(QtGui.QPixmap("D:/Work/F1/ATE SOFTWARES/MBO testing/images/icons_335318.svg"))
        self.IMAGE_65.setScaledContents(True)
        self.IMAGE_65.setAlignment(QtCore.Qt.AlignCenter)
        self.IMAGE_65.setObjectName("IMAGE_65")

        self.IMAGE_61 = QtWidgets.QLabel(self.Card_06)
        self.IMAGE_61.setGeometry(QtCore.QRect(270, 20, 50, 50))
        self.IMAGE_61.setMaximumSize(QtCore.QSize(50, 50))
        self.IMAGE_61.setStyleSheet("border:none;\n"
                                    "background-color: rgba(0, 0, 0, 0\n"
                                    ");")
        self.IMAGE_61.setText("")
        self.IMAGE_61.setPixmap(QtGui.QPixmap("D:/Work/F1/ATE SOFTWARES/MBO testing/images/icons_335318.svg"))
        self.IMAGE_61.setScaledContents(True)
        self.IMAGE_61.setAlignment(QtCore.Qt.AlignCenter)
        self.IMAGE_61.setObjectName("IMAGE_61")

        self.Card_02 = QtWidgets.QGroupBox(self.Out_Card)
        self.Card_02.setGeometry(QtCore.QRect(420, 70, 341, 391))
        self.Card_02.setStyleSheet(
            "color: white ; background-color: #0d4977 ;border: 3px solid white; border-radius: 30px;")
        self.Card_02.setTitle("")
        self.Card_02.setObjectName("Card_02")

        self.IMAGE_26 = QtWidgets.QLabel(self.Card_02)
        self.IMAGE_26.setGeometry(QtCore.QRect(270, 320, 50, 50))
        self.IMAGE_26.setMaximumSize(QtCore.QSize(50, 50))
        self.IMAGE_26.setStyleSheet("border:none;\n"
                                    "background-color: rgba(0, 0, 0, 0\n"
                                    ");")
        self.IMAGE_26.setText("")
        self.IMAGE_26.setPixmap(QtGui.QPixmap("D:/Work/F1/ATE SOFTWARES/MBO testing/images/disconnected.png"))
        self.IMAGE_26.setScaledContents(True)
        self.IMAGE_26.setAlignment(QtCore.Qt.AlignCenter)
        self.IMAGE_26.setObjectName("IMAGE_26")

        self.PERPARING_RESERVED = QtWidgets.QLabel(self.Card_02)
        self.PERPARING_RESERVED.setGeometry(QtCore.QRect(20, 320, 300, 50))
        self.PERPARING_RESERVED.setMaximumSize(QtCore.QSize(413, 50))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.PERPARING_RESERVED.setFont(font)
        self.PERPARING_RESERVED.setStyleSheet("color: white ; ;border: 3px solid  #7194ab; border-radius: 20px;\n"
                                              "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(55, 104, 136, 255), stop:0.307692 rgba(107, 143, 167, 255), stop:0.542125 rgba(153, 178, 195, 255), stop:0.754579 rgba(179, 198, 210, 255), stop:1 rgba(255, 255, 255, 255));")
        self.PERPARING_RESERVED.setObjectName("PERPARING_RESERVED")

        self.PERPARING_IDLE = QtWidgets.QLabel(self.Card_02)
        self.PERPARING_IDLE.setGeometry(QtCore.QRect(20, 20, 300, 50))
        self.PERPARING_IDLE.setMaximumSize(QtCore.QSize(413, 50))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.PERPARING_IDLE.setFont(font)
        self.PERPARING_IDLE.setStyleSheet("color: white ; ;border: 3px solid  #7194ab; border-radius: 20px;\n"
                                          "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(55, 104, 136, 255), stop:0.307692 rgba(107, 143, 167, 255), stop:0.542125 rgba(153, 178, 195, 255), stop:0.754579 rgba(179, 198, 210, 255), stop:1 rgba(255, 255, 255, 255));")
        self.PERPARING_IDLE.setObjectName("PERPARING_IDLE")

        self.IMAGE_23 = QtWidgets.QLabel(self.Card_02)
        self.IMAGE_23.setGeometry(QtCore.QRect(270, 140, 50, 50))
        self.IMAGE_23.setMaximumSize(QtCore.QSize(50, 50))
        self.IMAGE_23.setStyleSheet("border:none;\n"
                                    "background-color: rgba(0, 0, 0, 0\n"
                                    ");")
        self.IMAGE_23.setText("")
        self.IMAGE_23.setPixmap(QtGui.QPixmap("D:/Work/F1/ATE SOFTWARES/MBO testing/images/disconnected.png"))
        self.IMAGE_23.setScaledContents(True)
        self.IMAGE_23.setAlignment(QtCore.Qt.AlignCenter)
        self.IMAGE_23.setObjectName("IMAGE_23")

        self.IMAGE_22 = QtWidgets.QLabel(self.Card_02)
        self.IMAGE_22.setGeometry(QtCore.QRect(270, 80, 50, 50))
        self.IMAGE_22.setMaximumSize(QtCore.QSize(50, 50))
        self.IMAGE_22.setStyleSheet("border:none;\n"
                                    "background-color: rgba(0, 0, 0, 0\n"
                                    ");")
        self.IMAGE_22.setText("")
        self.IMAGE_22.setPixmap(QtGui.QPixmap("D:/Work/F1/ATE SOFTWARES/MBO testing/images/disconnected.png"))
        self.IMAGE_22.setScaledContents(True)
        self.IMAGE_22.setAlignment(QtCore.Qt.AlignCenter)
        self.IMAGE_22.setObjectName("IMAGE_22")

        self.PERPARING_CHARGING = QtWidgets.QLabel(self.Card_02)
        self.PERPARING_CHARGING.setGeometry(QtCore.QRect(20, 140, 300, 50))
        self.PERPARING_CHARGING.setMaximumSize(QtCore.QSize(413, 50))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.PERPARING_CHARGING.setFont(font)
        self.PERPARING_CHARGING.setStyleSheet("color: white ; ;border: 3px solid  #7194ab; border-radius: 20px;\n"
                                              "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(55, 104, 136, 255), stop:0.307692 rgba(107, 143, 167, 255), stop:0.542125 rgba(153, 178, 195, 255), stop:0.754579 rgba(179, 198, 210, 255), stop:1 rgba(255, 255, 255, 255));")
        self.PERPARING_CHARGING.setObjectName("PERPARING_CHARGING")

        self.PERPARING_PERPARING = QtWidgets.QLabel(self.Card_02)
        self.PERPARING_PERPARING.setGeometry(QtCore.QRect(20, 80, 300, 50))
        self.PERPARING_PERPARING.setMaximumSize(QtCore.QSize(413, 50))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.PERPARING_PERPARING.setFont(font)
        self.PERPARING_PERPARING.setStyleSheet("color: white ; ;border: 3px solid  #7194ab; border-radius: 20px;\n"
                                               "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(55, 104, 136, 255), stop:0.307692 rgba(107, 143, 167, 255), stop:0.542125 rgba(153, 178, 195, 255), stop:0.754579 rgba(179, 198, 210, 255), stop:1 rgba(255, 255, 255, 255));")
        self.PERPARING_PERPARING.setObjectName("PERPARING_PERPARING")

        self.PERPARING_FAULTY = QtWidgets.QLabel(self.Card_02)
        self.PERPARING_FAULTY.setGeometry(QtCore.QRect(20, 260, 300, 50))
        self.PERPARING_FAULTY.setMaximumSize(QtCore.QSize(413, 50))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.PERPARING_FAULTY.setFont(font)
        self.PERPARING_FAULTY.setStyleSheet("color: white ; ;border: 3px solid  #7194ab; border-radius: 20px;\n"
                                            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(55, 104, 136, 255), stop:0.307692 rgba(107, 143, 167, 255), stop:0.542125 rgba(153, 178, 195, 255), stop:0.754579 rgba(179, 198, 210, 255), stop:1 rgba(255, 255, 255, 255));")
        self.PERPARING_FAULTY.setObjectName("PERPARING_FAULTY")

        self.IMAGE_24 = QtWidgets.QLabel(self.Card_02)
        self.IMAGE_24.setGeometry(QtCore.QRect(270, 200, 50, 50))
        self.IMAGE_24.setMaximumSize(QtCore.QSize(50, 50))
        self.IMAGE_24.setStyleSheet("border:none;\n"
                                    "background-color: rgba(0, 0, 0, 0\n"
                                    ");")
        self.IMAGE_24.setText("")
        self.IMAGE_24.setPixmap(QtGui.QPixmap("D:/Work/F1/ATE SOFTWARES/MBO testing/images/disconnected.png"))
        self.IMAGE_24.setScaledContents(True)
        self.IMAGE_24.setAlignment(QtCore.Qt.AlignCenter)
        self.IMAGE_24.setObjectName("IMAGE_24")

        self.PERPARING_FINISHING = QtWidgets.QLabel(self.Card_02)
        self.PERPARING_FINISHING.setGeometry(QtCore.QRect(20, 200, 300, 50))
        self.PERPARING_FINISHING.setMaximumSize(QtCore.QSize(413, 50))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.PERPARING_FINISHING.setFont(font)
        self.PERPARING_FINISHING.setStyleSheet("color: white ; ;border: 3px solid  #7194ab; border-radius: 20px;\n"
                                               "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(55, 104, 136, 255), stop:0.307692 rgba(107, 143, 167, 255), stop:0.542125 rgba(153, 178, 195, 255), stop:0.754579 rgba(179, 198, 210, 255), stop:1 rgba(255, 255, 255, 255));")
        self.PERPARING_FINISHING.setObjectName("PERPARING_FINISHING")

        self.IMAGE_25 = QtWidgets.QLabel(self.Card_02)
        self.IMAGE_25.setGeometry(QtCore.QRect(270, 260, 50, 50))
        self.IMAGE_25.setMaximumSize(QtCore.QSize(50, 50))
        self.IMAGE_25.setStyleSheet("border:none;\n"
                                    "background-color: rgba(0, 0, 0, 0\n"
                                    ");")
        self.IMAGE_25.setText("")
        self.IMAGE_25.setPixmap(QtGui.QPixmap("D:/Work/F1/ATE SOFTWARES/MBO testing/images/disconnected.png"))
        self.IMAGE_25.setScaledContents(True)
        self.IMAGE_25.setAlignment(QtCore.Qt.AlignCenter)
        self.IMAGE_25.setObjectName("IMAGE_25")

        self.IMAGE_21 = QtWidgets.QLabel(self.Card_02)
        self.IMAGE_21.setGeometry(QtCore.QRect(270, 20, 50, 50))
        self.IMAGE_21.setMaximumSize(QtCore.QSize(50, 50))
        self.IMAGE_21.setStyleSheet("border:none;\n"
                                    "background-color: rgba(0, 0, 0, 0\n"
                                    ");")
        self.IMAGE_21.setText("")
        self.IMAGE_21.setPixmap(QtGui.QPixmap("D:/Work/F1/ATE SOFTWARES/MBO testing/images/disconnected.png"))
        self.IMAGE_21.setScaledContents(True)
        self.IMAGE_21.setAlignment(QtCore.Qt.AlignCenter)
        self.IMAGE_21.setObjectName("IMAGE_21")

        self.PERPARING_RESERVED.raise_()
        self.PERPARING_IDLE.raise_()
        self.PERPARING_CHARGING.raise_()
        self.PERPARING_PERPARING.raise_()
        self.PERPARING_FAULTY.raise_()
        self.PERPARING_FINISHING.raise_()
        self.IMAGE_25.raise_()
        self.IMAGE_21.raise_()
        self.IMAGE_24.raise_()
        self.IMAGE_26.raise_()
        self.IMAGE_22.raise_()
        self.IMAGE_23.raise_()

        self.Card_04 = QtWidgets.QGroupBox(self.Out_Card)
        self.Card_04.setGeometry(QtCore.QRect(40, 480, 341, 391))
        self.Card_04.setStyleSheet(
            "color: white ; background-color: #0d4977 ;border: 3px solid white; border-radius: 30px;")
        self.Card_04.setTitle("")
        self.Card_04.setObjectName("Card_04")

        self.IMAGE_46 = QtWidgets.QLabel(self.Card_04)
        self.IMAGE_46.setGeometry(QtCore.QRect(270, 320, 50, 50))
        self.IMAGE_46.setMaximumSize(QtCore.QSize(50, 50))
        self.IMAGE_46.setStyleSheet("border:none;\n"
                                    "background-color: rgba(0, 0, 0, 0\n"
                                    ");")
        self.IMAGE_46.setText("")
        self.IMAGE_46.setPixmap(QtGui.QPixmap("D:/Work/F1/ATE SOFTWARES/MBO testing/images/icons_335318.svg"))
        self.IMAGE_46.setScaledContents(True)
        self.IMAGE_46.setAlignment(QtCore.Qt.AlignCenter)
        self.IMAGE_46.setObjectName("IMAGE_46")

        self.FINISHING_RESERVED = QtWidgets.QLabel(self.Card_04)
        self.FINISHING_RESERVED.setGeometry(QtCore.QRect(20, 320, 300, 50))
        self.FINISHING_RESERVED.setMaximumSize(QtCore.QSize(413, 50))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.FINISHING_RESERVED.setFont(font)
        self.FINISHING_RESERVED.setStyleSheet("color: white ; ;border: 3px solid  #7194ab; border-radius: 20px;\n"
                                              "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(55, 104, 136, 255), stop:0.307692 rgba(107, 143, 167, 255), stop:0.542125 rgba(153, 178, 195, 255), stop:0.754579 rgba(179, 198, 210, 255), stop:1 rgba(255, 255, 255, 255));")
        self.FINISHING_RESERVED.setObjectName("FINISHING_RESERVED")

        self.FINISHING_IDLE = QtWidgets.QLabel(self.Card_04)
        self.FINISHING_IDLE.setGeometry(QtCore.QRect(20, 20, 300, 50))
        self.FINISHING_IDLE.setMaximumSize(QtCore.QSize(413, 50))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.FINISHING_IDLE.setFont(font)
        self.FINISHING_IDLE.setStyleSheet("color: white ; ;border: 3px solid  #7194ab; border-radius: 20px;\n"
                                          "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(55, 104, 136, 255), stop:0.307692 rgba(107, 143, 167, 255), stop:0.542125 rgba(153, 178, 195, 255), stop:0.754579 rgba(179, 198, 210, 255), stop:1 rgba(255, 255, 255, 255));")
        self.FINISHING_IDLE.setObjectName("FINISHING_IDLE")

        self.IMAGE_43 = QtWidgets.QLabel(self.Card_04)
        self.IMAGE_43.setGeometry(QtCore.QRect(270, 140, 50, 50))
        self.IMAGE_43.setMaximumSize(QtCore.QSize(50, 50))
        self.IMAGE_43.setStyleSheet("border:none;\n"
                                    "background-color: rgba(0, 0, 0, 0\n"
                                    ");")
        self.IMAGE_43.setText("")
        self.IMAGE_43.setPixmap(QtGui.QPixmap("D:/Work/F1/ATE SOFTWARES/MBO testing/images/icons_335318.svg"))
        self.IMAGE_43.setScaledContents(True)
        self.IMAGE_43.setAlignment(QtCore.Qt.AlignCenter)
        self.IMAGE_43.setObjectName("IMAGE_43")

        self.IMAGE_42 = QtWidgets.QLabel(self.Card_04)
        self.IMAGE_42.setGeometry(QtCore.QRect(270, 80, 50, 50))
        self.IMAGE_42.setMaximumSize(QtCore.QSize(50, 50))
        self.IMAGE_42.setStyleSheet("border:none;\n"
                                    "background-color: rgba(0, 0, 0, 0\n"
                                    ");")
        self.IMAGE_42.setText("")
        self.IMAGE_42.setPixmap(QtGui.QPixmap("D:/Work/F1/ATE SOFTWARES/MBO testing/images/icons_335318.svg"))
        self.IMAGE_42.setScaledContents(True)
        self.IMAGE_42.setAlignment(QtCore.Qt.AlignCenter)
        self.IMAGE_42.setObjectName("IMAGE_42")

        self.FINISHING_CHARGING = QtWidgets.QLabel(self.Card_04)
        self.FINISHING_CHARGING.setGeometry(QtCore.QRect(20, 140, 300, 50))
        self.FINISHING_CHARGING.setMaximumSize(QtCore.QSize(413, 50))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.FINISHING_CHARGING.setFont(font)
        self.FINISHING_CHARGING.setStyleSheet("color: white ; ;border: 3px solid  #7194ab; border-radius: 20px;\n"
                                              "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(55, 104, 136, 255), stop:0.307692 rgba(107, 143, 167, 255), stop:0.542125 rgba(153, 178, 195, 255), stop:0.754579 rgba(179, 198, 210, 255), stop:1 rgba(255, 255, 255, 255));")
        self.FINISHING_CHARGING.setObjectName("FINISHING_CHARGING")

        self.FINISHING_PREPARING = QtWidgets.QLabel(self.Card_04)
        self.FINISHING_PREPARING.setGeometry(QtCore.QRect(20, 80, 300, 50))
        self.FINISHING_PREPARING.setMaximumSize(QtCore.QSize(413, 50))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.FINISHING_PREPARING.setFont(font)
        self.FINISHING_PREPARING.setStyleSheet("color: white ; ;border: 3px solid  #7194ab; border-radius: 20px;\n"
                                               "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(55, 104, 136, 255), stop:0.307692 rgba(107, 143, 167, 255), stop:0.542125 rgba(153, 178, 195, 255), stop:0.754579 rgba(179, 198, 210, 255), stop:1 rgba(255, 255, 255, 255));")
        self.FINISHING_PREPARING.setObjectName("FINISHING_PREPARING")

        self.FINISHING_FAULTED = QtWidgets.QLabel(self.Card_04)
        self.FINISHING_FAULTED.setGeometry(QtCore.QRect(20, 260, 300, 50))
        self.FINISHING_FAULTED.setMaximumSize(QtCore.QSize(413, 50))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.FINISHING_FAULTED.setFont(font)
        self.FINISHING_FAULTED.setStyleSheet("color: white ; ;border: 3px solid  #7194ab; border-radius: 20px;\n"
                                             "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(55, 104, 136, 255), stop:0.307692 rgba(107, 143, 167, 255), stop:0.542125 rgba(153, 178, 195, 255), stop:0.754579 rgba(179, 198, 210, 255), stop:1 rgba(255, 255, 255, 255));")
        self.FINISHING_FAULTED.setObjectName("FINISHING_FAULTED")

        self.IMAGE_44 = QtWidgets.QLabel(self.Card_04)
        self.IMAGE_44.setGeometry(QtCore.QRect(270, 200, 50, 50))
        self.IMAGE_44.setMaximumSize(QtCore.QSize(50, 50))
        self.IMAGE_44.setStyleSheet("border:none;\n"
                                    "background-color: rgba(0, 0, 0, 0\n"
                                    ");")
        self.IMAGE_44.setText("")
        self.IMAGE_44.setPixmap(QtGui.QPixmap("D:/Work/F1/ATE SOFTWARES/MBO testing/images/icons_335318.svg"))
        self.IMAGE_44.setScaledContents(True)
        self.IMAGE_44.setAlignment(QtCore.Qt.AlignCenter)
        self.IMAGE_44.setObjectName("IMAGE_44")

        self.FINISHING_FINISHING = QtWidgets.QLabel(self.Card_04)
        self.FINISHING_FINISHING.setGeometry(QtCore.QRect(20, 200, 300, 50))
        self.FINISHING_FINISHING.setMaximumSize(QtCore.QSize(413, 50))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.FINISHING_FINISHING.setFont(font)
        self.FINISHING_FINISHING.setStyleSheet("color: white ; ;border: 3px solid  #7194ab; border-radius: 20px;\n"
                                               "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(55, 104, 136, 255), stop:0.307692 rgba(107, 143, 167, 255), stop:0.542125 rgba(153, 178, 195, 255), stop:0.754579 rgba(179, 198, 210, 255), stop:1 rgba(255, 255, 255, 255));")
        self.FINISHING_FINISHING.setObjectName("FINISHING_FINISHING")

        self.IMAGE_45 = QtWidgets.QLabel(self.Card_04)
        self.IMAGE_45.setGeometry(QtCore.QRect(270, 260, 50, 50))
        self.IMAGE_45.setMaximumSize(QtCore.QSize(50, 50))
        self.IMAGE_45.setStyleSheet("border:none;\n"
                                    "background-color: rgba(0, 0, 0, 0\n"
                                    ");")
        self.IMAGE_45.setText("")
        self.IMAGE_45.setPixmap(QtGui.QPixmap("D:/Work/F1/ATE SOFTWARES/MBO testing/images/icons_335318.svg"))
        self.IMAGE_45.setScaledContents(True)
        self.IMAGE_45.setAlignment(QtCore.Qt.AlignCenter)
        self.IMAGE_45.setObjectName("IMAGE_45")

        self.IMAGE_41 = QtWidgets.QLabel(self.Card_04)
        self.IMAGE_41.setGeometry(QtCore.QRect(270, 20, 50, 50))
        self.IMAGE_41.setMaximumSize(QtCore.QSize(50, 50))
        self.IMAGE_41.setStyleSheet("border:none;\n"
                                    "background-color: rgba(0, 0, 0, 0\n"
                                    ");")
        self.IMAGE_41.setText("")
        self.IMAGE_41.setPixmap(QtGui.QPixmap("D:/Work/F1/ATE SOFTWARES/MBO testing/images/icons_335318.svg"))
        self.IMAGE_41.setScaledContents(True)
        self.IMAGE_41.setAlignment(QtCore.Qt.AlignCenter)
        self.IMAGE_41.setObjectName("IMAGE_41")

        self.FINISHING_RESERVED.raise_()
        self.FINISHING_IDLE.raise_()
        self.FINISHING_CHARGING.raise_()
        self.FINISHING_PREPARING.raise_()
        self.FINISHING_FAULTED.raise_()
        self.IMAGE_45.raise_()
        self.IMAGE_41.raise_()
        self.IMAGE_43.raise_()
        self.FINISHING_FINISHING.raise_()
        self.IMAGE_46.raise_()
        self.IMAGE_42.raise_()
        self.IMAGE_44.raise_()

        self.Card_03 = QtWidgets.QGroupBox(self.Out_Card)
        self.Card_03.setGeometry(QtCore.QRect(800, 70, 341, 391))
        self.Card_03.setStyleSheet(
            "color: white ; background-color: #0d4977 ;border: 3px solid white; border-radius: 30px;")
        self.Card_03.setTitle("")
        self.Card_03.setObjectName("Card_03")

        self.IMAGE_36 = QtWidgets.QLabel(self.Card_03)
        self.IMAGE_36.setGeometry(QtCore.QRect(270, 320, 50, 50))
        self.IMAGE_36.setMaximumSize(QtCore.QSize(50, 50))
        self.IMAGE_36.setStyleSheet("border:none;\n"
                                    "background-color: rgba(0, 0, 0, 0\n"
                                    ");")
        self.IMAGE_36.setText("")
        self.IMAGE_36.setPixmap(QtGui.QPixmap("D:/Work/F1/ATE SOFTWARES/MBO testing/images/icons_335318.svg"))
        self.IMAGE_36.setScaledContents(True)
        self.IMAGE_36.setAlignment(QtCore.Qt.AlignCenter)
        self.IMAGE_36.setObjectName("IMAGE_36")

        self.CHARGING_RESERVED = QtWidgets.QLabel(self.Card_03)
        self.CHARGING_RESERVED.setGeometry(QtCore.QRect(20, 320, 300, 50))
        self.CHARGING_RESERVED.setMaximumSize(QtCore.QSize(413, 50))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.CHARGING_RESERVED.setFont(font)
        self.CHARGING_RESERVED.setStyleSheet("color: white ; ;border: 3px solid  #7194ab; border-radius: 20px;\n"
                                             "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(55, 104, 136, 255), stop:0.307692 rgba(107, 143, 167, 255), stop:0.542125 rgba(153, 178, 195, 255), stop:0.754579 rgba(179, 198, 210, 255), stop:1 rgba(255, 255, 255, 255));")
        self.CHARGING_RESERVED.setObjectName("CHARGING_RESERVED")

        self.CHARGING_IDLE = QtWidgets.QLabel(self.Card_03)
        self.CHARGING_IDLE.setGeometry(QtCore.QRect(20, 20, 300, 50))
        self.CHARGING_IDLE.setMaximumSize(QtCore.QSize(413, 50))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.CHARGING_IDLE.setFont(font)
        self.CHARGING_IDLE.setStyleSheet("color: white ; ;border: 3px solid  #7194ab; border-radius: 20px;\n"
                                         "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(55, 104, 136, 255), stop:0.307692 rgba(107, 143, 167, 255), stop:0.542125 rgba(153, 178, 195, 255), stop:0.754579 rgba(179, 198, 210, 255), stop:1 rgba(255, 255, 255, 255));")
        self.CHARGING_IDLE.setObjectName("CHARGING_IDLE")

        self.IMAGE_33 = QtWidgets.QLabel(self.Card_03)
        self.IMAGE_33.setGeometry(QtCore.QRect(270, 140, 50, 50))
        self.IMAGE_33.setMaximumSize(QtCore.QSize(50, 50))
        self.IMAGE_33.setStyleSheet("border:none;\n"
                                    "background-color: rgba(0, 0, 0, 0\n"
                                    ");")
        self.IMAGE_33.setText("")
        self.IMAGE_33.setPixmap(QtGui.QPixmap("D:/Work/F1/ATE SOFTWARES/MBO testing/images/icons_335318.svg"))
        self.IMAGE_33.setScaledContents(True)
        self.IMAGE_33.setAlignment(QtCore.Qt.AlignCenter)
        self.IMAGE_33.setObjectName("IMAGE_33")

        self.IMAGE_32 = QtWidgets.QLabel(self.Card_03)
        self.IMAGE_32.setGeometry(QtCore.QRect(270, 80, 50, 50))
        self.IMAGE_32.setMaximumSize(QtCore.QSize(50, 50))
        self.IMAGE_32.setStyleSheet("border:none;\n"
                                    "background-color: rgba(0, 0, 0, 0\n"
                                    ");")
        self.IMAGE_32.setText("")
        self.IMAGE_32.setPixmap(QtGui.QPixmap("D:/Work/F1/ATE SOFTWARES/MBO testing/images/icons_335318.svg"))
        self.IMAGE_32.setScaledContents(True)
        self.IMAGE_32.setAlignment(QtCore.Qt.AlignCenter)
        self.IMAGE_32.setObjectName("IMAGE_32")

        self.CHARGING_CHARGING = QtWidgets.QLabel(self.Card_03)
        self.CHARGING_CHARGING.setGeometry(QtCore.QRect(20, 140, 300, 50))
        self.CHARGING_CHARGING.setMaximumSize(QtCore.QSize(413, 50))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.CHARGING_CHARGING.setFont(font)
        self.CHARGING_CHARGING.setStyleSheet("color: white ; ;border: 3px solid  #7194ab; border-radius: 20px;\n"
                                             "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(55, 104, 136, 255), stop:0.307692 rgba(107, 143, 167, 255), stop:0.542125 rgba(153, 178, 195, 255), stop:0.754579 rgba(179, 198, 210, 255), stop:1 rgba(255, 255, 255, 255));")
        self.CHARGING_CHARGING.setObjectName("CHARGING_CHARGING")

        self.CHARGING_PREPARING = QtWidgets.QLabel(self.Card_03)
        self.CHARGING_PREPARING.setGeometry(QtCore.QRect(20, 80, 300, 50))
        self.CHARGING_PREPARING.setMaximumSize(QtCore.QSize(413, 50))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.CHARGING_PREPARING.setFont(font)
        self.CHARGING_PREPARING.setStyleSheet("color: white ; ;border: 3px solid  #7194ab; border-radius: 20px;\n"
                                              "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(55, 104, 136, 255), stop:0.307692 rgba(107, 143, 167, 255), stop:0.542125 rgba(153, 178, 195, 255), stop:0.754579 rgba(179, 198, 210, 255), stop:1 rgba(255, 255, 255, 255));")
        self.CHARGING_PREPARING.setObjectName("CHARGING_PREPARING")

        self.CHARGING_FAULTED = QtWidgets.QLabel(self.Card_03)
        self.CHARGING_FAULTED.setGeometry(QtCore.QRect(20, 260, 300, 50))
        self.CHARGING_FAULTED.setMaximumSize(QtCore.QSize(413, 50))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.CHARGING_FAULTED.setFont(font)
        self.CHARGING_FAULTED.setStyleSheet("color: white ; ;border: 3px solid  #7194ab; border-radius: 20px;\n"
                                            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(55, 104, 136, 255), stop:0.307692 rgba(107, 143, 167, 255), stop:0.542125 rgba(153, 178, 195, 255), stop:0.754579 rgba(179, 198, 210, 255), stop:1 rgba(255, 255, 255, 255));")
        self.CHARGING_FAULTED.setObjectName("CHARGING_FAULTED")

        self.IMAGE_34 = QtWidgets.QLabel(self.Card_03)
        self.IMAGE_34.setGeometry(QtCore.QRect(270, 200, 50, 50))
        self.IMAGE_34.setMaximumSize(QtCore.QSize(50, 50))
        self.IMAGE_34.setStyleSheet("border:none;\n"
                                    "background-color: rgba(0, 0, 0, 0\n"
                                    ");")
        self.IMAGE_34.setText("")
        self.IMAGE_34.setPixmap(QtGui.QPixmap("D:/Work/F1/ATE SOFTWARES/MBO testing/images/icons_335318.svg"))
        self.IMAGE_34.setScaledContents(True)
        self.IMAGE_34.setAlignment(QtCore.Qt.AlignCenter)
        self.IMAGE_34.setObjectName("IMAGE_34")

        self.CHARGING_FINISHED = QtWidgets.QLabel(self.Card_03)
        self.CHARGING_FINISHED.setGeometry(QtCore.QRect(20, 200, 300, 50))
        self.CHARGING_FINISHED.setMaximumSize(QtCore.QSize(413, 50))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.CHARGING_FINISHED.setFont(font)
        self.CHARGING_FINISHED.setStyleSheet("color: white ; ;border: 3px solid  #7194ab; border-radius: 20px;\n"
                                             "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(55, 104, 136, 255), stop:0.307692 rgba(107, 143, 167, 255), stop:0.542125 rgba(153, 178, 195, 255), stop:0.754579 rgba(179, 198, 210, 255), stop:1 rgba(255, 255, 255, 255));")
        self.CHARGING_FINISHED.setObjectName("CHARGING_FINISHED")

        self.IMAGE_35 = QtWidgets.QLabel(self.Card_03)
        self.IMAGE_35.setGeometry(QtCore.QRect(270, 260, 50, 50))
        self.IMAGE_35.setMaximumSize(QtCore.QSize(50, 50))
        self.IMAGE_35.setStyleSheet("border:none;\n"
                                    "background-color: rgba(0, 0, 0, 0\n"
                                    ");")
        self.IMAGE_35.setText("")
        self.IMAGE_35.setPixmap(QtGui.QPixmap("D:/Work/F1/ATE SOFTWARES/MBO testing/images/icons_335318.svg"))
        self.IMAGE_35.setScaledContents(True)
        self.IMAGE_35.setAlignment(QtCore.Qt.AlignCenter)
        self.IMAGE_35.setObjectName("IMAGE_35")

        self.IMAGE_31 = QtWidgets.QLabel(self.Card_03)
        self.IMAGE_31.setGeometry(QtCore.QRect(270, 20, 50, 50))
        self.IMAGE_31.setMaximumSize(QtCore.QSize(50, 50))
        self.IMAGE_31.setStyleSheet("border:none;\n"
                                    "background-color: rgba(0, 0, 0, 0\n"
                                    ");")
        self.IMAGE_31.setText("")
        self.IMAGE_31.setPixmap(QtGui.QPixmap("D:/Work/F1/ATE SOFTWARES/MBO testing/images/icons_335318.svg"))
        self.IMAGE_31.setScaledContents(True)
        self.IMAGE_31.setAlignment(QtCore.Qt.AlignCenter)
        self.IMAGE_31.setObjectName("IMAGE_31")

        self.CHARGING_RESERVED.raise_()
        self.CHARGING_IDLE.raise_()
        self.CHARGING_CHARGING.raise_()
        self.CHARGING_PREPARING.raise_()
        self.CHARGING_FAULTED.raise_()
        self.CHARGING_FINISHED.raise_()
        self.IMAGE_35.raise_()
        self.IMAGE_31.raise_()
        self.IMAGE_33.raise_()
        self.IMAGE_32.raise_()
        self.IMAGE_36.raise_()
        self.IMAGE_34.raise_()

        self.Bardode_label = QtWidgets.QLabel(self.Out_Card)
        self.Bardode_label.setGeometry(QtCore.QRect(320, 10, 470, 50))
        self.Bardode_label.setMaximumSize(QtCore.QSize(800, 50))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Bardode_label.setFont(font)
        self.Bardode_label.setStyleSheet(
            "color: white ; ;border: 3px solid  white; border-radius: 20px;\n background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(55, 104, 136, 255), stop:0.307692 rgba(107, 143, 167, 255), stop:0.542125 rgba(153, 178, 195, 255),  stop:0.754579 rgba(153, 178, 195, 255),stop:0.994579 rgba(179, 198, 210, 255), stop:1 rgba(255, 255, 255, 255));")
        self.Bardode_label.setObjectName("Bardode_label")

        self.Card_01 = QtWidgets.QGroupBox(self.Out_Card)
        self.Card_01.setGeometry(QtCore.QRect(40, 70, 341, 391))
        self.Card_01.setStyleSheet(
            "color: white ; background-color: #0d4977 ;border: 3px solid white; border-radius: 30px;")
        self.Card_01.setTitle("")
        self.Card_01.setObjectName("Card_01")

        self.IMAGE_16 = QtWidgets.QLabel(self.Card_01)
        self.IMAGE_16.setGeometry(QtCore.QRect(270, 320, 50, 50))
        self.IMAGE_16.setMaximumSize(QtCore.QSize(50, 50))
        self.IMAGE_16.setStyleSheet("border:none;\n"
                                    "background-color: rgba(0, 0, 0, 0\n"
                                    ");")
        self.IMAGE_16.setText("")
        self.IMAGE_16.setPixmap(QtGui.QPixmap("D:/Work/F1/ATE SOFTWARES/MBO testing/images/dont-touch.png"))
        self.IMAGE_16.setScaledContents(True)
        self.IMAGE_16.setAlignment(QtCore.Qt.AlignCenter)
        self.IMAGE_16.setObjectName("IMAGE_16")

        self.IDLE_RESERVED = QtWidgets.QLabel(self.Card_01)
        self.IDLE_RESERVED.setGeometry(QtCore.QRect(20, 320, 300, 50))
        self.IDLE_RESERVED.setMaximumSize(QtCore.QSize(413, 50))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.IDLE_RESERVED.setFont(font)
        self.IDLE_RESERVED.setStyleSheet("color: white ; ;border: 3px solid  #7194ab; border-radius: 20px;\n"
                                         "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(55, 104, 136, 255), stop:0.307692 rgba(107, 143, 167, 255), stop:0.542125 rgba(153, 178, 195, 255), stop:0.754579 rgba(179, 198, 210, 255), stop:1 rgba(255, 255, 255, 255));")
        self.IDLE_RESERVED.setObjectName("IDLE_RESERVED")

        self.IDLE_IDLE = QtWidgets.QLabel(self.Card_01)
        self.IDLE_IDLE.setGeometry(QtCore.QRect(20, 20, 300, 50))
        self.IDLE_IDLE.setMaximumSize(QtCore.QSize(413, 50))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.IDLE_IDLE.setFont(font)
        self.IDLE_IDLE.setStyleSheet("color: white ; ;border: 3px solid  #7194ab; border-radius: 20px;\n"
                                     "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(55, 104, 136, 255), stop:0.307692 rgba(107, 143, 167, 255), stop:0.542125 rgba(153, 178, 195, 255), stop:0.754579 rgba(179, 198, 210, 255), stop:1 rgba(255, 255, 255, 255));")
        self.IDLE_IDLE.setObjectName("IDLE_IDLE")

        self.IMAGE_13 = QtWidgets.QLabel(self.Card_01)
        self.IMAGE_13.setGeometry(QtCore.QRect(270, 140, 50, 50))
        self.IMAGE_13.setMaximumSize(QtCore.QSize(50, 50))
        self.IMAGE_13.setStyleSheet("border:none;\n"
                                    "background-color: rgba(0, 0, 0, 0\n"
                                    ");")
        self.IMAGE_13.setText("")
        self.IMAGE_13.setPixmap(QtGui.QPixmap("D:/Work/F1/ATE SOFTWARES/MBO testing/images/dont-touch.png"))
        self.IMAGE_13.setScaledContents(True)
        self.IMAGE_13.setAlignment(QtCore.Qt.AlignCenter)
        self.IMAGE_13.setObjectName("IMAGE_13")

        self.IMAGE_12 = QtWidgets.QLabel(self.Card_01)
        self.IMAGE_12.setGeometry(QtCore.QRect(270, 80, 50, 50))
        self.IMAGE_12.setMaximumSize(QtCore.QSize(50, 50))
        self.IMAGE_12.setStyleSheet("border:none;\n"
                                    "background-color: rgba(0, 0, 0, 0\n"
                                    ");")
        self.IMAGE_12.setText("")
        self.IMAGE_12.setPixmap(QtGui.QPixmap("D:/Work/F1/ATE SOFTWARES/MBO testing/images/dont-touch.png"))
        self.IMAGE_12.setScaledContents(True)
        self.IMAGE_12.setAlignment(QtCore.Qt.AlignCenter)
        self.IMAGE_12.setObjectName("IMAGE_12")

        self.IDLE_CHARGING = QtWidgets.QLabel(self.Card_01)
        self.IDLE_CHARGING.setGeometry(QtCore.QRect(20, 140, 300, 50))
        self.IDLE_CHARGING.setMaximumSize(QtCore.QSize(413, 50))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.IDLE_CHARGING.setFont(font)
        self.IDLE_CHARGING.setStyleSheet("color: white ; ;border: 3px solid  #7194ab; border-radius: 20px;\n"
                                         "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(55, 104, 136, 255), stop:0.307692 rgba(107, 143, 167, 255), stop:0.542125 rgba(153, 178, 195, 255), stop:0.754579 rgba(179, 198, 210, 255), stop:1 rgba(255, 255, 255, 255));")
        self.IDLE_CHARGING.setObjectName("IDLE_CHARGING")

        self.IDLE_PERPARING = QtWidgets.QLabel(self.Card_01)
        self.IDLE_PERPARING.setGeometry(QtCore.QRect(20, 80, 300, 50))
        self.IDLE_PERPARING.setMaximumSize(QtCore.QSize(413, 50))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.IDLE_PERPARING.setFont(font)
        self.IDLE_PERPARING.setStyleSheet("color: white ; ;border: 3px solid  #7194ab; border-radius: 20px;\n"
                                          "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(55, 104, 136, 255), stop:0.307692 rgba(107, 143, 167, 255), stop:0.542125 rgba(153, 178, 195, 255), stop:0.754579 rgba(179, 198, 210, 255), stop:1 rgba(255, 255, 255, 255));")
        self.IDLE_PERPARING.setObjectName("IDLE_PERPARING")

        self.IDLE_FAULTED = QtWidgets.QLabel(self.Card_01)
        self.IDLE_FAULTED.setGeometry(QtCore.QRect(20, 260, 300, 50))
        self.IDLE_FAULTED.setMaximumSize(QtCore.QSize(413, 50))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.IDLE_FAULTED.setFont(font)
        self.IDLE_FAULTED.setStyleSheet("color: white ; ;border: 3px solid  #7194ab; border-radius: 20px;\n"
                                        "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(55, 104, 136, 255), stop:0.307692 rgba(107, 143, 167, 255), stop:0.542125 rgba(153, 178, 195, 255), stop:0.754579 rgba(179, 198, 210, 255), stop:1 rgba(255, 255, 255, 255));")
        self.IDLE_FAULTED.setObjectName("IDLE_FAULTED")

        self.IMAGE_14 = QtWidgets.QLabel(self.Card_01)
        self.IMAGE_14.setGeometry(QtCore.QRect(270, 200, 50, 50))
        self.IMAGE_14.setMaximumSize(QtCore.QSize(50, 50))
        self.IMAGE_14.setStyleSheet("border:none;\n"
                                    "background-color: rgba(0, 0, 0, 0\n"
                                    ");")
        self.IMAGE_14.setText("")
        self.IMAGE_14.setPixmap(QtGui.QPixmap("D:/Work/F1/ATE SOFTWARES/MBO testing/images/dont-touch.png"))
        self.IMAGE_14.setScaledContents(True)
        self.IMAGE_14.setAlignment(QtCore.Qt.AlignCenter)
        self.IMAGE_14.setObjectName("IMAGE_14")

        self.IDLE_FINISHING = QtWidgets.QLabel(self.Card_01)
        self.IDLE_FINISHING.setGeometry(QtCore.QRect(20, 200, 300, 50))
        self.IDLE_FINISHING.setMaximumSize(QtCore.QSize(413, 50))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.IDLE_FINISHING.setFont(font)
        self.IDLE_FINISHING.setStyleSheet("color: white ; ;border: 3px solid  #7194ab; border-radius: 20px;\n"
                                          "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(55, 104, 136, 255), stop:0.307692 rgba(107, 143, 167, 255), stop:0.542125 rgba(153, 178, 195, 255), stop:0.754579 rgba(179, 198, 210, 255), stop:1 rgba(255, 255, 255, 255));")
        self.IDLE_FINISHING.setObjectName("IDLE_FINISHING")

        self.IMAGE_15 = QtWidgets.QLabel(self.Card_01)
        self.IMAGE_15.setGeometry(QtCore.QRect(270, 260, 50, 50))
        self.IMAGE_15.setMaximumSize(QtCore.QSize(50, 50))
        self.IMAGE_15.setStyleSheet("border:none;\n"
                                    "background-color: rgba(0, 0, 0, 0\n"
                                    ");")
        self.IMAGE_15.setText("")
        self.IMAGE_15.setPixmap(QtGui.QPixmap("D:/Work/F1/ATE SOFTWARES/MBO testing/images/dont-touch.png"))
        self.IMAGE_15.setScaledContents(True)
        self.IMAGE_15.setAlignment(QtCore.Qt.AlignCenter)
        self.IMAGE_15.setObjectName("IMAGE_15")

        self.IMAGE_11 = QtWidgets.QLabel(self.Card_01)
        self.IMAGE_11.setGeometry(QtCore.QRect(270, 20, 50, 50))
        self.IMAGE_11.setMaximumSize(QtCore.QSize(50, 50))
        self.IMAGE_11.setStyleSheet("border:none;\n"
                                    "background-color: rgba(0, 0, 0, 0\n"
                                    ");")
        self.IMAGE_11.setText("")
        self.IMAGE_11.setPixmap(QtGui.QPixmap("D:/Work/F1/ATE SOFTWARES/MBO testing/images/dont-touch.png"))
        self.IMAGE_11.setScaledContents(True)
        self.IMAGE_11.setAlignment(QtCore.Qt.AlignCenter)
        self.IMAGE_11.setObjectName("IMAGE_11")

        """Search Button"""
        self.btn_search = QtWidgets.QPushButton(self.Report_Search_Box)
        self.btn_search.setGeometry(QtCore.QRect(550, 173, 95, 30))
        self.btn_search.setFixedSize(140, 70)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setFamily("Arial Black")
        font.setCapitalization(True)
        font.setBold(True)
        self.btn_search.setFont(font)
        self.btn_search.setObjectName("btn_search")
        shadow_effect = QGraphicsDropShadowEffect(self.btn_search)
        shadow_effect.setColor(QColor(0, 0, 0, 200))  # Shadow color (black with alpha)
        shadow_effect.setBlurRadius(10)  # Shadow blur radius
        shadow_effect.setXOffset(5)  # Shadow x-offset
        shadow_effect.setYOffset(5)  # Shadow y-offset
        self.btn_search.setGraphicsEffect(shadow_effect)
        self.btn_search.setStyleSheet("QPushButton{color: white ; ;border: 3px solid  #7194ab; border-radius: 35px; font : 75 15pt 'Arial Black';background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(55, 104, 136, 255), stop:1.615819 rgba(179, 198, 210, 255), stop:1 rgba(179, 198, 210, 255));}"
                                      "QPushButton::hover{color: white ; ;border: 3px solid  #7194ab; border-radius: 35px;font : 75 18pt 'Arial Black';background-color: qlineargradient(spread:pad, x:0, y1:0, x2:1, y2:0, stop:0 rgba(55, 104, 136, 255), stop:1.615819 rgba(179, 198, 210, 255), stop:1 rgba(179, 198, 210, 255));}"
                                      "QPushButton::pressed{color: white ; ;border: 3px solid  #7194ab; border-radius: 35px;font : 75 18pt 'Arial Black';background-color: qlineargradient(spread:pad, x:0, y1:0, x2:1, y2:0, stop:0 rgba(55, 104, 136, 255), stop:1.615819 rgba(179, 198, 210, 255), stop:1 rgba(179, 198, 210, 255));padding-top:10px;}")
        self.btn_search.clicked.connect(self.Search)


        """
        
        LOGO
        
        """

        self.pushButton = QtWidgets.QPushButton(self.Report_Search_Box)
        # self.pushButton.setGeometry(QtCore.QRect(300, 390, 150, 80))
        self.pushButton.setGeometry(75, 100, 150, 80)
        font = QtGui.QFont()
        font.setPointSize(40)
        self.pushButton.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(f"{os.getcwd()}/images/logo_1.png"), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(70, 70))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setStyleSheet("QPushButton { border-radius: 30px; }")

        """
        
        LOGO Creation Ends
        
        """
        self.IDLE_RESERVED.raise_()
        self.IDLE_IDLE.raise_()
        self.IDLE_CHARGING.raise_()
        self.IDLE_PERPARING.raise_()
        self.IDLE_FAULTED.raise_()
        self.IDLE_FINISHING.raise_()
        self.IMAGE_15.raise_()
        self.IMAGE_11.raise_()
        self.IMAGE_16.raise_()
        self.IMAGE_12.raise_()
        self.IMAGE_14.raise_()
        self.IMAGE_13.raise_()
        self.pushButton.raise_()

        self.Barcode_lineEdit = QtWidgets.QComboBox(self.Out_Card)
        self.Barcode_lineEdit.setGeometry(QtCore.QRect(530, 10, 251, 51))
        # self.Barcode_lineEdit.setCurrentIndex()
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setCapitalization(True)
        font.setBold(True)
        font.setWeight(75)
        self.Barcode_lineEdit.setFont(font)
        # line = self.Barcode_lineEdit.lineEdit().setAlignment(Qt.AlignCenter)
        # line.setAlignment(Qt.AlignCenter)
        self.Barcode_lineEdit.setStyleSheet(
            "QComboBox {background-color:rgba(0,0,0,0); color: white; font-size: 14px; text-align: center;}"
            "QComboBox QAbstractItemView { color: red; font-size: 12px; background-color: white; text-align: center;}")
        self.Barcode_lineEdit.setObjectName("Barcode_lineEdit")
        self.Out_Card.raise_()
        self.Report_Search.raise_()

        self.checked = QTimer()
        self.checked.timeout.connect(self.logoAnimation)
        self.checked.start(500)
        # self.checked.stop()
        MainWindow.move(600, 20)

        self.resetButton = QTimer()
        # self.resetButton.timeout.connect(self.resetButtonFunction)
        # self.resetButton.start(5000)

        self.fullsize = False
        self.Report_Table.clicked.connect(self.check)
        self.Barcode_lineEdit.activated.connect(self.updateDashboard)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.unique_list = set()
        self.btn_search.setVisible(False)
        self.Start_dateEdit.setVisible(False)
        self.start_time_label.setVisible(False)
        self.End_time_label.setVisible(False)
        self.End_dateEdit.setVisible(False)
        self.Part_Num_label.setVisible(False)
        self.lineEdit.setVisible(False)
        self.Report_Table.setVisible(False)
        self.Out_Card.setVisible(False)
        self.closeButton.setVisible(False)
        self.Report_Search_Box.setGeometry(250, 330, 190, 120)
        self.pushButton.setGeometry(20, 20, 150, 80)
        # self.Report_Table.clicked.connect(self.logoAnimation)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "LED TESTING"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Enter Part / Serial No. or Both"))
        self.start_time_label.setText(_translate("MainWindow", "   START TIME"))
        self.End_time_label.setText(_translate("MainWindow", "   END TIME"))
        self.Part_Num_label.setText(_translate("MainWindow", " Part / Serial Number : "))
        self.Serial_Num_label.setText(_translate("MainWindow", "SERIAL NUMBER"))
        self.FAULTED_RESERVED.setText(_translate("MainWindow", "FAULTED - RESERVED"))
        self.FAULTED_IDLE.setText(_translate("MainWindow", "FAULTED - IDLE"))
        self.FAULTED_CHARGING.setText(_translate("MainWindow", "FAULTED - CHARGING"))
        self.FAULTED_PREPARING.setText(_translate("MainWindow", "FAULTED - PREPARING"))
        self.FAULTED_FAULTED.setText(_translate("MainWindow", "FAULTED - FAULTED"))
        self.FAULTED_FINISHING.setText(_translate("MainWindow", "FAULTED - FINISHING"))
        self.RESERVED_RESERVED.setText(_translate("MainWindow", "RESERVED - RESERVED"))
        self.RESERVED_IDLE.setText(_translate("MainWindow", "RESERVED - IDLE"))
        self.RESERVED_CHARGING.setText(_translate("MainWindow", "RESERVED - CHARGING"))
        self.RESERVED_PREPARING.setText(_translate("MainWindow", "RESERVED - PREPARING"))
        self.RESERVED_FAULTED.setText(_translate("MainWindow", "RESERVED - FAULTED"))
        self.RESERVED_FINISHING.setText(_translate("MainWindow", "RESERVED - FINISHING"))
        self.PERPARING_RESERVED.setText(_translate("MainWindow", "PREPARING - RESERVED"))
        self.PERPARING_IDLE.setText(_translate("MainWindow", "PREPARING - IDLE"))
        self.PERPARING_CHARGING.setText(_translate("MainWindow", "PREPARING - CHARGING"))
        self.PERPARING_PERPARING.setText(_translate("MainWindow", "PREPARING - PREPARING"))
        self.PERPARING_FAULTY.setText(_translate("MainWindow", "PREPARING - FAULTED"))
        self.PERPARING_FINISHING.setText(_translate("MainWindow", "PREPARING - FINISHING"))
        self.FINISHING_RESERVED.setText(_translate("MainWindow", "FINISHING - RESERVED"))
        self.FINISHING_IDLE.setText(_translate("MainWindow", "FINISHING - IDLE"))
        self.FINISHING_CHARGING.setText(_translate("MainWindow", "FINISHING - CHARGING"))
        self.FINISHING_PREPARING.setText(_translate("MainWindow", "FINISHING - PREPARING"))
        self.FINISHING_FAULTED.setText(_translate("MainWindow", "FINISHING - FAULTED"))
        self.FINISHING_FINISHING.setText(_translate("MainWindow", "FINISHING - FINISHING"))
        self.CHARGING_RESERVED.setText(_translate("MainWindow", "CHARGING - RESERVED"))
        self.CHARGING_IDLE.setText(_translate("MainWindow", "CHARGING - IDLE"))
        self.CHARGING_CHARGING.setText(_translate("MainWindow", "CHARGING - CHARGING"))
        self.CHARGING_PREPARING.setText(_translate("MainWindow", "CHARGING - PREPARING"))
        self.CHARGING_FAULTED.setText(_translate("MainWindow", "CHARGING - FAULTED"))
        self.CHARGING_FINISHED.setText(_translate("MainWindow", "CHARGING - FINISHING"))
        self.IDLE_RESERVED.setText(_translate("MainWindow", "IDLE - RESERVED"))
        self.IDLE_IDLE.setText(_translate("MainWindow", "IDLE - IDLE"))
        self.IDLE_CHARGING.setText(_translate("MainWindow", "IDLED - CHARGING"))
        self.IDLE_PERPARING.setText(_translate("MainWindow", "IDLE - PREPARING"))
        self.IDLE_FAULTED.setText(_translate("MainWindow", "IDLE - FAULTED"))
        self.IDLE_FINISHING.setText(_translate("MainWindow", "IDLE - FINISHING"))

        self.Bardode_label.setText(_translate("MainWindow", "Displaying Test Details of Test ID: "))

        self.btn_search.setText(_translate("MainWindow", "Search"))

        self.pushButton.setText(_translate("MainWindow", ""))

        item = self.Report_Table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.Report_Table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Serial Number"))
        item = self.Report_Table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Engg. Name"))
        item = self.Report_Table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Start Time"))
        item = self.Report_Table.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "End Time"))
        item = self.Report_Table.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Result"))


    def resetButtonFunction(self):
        shadow_effect = QGraphicsDropShadowEffect(self.btn_search)
        shadow_effect.setColor(QColor(0, 0, 0, 200))  # Shadow color (black with alpha)
        shadow_effect.setBlurRadius(10)  # Shadow blur radius
        shadow_effect.setXOffset(5)  # Shadow x-offset
        shadow_effect.setYOffset(5)  # Shadow y-offset
        self.btn_search.setGraphicsEffect(shadow_effect)
        self.btn_search.setStyleSheet(
            "QPushButton{color: white ; ;border: 3px solid  #7194ab; border-radius: 35px; font : 75 15pt 'Arial Black';background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(55, 104, 136, 255), stop:1.615819 rgba(179, 198, 210, 255), stop:1 rgba(179, 198, 210, 255));}"
            "QPushButton::hover{color: white ; ;border: 3px solid  #7194ab; border-radius: 35px;font : 75 18pt 'Arial Black';background-color: qlineargradient(spread:pad, x:0, y1:0, x2:1, y2:0, stop:0 rgba(55, 104, 136, 255), stop:1.615819 rgba(179, 198, 210, 255), stop:1 rgba(179, 198, 210, 255));}"
            "QPushButton::pressed{color: white ; ;border: 3px solid  #7194ab; border-radius: 35px;font : 75 18pt 'Arial Black';background-color: qlineargradient(spread:pad, x:0, y1:0, x2:1, y2:0, stop:0 rgba(55, 104, 136, 255), stop:1.615819 rgba(179, 198, 210, 255), stop:1 rgba(179, 198, 210, 255));padding-top:10px;}")
        self.resetButton.stop()

    def logoAnimation(self):
        self.Report_Search_Box.setGeometry(250, 330, 190, 120)
        self.pushButton.setGeometry(20, 20, 150, 80)
        #        self.Report_Search_Box.setGeometry(QtCore.QRect(0, 10, 741, 941))
        qApp.processEvents()
        time.sleep(0.5)
        text = "  Report Dashboard"
        output = ""
        rleft = 14
        lleft = 29
        x = 3
        y = 8
        for i in text:
            output += i
            rleft += 14
            lleft += 29
            x += 3
            y += 4
            self.pushButton.setText(output)
            self.pushButton.setGeometry(20, 20, 150+lleft, 80)
            self.Report_Search_Box.setGeometry(250-rleft, 330, 190+lleft+5, 120)
            time.sleep(0.05)
            qApp.processEvents()
        self.Report_Search_Box.setGeometry(0, 330, 741, 120)
        qApp.processEvents()
        print(self.pushButton.geometry())
        outer_h = 10
        value1 = 10
        value2 = 10
        while value1 <= 320:
            self.Report_Search_Box.setGeometry(0, 330 - value1, 741, 120 + value2)
            value1 += outer_h
            value2 += outer_h*2 + 6
            time.sleep(0.01)
            qApp.processEvents()
        print("Vlaue 2" , value2+120, value1)
        print(self.Report_Search_Box.geometry())

        self.checked.stop()
        self.btn_search.setVisible(True)
        self.Start_dateEdit.setVisible(True)
        self.start_time_label.setVisible(True)
        self.End_time_label.setVisible(True)
        self.End_dateEdit.setVisible(True)
        self.Part_Num_label.setVisible(True)
        self.lineEdit.setVisible(True)
        self.Report_Table.setVisible(True)
        self.closeButton.setVisible(True)
        self.Out_Card.setVisible(True)

    def updateDashboard(self, index):
        self.labelList = [self.IMAGE_11, self.IMAGE_12, self.IMAGE_13, self.IMAGE_14, self.IMAGE_15, self.IMAGE_16,
                          self.IMAGE_21, self.IMAGE_22, self.IMAGE_23, self.IMAGE_24, self.IMAGE_25, self.IMAGE_26,
                          self.IMAGE_31, self.IMAGE_32, self.IMAGE_33, self.IMAGE_34, self.IMAGE_35, self.IMAGE_36,
                          self.IMAGE_41, self.IMAGE_42, self.IMAGE_43, self.IMAGE_44, self.IMAGE_45, self.IMAGE_46,
                          self.IMAGE_51, self.IMAGE_52, self.IMAGE_53, self.IMAGE_54, self.IMAGE_55, self.IMAGE_56,
                          self.IMAGE_61, self.IMAGE_62, self.IMAGE_63, self.IMAGE_64, self.IMAGE_65, self.IMAGE_66]
        print(f"select * from LedState where testId = {int(self.checked_rows_text[self.checked_rows_text.index(self.Barcode_lineEdit.currentText())])}")
        states = self.db.searchQuery(
            f"select * from LedState where testId = {int(self.checked_rows_text[self.checked_rows_text.index(self.Barcode_lineEdit.currentText())])}")
        state = states[0][1:]
        for i in range(len(state[1:]) + 1):
            if state[i] == '1':
                self.passLabel(self.labelList[i])
            elif state[i] == '0':
                self.failLabel(self.labelList[i])
            else:
                self.notTestedLabel(self.labelList[i])
        print(index, "pass")
        self.highlight(self.checked_rows_text.index(self.Barcode_lineEdit.currentText()))

    def highlight(self, indexing):
        for row in range(self.Report_Table.rowCount()):
            for col in range(self.Report_Table.columnCount()):
                item = self.Report_Table.item(row, col)
                item.setBackground(QColor(255, 255, 255))
                qApp.processEvents()
        self.Report_Table.item(indexing, 0).setBackground(QColor(3, 227, 252))
        qApp.processEvents()
        self.Report_Table.item(indexing, 1).setBackground(QColor(3, 227, 252))
        qApp.processEvents()
        self.Report_Table.item(indexing, 2).setBackground(QColor(3, 227, 252))
        qApp.processEvents()
        self.Report_Table.item(indexing, 3).setBackground(QColor(3, 227, 252))
        qApp.processEvents()
        self.Report_Table.item(indexing, 4).setBackground(QColor(3, 227, 252))
        qApp.processEvents()
        self.Report_Table.item(indexing, 5).setBackground(QColor(3, 227, 252))
        qApp.processEvents()


    def closeFunction(self):
        self.btn_search.setVisible(False)
        self.Start_dateEdit.setVisible(False)
        self.start_time_label.setVisible(False)
        self.End_time_label.setVisible(False)
        self.End_dateEdit.setVisible(False)
        self.Part_Num_label.setVisible(False)
        self.lineEdit.setVisible(False)
        self.Report_Table.setVisible(False)
        self.closeButton.setVisible(False)
        self.Out_Card.setVisible(False)
        #        self.Report_Search_Box.setGeometry(QtCore.QRect(0, 10, 741, 941))
        #
        # self.Report_Search_Box.setGeometry(250, 330, 190, 120)
        # self.pushButton.setGeometry(20, 20, 150, 80)

        qApp.processEvents()
        # time.sleep(1)

        outer_h = 10
        value1 = 10
        value2 = 10
        while value1 <= 320:
            self.Report_Search_Box.setGeometry(0, value1, 741, 962 - value2)
            value1 += outer_h
            value2 += outer_h * 2 + 6
            time.sleep(0.01)
            qApp.processEvents()
        self.Report_Search_Box.setGeometry(0, 330, 741, 120)
        qApp.processEvents()
        text = "  Report Dashboard"
        rleft = 14
        lleft = 29
        x = 3
        y = 8
        for i in range(1, len(text)+1):
            rleft += 14
            lleft += 29
            x += 3
            y += 4
            self.pushButton.setText(text[:-i])
            self.pushButton.setGeometry(20, 20, 701 - lleft, 80)
            self.Report_Search_Box.setGeometry(rleft, 330, 741 - lleft + 5, 120)
            time.sleep(0.05)
            # print(len(self.pushButton.text()))
            qApp.processEvents()

        # print(rleft, lleft)
        # self.Report_Search_Box.setGeometry(0, 330, 741, 120)
        qApp.processEvents()
        time.sleep(0.5)
        QApplication.quit()


    def check(self):
        self.labelList = [self.IMAGE_11, self.IMAGE_12, self.IMAGE_13, self.IMAGE_14, self.IMAGE_15, self.IMAGE_16,
                          self.IMAGE_21, self.IMAGE_22, self.IMAGE_23, self.IMAGE_24, self.IMAGE_25, self.IMAGE_26,
                          self.IMAGE_31, self.IMAGE_32, self.IMAGE_33, self.IMAGE_34, self.IMAGE_35, self.IMAGE_36,
                          self.IMAGE_41, self.IMAGE_42, self.IMAGE_43, self.IMAGE_44, self.IMAGE_45, self.IMAGE_46,
                          self.IMAGE_51, self.IMAGE_52, self.IMAGE_53, self.IMAGE_54, self.IMAGE_55, self.IMAGE_56,
                          self.IMAGE_61, self.IMAGE_62, self.IMAGE_63, self.IMAGE_64, self.IMAGE_65, self.IMAGE_66]
        self.checked_states = [self.Report_Table.item(row, 0).checkState() == Qt.Checked for row in range(self.Report_Table.rowCount())]
        self.checked_rows_text = [self.Report_Table.item(row, 0).text() for row in range(self.Report_Table.rowCount())]  # if self.Report_Table.item(row, 0).checkState() == QtCore.Qt.Checked]
        self.checked_row_serial_number = [self.Report_Table.item(row, 1).text() for row in range(self.Report_Table.rowCount())]  # if self.Report_Table.item(row, 0).checkState() == QtCore.Qt.Checked]
        # print(self.checked_states, self.checked_rows_text, self.checked_row_serial_number)
        for i in self.checked_rows_text:
            if i not in self.unique_list and self.checked_states[self.checked_rows_text.index(i)] == True:
                self.unique_list.add(i)
                print(f"unique list {self.unique_list}")
                self.Barcode_lineEdit.setEditable(True)
                self.Barcode_lineEdit.lineEdit().setAlignment(Qt.AlignCenter)
                self.Barcode_lineEdit.addItem(i)
            self.Barcode_lineEdit.setStyleSheet(
                "QComboBox {background-color:rgba(0,0,0,0); color: white; font-size: 14px;text-align: center; }"
                "QComboBox QAbstractItemView { color: black; font-size: 20px; background-color: white;text-align: center; }")
            # self.Barcode_lineEdit.setEditable(False)
        if True in self.checked_states:
            MainWindow.move(0, 20)
            size = 721
            print(self.fullsize)
            if self.fullsize == 1910:
                pass
            else:
                for i in range(18):
                    self.frame.setGeometry(QRect(10, 10, self.frame.sizeHint().width() + size, 980))
                    size += 70
                    time.sleep(0.05)
                    QtWidgets.qApp.processEvents()
                states = self.db.searchQuery(
                    f"select * from LedState where testId = {int(self.checked_rows_text[self.checked_rows_text.index(self.Barcode_lineEdit.currentText())])}")
                state = states[0][1:]
                for i in range(len(state[1:]) + 1):
                    if state[i] == '1':
                        self.passLabel(self.labelList[i])
                    elif state[i] == '0':
                        self.failLabel(self.labelList[i])
                    else:
                        self.notTestedLabel(self.labelList[i])
                self.highlight(self.checked_rows_text.index(self.checked_rows_text[self.checked_states.index(True)]))
            self.fullsize = self.frame.width()


        else:
            MainWindow.move(600, 20)
            self.fullsize = 0
            self.frame.setGeometry(QtCore.QRect(10, 10, 750, 1000))


    def resetDashboard(self):
        self.Report_Table.setRowCount(0)
        MainWindow.move(600, 20)
        self.frame.setGeometry(QtCore.QRect(10, 10, 750, 1000))
        self.fullsize = 0
        self.checked_states = []
        self.checked_row_serial_number = []
        self.checked_rows_text = []
        self.unique_list = set()
        self.Barcode_lineEdit.clear()
        qApp.processEvents()


    def Search(self):
        global data
        data = []
        self.resetDashboard()
        self.db = Database()
        status = self.db.connect_DB()

        if status is None:
            return None

        start_date = str(self.Start_dateEdit.dateTime().toString("yyyy-MM-dd HH:mm:ss"))
        end_date = str(self.End_dateEdit.dateTime().toString("yyyy-MM-dd HH:mm:ss"))
        search_string = str(self.lineEdit.text())
        if start_date != "" and end_date != "":
            end_date = end_date[0:11] + "23:59:59"
            if start_date == end_date and search_string == "":
                data = self.db.searchQuery(f"Select * from Testlog where Start_Time >= '{start_date}' and End_Time <= '{end_date}'")
            elif start_date != end_date and search_string == "":
                data = self.db.searchQuery(f"Select * from Testlog where Start_Time >= '{start_date}' and End_Time <= '{end_date}'")
            elif search_string != "":
                if len(search_string) <= 24:
                    if len(search_string) == 24:
                        data = self.db.searchQuery(
                            f"Select * from Testlog where Start_Time >= '{start_date}' and End_Time <= '{end_date}' and Serial_Number = '{search_string}';")
                    elif "HE518860" in search_string.upper():
                        data = self.db.searchQuery(f"Select * from Testlog where Start_Time >= '{start_date}' and End_Time <= '{end_date}' and Serial_Number like '{search_string[0:8]}%';")
                    else:
                        data = self.db.searchQuery(
                            f"Select * from Testlog where Start_Time >= '{start_date}' and End_Time <= '{end_date}' and Serial_Number = '%{search_string}';")
                else:
                    self.Message("Error", "Wrong Barcode!")
            else:
                if len(search_string) <= 24:
                    if len(search_string) == 24:
                        data = self.db.searchQuery(
                            f"Select * from Testlog where Start_Time >= '{start_date}' and End_Time <= '{end_date}' and Serial_Number = '{search_string}';")
                    elif "HE518860" in search_string.upper():
                        data = self.db.searchQuery(f"Select * from Testlog where Start_Time >= '{start_date}' and End_Time <= '{end_date}' and Serial_Number like '{search_string[0:8]}%';")
                    else:
                        data = self.db.searchQuery(
                            f"Select * from Testlog where Start_Time >= '{start_date}' and End_Time <= '{end_date}' and Serial_Number like '%{search_string}';")
                else:
                    self.Message("Error", "Wrong Barcode!")
        else:
            data = self.db.searchQuery(f"Select * from Testlog")
        if data == []:
            self.Message("Error", "No Record(s) Found")
        else:
            self.tableUpdate(data)
        self.btn_search.setStyleSheet("color: white ; font: 75 18pt 'Arial Black' ;border: 3px solid  #7194ab; border-radius: 35px;\n"
                                      "background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:0, stop:0 rgba(55, 104, 136, 255), stop:1.615819 rgba(179, 198, 210, 255), stop:1 rgba(179, 198, 210, 255));")
        shadow_effect = QGraphicsDropShadowEffect(self.btn_search)
        shadow_effect.setColor(QColor(0, 0, 0, 200))  # Shadow color (black with alpha)
        shadow_effect.setBlurRadius(50)  # Shadow blur radius
        shadow_effect.setXOffset(0)  # Shadow x-offset
        shadow_effect.setYOffset(0)  # Shadow y-offset
        self.btn_search.setGraphicsEffect(shadow_effect)
        self.resetButton.timeout.connect(self.resetButtonFunction)
        self.resetButton.start(1000)


    def Message(self, title: str = "MESSAGE", prompt: str = ""):
        self.message = QMessageBox()
        self.message.setWindowTitle(title)
        self.message.setWindowIcon(QIcon(f"{os.getcwd()}\images\logo_1.png"))
        self.message.setText(prompt)
        self.message.setStandardButtons(QMessageBox.StandardButton.Ok)
        self.message.exec_()

    def tableUpdate(self, parameters):
        if parameters is None:
            self.Message("Error!", "Database is empty")
        else:
            self.Report_Table.setRowCount(len(parameters))
            for i in range(len(parameters)):
                self.Report_Table.setItem(i, 0, QTableWidgetItem(str(parameters[i][0])))
                self.Report_Table.item(i, 0).setTextAlignment(Qt.AlignCenter)
                self.Report_Table.item(i, 0).setBackground(QBrush(QtGui.QColor(255, 255, 255)))
                self.Report_Table.item(i, 0).setCheckState(Qt.Unchecked)
                self.Report_Table.setStyleSheet("color:black; font: 50 10pt 'Arial Rounded MT Bold'")

            for i in range(len(parameters)):
                self.Report_Table.setItem(i, 1, QTableWidgetItem(parameters[i][1]))
                self.Report_Table.item(i, 1).setBackground(QBrush(QtGui.QColor(255, 255, 255)))
                self.Report_Table.item(i, 1).setTextAlignment(Qt.AlignCenter)

            for i in range(len(parameters)):
                self.Report_Table.setItem(i, 2, QTableWidgetItem(parameters[i][2]))
                self.Report_Table.item(i, 2).setBackground(QBrush(QtGui.QColor(255, 255, 255)))
                self.Report_Table.item(i, 2).setTextAlignment(Qt.AlignCenter)

            for i in range(len(parameters)):
                self.Report_Table.setItem(i, 3, QTableWidgetItem(parameters[i][3]))
                self.Report_Table.item(i, 3).setBackground(QBrush(QtGui.QColor(255, 255, 255)))
                self.Report_Table.item(i, 3).setTextAlignment(Qt.AlignCenter)

            for i in range(len(parameters)):
                self.Report_Table.setItem(i, 4, QTableWidgetItem(parameters[i][4]))
                self.Report_Table.item(i, 4).setBackground(QBrush(QtGui.QColor(255, 255, 255)))
                self.Report_Table.item(i, 4).setTextAlignment(Qt.AlignCenter)

            for i in range(len(parameters)):
                self.Report_Table.setItem(i, 5, QTableWidgetItem(parameters[i][5]))
                self.Report_Table.item(i, 5).setBackground(QBrush(QtGui.QColor(255, 255, 255)))
                self.Report_Table.item(i, 5).setTextAlignment(Qt.AlignCenter)

    def passLabel(self, label_text):
        label_text.setPixmap(
            QtGui.QPixmap(f"{os.getcwd()}\images\Tick.png"))
        QtWidgets.qApp.processEvents()

    def failLabel(self, label_text):
        label_text.setPixmap(
            QtGui.QPixmap(f"{os.getcwd()}\images\Cross.png"))
        QtWidgets.qApp.processEvents()

    def notTestedLabel(self, label_text):
        label_text.setPixmap(QtGui.QPixmap(f"{os.getcwd()}\images\icons_335318.svg"))
        QtWidgets.qApp.processEvents()

    def checkversion(self):
        self.Message(title="ERROR", prompt="Can't Execute this program below Windows 10")
        self.closeFunction()


if __name__ == "__main__":
    import sys
    import platform
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QWidget()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    # MainWindow.showMaximized()
    MainWindow.setWindowFlag(QtCore.Qt.FramelessWindowHint)
    MainWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)
    MainWindow.setAttribute(QtCore.Qt.WA_NoSystemBackground, True)
    MainWindow.show()
    sys.exit(app.exec_())
