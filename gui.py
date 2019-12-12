# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(770, 650)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 10, 651, 91))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(55)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.augment = QtWidgets.QPushButton(self.centralwidget)
        self.augment.setGeometry(QtCore.QRect(430, 560, 181, 51))
        self.augment.setToolTip("")
        self.augment.setStyleSheet("QPushButton#augment{\n"
"color: rgb(0, 0, 0);\n"
"            background-color: #ffff8d; \n"
"        }\n"
"        QPushButton#augment:hover {\n"
"            background-color: #ffff00; \n"
"        }\n"
"        QPushButton#augment:pressed {\n"
"            background-color: #ffea00;\n"
"        }    ")
        self.augment.setObjectName("augment")
        self.quit = QtWidgets.QPushButton(self.centralwidget)
        self.quit.setGeometry(QtCore.QRect(630, 560, 121, 51))
        self.quit.setStyleSheet("QPushButton#quit{\n"
"            color: rgb(0, 0, 0);\n"
"            background-color: #ff9e80;\n"
"        }\n"
"        QPushButton#quit:hover {\n"
"            background-color: #ff6e40;\n"
"        }\n"
"        QPushButton#quit:pressed {\n"
"            background-color: #ff3d00;\n"
"        }    ")
        self.quit.setObjectName("quit")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(180, 284, 61, 25))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(16)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(136, 138, 133);")
        self.label_4.setObjectName("label_4")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(430, 170, 321, 381))
        self.tabWidget.setStyleSheet("")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(10, 40, 71, 17))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_9 = QtWidgets.QLabel(self.tab)
        self.label_9.setGeometry(QtCore.QRect(10, 80, 121, 17))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.tab)
        self.label_10.setGeometry(QtCore.QRect(10, 120, 111, 17))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.tab)
        self.label_11.setGeometry(QtCore.QRect(10, 160, 191, 17))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.tab)
        self.label_12.setGeometry(QtCore.QRect(10, 200, 211, 17))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.tab)
        self.label_13.setGeometry(QtCore.QRect(10, 240, 231, 17))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.tab)
        self.label_14.setGeometry(QtCore.QRect(10, 280, 221, 17))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.gcc = QtWidgets.QPushButton(self.tab)
        self.gcc.setGeometry(QtCore.QRect(220, 240, 89, 25))
        self.gcc.setObjectName("gcc")
        self.resz = QtWidgets.QPushButton(self.tab)
        self.resz.setGeometry(QtCore.QRect(220, 40, 89, 25))
        self.resz.setObjectName("resz")
        self.pchmul = QtWidgets.QPushButton(self.tab)
        self.pchmul.setGeometry(QtCore.QRect(220, 280, 89, 25))
        self.pchmul.setObjectName("pchmul")
        self.pad = QtWidgets.QPushButton(self.tab)
        self.pad.setGeometry(QtCore.QRect(220, 80, 89, 25))
        self.pad.setObjectName("pad")
        self.gc = QtWidgets.QPushButton(self.tab)
        self.gc.setGeometry(QtCore.QRect(220, 200, 89, 25))
        self.gc.setObjectName("gc")
        self.hsi = QtWidgets.QPushButton(self.tab)
        self.hsi.setGeometry(QtCore.QRect(220, 160, 89, 25))
        self.hsi.setObjectName("hsi")
        self.flip = QtWidgets.QPushButton(self.tab)
        self.flip.setGeometry(QtCore.QRect(220, 120, 89, 25))
        self.flip.setObjectName("flip")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.mb = QtWidgets.QPushButton(self.tab_2)
        self.mb.setGeometry(QtCore.QRect(220, 120, 89, 25))
        self.mb.setObjectName("mb")
        self.label_15 = QtWidgets.QLabel(self.tab_2)
        self.label_15.setGeometry(QtCore.QRect(10, 160, 171, 17))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.gb = QtWidgets.QPushButton(self.tab_2)
        self.gb.setGeometry(QtCore.QRect(220, 40, 89, 25))
        self.gb.setObjectName("gb")
        self.label_16 = QtWidgets.QLabel(self.tab_2)
        self.label_16.setGeometry(QtCore.QRect(10, 200, 171, 17))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.tab_2)
        self.label_17.setGeometry(QtCore.QRect(10, 240, 221, 17))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.bb = QtWidgets.QPushButton(self.tab_2)
        self.bb.setEnabled(True)
        self.bb.setGeometry(QtCore.QRect(220, 160, 89, 25))
        self.bb.setObjectName("bb")
        self.mor2 = QtWidgets.QPushButton(self.tab_2)
        self.mor2.setGeometry(QtCore.QRect(220, 280, 89, 25))
        self.mor2.setObjectName("mor2")
        self.label_18 = QtWidgets.QLabel(self.tab_2)
        self.label_18.setGeometry(QtCore.QRect(10, 40, 131, 17))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.tab_2)
        self.label_19.setGeometry(QtCore.QRect(10, 319, 191, 17))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.mor1 = QtWidgets.QPushButton(self.tab_2)
        self.mor1.setGeometry(QtCore.QRect(220, 240, 89, 25))
        self.mor1.setObjectName("mor1")
        self.ab = QtWidgets.QPushButton(self.tab_2)
        self.ab.setGeometry(QtCore.QRect(220, 80, 89, 25))
        self.ab.setObjectName("ab")
        self.label_20 = QtWidgets.QLabel(self.tab_2)
        self.label_20.setGeometry(QtCore.QRect(10, 280, 231, 17))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.tab_2)
        self.label_21.setGeometry(QtCore.QRect(10, 80, 141, 17))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.cc = QtWidgets.QPushButton(self.tab_2)
        self.cc.setGeometry(QtCore.QRect(220, 200, 89, 25))
        self.cc.setObjectName("cc")
        self.sharp = QtWidgets.QPushButton(self.tab_2)
        self.sharp.setGeometry(QtCore.QRect(220, 316, 89, 25))
        self.sharp.setObjectName("sharp")
        self.label_22 = QtWidgets.QLabel(self.tab_2)
        self.label_22.setGeometry(QtCore.QRect(10, 120, 151, 17))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.label_39 = QtWidgets.QLabel(self.tab_5)
        self.label_39.setGeometry(QtCore.QRect(10, 40, 121, 17))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_39.setFont(font)
        self.label_39.setObjectName("label_39")
        self.emboss = QtWidgets.QPushButton(self.tab_5)
        self.emboss.setGeometry(QtCore.QRect(220, 40, 89, 25))
        self.emboss.setObjectName("emboss")
        self.label_40 = QtWidgets.QLabel(self.tab_5)
        self.label_40.setGeometry(QtCore.QRect(10, 240, 191, 17))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_40.setFont(font)
        self.label_40.setObjectName("label_40")
        self.label_41 = QtWidgets.QLabel(self.tab_5)
        self.label_41.setGeometry(QtCore.QRect(10, 80, 161, 17))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_41.setFont(font)
        self.label_41.setObjectName("label_41")
        self.pnoi = QtWidgets.QPushButton(self.tab_5)
        self.pnoi.setGeometry(QtCore.QRect(220, 200, 89, 25))
        self.pnoi.setObjectName("pnoi")
        self.label_42 = QtWidgets.QLabel(self.tab_5)
        self.label_42.setGeometry(QtCore.QRect(10, 120, 181, 17))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_42.setFont(font)
        self.label_42.setObjectName("label_42")
        self.label_43 = QtWidgets.QLabel(self.tab_5)
        self.label_43.setGeometry(QtCore.QRect(10, 200, 181, 17))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_43.setFont(font)
        self.label_43.setObjectName("label_43")
        self.sp = QtWidgets.QPushButton(self.tab_5)
        self.sp.setGeometry(QtCore.QRect(220, 160, 89, 25))
        self.sp.setObjectName("sp")
        self.label_44 = QtWidgets.QLabel(self.tab_5)
        self.label_44.setGeometry(QtCore.QRect(10, 160, 191, 17))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_44.setFont(font)
        self.label_44.setObjectName("label_44")
        self.contrast = QtWidgets.QPushButton(self.tab_5)
        self.contrast.setGeometry(QtCore.QRect(220, 280, 89, 25))
        self.contrast.setObjectName("contrast")
        self.label_45 = QtWidgets.QLabel(self.tab_5)
        self.label_45.setGeometry(QtCore.QRect(10, 316, 191, 17))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_45.setFont(font)
        self.label_45.setObjectName("label_45")
        self.label_46 = QtWidgets.QLabel(self.tab_5)
        self.label_46.setGeometry(QtCore.QRect(10, 280, 211, 17))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_46.setFont(font)
        self.label_46.setObjectName("label_46")
        self.edge = QtWidgets.QPushButton(self.tab_5)
        self.edge.setGeometry(QtCore.QRect(220, 80, 89, 25))
        self.edge.setObjectName("edge")
        self.scale = QtWidgets.QPushButton(self.tab_5)
        self.scale.setGeometry(QtCore.QRect(220, 316, 89, 25))
        self.scale.setObjectName("scale")
        self.agn = QtWidgets.QPushButton(self.tab_5)
        self.agn.setGeometry(QtCore.QRect(220, 120, 89, 25))
        self.agn.setObjectName("agn")
        self.spnoi = QtWidgets.QPushButton(self.tab_5)
        self.spnoi.setGeometry(QtCore.QRect(220, 240, 89, 25))
        self.spnoi.setObjectName("spnoi")
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.label_47 = QtWidgets.QLabel(self.tab_6)
        self.label_47.setGeometry(QtCore.QRect(10, 40, 141, 17))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_47.setFont(font)
        self.label_47.setObjectName("label_47")
        self.rot = QtWidgets.QPushButton(self.tab_6)
        self.rot.setGeometry(QtCore.QRect(220, 40, 89, 25))
        self.rot.setObjectName("rot")
        self.label_48 = QtWidgets.QLabel(self.tab_6)
        self.label_48.setGeometry(QtCore.QRect(10, 240, 191, 17))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_48.setFont(font)
        self.label_48.setObjectName("label_48")
        self.label_49 = QtWidgets.QLabel(self.tab_6)
        self.label_49.setGeometry(QtCore.QRect(10, 80, 131, 17))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_49.setFont(font)
        self.label_49.setObjectName("label_49")
        self.skel = QtWidgets.QPushButton(self.tab_6)
        self.skel.setGeometry(QtCore.QRect(220, 200, 89, 25))
        self.skel.setObjectName("skel")
        self.label_50 = QtWidgets.QLabel(self.tab_6)
        self.label_50.setGeometry(QtCore.QRect(10, 120, 141, 17))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_50.setFont(font)
        self.label_50.setObjectName("label_50")
        self.label_51 = QtWidgets.QLabel(self.tab_6)
        self.label_51.setGeometry(QtCore.QRect(10, 200, 171, 17))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_51.setFont(font)
        self.label_51.setObjectName("label_51")
        self.histeq = QtWidgets.QPushButton(self.tab_6)
        self.histeq.setGeometry(QtCore.QRect(220, 160, 89, 25))
        self.histeq.setObjectName("histeq")
        self.label_52 = QtWidgets.QLabel(self.tab_6)
        self.label_52.setGeometry(QtCore.QRect(10, 160, 201, 17))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_52.setFont(font)
        self.label_52.setObjectName("label_52")
        self.trans = QtWidgets.QPushButton(self.tab_6)
        self.trans.setGeometry(QtCore.QRect(220, 80, 89, 25))
        self.trans.setObjectName("trans")
        self.superpixel = QtWidgets.QPushButton(self.tab_6)
        self.superpixel.setGeometry(QtCore.QRect(220, 120, 89, 25))
        self.superpixel.setObjectName("superpixel")
        self.affine = QtWidgets.QPushButton(self.tab_6)
        self.affine.setGeometry(QtCore.QRect(220, 240, 89, 25))
        self.affine.setObjectName("affine")
        self.tabWidget.addTab(self.tab_6, "")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(460, 130, 241, 25))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(16)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(136, 138, 133);")
        self.label_7.setObjectName("label_7")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(70, 130, 256, 31))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(15)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(136, 138, 133);")
        self.label_6.setObjectName("label_6")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 190, 181, 23))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(186, 189, 182);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 250, 181, 23))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("\n"
"color: rgb(186, 189, 182);")
        self.label_3.setObjectName("label_3")
        self.cmdop = QtWidgets.QTextEdit(self.centralwidget)
        self.cmdop.setGeometry(QtCore.QRect(10, 320, 401, 291))
        self.cmdop.setObjectName("cmdop")
        self.browse = QtWidgets.QPushButton(self.centralwidget)
        self.browse.setGeometry(QtCore.QRect(250, 190, 111, 31))
        self.browse.setStyleSheet("QPushButton#browse{\n"
"             color: rgb(0, 0, 0);\n"
"            background-color: rgb(187, 255, 176); \n"
"        }\n"
"        QPushButton#browse:hover {\n"
"            background-color: rgb(151, 255, 128);\n"
"        }\n"
"        QPushButton#browse:pressed {\n"
"            background-color: rgb(85, 255, 0);\n"
"        }   ")
        self.browse.setObjectName("browse")
        self.showim = QtWidgets.QPushButton(self.centralwidget)
        self.showim.setGeometry(QtCore.QRect(250, 250, 111, 31))
        self.showim.setStyleSheet("QPushButton{\n"
"             color: rgb(0, 0, 0);\n"
"            background-color: #b9f6ca; \n"
"        }\n"
"        QPushButton:hover {\n"
"            background-color: #69f0ae;\n"
"        }\n"
"        QPushButton:pressed {\n"
"           background-color: #00e676;\n"
"        }    ")
        self.showim.setObjectName("showim")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(72, 83, 621, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.clear = QtWidgets.QPushButton(self.centralwidget)
        self.clear.setGeometry(QtCore.QRect(303, 570, 89, 25))
        self.clear.setObjectName("clear")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(64, 151, 261, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(456, 152, 241, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(170, 301, 81, 20))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Image Augmenter"))
        self.label.setText(_translate("MainWindow", "Image Augmenter"))
        self.augment.setText(_translate("MainWindow", "Augment!"))
        self.quit.setText(_translate("MainWindow", "Quit"))
        self.label_4.setText(_translate("MainWindow", "Status"))
        self.label_5.setText(_translate("MainWindow", "Resize "))
        self.label_9.setText(_translate("MainWindow", "Pad "))
        self.label_10.setText(_translate("MainWindow", "Flip "))
        self.label_11.setText(_translate("MainWindow", "Hue, Saturate & Invert  "))
        self.label_12.setText(_translate("MainWindow", "Gamma Correction"))
        self.label_13.setText(_translate("MainWindow", "Gamma correction with color"))
        self.label_14.setText(_translate("MainWindow", "Per Channel Multiplication"))
        self.gcc.setText(_translate("MainWindow", "Push"))
        self.resz.setText(_translate("MainWindow", "Push"))
        self.pchmul.setText(_translate("MainWindow", "Push"))
        self.pad.setText(_translate("MainWindow", "Push"))
        self.gc.setText(_translate("MainWindow", "Push"))
        self.hsi.setText(_translate("MainWindow", "Push"))
        self.flip.setText(_translate("MainWindow", "Push"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Ops 1"))
        self.mb.setText(_translate("MainWindow", "Push"))
        self.label_15.setText(_translate("MainWindow", "Bilateral Blur"))
        self.gb.setText(_translate("MainWindow", "Push"))
        self.label_16.setText(_translate("MainWindow", "Color Convertions"))
        self.label_17.setText(_translate("MainWindow", "Morphological Operations 1"))
        self.bb.setText(_translate("MainWindow", "Push"))
        self.mor2.setText(_translate("MainWindow", "Push"))
        self.label_18.setText(_translate("MainWindow", "Gaussain Blur"))
        self.label_19.setText(_translate("MainWindow", "Sharpen "))
        self.mor1.setText(_translate("MainWindow", "Push"))
        self.ab.setText(_translate("MainWindow", "Push"))
        self.label_20.setText(_translate("MainWindow", "Morphological Operations 2"))
        self.label_21.setText(_translate("MainWindow", "Average Blur"))
        self.cc.setText(_translate("MainWindow", "Push"))
        self.sharp.setText(_translate("MainWindow", "Push"))
        self.label_22.setText(_translate("MainWindow", "Median Blur"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Ops 2"))
        self.label_39.setText(_translate("MainWindow", "Emboss"))
        self.emboss.setText(_translate("MainWindow", "Push"))
        self.label_40.setText(_translate("MainWindow", "Speckle Noise"))
        self.label_41.setText(_translate("MainWindow", "Edge Detection"))
        self.pnoi.setText(_translate("MainWindow", "Push"))
        self.label_42.setText(_translate("MainWindow", "AdaGussian Noise"))
        self.label_43.setText(_translate("MainWindow", "Poisson Noise"))
        self.sp.setText(_translate("MainWindow", "Push"))
        self.label_44.setText(_translate("MainWindow", "Salt & Pepper Noise"))
        self.contrast.setText(_translate("MainWindow", "Push"))
        self.label_45.setText(_translate("MainWindow", "Scaling"))
        self.label_46.setText(_translate("MainWindow", "Contrasting"))
        self.edge.setText(_translate("MainWindow", "Push"))
        self.scale.setText(_translate("MainWindow", "Push"))
        self.agn.setText(_translate("MainWindow", "Push"))
        self.spnoi.setText(_translate("MainWindow", "Push"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "Ops 3"))
        self.label_47.setText(_translate("MainWindow", "Rotate"))
        self.rot.setText(_translate("MainWindow", "Push"))
        self.label_48.setText(_translate("MainWindow", "Affine "))
        self.label_49.setText(_translate("MainWindow", "Translate"))
        self.skel.setText(_translate("MainWindow", "Push"))
        self.label_50.setText(_translate("MainWindow", "SuperPixel"))
        self.label_51.setText(_translate("MainWindow", "Skelotonize"))
        self.histeq.setText(_translate("MainWindow", "Push"))
        self.label_52.setText(_translate("MainWindow", "Histogram Equalization"))
        self.trans.setText(_translate("MainWindow", "Push"))
        self.superpixel.setText(_translate("MainWindow", "Push"))
        self.affine.setText(_translate("MainWindow", "Push"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("MainWindow", "Ops 4"))
        self.label_7.setText(_translate("MainWindow", "Selective Augmentation"))
        self.label_6.setText(_translate("MainWindow", "Image Loading and Preview"))
        self.label_2.setText(_translate("MainWindow", "Load an image"))
        self.label_3.setText(_translate("MainWindow", "Show the Image"))
        self.browse.setText(_translate("MainWindow", "Browse"))
        self.showim.setText(_translate("MainWindow", "Show"))
        self.clear.setText(_translate("MainWindow", "Clear"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
