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
import sys,re,os

PIN_MODE=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1];
PIN_DIRE=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1];

class Ui_Form(object):    
    def setupUi(self, Form):
        if Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(520, 207)
        self.Out_lineEdit = QLineEdit(Form)
        self.Out_lineEdit.setObjectName(u"Out_lineEdit")
        self.Out_lineEdit.setGeometry(QRect(80, 180, 221, 20))
        self.Out_label = QLabel(Form)
        self.Out_label.setObjectName(u"Out_label")
        self.Out_label.setGeometry(QRect(10, 180, 71, 20))
        self.Generate_pushButton = QPushButton(Form)
        self.Generate_pushButton.setObjectName(u"Generate_pushButton")
        self.Generate_pushButton.setGeometry(QRect(310, 180, 75, 22))
        self.PINA0_groupBox = QGroupBox(Form)
        self.PINA0_groupBox.setObjectName(u"PINA0_groupBox")
        self.PINA0_groupBox.setGeometry(QRect(10, 50, 381, 121))
        self.ModeA0_groupBox = QGroupBox(self.PINA0_groupBox)
        self.ModeA0_groupBox.setObjectName(u"ModeA0_groupBox")
        self.ModeA0_groupBox.setGeometry(QRect(60, 10, 121, 71))
        self.INA0_radioButton = QRadioButton(self.ModeA0_groupBox)
        self.INA0_radioButton.setObjectName(u"INA0_radioButton")
        self.INA0_radioButton.setGeometry(QRect(10, 20, 51, 18))
        self.INA0_radioButton.setChecked(True)
        self.OutA0_radioButton = QRadioButton(self.ModeA0_groupBox)
        self.OutA0_radioButton.setObjectName(u"OutA0_radioButton")
        self.OutA0_radioButton.setGeometry(QRect(10, 40, 61, 18))
        self.OutConfigA0_groupBox = QGroupBox(self.PINA0_groupBox)
        self.OutConfigA0_groupBox.setObjectName(u"OutConfigA0_groupBox")
        self.OutConfigA0_groupBox.setEnabled(False)
        self.OutConfigA0_groupBox.setGeometry(QRect(190, 48, 181, 33))
        self.HighA0_radioButton = QRadioButton(self.OutConfigA0_groupBox)
        self.HighA0_radioButton.setObjectName(u"HighA0_radioButton")
        self.HighA0_radioButton.setGeometry(QRect(10, 12, 41, 18))
        self.LowA0_radioButton = QRadioButton(self.OutConfigA0_groupBox)
        self.LowA0_radioButton.setObjectName(u"LowA0_radioButton")
        self.LowA0_radioButton.setGeometry(QRect(70, 12, 41, 20))
        self.LowA0_radioButton.setChecked(True)
        self.InConfigA0_groupBox = QGroupBox(self.PINA0_groupBox)
        self.InConfigA0_groupBox.setObjectName(u"InConfigA0_groupBox")
        self.InConfigA0_groupBox.setGeometry(QRect(190, 10, 181, 33))
        self.PullA0_radioButton = QRadioButton(self.InConfigA0_groupBox)
        self.PullA0_radioButton.setObjectName(u"PullA0_radioButton")
        self.PullA0_radioButton.setGeometry(QRect(10, 12, 51, 18))
        self.PullA0_radioButton.setChecked(True)
        self.ImpA0_radioButton = QRadioButton(self.InConfigA0_groupBox)
        self.ImpA0_radioButton.setObjectName(u"ImpA0_radioButton")
        self.ImpA0_radioButton.setGeometry(QRect(70, 12, 101, 20))
        self.DefA0_checkBox = QCheckBox(self.PINA0_groupBox)
        self.DefA0_checkBox.setObjectName(u"DefA0_checkBox")
        self.DefA0_checkBox.setGeometry(QRect(240, 90, 111, 18))
        self.DefA0_checkBox.setChecked(True)
        self.PINA0_label = QLabel(self.PINA0_groupBox)
        self.PINA0_label.setObjectName(u"PINA0_label")
        self.PINA0_label.setGeometry(QRect(10, 20, 41, 20))
        font = QFont()
        font.setBold(False)
        font.setWeight(50);
        self.PINA0_label.setFont(font)
        self.NewA0_lineEdit = QLineEdit(self.PINA0_groupBox)
        self.NewA0_lineEdit.setObjectName(u"NewA0_lineEdit")
        self.NewA0_lineEdit.setEnabled(False)
        self.NewA0_lineEdit.setGeometry(QRect(60, 90, 161, 20))
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(130, 10, 81, 16))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setWeight(75);
        self.label.setFont(font1)
        self.PIN_comboBox = QComboBox(Form)
        self.PIN_comboBox.addItem(str())
        self.PIN_comboBox.addItem(str())
        self.PIN_comboBox.addItem(str())
        self.PIN_comboBox.addItem(str())
        self.PIN_comboBox.addItem(str())
        self.PIN_comboBox.addItem(str())
        self.PIN_comboBox.addItem(str())
        self.PIN_comboBox.addItem(str())
        self.PIN_comboBox.addItem(str())
        self.PIN_comboBox.addItem(str())
        self.PIN_comboBox.addItem(str())
        self.PIN_comboBox.addItem(str())
        self.PIN_comboBox.addItem(str())
        self.PIN_comboBox.addItem(str())
        self.PIN_comboBox.addItem(str())
        self.PIN_comboBox.addItem(str())
        self.PIN_comboBox.addItem(str())
        self.PIN_comboBox.addItem(str())
        self.PIN_comboBox.addItem(str())
        self.PIN_comboBox.addItem(str())
        self.PIN_comboBox.addItem(str())
        self.PIN_comboBox.addItem(str())
        self.PIN_comboBox.addItem(str())
        self.PIN_comboBox.addItem(str())
        self.PIN_comboBox.addItem(str())
        self.PIN_comboBox.addItem(str())
        self.PIN_comboBox.addItem(str())
        self.PIN_comboBox.addItem(str())
        self.PIN_comboBox.addItem(str())
        self.PIN_comboBox.addItem(str())
        self.PIN_comboBox.addItem(str())
        self.PIN_comboBox.addItem(str())
        self.PIN_comboBox.setObjectName(u"PIN_comboBox")
        self.PIN_comboBox.setGeometry(QRect(220, 10, 62, 21))
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(100, 30, 231, 21))
        self.Picture_label = QLabel(Form)
        self.Picture_label.setObjectName(u"Picture_label")
        self.Picture_label.setGeometry(QRect(390, 10, 121, 191))
        self.Picture_label.setPixmap(QPixmap(u"Avr0.png"))
        self.Picture_label.setScaledContents(True)

        self.retranslateUi(Form)
        QObject.connect(self.INA0_radioButton,SIGNAL("toggled(bool)"),self.OutConfigA0_groupBox.setDisabled)
        #self.INA0_radioButton.toggled.connect(self.OutConfigA0_groupBox.setDisabled)
        QObject.connect(self.OutA0_radioButton,SIGNAL("toggled(bool)"),self.InConfigA0_groupBox.setDisabled)
        #self.OutA0_radioButton.toggled.connect(self.InConfigA0_groupBox.setDisabled)
        QObject.connect(self.DefA0_checkBox,SIGNAL("clicked(bool)"),self.NewA0_lineEdit.setDisabled)
        #self.DefA0_checkBox.clicked.connect(self.NewA0_lineEdit.setDisabled)

        self.PIN_comboBox.activated.connect(self.Menu)
        self.PIN_comboBox.highlighted.connect(self.Save)

        self.Generate_pushButton.clicked.connect(self.Generate)

        QMetaObject.connectSlotsByName(Form)
    # setupUi
    def Save(self):
        pin_name = str(self.PIN_comboBox.currentText())
        pin_name = re.findall(r'\d+', pin_name)
        pin_name = int(pin_name[0])
        PIN_DIRE[pin_name] = int(self.INA0_radioButton.isChecked())
        if self.INA0_radioButton.isChecked():
            PIN_MODE[pin_name] = int(self.PullA0_radioButton.isChecked())
        else:
            PIN_MODE[pin_name] = int(self.HighA0_radioButton.isChecked())
        return

    def Menu(self):
        text = str(self.PIN_comboBox.currentText())
        self.PINA0_label.setText(text)
        pin_name = re.findall(r'\d+', text)
        pin_name = pin_name[0]
        self.Picture_label.setPixmap(QPixmap(u"Avr"+pin_name+".png"))
        pin_name = int(pin_name)
        In_or_Out = PIN_DIRE[pin_name]
        Pull_or_Imp = PIN_MODE[pin_name]
        High_or_Low = PIN_MODE[pin_name]
        if In_or_Out:
            self.InConfigA0_groupBox.setDisabled(False)
            self.OutConfigA0_groupBox.setDisabled(True)
            self.INA0_radioButton.setChecked(True)
            self.OutA0_radioButton.setChecked(False)
            if Pull_or_Imp:
                self.PullA0_radioButton.setChecked(True)
                self.ImpA0_radioButton.setChecked(False)
            else:
                self.PullA0_radioButton.setChecked(False)
                self.ImpA0_radioButton.setChecked(True)
        else:
            self.InConfigA0_groupBox.setDisabled(True)
            self.OutConfigA0_groupBox.setDisabled(False)
            self.INA0_radioButton.setChecked(False)
            self.OutA0_radioButton.setChecked(True)
            if High_or_Low:
                self.HighA0_radioButton.setChecked(True)
                self.LowA0_radioButton.setChecked(False)
            else:
                self.HighA0_radioButton.setChecked(False)
                self.LowA0_radioButton.setChecked(True)
        return

    def Generate(self):
        self.Save()
        out=self.Out_lineEdit.text()
        filename = out+"\\DIO_Config.h"
        f=open(filename,'w+')
        f.seek(0)
        PINS = range(0,32,1)
        for pin in PINS:
            In_or_Out = PIN_DIRE[pin]
            Pull_or_Imp = PIN_MODE[pin]
            High_or_Low = PIN_MODE[pin]
            if self.DefA0_checkBox.isChecked():
                name = "PIN"+str(pin)
            else:
                name = self.NewA0_lineEdit.text()+str(pin)
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
        f.close()
        return      

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Pins_Config", None))
        self.Out_lineEdit.setText(QCoreApplication.translate("Form", os.getcwd(), None))
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
        self.PINA0_label.setText(QCoreApplication.translate("Form", u"Pin 0", None))
#if QT_CONFIG(statustip)
        self.NewA0_lineEdit.setStatusTip("")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.NewA0_lineEdit.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.NewA0_lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"Write new name here", None))
        self.label.setText(QCoreApplication.translate("Form", u"Choose PIN", None))
        self.PIN_comboBox.setItemText(0, QCoreApplication.translate("Form", u"Pin 0", None))
        self.PIN_comboBox.setItemText(1, QCoreApplication.translate("Form", u"Pin 1", None))
        self.PIN_comboBox.setItemText(2, QCoreApplication.translate("Form", u"Pin 2", None))
        self.PIN_comboBox.setItemText(3, QCoreApplication.translate("Form", u"Pin 3", None))
        self.PIN_comboBox.setItemText(4, QCoreApplication.translate("Form", u"Pin 4", None))
        self.PIN_comboBox.setItemText(5, QCoreApplication.translate("Form", u"Pin 5", None))
        self.PIN_comboBox.setItemText(6, QCoreApplication.translate("Form", u"Pin 6", None))
        self.PIN_comboBox.setItemText(7, QCoreApplication.translate("Form", u"Pin 7", None))
        self.PIN_comboBox.setItemText(8, QCoreApplication.translate("Form", u"Pin 8", None))
        self.PIN_comboBox.setItemText(9, QCoreApplication.translate("Form", u"Pin 9", None))
        self.PIN_comboBox.setItemText(10, QCoreApplication.translate("Form", u"Pin 10", None))
        self.PIN_comboBox.setItemText(11, QCoreApplication.translate("Form", u"Pin 11", None))
        self.PIN_comboBox.setItemText(12, QCoreApplication.translate("Form", u"Pin 12", None))
        self.PIN_comboBox.setItemText(13, QCoreApplication.translate("Form", u"Pin 13", None))
        self.PIN_comboBox.setItemText(14, QCoreApplication.translate("Form", u"Pin 14", None))
        self.PIN_comboBox.setItemText(15, QCoreApplication.translate("Form", u"Pin 15", None))
        self.PIN_comboBox.setItemText(16, QCoreApplication.translate("Form", u"Pin 16", None))
        self.PIN_comboBox.setItemText(17, QCoreApplication.translate("Form", u"Pin 17", None))
        self.PIN_comboBox.setItemText(18, QCoreApplication.translate("Form", u"Pin 18", None))
        self.PIN_comboBox.setItemText(19, QCoreApplication.translate("Form", u"Pin 19", None))
        self.PIN_comboBox.setItemText(20, QCoreApplication.translate("Form", u"Pin 20", None))
        self.PIN_comboBox.setItemText(21, QCoreApplication.translate("Form", u"Pin 21", None))
        self.PIN_comboBox.setItemText(22, QCoreApplication.translate("Form", u"Pin 22", None))
        self.PIN_comboBox.setItemText(23, QCoreApplication.translate("Form", u"Pin 23", None))
        self.PIN_comboBox.setItemText(24, QCoreApplication.translate("Form", u"Pin 24", None))
        self.PIN_comboBox.setItemText(25, QCoreApplication.translate("Form", u"Pin 25", None))
        self.PIN_comboBox.setItemText(26, QCoreApplication.translate("Form", u"Pin 26", None))
        self.PIN_comboBox.setItemText(27, QCoreApplication.translate("Form", u"Pin 27", None))
        self.PIN_comboBox.setItemText(28, QCoreApplication.translate("Form", u"Pin 28", None))
        self.PIN_comboBox.setItemText(29, QCoreApplication.translate("Form", u"Pin 29", None))
        self.PIN_comboBox.setItemText(30, QCoreApplication.translate("Form", u"Pin 30", None))
        self.PIN_comboBox.setItemText(31, QCoreApplication.translate("Form", u"Pin 31", None))

        self.label_2.setText(QCoreApplication.translate("Form", u"Note: Default value for any Pin is Input Pullup", None))
        self.Picture_label.setText("")
    # retranslateUi

app = QApplication(sys.argv)
Widget = QWidget()
Form = Ui_Form()
Form.setupUi(Widget)
Widget.show()
app.exec_()