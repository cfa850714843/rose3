# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DockerMe(object):
    def setupUi(self, DockerMe):
        DockerMe.setObjectName("DockerMe")
        DockerMe.resize(965, 585)
        self.centralwidget = QtWidgets.QWidget(DockerMe)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 411, 241))
        self.tabWidget.setObjectName("tabWidget")
        self.Image = QtWidgets.QWidget()
        self.Image.setObjectName("Image")
        self.tabWidget.addTab(self.Image, "")
        self.Container = QtWidgets.QWidget()
        self.Container.setObjectName("Container")
        self.tabWidget.addTab(self.Container, "")
        DockerMe.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(DockerMe)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 965, 21))
        self.menubar.setObjectName("menubar")
        self.menustart = QtWidgets.QMenu(self.menubar)
        self.menustart.setObjectName("menustart")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        self.menuHELP = QtWidgets.QMenu(self.menubar)
        self.menuHELP.setObjectName("menuHELP")
        DockerMe.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(DockerMe)
        self.statusbar.setObjectName("statusbar")
        DockerMe.setStatusBar(self.statusbar)
        self.actionhelp = QtWidgets.QAction(DockerMe)
        self.actionhelp.setObjectName("actionhelp")
        self.actionrun = QtWidgets.QAction(DockerMe)
        self.actionrun.setObjectName("actionrun")
        self.actionINFO = QtWidgets.QAction(DockerMe)
        self.actionINFO.setObjectName("actionINFO")
        self.menustart.addAction(self.actionhelp)
        self.menustart.addAction(self.actionrun)
        self.menustart.addAction(self.actionINFO)
        self.menubar.addAction(self.menustart.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.menubar.addAction(self.menuHELP.menuAction())

        self.retranslateUi(DockerMe)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(DockerMe)

    def retranslateUi(self, DockerMe):
        _translate = QtCore.QCoreApplication.translate
        DockerMe.setWindowTitle(_translate("DockerMe", "DockerMe"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Image), _translate("DockerMe", "Image"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Container), _translate("DockerMe", "Container"))
        self.menustart.setTitle(_translate("DockerMe", "Start"))
        self.menuAbout.setTitle(_translate("DockerMe", "About"))
        self.menuHELP.setTitle(_translate("DockerMe", "Help"))
        self.actionhelp.setText(_translate("DockerMe", "HELP"))
        self.actionrun.setText(_translate("DockerMe", "RUN"))
        self.actionINFO.setText(_translate("DockerMe", "INFO"))
