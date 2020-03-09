# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainUI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Face_Recognition_window(object):
    def setupUi(self, Face_Recognition_window):
        Face_Recognition_window.setObjectName("Face_Recognition_window")
        Face_Recognition_window.resize(843, 694)
        Face_Recognition_window.setMinimumSize(QtCore.QSize(843, 694))
        Face_Recognition_window.setMaximumSize(QtCore.QSize(843, 694))
        Face_Recognition_window.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.centralwidget = QtWidgets.QWidget(Face_Recognition_window)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 40, 798, 557))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lab_frame = QtWidgets.QLabel(self.layoutWidget)
        self.lab_frame.setEnabled(True)
        self.lab_frame.setMinimumSize(QtCore.QSize(641, 481))
        self.lab_frame.setMaximumSize(QtCore.QSize(641, 481))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(False)
        font.setWeight(50)
        self.lab_frame.setFont(font)
        self.lab_frame.setToolTip("")
        self.lab_frame.setTextFormat(QtCore.Qt.RichText)
        self.lab_frame.setAlignment(QtCore.Qt.AlignCenter)
        self.lab_frame.setObjectName("lab_frame")
        self.verticalLayout.addWidget(self.lab_frame)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lab_selecCalss = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lab_selecCalss.setFont(font)
        self.lab_selecCalss.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lab_selecCalss.setObjectName("lab_selecCalss")
        self.verticalLayout_2.addWidget(self.lab_selecCalss)
        self.lab_selecLable = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lab_selecLable.setFont(font)
        self.lab_selecLable.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lab_selecLable.setObjectName("lab_selecLable")
        self.verticalLayout_2.addWidget(self.lab_selecLable)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.comboBox_selectClass = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox_selectClass.setObjectName("comboBox_selectClass")
        self.verticalLayout_3.addWidget(self.comboBox_selectClass)
        self.comboBox_selectLabel = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox_selectLabel.setObjectName("comboBox_selectLabel")
        self.verticalLayout_3.addWidget(self.comboBox_selectLabel)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.btn_openCamera = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_openCamera.setMaximumSize(QtCore.QSize(200, 60))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.btn_openCamera.setFont(font)
        self.btn_openCamera.setObjectName("btn_openCamera")
        self.verticalLayout_4.addWidget(self.btn_openCamera)
        self.btn_addNewFace = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_addNewFace.setMinimumSize(QtCore.QSize(50, 50))
        self.btn_addNewFace.setMaximumSize(QtCore.QSize(200, 60))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.btn_addNewFace.setFont(font)
        self.btn_addNewFace.setAutoRepeatInterval(100)
        self.btn_addNewFace.setObjectName("btn_addNewFace")
        self.verticalLayout_4.addWidget(self.btn_addNewFace)
        self.btn_takePhoto = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_takePhoto.setMaximumSize(QtCore.QSize(200, 60))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.btn_takePhoto.setFont(font)
        self.btn_takePhoto.setObjectName("btn_takePhoto")
        self.verticalLayout_4.addWidget(self.btn_takePhoto)
        self.btn_train = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_train.setMinimumSize(QtCore.QSize(100, 50))
        self.btn_train.setMaximumSize(QtCore.QSize(200, 60))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.btn_train.setFont(font)
        self.btn_train.setObjectName("btn_train")
        self.verticalLayout_4.addWidget(self.btn_train)
        self.btn_recogniton = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_recogniton.setMinimumSize(QtCore.QSize(100, 50))
        self.btn_recogniton.setMaximumSize(QtCore.QSize(200, 60))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.btn_recogniton.setFont(font)
        self.btn_recogniton.setObjectName("btn_recogniton")
        self.verticalLayout_4.addWidget(self.btn_recogniton)
        self.btn_delFace = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_delFace.setMinimumSize(QtCore.QSize(100, 50))
        self.btn_delFace.setMaximumSize(QtCore.QSize(200, 60))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.btn_delFace.setFont(font)
        self.btn_delFace.setObjectName("btn_delFace")
        self.verticalLayout_4.addWidget(self.btn_delFace)
        self.btn_refresh = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_refresh.setMinimumSize(QtCore.QSize(100, 50))
        self.btn_refresh.setMaximumSize(QtCore.QSize(200, 60))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.btn_refresh.setFont(font)
        self.btn_refresh.setObjectName("btn_refresh")
        self.verticalLayout_4.addWidget(self.btn_refresh)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        Face_Recognition_window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Face_Recognition_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 843, 23))
        self.menubar.setObjectName("menubar")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        Face_Recognition_window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Face_Recognition_window)
        self.statusbar.setObjectName("statusbar")
        Face_Recognition_window.setStatusBar(self.statusbar)
        self.actionAdd_Person = QtWidgets.QAction(Face_Recognition_window)
        self.actionAdd_Person.setObjectName("actionAdd_Person")
        self.actionDelete_Person = QtWidgets.QAction(Face_Recognition_window)
        self.actionDelete_Person.setObjectName("actionDelete_Person")
        self.actionHelp = QtWidgets.QAction(Face_Recognition_window)
        self.actionHelp.setObjectName("actionHelp")
        self.actionExit = QtWidgets.QAction(Face_Recognition_window)
        self.actionExit.setObjectName("actionExit")
        self.actionauthor = QtWidgets.QAction(Face_Recognition_window)
        self.actionauthor.setObjectName("actionauthor")
        self.actionAddClass = QtWidgets.QAction(Face_Recognition_window)
        self.actionAddClass.setObjectName("actionAddClass")
        self.actionDelClass = QtWidgets.QAction(Face_Recognition_window)
        self.actionDelClass.setObjectName("actionDelClass")
        self.menuHelp.addAction(self.actionHelp)
        self.menuHelp.addAction(self.actionauthor)
        self.menu.addAction(self.actionAddClass)
        self.menu.addAction(self.actionDelClass)
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(Face_Recognition_window)
        QtCore.QMetaObject.connectSlotsByName(Face_Recognition_window)

    def retranslateUi(self, Face_Recognition_window):
        _translate = QtCore.QCoreApplication.translate
        Face_Recognition_window.setWindowTitle(_translate("Face_Recognition_window", "人脸识别1.0"))
        self.lab_frame.setText(_translate("Face_Recognition_window", "没有图像输入"))
        self.lab_selecCalss.setText(_translate("Face_Recognition_window", "选择班级"))
        self.lab_selecLable.setText(_translate("Face_Recognition_window", "选择学号"))
        self.btn_openCamera.setText(_translate("Face_Recognition_window", "打开摄像头"))
        self.btn_addNewFace.setText(_translate("Face_Recognition_window", "添加新用户"))
        self.btn_takePhoto.setText(_translate("Face_Recognition_window", "录入人脸"))
        self.btn_train.setText(_translate("Face_Recognition_window", "提取特征"))
        self.btn_recogniton.setText(_translate("Face_Recognition_window", "开始检测"))
        self.btn_delFace.setText(_translate("Face_Recognition_window", "删除人脸"))
        self.btn_refresh.setText(_translate("Face_Recognition_window", "刷新"))
        self.menuHelp.setTitle(_translate("Face_Recognition_window", "帮助"))
        self.menu.setTitle(_translate("Face_Recognition_window", "创建新表"))
        self.actionAdd_Person.setText(_translate("Face_Recognition_window", "添加人脸"))
        self.actionDelete_Person.setText(_translate("Face_Recognition_window", "删除人脸"))
        self.actionHelp.setText(_translate("Face_Recognition_window", "操作细节"))
        self.actionExit.setText(_translate("Face_Recognition_window", "退出"))
        self.actionauthor.setText(_translate("Face_Recognition_window", "关于作者"))
        self.actionAddClass.setText(_translate("Face_Recognition_window", "添加新班级"))
        self.actionDelClass.setText(_translate("Face_Recognition_window", "删除班级表"))

