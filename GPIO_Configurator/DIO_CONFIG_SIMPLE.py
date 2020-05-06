# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Pin_Config.ui'
##
## Created by: Qt User Interface Compiler version 5.14.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt, SIGNAL)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *
import sys


class Ui_Form(object):
    def setupUi(self, Form):
        if Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(531, 120)
        self.Out_lineEdit = QLineEdit(Form)
        self.Out_lineEdit.setObjectName(u"Out_lineEdit")
        self.Out_lineEdit.setGeometry(QRect(90, 90, 331, 20))
        self.Out_label = QLabel(Form)
        self.Out_label.setObjectName(u"Out_label")
        self.Out_label.setGeometry(QRect(20, 90, 71, 16))
        self.Generate_pushButton = QPushButton(Form)
        self.Generate_pushButton.setObjectName(u"Generate_pushButton")
        self.Generate_pushButton.setGeometry(QRect(440, 90, 75, 23))
        self.PINA0_groupBox = QGroupBox(Form)
        self.PINA0_groupBox.setObjectName(u"PINA0_groupBox")
        self.PINA0_groupBox.setGeometry(QRect(10, 0, 511, 81))
        self.ModeA0_groupBox = QGroupBox(self.PINA0_groupBox)
        self.ModeA0_groupBox.setObjectName(u"ModeA0_groupBox")
        self.ModeA0_groupBox.setGeometry(QRect(60, 10, 121, 31))
        self.INA0_radioButton = QRadioButton(self.ModeA0_groupBox)
        self.INA0_radioButton.setObjectName(u"INA0_radioButton")
        self.INA0_radioButton.setGeometry(QRect(10, 10, 51, 18))
        self.INA0_radioButton.setChecked(True)
        self.OutA0_radioButton = QRadioButton(self.ModeA0_groupBox)
        self.OutA0_radioButton.setObjectName(u"OutA0_radioButton")
        self.OutA0_radioButton.setGeometry(QRect(60, 10, 61, 18))
        self.OutConfigA0_groupBox = QGroupBox(self.PINA0_groupBox)
        self.OutConfigA0_groupBox.setObjectName(u"OutConfigA0_groupBox")
        self.OutConfigA0_groupBox.setEnabled(False)
        self.OutConfigA0_groupBox.setGeometry(QRect(380, 10, 120, 31))
        self.HighA0_radioButton = QRadioButton(self.OutConfigA0_groupBox)
        self.HighA0_radioButton.setObjectName(u"HighA0_radioButton")
        self.HighA0_radioButton.setGeometry(QRect(10, 10, 41, 18))
        self.LowA0_radioButton = QRadioButton(self.OutConfigA0_groupBox)
        self.LowA0_radioButton.setObjectName(u"LowA0_radioButton")
        self.LowA0_radioButton.setGeometry(QRect(70, 10, 41, 20))
        self.LowA0_radioButton.setChecked(True)
        self.InConfigA0_groupBox = QGroupBox(self.PINA0_groupBox)
        self.InConfigA0_groupBox.setObjectName(u"InConfigA0_groupBox")
        self.InConfigA0_groupBox.setGeometry(QRect(190, 10, 181, 31))
        self.PullA0_radioButton = QRadioButton(self.InConfigA0_groupBox)
        self.PullA0_radioButton.setObjectName(u"PullA0_radioButton")
        self.PullA0_radioButton.setGeometry(QRect(10, 10, 51, 18))
        self.PullA0_radioButton.setChecked(True)
        self.ImpA0_radioButton = QRadioButton(self.InConfigA0_groupBox)
        self.ImpA0_radioButton.setObjectName(u"ImpA0_radioButton")
        self.ImpA0_radioButton.setGeometry(QRect(70, 10, 101, 20))
        self.DefA0_checkBox = QCheckBox(self.PINA0_groupBox)
        self.DefA0_checkBox.setObjectName(u"DefA0_checkBox")
        self.DefA0_checkBox.setGeometry(QRect(300, 50, 111, 18))
        self.DefA0_checkBox.setChecked(True)
        self.PINA0_label = QLabel(self.PINA0_groupBox)
        self.PINA0_label.setObjectName(u"PINA0_label")
        self.PINA0_label.setGeometry(QRect(20, 20, 31, 16))
        self.NewA0_lineEdit = QLineEdit(self.PINA0_groupBox)
        self.NewA0_lineEdit.setObjectName(u"NewA0_lineEdit")
        self.NewA0_lineEdit.setEnabled(False)
        self.NewA0_lineEdit.setGeometry(QRect(102, 50, 161, 20))

        self.retranslateUi(Form)
        QObject.connect(self.INA0_radioButton,SIGNAL("toggled(bool)"),self.OutConfigA0_groupBox.setDisabled)
        #self.INA0_radioButton.toggled.connect(self.OutConfigA0_groupBox.setDisabled)
        QObject.connect(self.OutA0_radioButton,SIGNAL("toggled(bool)"),self.InConfigA0_groupBox.setDisabled)
        #self.OutA0_radioButton.toggled.connect(self.InConfigA0_groupBox.setDisabled)
        QObject.connect(self.DefA0_checkBox,SIGNAL("clicked(bool)"),self.NewA0_lineEdit.setDisabled)
        #self.DefA0_checkBox.clicked.connect(self.NewA0_lineEdit.setDisabled)
        self.Generate_pushButton.clicked.connect(self.Generate)

        QMetaObject.connectSlotsByName(Form)
    # setupUi
    def Generate(self):
        out=self.Out_lineEdit.text()
        In_or_Out = self.INA0_radioButton.isChecked()
        Pull_or_Imp = self.PullA0_radioButton.isChecked()
        High_or_Low = self.HighA0_radioButton.isChecked()
        if self.DefA0_checkBox.isChecked():
            name = "PINA0"
        else:
            name = self.NewA0_lineEdit.text()
        filename = out+"\\DIO_Config.h"
        f=open(filename,'w')
        f.seek(0)
        if In_or_Out:
            f.write('#define '+name+'_DIR   '+"INPUT"+"\n")
            if Pull_or_Imp:
                f.write('#define '+name+'_Mode   '+"PULL_UP"+"\n")
            else:
                f.write('#define '+name+'_Mode   '+"HIGH_IMPEDENCE"+"\n")
        else:
            f.write('#define '+name+'_DIR   '+"OUTPUT"+"\n")
            if High_or_Low:
                f.write('#define '+name+'_Mode   '+"OUT_HIGH"+"\n")
            else:
                f.write('#define '+name+'_Mode   '+"OUT_LOW"+"\n")
        return
        
        f.close()


    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Pins_Config", None))
        self.Out_lineEdit.setText(QCoreApplication.translate("Form", u"C:\\Users\\Moustafa Ghareeb\\Desktop\\HabdPy", None))
        self.Out_lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"Enter a valid path", None))
        self.Out_label.setText(QCoreApplication.translate("Form", u"Output Path", None))
        self.Generate_pushButton.setText(QCoreApplication.translate("Form", u"Generate", None))
        self.PINA0_groupBox.setTitle(QCoreApplication.translate("Form", u"DIO", None))
        self.ModeA0_groupBox.setTitle(QCoreApplication.translate("Form", u"Mode", None))
        self.INA0_radioButton.setText(QCoreApplication.translate("Form", u"Input", None))
        self.OutA0_radioButton.setText(QCoreApplication.translate("Form", u"Output", None))
        self.OutConfigA0_groupBox.setTitle(QCoreApplication.translate("Form", u"Output config", None))
        self.HighA0_radioButton.setText(QCoreApplication.translate("Form", u"High", None))
        self.LowA0_radioButton.setText(QCoreApplication.translate("Form", u"Low", None))
        self.InConfigA0_groupBox.setTitle(QCoreApplication.translate("Form", u"Input config", None))
        self.PullA0_radioButton.setText(QCoreApplication.translate("Form", u"PullUp", None))
        self.ImpA0_radioButton.setText(QCoreApplication.translate("Form", u"High Impedance", None))
        self.DefA0_checkBox.setText(QCoreApplication.translate("Form", u"Use Default Name", None))
        self.PINA0_label.setText(QCoreApplication.translate("Form", u"PinA0", None))
#if QT_CONFIG(statustip)
        self.NewA0_lineEdit.setStatusTip("")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.NewA0_lineEdit.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.NewA0_lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"Write new name here", None))
    # retranslateUi



app = QApplication(sys.argv)
Widget = QWidget()
Form = Ui_Form()
Form.setupUi(Widget)
Widget.show()
app.exec_()