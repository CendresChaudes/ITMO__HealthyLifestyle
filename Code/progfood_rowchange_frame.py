# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'progfood_rowchange_frame.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_RowChange(object):
    def setupUi(self, RowChange):
        RowChange.setObjectName("RowChange")
        RowChange.resize(270, 290)
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
        RowChange.setPalette(palette)
        RowChange.setAcceptDrops(False)
        RowChange.setAutoFillBackground(False)
        RowChange.setStyleSheet("background-color:\n"
"rba(0,0,0,0);")
        self.verticalWidget = QtWidgets.QWidget(RowChange)
        self.verticalWidget.setGeometry(QtCore.QRect(10, 0, 247, 288))
        self.verticalWidget.setObjectName("verticalWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_10 = QtWidgets.QLabel(self.verticalWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setMinimumSize(QtCore.QSize(0, 30))
        self.label_10.setMaximumSize(QtCore.QSize(16777215, 30))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_10.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Gill Sans Nova")
        font.setPointSize(13)
        font.setItalic(True)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("background-color:\n"
"rba(0,0,0,1)")
        self.label_10.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_10.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.verticalLayout.addWidget(self.label_10)
        self.lineEdit_inputWeightProduct = QtWidgets.QLineEdit(self.verticalWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_inputWeightProduct.sizePolicy().hasHeightForWidth())
        self.lineEdit_inputWeightProduct.setSizePolicy(sizePolicy)
        self.lineEdit_inputWeightProduct.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Gill Sans Nova")
        font.setPointSize(10)
        self.lineEdit_inputWeightProduct.setFont(font)
        self.lineEdit_inputWeightProduct.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.lineEdit_inputWeightProduct.setStyleSheet("background-color:\n"
"white;\n"
"border-radius:\n"
"15px;\n"
"padding-left:\n"
"10px")
        self.lineEdit_inputWeightProduct.setInputMethodHints(QtCore.Qt.ImhMultiLine)
        self.lineEdit_inputWeightProduct.setInputMask("")
        self.lineEdit_inputWeightProduct.setText("")
        self.lineEdit_inputWeightProduct.setMaxLength(4)
        self.lineEdit_inputWeightProduct.setFrame(False)
        self.lineEdit_inputWeightProduct.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_inputWeightProduct.setObjectName("lineEdit_inputWeightProduct")
        self.verticalLayout.addWidget(self.lineEdit_inputWeightProduct)
        self.label_14 = QtWidgets.QLabel(self.verticalWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy)
        self.label_14.setMaximumSize(QtCore.QSize(16777215, 1))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_14.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Gill Sans Nova Light")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("background-color:\n"
"rba(0,0,0,0)")
        self.label_14.setText("")
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setIndent(-1)
        self.label_14.setObjectName("label_14")
        self.verticalLayout.addWidget(self.label_14)
        self.pushButton_acceptChange = QtWidgets.QPushButton(self.verticalWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(40)
        sizePolicy.setHeightForWidth(self.pushButton_acceptChange.sizePolicy().hasHeightForWidth())
        self.pushButton_acceptChange.setSizePolicy(sizePolicy)
        self.pushButton_acceptChange.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_acceptChange.setMaximumSize(QtCore.QSize(16777215, 40))
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
        self.pushButton_acceptChange.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Gill Sans Nova")
        font.setPointSize(12)
        self.pushButton_acceptChange.setFont(font)
        self.pushButton_acceptChange.setStyleSheet("background-color:\n"
"qlineargradient(spread:pad, x1:0.469, y1:0, x2:1, y2:0, stop:0 rgba(0, 197, 227, 255), stop:1 rgba(0, 224, 46, 255));\n"
"border-radius:\n"
"19px;\n"
"color:\n"
"white")
        self.pushButton_acceptChange.setCheckable(False)
        self.pushButton_acceptChange.setAutoRepeat(False)
        self.pushButton_acceptChange.setAutoDefault(True)
        self.pushButton_acceptChange.setDefault(False)
        self.pushButton_acceptChange.setFlat(False)
        self.pushButton_acceptChange.setObjectName("pushButton_acceptChange")
        self.verticalLayout.addWidget(self.pushButton_acceptChange)
        self.pushButton_delRow = QtWidgets.QPushButton(self.verticalWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(40)
        sizePolicy.setHeightForWidth(self.pushButton_delRow.sizePolicy().hasHeightForWidth())
        self.pushButton_delRow.setSizePolicy(sizePolicy)
        self.pushButton_delRow.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_delRow.setMaximumSize(QtCore.QSize(16777215, 40))
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
        self.pushButton_delRow.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Gill Sans Nova")
        font.setPointSize(12)
        self.pushButton_delRow.setFont(font)
        self.pushButton_delRow.setStyleSheet("background-color:\n"
"qlineargradient(spread:pad, x1:0.469, y1:0, x2:1, y2:0, stop:0 rgba(0, 197, 227, 255), stop:1 rgba(0, 224, 46, 255));\n"
"border-radius:\n"
"19px;\n"
"color:\n"
"white")
        self.pushButton_delRow.setCheckable(False)
        self.pushButton_delRow.setAutoRepeat(False)
        self.pushButton_delRow.setAutoDefault(True)
        self.pushButton_delRow.setDefault(False)
        self.pushButton_delRow.setFlat(False)
        self.pushButton_delRow.setObjectName("pushButton_delRow")
        self.verticalLayout.addWidget(self.pushButton_delRow)
        self.label_13 = QtWidgets.QLabel(self.verticalWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy)
        self.label_13.setMaximumSize(QtCore.QSize(16777215, 20))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_13.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Gill Sans Nova Light")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("background-color:\n"
"rba(0,0,0,0)")
        self.label_13.setText("")
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setIndent(-1)
        self.label_13.setObjectName("label_13")
        self.verticalLayout.addWidget(self.label_13)
        self.pushButton_closeWindow = QtWidgets.QPushButton(self.verticalWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(40)
        sizePolicy.setHeightForWidth(self.pushButton_closeWindow.sizePolicy().hasHeightForWidth())
        self.pushButton_closeWindow.setSizePolicy(sizePolicy)
        self.pushButton_closeWindow.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_closeWindow.setMaximumSize(QtCore.QSize(16777215, 40))
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
        self.pushButton_closeWindow.setCheckable(False)
        self.pushButton_closeWindow.setAutoRepeat(False)
        self.pushButton_closeWindow.setAutoDefault(True)
        self.pushButton_closeWindow.setDefault(False)
        self.pushButton_closeWindow.setFlat(False)
        self.pushButton_closeWindow.setObjectName("pushButton_closeWindow")
        self.verticalLayout.addWidget(self.pushButton_closeWindow)

        self.retranslateUi(RowChange)
        QtCore.QMetaObject.connectSlotsByName(RowChange)

    def retranslateUi(self, RowChange):
        _translate = QtCore.QCoreApplication.translate
        RowChange.setWindowTitle(_translate("RowChange", "Healthy Lifestyle"))
        self.label_10.setText(_translate("RowChange", "Вес, г"))
        self.pushButton_acceptChange.setText(_translate("RowChange", "Изменить"))
        self.pushButton_delRow.setText(_translate("RowChange", "Удалить строку"))
        self.pushButton_closeWindow.setText(_translate("RowChange", "Закрыть окно"))
