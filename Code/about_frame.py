# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'about_frame.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AboutWindow(object):
    def setupUi(self, AboutWindow):
        AboutWindow.setObjectName("AboutWindow")
        AboutWindow.resize(575, 675)
        palette = QtGui.QPalette()
        gradient = QtGui.QLinearGradient(0.0, 1.0, 1.0, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(0, 0, 0))
        gradient.setColorAt(0.05, QtGui.QColor(14, 8, 73))
        gradient.setColorAt(0.36, QtGui.QColor(28, 17, 145))
        gradient.setColorAt(0.6, QtGui.QColor(126, 14, 81))
        gradient.setColorAt(0.75, QtGui.QColor(234, 11, 11))
        gradient.setColorAt(0.79, QtGui.QColor(244, 70, 5))
        gradient.setColorAt(0.86, QtGui.QColor(255, 136, 0))
        gradient.setColorAt(0.973684, QtGui.QColor(239, 133, 55))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        gradient = QtGui.QLinearGradient(0.0, 1.0, 1.0, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(0, 0, 0))
        gradient.setColorAt(0.05, QtGui.QColor(14, 8, 73))
        gradient.setColorAt(0.36, QtGui.QColor(28, 17, 145))
        gradient.setColorAt(0.6, QtGui.QColor(126, 14, 81))
        gradient.setColorAt(0.75, QtGui.QColor(234, 11, 11))
        gradient.setColorAt(0.79, QtGui.QColor(244, 70, 5))
        gradient.setColorAt(0.86, QtGui.QColor(255, 136, 0))
        gradient.setColorAt(0.973684, QtGui.QColor(239, 133, 55))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        gradient = QtGui.QLinearGradient(0.0, 1.0, 1.0, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(0, 0, 0))
        gradient.setColorAt(0.05, QtGui.QColor(14, 8, 73))
        gradient.setColorAt(0.36, QtGui.QColor(28, 17, 145))
        gradient.setColorAt(0.6, QtGui.QColor(126, 14, 81))
        gradient.setColorAt(0.75, QtGui.QColor(234, 11, 11))
        gradient.setColorAt(0.79, QtGui.QColor(244, 70, 5))
        gradient.setColorAt(0.86, QtGui.QColor(255, 136, 0))
        gradient.setColorAt(0.973684, QtGui.QColor(239, 133, 55))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        gradient = QtGui.QLinearGradient(0.0, 1.0, 1.0, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(0, 0, 0))
        gradient.setColorAt(0.05, QtGui.QColor(14, 8, 73))
        gradient.setColorAt(0.36, QtGui.QColor(28, 17, 145))
        gradient.setColorAt(0.6, QtGui.QColor(126, 14, 81))
        gradient.setColorAt(0.75, QtGui.QColor(234, 11, 11))
        gradient.setColorAt(0.79, QtGui.QColor(244, 70, 5))
        gradient.setColorAt(0.86, QtGui.QColor(255, 136, 0))
        gradient.setColorAt(0.973684, QtGui.QColor(239, 133, 55))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        gradient = QtGui.QLinearGradient(0.0, 1.0, 1.0, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(0, 0, 0))
        gradient.setColorAt(0.05, QtGui.QColor(14, 8, 73))
        gradient.setColorAt(0.36, QtGui.QColor(28, 17, 145))
        gradient.setColorAt(0.6, QtGui.QColor(126, 14, 81))
        gradient.setColorAt(0.75, QtGui.QColor(234, 11, 11))
        gradient.setColorAt(0.79, QtGui.QColor(244, 70, 5))
        gradient.setColorAt(0.86, QtGui.QColor(255, 136, 0))
        gradient.setColorAt(0.973684, QtGui.QColor(239, 133, 55))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        gradient = QtGui.QLinearGradient(0.0, 1.0, 1.0, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(0, 0, 0))
        gradient.setColorAt(0.05, QtGui.QColor(14, 8, 73))
        gradient.setColorAt(0.36, QtGui.QColor(28, 17, 145))
        gradient.setColorAt(0.6, QtGui.QColor(126, 14, 81))
        gradient.setColorAt(0.75, QtGui.QColor(234, 11, 11))
        gradient.setColorAt(0.79, QtGui.QColor(244, 70, 5))
        gradient.setColorAt(0.86, QtGui.QColor(255, 136, 0))
        gradient.setColorAt(0.973684, QtGui.QColor(239, 133, 55))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        gradient = QtGui.QLinearGradient(0.0, 1.0, 1.0, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(0, 0, 0))
        gradient.setColorAt(0.05, QtGui.QColor(14, 8, 73))
        gradient.setColorAt(0.36, QtGui.QColor(28, 17, 145))
        gradient.setColorAt(0.6, QtGui.QColor(126, 14, 81))
        gradient.setColorAt(0.75, QtGui.QColor(234, 11, 11))
        gradient.setColorAt(0.79, QtGui.QColor(244, 70, 5))
        gradient.setColorAt(0.86, QtGui.QColor(255, 136, 0))
        gradient.setColorAt(0.973684, QtGui.QColor(239, 133, 55))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        gradient = QtGui.QLinearGradient(0.0, 1.0, 1.0, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(0, 0, 0))
        gradient.setColorAt(0.05, QtGui.QColor(14, 8, 73))
        gradient.setColorAt(0.36, QtGui.QColor(28, 17, 145))
        gradient.setColorAt(0.6, QtGui.QColor(126, 14, 81))
        gradient.setColorAt(0.75, QtGui.QColor(234, 11, 11))
        gradient.setColorAt(0.79, QtGui.QColor(244, 70, 5))
        gradient.setColorAt(0.86, QtGui.QColor(255, 136, 0))
        gradient.setColorAt(0.973684, QtGui.QColor(239, 133, 55))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        gradient = QtGui.QLinearGradient(0.0, 1.0, 1.0, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(0, 0, 0))
        gradient.setColorAt(0.05, QtGui.QColor(14, 8, 73))
        gradient.setColorAt(0.36, QtGui.QColor(28, 17, 145))
        gradient.setColorAt(0.6, QtGui.QColor(126, 14, 81))
        gradient.setColorAt(0.75, QtGui.QColor(234, 11, 11))
        gradient.setColorAt(0.79, QtGui.QColor(244, 70, 5))
        gradient.setColorAt(0.86, QtGui.QColor(255, 136, 0))
        gradient.setColorAt(0.973684, QtGui.QColor(239, 133, 55))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        AboutWindow.setPalette(palette)
        AboutWindow.setAcceptDrops(False)
        AboutWindow.setAutoFillBackground(False)
        AboutWindow.setStyleSheet("background-color:\n"
"qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:0.05 rgba(14, 8, 73, 255), stop:0.36 rgba(28, 17, 145, 255), stop:0.6 rgba(126, 14, 81, 255), stop:0.75 rgba(234, 11, 11, 255), stop:0.79 rgba(244, 70, 5, 255), stop:0.86 rgba(255, 136, 0, 255), stop:0.973684 rgba(239, 133, 55, 255))")
        self.label = QtWidgets.QLabel(AboutWindow)
        self.label.setGeometry(QtCore.QRect(0, 0, 575, 60))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.label.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Gill Sans Nova")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color:\n"
"rba(0,0,0,0)")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.line = QtWidgets.QFrame(AboutWindow)
        self.line.setGeometry(QtCore.QRect(165, 40, 250, 31))
        self.line.setStyleSheet("background-color:\n"
"rba(0,0,0,0);\n"
"color:\n"
"white")
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(3)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.horizontalWidget = QtWidgets.QWidget(AboutWindow)
        self.horizontalWidget.setGeometry(QtCore.QRect(30, 609, 511, 58))
        self.horizontalWidget.setStyleSheet("background-color:\n"
"rba(0,0,0,0)")
        self.horizontalWidget.setObjectName("horizontalWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_closeWindow = QtWidgets.QPushButton(self.horizontalWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_closeWindow.sizePolicy().hasHeightForWidth())
        self.pushButton_closeWindow.setSizePolicy(sizePolicy)
        self.pushButton_closeWindow.setMinimumSize(QtCore.QSize(280, 0))
        self.pushButton_closeWindow.setMaximumSize(QtCore.QSize(280, 40))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        gradient = QtGui.QLinearGradient(0.469, 0.0, 1.0, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(0, 197, 227))
        gradient.setColorAt(1.0, QtGui.QColor(0, 224, 46))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        gradient = QtGui.QLinearGradient(0.469, 0.0, 1.0, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(0, 197, 227))
        gradient.setColorAt(1.0, QtGui.QColor(0, 224, 46))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        gradient = QtGui.QLinearGradient(0.469, 0.0, 1.0, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(0, 197, 227))
        gradient.setColorAt(1.0, QtGui.QColor(0, 224, 46))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        gradient = QtGui.QLinearGradient(0.469, 0.0, 1.0, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(0, 197, 227))
        gradient.setColorAt(1.0, QtGui.QColor(0, 224, 46))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        gradient = QtGui.QLinearGradient(0.469, 0.0, 1.0, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(0, 197, 227))
        gradient.setColorAt(1.0, QtGui.QColor(0, 224, 46))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        gradient = QtGui.QLinearGradient(0.469, 0.0, 1.0, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(0, 197, 227))
        gradient.setColorAt(1.0, QtGui.QColor(0, 224, 46))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        gradient = QtGui.QLinearGradient(0.469, 0.0, 1.0, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(0, 197, 227))
        gradient.setColorAt(1.0, QtGui.QColor(0, 224, 46))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        gradient = QtGui.QLinearGradient(0.469, 0.0, 1.0, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(0, 197, 227))
        gradient.setColorAt(1.0, QtGui.QColor(0, 224, 46))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        gradient = QtGui.QLinearGradient(0.469, 0.0, 1.0, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(0, 197, 227))
        gradient.setColorAt(1.0, QtGui.QColor(0, 224, 46))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.pushButton_closeWindow.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Gill Sans Nova")
        font.setPointSize(12)
        self.pushButton_closeWindow.setFont(font)
        self.pushButton_closeWindow.setStyleSheet("background-color:\n"
"qlineargradient(spread:pad, x1:0.469, y1:0, x2:1, y2:0, stop:0 rgba(0, 197, 227, 255), stop:1 rgba(0, 224, 46, 255));\n"
"border-radius:\n"
"19px;\n"
"color:\n"
"white")
        self.pushButton_closeWindow.setObjectName("pushButton_closeWindow")
        self.horizontalLayout.addWidget(self.pushButton_closeWindow, 0, QtCore.Qt.AlignHCenter)
        self.label_2 = QtWidgets.QLabel(AboutWindow)
        self.label_2.setGeometry(QtCore.QRect(0, 65, 571, 551))
        font = QtGui.QFont()
        font.setFamily("Gill Sans Nova")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setMouseTracking(True)
        self.label_2.setStyleSheet("background-color:\n"
"rba(0,0,0,0);\n"
"color:\n"
"white;\n"
"padding:\n"
"15px;")
        self.label_2.setInputMethodHints(QtCore.Qt.ImhNone)
        self.label_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(AboutWindow)
        QtCore.QMetaObject.connectSlotsByName(AboutWindow)

    def retranslateUi(self, AboutWindow):
        _translate = QtCore.QCoreApplication.translate
        AboutWindow.setWindowTitle(_translate("AboutWindow", "Healthy Lifestyle"))
        self.label.setText(_translate("AboutWindow", "О ПРОГРАММЕ"))
        self.pushButton_closeWindow.setText(_translate("AboutWindow", "Закрыть окно"))
        self.label_2.setText(_translate("AboutWindow", "<html><head/><body><p align=\"justify\">&nbsp;  Здоровье – неотъемлемая часть каждого живого существа, проживающего на нашей планете. Эта часть существует еще до нашего появления на свет из утробы матери и уходит вместе с нами, когда мы покидаем этот мир, мир живых. Здоровье – это сокровище, которое мы должны ценить, беречь и поддерживать в хорошем состоянии как только можем.</p><p align=\"justify\">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; В современном мире интерес общества к здоровому образу растет с каждым годом и, благодаря этому интересу, существует огромное количество брендов витаминов, БАДов (биологически активные добавки), спортивных комплексов и секций, но наш век интересен не только этой «страстью» к здоровому, но и теми технологиями, которыми человечество обладает. Компьютер перестал быть роскошью и есть практически у каждого в доме, а большая часть работы происходит именно на мониторе, а не на бумажном листе – мы с каждым годом все больше погружаемся в цифровой мир: компьютер и программы, запускаемые на нем, стали неотъемлемой частью нашей жизни как в работе, так и во время отдыха.</p><p align=\"justify\">&nbsp;&nbsp; Моя программа была написана для тех, кто также поддерживает здоровый образ жизни, кто хочет добиваться новых вершин в спорте, не тратя при этом свое время на ведение бумажной книги от руки. </p><p align=\"left\"><br/><span style=\" font-weight:600; font-style:italic;\">Автор: Пронин Р. А.<br/>Версия: 1.0</span></p></body></html>"))