# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'task4.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1069, 804)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_18 = QtWidgets.QFrame(self.centralwidget)
        self.frame_18.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_18.setObjectName("frame_18")
        self.horizontalLayout.addWidget(self.frame_18)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_4 = QtWidgets.QFrame(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_1 = QtWidgets.QLabel(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_1.sizePolicy().hasHeightForWidth())
        self.label_1.setSizePolicy(sizePolicy)
        self.label_1.setStyleSheet("background-color: rgb(207, 207, 207);\n"
"font: 75 9pt \"MS Shell Dlg 2\";")
        self.label_1.setObjectName("label_1")
        self.horizontalLayout_3.addWidget(self.label_1)
        self.frame_5 = QtWidgets.QFrame(self.frame_4)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.comboBox = QtWidgets.QComboBox(self.frame_5)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.verticalLayout_2.addWidget(self.comboBox)
        self.label_2 = QtWidgets.QLabel(self.frame_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setStyleSheet("background-color: rgb(207, 207, 207);")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.horizontalLayout_3.addWidget(self.frame_5)
        self.verticalLayout.addWidget(self.frame_4)
        self.frame_6 = QtWidgets.QFrame(self.frame_2)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.frame_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setStyleSheet("background-color: rgb(207, 207, 207);\n"
"font: 75 9pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.frame_7 = QtWidgets.QFrame(self.frame_6)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.comboBox_2 = QtWidgets.QComboBox(self.frame_7)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.verticalLayout_3.addWidget(self.comboBox_2)
        self.label_4 = QtWidgets.QLabel(self.frame_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setStyleSheet("background-color: rgb(207, 207, 207);\n"
"")
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        self.horizontalLayout_4.addWidget(self.frame_7)
        self.verticalLayout.addWidget(self.frame_6)
        self.frame_8 = QtWidgets.QFrame(self.frame_2)
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.frame_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setStyleSheet("background-color: rgb(207, 207, 207);\n"
"font: 75 9pt \"MS Shell Dlg 2\";")
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.frame_9 = QtWidgets.QFrame(self.frame_8)
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_9)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.comboBox_3 = QtWidgets.QComboBox(self.frame_9)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.verticalLayout_4.addWidget(self.comboBox_3)
        self.label_6 = QtWidgets.QLabel(self.frame_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setStyleSheet("background-color: rgb(207, 207, 207);")
        self.label_6.setObjectName("label_6")
        self.verticalLayout_4.addWidget(self.label_6)
        self.horizontalLayout_5.addWidget(self.frame_9)
        self.verticalLayout.addWidget(self.frame_8)
        self.frame_10 = QtWidgets.QFrame(self.frame_2)
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_10.setObjectName("frame_10")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_10)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_7 = QtWidgets.QLabel(self.frame_10)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setStyleSheet("background-color: rgb(207, 207, 207);\n"
"font: 75 9pt \"MS Shell Dlg 2\";")
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_6.addWidget(self.label_7)
        self.frame_11 = QtWidgets.QFrame(self.frame_10)
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_11)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.comboBox_4 = QtWidgets.QComboBox(self.frame_11)
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.verticalLayout_5.addWidget(self.comboBox_4)
        self.label_8 = QtWidgets.QLabel(self.frame_11)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setStyleSheet("background-color: rgb(207, 207, 207);")
        self.label_8.setObjectName("label_8")
        self.verticalLayout_5.addWidget(self.label_8)
        self.horizontalLayout_6.addWidget(self.frame_11)
        self.verticalLayout.addWidget(self.frame_10)
        self.horizontalLayout_2.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.frame_12 = QtWidgets.QFrame(self.frame_3)
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_12)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.comboBox_5 = QtWidgets.QComboBox(self.frame_12)
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.addItem("")
        self.verticalLayout_8.addWidget(self.comboBox_5)
        self.frame_14 = QtWidgets.QFrame(self.frame_12)
        self.frame_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_14)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_11 = QtWidgets.QLabel(self.frame_14)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_7.addWidget(self.label_11)
        self.speed_slider = QtWidgets.QSlider(self.frame_14)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.speed_slider.sizePolicy().hasHeightForWidth())
        self.speed_slider.setSizePolicy(sizePolicy)
        self.speed_slider.setMinimumSize(QtCore.QSize(0, 0))
        self.speed_slider.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.speed_slider.setMinimum(1)
        self.speed_slider.setMaximum(8)
        self.speed_slider.setProperty("value", 4)
        self.speed_slider.setTracking(True)
        self.speed_slider.setOrientation(QtCore.Qt.Horizontal)
        self.speed_slider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.speed_slider.setTickInterval(0)
        self.speed_slider.setObjectName("speed_slider")
        self.horizontalLayout_7.addWidget(self.speed_slider)
        self.lcdNumber = QtWidgets.QLCDNumber(self.frame_14)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lcdNumber.sizePolicy().hasHeightForWidth())
        self.lcdNumber.setSizePolicy(sizePolicy)
        self.lcdNumber.setMaximumSize(QtCore.QSize(50, 25))
        self.lcdNumber.setObjectName("lcdNumber")
        self.horizontalLayout_7.addWidget(self.lcdNumber)
        self.verticalLayout_8.addWidget(self.frame_14)
        self.frame_15 = QtWidgets.QFrame(self.frame_12)
        self.frame_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_15)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_12 = QtWidgets.QLabel(self.frame_15)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_8.addWidget(self.label_12)
        self.speed_slider_2 = QtWidgets.QSlider(self.frame_15)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.speed_slider_2.sizePolicy().hasHeightForWidth())
        self.speed_slider_2.setSizePolicy(sizePolicy)
        self.speed_slider_2.setMinimumSize(QtCore.QSize(0, 0))
        self.speed_slider_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.speed_slider_2.setMinimum(1)
        self.speed_slider_2.setMaximum(8)
        self.speed_slider_2.setProperty("value", 4)
        self.speed_slider_2.setTracking(True)
        self.speed_slider_2.setOrientation(QtCore.Qt.Horizontal)
        self.speed_slider_2.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.speed_slider_2.setTickInterval(0)
        self.speed_slider_2.setObjectName("speed_slider_2")
        self.horizontalLayout_8.addWidget(self.speed_slider_2)
        self.lcdNumber_2 = QtWidgets.QLCDNumber(self.frame_15)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lcdNumber_2.sizePolicy().hasHeightForWidth())
        self.lcdNumber_2.setSizePolicy(sizePolicy)
        self.lcdNumber_2.setMaximumSize(QtCore.QSize(50, 25))
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.horizontalLayout_8.addWidget(self.lcdNumber_2)
        self.verticalLayout_8.addWidget(self.frame_15)
        self.frame_17 = QtWidgets.QFrame(self.frame_12)
        self.frame_17.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_17.setObjectName("frame_17")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_17)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_14 = QtWidgets.QLabel(self.frame_17)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_10.addWidget(self.label_14)
        self.speed_slider_4 = QtWidgets.QSlider(self.frame_17)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.speed_slider_4.sizePolicy().hasHeightForWidth())
        self.speed_slider_4.setSizePolicy(sizePolicy)
        self.speed_slider_4.setMinimumSize(QtCore.QSize(0, 0))
        self.speed_slider_4.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.speed_slider_4.setMinimum(1)
        self.speed_slider_4.setMaximum(8)
        self.speed_slider_4.setProperty("value", 4)
        self.speed_slider_4.setTracking(True)
        self.speed_slider_4.setOrientation(QtCore.Qt.Horizontal)
        self.speed_slider_4.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.speed_slider_4.setTickInterval(0)
        self.speed_slider_4.setObjectName("speed_slider_4")
        self.horizontalLayout_10.addWidget(self.speed_slider_4)
        self.lcdNumber_4 = QtWidgets.QLCDNumber(self.frame_17)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lcdNumber_4.sizePolicy().hasHeightForWidth())
        self.lcdNumber_4.setSizePolicy(sizePolicy)
        self.lcdNumber_4.setMaximumSize(QtCore.QSize(50, 25))
        self.lcdNumber_4.setObjectName("lcdNumber_4")
        self.horizontalLayout_10.addWidget(self.lcdNumber_4)
        self.verticalLayout_8.addWidget(self.frame_17)
        self.frame_16 = QtWidgets.QFrame(self.frame_12)
        self.frame_16.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_16.setObjectName("frame_16")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame_16)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_13 = QtWidgets.QLabel(self.frame_16)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_9.addWidget(self.label_13)
        self.speed_slider_3 = QtWidgets.QSlider(self.frame_16)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.speed_slider_3.sizePolicy().hasHeightForWidth())
        self.speed_slider_3.setSizePolicy(sizePolicy)
        self.speed_slider_3.setMinimumSize(QtCore.QSize(0, 0))
        self.speed_slider_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.speed_slider_3.setMinimum(1)
        self.speed_slider_3.setMaximum(8)
        self.speed_slider_3.setProperty("value", 4)
        self.speed_slider_3.setTracking(True)
        self.speed_slider_3.setOrientation(QtCore.Qt.Horizontal)
        self.speed_slider_3.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.speed_slider_3.setTickInterval(0)
        self.speed_slider_3.setObjectName("speed_slider_3")
        self.horizontalLayout_9.addWidget(self.speed_slider_3)
        self.lcdNumber_3 = QtWidgets.QLCDNumber(self.frame_16)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lcdNumber_3.sizePolicy().hasHeightForWidth())
        self.lcdNumber_3.setSizePolicy(sizePolicy)
        self.lcdNumber_3.setMaximumSize(QtCore.QSize(50, 25))
        self.lcdNumber_3.setObjectName("lcdNumber_3")
        self.horizontalLayout_9.addWidget(self.lcdNumber_3)
        self.verticalLayout_8.addWidget(self.frame_16)
        self.verticalLayout_6.addWidget(self.frame_12)
        self.frame_13 = QtWidgets.QFrame(self.frame_3)
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_13)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_9 = QtWidgets.QLabel(self.frame_13)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_7.addWidget(self.label_9)
        self.label_10 = QtWidgets.QLabel(self.frame_13)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_7.addWidget(self.label_10)
        self.verticalLayout_6.addWidget(self.frame_13)
        self.horizontalLayout_2.addWidget(self.frame_3)
        self.horizontalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1069, 26))
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menuBar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menuBar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionUniform_Range_Mode = QtWidgets.QAction(MainWindow)
        self.actionUniform_Range_Mode.setCheckable(True)
        self.actionUniform_Range_Mode.setChecked(True)
        self.actionUniform_Range_Mode.setObjectName("actionUniform_Range_Mode")
        self.actionMusical_Instruments_Mode = QtWidgets.QAction(MainWindow)
        self.actionMusical_Instruments_Mode.setCheckable(True)
        self.actionMusical_Instruments_Mode.setObjectName("actionMusical_Instruments_Mode")
        self.actionAnimals_Sound_Mode = QtWidgets.QAction(MainWindow)
        self.actionAnimals_Sound_Mode.setCheckable(True)
        self.actionAnimals_Sound_Mode.setObjectName("actionAnimals_Sound_Mode")
        self.actionECG_Mode = QtWidgets.QAction(MainWindow)
        self.actionECG_Mode.setCheckable(True)
        self.actionECG_Mode.setObjectName("actionECG_Mode")
        self.actionCall_3asfoor = QtWidgets.QAction(MainWindow)
        self.actionCall_3asfoor.setObjectName("actionCall_3asfoor")
        self.actionPlay_Input = QtWidgets.QAction(MainWindow)
        self.actionPlay_Input.setCheckable(False)
        self.actionPlay_Input.setChecked(False)
        self.actionPlay_Input.setObjectName("actionPlay_Input")
        self.actionPlay_Output = QtWidgets.QAction(MainWindow)
        self.actionPlay_Output.setObjectName("actionPlay_Output")
        self.actionPlay_Input_2 = QtWidgets.QAction(MainWindow)
        self.actionPlay_Input_2.setObjectName("actionPlay_Input_2")
        self.actionPlay_Output_2 = QtWidgets.QAction(MainWindow)
        self.actionPlay_Output_2.setObjectName("actionPlay_Output_2")
        self.menuFile.addAction(self.actionOpen)
        self.menuHelp.addAction(self.actionCall_3asfoor)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_1.setText(_translate("MainWindow", "Double click to add Image"))
        self.comboBox.setItemText(0, _translate("MainWindow", "FT Magnitude"))
        self.comboBox.setItemText(1, _translate("MainWindow", "FT Phase"))
        self.comboBox.setItemText(2, _translate("MainWindow", "FT Real"))
        self.comboBox.setItemText(3, _translate("MainWindow", "FT Imaginary"))
        self.label_2.setText(_translate("MainWindow", "TextLabel"))
        self.label_3.setText(_translate("MainWindow", "Double click to add Image"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "FT Magnitude"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "FT Phase"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "FT Real"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "FT Imaginary"))
        self.label_4.setText(_translate("MainWindow", "TextLabel"))
        self.label_5.setText(_translate("MainWindow", "Double click to add Image"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "FT Magnitude"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "FT Phase"))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "FT Real"))
        self.comboBox_3.setItemText(3, _translate("MainWindow", "FT Imaginary"))
        self.label_6.setText(_translate("MainWindow", "TextLabel"))
        self.label_7.setText(_translate("MainWindow", "Double click to add Image"))
        self.comboBox_4.setItemText(0, _translate("MainWindow", "FT Magnitude"))
        self.comboBox_4.setItemText(1, _translate("MainWindow", "FT Phase"))
        self.comboBox_4.setItemText(2, _translate("MainWindow", "FT Real"))
        self.comboBox_4.setItemText(3, _translate("MainWindow", "FT Imaginary"))
        self.label_8.setText(_translate("MainWindow", "TextLabel"))
        self.comboBox_5.setItemText(0, _translate("MainWindow", "1 - 2"))
        self.label_11.setText(_translate("MainWindow", "Component 1"))
        self.label_12.setText(_translate("MainWindow", "Component 2"))
        self.label_14.setText(_translate("MainWindow", "Component 3"))
        self.label_13.setText(_translate("MainWindow", "Component 4"))
        self.label_9.setText(_translate("MainWindow", "TextLabel"))
        self.label_10.setText(_translate("MainWindow", "TextLabel"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionUniform_Range_Mode.setText(_translate("MainWindow", "Uniform Range Mode"))
        self.actionMusical_Instruments_Mode.setText(_translate("MainWindow", "Musical Instruments Mode"))
        self.actionAnimals_Sound_Mode.setText(_translate("MainWindow", "Animals Sound Mode"))
        self.actionECG_Mode.setText(_translate("MainWindow", "ECG Mode"))
        self.actionCall_3asfoor.setText(_translate("MainWindow", "Call 3asfoor"))
        self.actionPlay_Input.setText(_translate("MainWindow", "Play Input"))
        self.actionPlay_Output.setText(_translate("MainWindow", "Play Output"))
        self.actionPlay_Input_2.setText(_translate("MainWindow", "Play Input"))
        self.actionPlay_Output_2.setText(_translate("MainWindow", "Play Output"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
