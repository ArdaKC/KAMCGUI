# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'guiconfig.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def bas4(self):
        import os
        if os.system('xterm -e "ifconfig; sleep 300"') == 0:
            self.label_3.setText("Xterm Başarıyla Başlatıldı.")
        else:
            self.label_3.setText("Eksik Paket Mevcut. (xterm)")

    def bas3(self):
        from io import StringIO
        import os
        import os.path
        import subprocess

        import os

        def alan():
            if os.system('macchanger') == 0:
                if os.system('ifconfig') == 0:
                     try:
                         with open("agcihazi.txt", "r") as f:
                             icerik = f.read()
                             agcihazi = icerik
                             if agcihazi == "":
                                 self.label_3.setText("agcihazı.txt boş olduğundan işlem uygulanamıyor.")
                             else:
                                 if os.system(
                                         "sudo ifconfig " + agcihazi + " down && sudo macchanger -r " + agcihazi + " && sudo ifconfig " + agcihazi + " up") == 0:

                                     self.label_3.setText("Komut Başarıyla Uygulandı.")
                                 else:
                                     self.label_3.setText("Komut Uygulanamadı Bir Sorun Var. Terminali Kontrol Edin.")
                     except FileNotFoundError:
                         self.label_3.setText("agcihazi.txt dosyasına erişilemiyor.")



                else:
                    print("Eksik Paketler Mevcut.")
                    self.label_3.setText("Eksik Paket Mevcut. (ifconfig)")
            else:
                self.label_3.setText("Eksik Paket Mevcut. (macchanger)")

        alan()

    def bas2(self):
        yazi = self.textEdit.toPlainText()
        self.textEdit.setPlainText(yazi)
        if yazi == "":

            self.label_3.setText("Ağ Cihazını Girin.")

        else:

            with open("agcihazi.txt", "w") as f:
                agcihazi2 = yazi
                f.write(agcihazi2)
                self.label_3.setText("Ağ Cihazı Kayıt Edildi.")

    def bas1(self):

        yazi = self.textEdit.toPlainText()
        self.textEdit.setPlainText(yazi)
        if yazi == "":
            self.label_3.setText("Ağ Cihazını Girin.")

        else:
            from io import StringIO
            import os
            import os.path
            import subprocess
            agcihazi = yazi

            import os

            def alan():
                if os.system('macchanger') == 0:
                    if os.system('ifconfig') == 0:
                        if os.system(
                                         "sudo ifconfig " + agcihazi + " down && sudo macchanger -r " + agcihazi + " && sudo ifconfig " + agcihazi + " up") == 0:

                            self.label_3.setText("Komut Başarıyla Uygulandı.")
                        else:
                            self.label_3.setText("Komut Uygulanamadı Bir Sorun Var. Terminali Kontrol Edin.")
                    else:
                        print("Eksik Paketler Mevcut.")
                        self.label_3.setText("Eksik Paketler Mevcut. (ifconfig)")
                else:
                    self.label_3.setText("Eksik Paketler Mevcut. (macchanger)")

            alan()
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(643, 308)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(120, 170, 481, 17))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(120, 10, 401, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(120, 50, 401, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(120, 90, 401, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(120, 190, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(120, 130, 401, 31))
        self.pushButton_5.setObjectName("pushButton_5")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(-10, 270, 1141, 51))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(20, 10, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(110, 10, 1501, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.pushButton.clicked.connect(self.bas1)
        self.pushButton_2.clicked.connect(self.bas2)
        self.pushButton_3.clicked.connect(self.bas3)

        self.pushButton_5.clicked.connect(self.bas4)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "KCS AutoMacchangerGUI 1.1"))
        self.label.setText(_translate("Form", "Ağ cihazını yazın örnek : wlp3s0 veya wlan0"))
        self.pushButton.setText(_translate("Form", "Mac Adresini Değiştir"))
        self.pushButton_2.setText(_translate("Form", "Ağ Cihazını Metin Belgesine Kaydet"))
        self.pushButton_3.setText(_translate("Form", "Kayıt Edilmiş Ağ Cihazını Kullan"))

        self.pushButton_5.setText(_translate("Form", "Ağ Bilgilerini Xterm İle Göster"))
        self.label_3.setText(_translate("Form", "İşlem Yok"))
        self.label_2.setText(_translate("Form", "Durum : "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
