# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Code_org\DDish EPG\DDishEPG.ui'
#
# Created: Wed Jul 30 12:07:17 2014
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(427, 232)
        self.openEPG = QtGui.QPushButton(Dialog)
        self.openEPG.setGeometry(QtCore.QRect(330, 20, 75, 23))
        self.openEPG.setObjectName(_fromUtf8("openEPG"))
        self.EPGFILE = QtGui.QLineEdit(Dialog)
        self.EPGFILE.setGeometry(QtCore.QRect(70, 20, 251, 20))
        self.EPGFILE.setObjectName(_fromUtf8("EPGFILE"))
        self.EPGFILE_2 = QtGui.QLabel(Dialog)
        self.EPGFILE_2.setGeometry(QtCore.QRect(20, 23, 46, 13))
        self.EPGFILE_2.setObjectName(_fromUtf8("EPGFILE_2"))
        self.Channel_tem_2 = QtGui.QLabel(Dialog)
        self.Channel_tem_2.setGeometry(QtCore.QRect(20, 60, 51, 16))
        self.Channel_tem_2.setObjectName(_fromUtf8("Channel_tem_2"))
        self.Generate = QtGui.QPushButton(Dialog)
        self.Generate.setGeometry(QtCore.QRect(330, 198, 75, 21))
        self.Generate.setObjectName(_fromUtf8("Generate"))
        self.Channel_tem = QtGui.QLineEdit(Dialog)
        self.Channel_tem.setGeometry(QtCore.QRect(70, 60, 251, 20))
        self.Channel_tem.setObjectName(_fromUtf8("Channel_tem"))
        self.openTem = QtGui.QPushButton(Dialog)
        self.openTem.setGeometry(QtCore.QRect(330, 60, 75, 23))
        self.openTem.setObjectName(_fromUtf8("openTem"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.openEPG.setText(_translate("Dialog", "OPEN", None))
        self.EPGFILE_2.setText(_translate("Dialog", "EPG FILE", None))
        self.Channel_tem_2.setText(_translate("Dialog", "Template", None))
        self.Generate.setText(_translate("Dialog", "Generate", None))
        self.openTem.setText(_translate("Dialog", "OPEN", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

