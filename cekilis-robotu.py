import random, cv2
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication
import sys,os

katilimcilar=[]
kazananlar=[]
hediye_listesi=[]
katilimci_sayisi=0
hediye_sayisi=0
resim_adr=""

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1002, 703)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 1051, 791))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.gridLayoutWidget_2)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.gridLayoutWidget_2)
        self.tabWidget.setStyleSheet("")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(100, 120, 131, 41))
        self.label.setStyleSheet("font: 13pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(80, 160, 141, 41))
        self.label_2.setStyleSheet("font: 13pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab)
        self.pushButton_2.setGeometry(QtCore.QRect(720, 170, 131, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.textEdit_2 = QtWidgets.QTextEdit(self.tab)
        self.textEdit_2.setGeometry(QtCore.QRect(250, 170, 451, 31))
        self.textEdit_2.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.textEdit_2.setObjectName("textEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(720, 130, 131, 31))
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(140, 220, 121, 41))
        self.label_3.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        self.textEdit = QtWidgets.QTextEdit(self.tab)
        self.textEdit.setGeometry(QtCore.QRect(250, 130, 451, 31))
        self.textEdit.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.textEdit.setObjectName("textEdit")
        self.pushButton_3 = QtWidgets.QPushButton(self.tab)
        self.pushButton_3.setGeometry(QtCore.QRect(390, 230, 131, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.spinBox = QtWidgets.QSpinBox(self.tab)
        self.spinBox.setGeometry(QtCore.QRect(270, 230, 71, 31))
        self.spinBox.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";")
        self.spinBox.setObjectName("spinBox")
        self.pushButton_4 = QtWidgets.QPushButton(self.tab)
        self.pushButton_4.setGeometry(QtCore.QRect(780, 550, 151, 51))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_8 = QtWidgets.QPushButton(self.tab)
        self.pushButton_8.setGeometry(QtCore.QRect(560, 230, 131, 31))
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayoutWidget = QtWidgets.QWidget(self.tab)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(30, 280, 901, 251))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.tableWidget = QtWidgets.QTableWidget(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setStyleSheet("font: 63 13pt \"Myriad Pro Light\";")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignVCenter)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignVCenter)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.gridLayout.addWidget(self.tableWidget, 0, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.tab)
        self.label_7.setGeometry(QtCore.QRect(310, 10, 341, 51))
        self.label_7.setStyleSheet("color: rgb(53, 255, 70);\n"
                                   "font: 57 italic 36pt \"Noto Sans\";")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.tab)
        self.label_8.setGeometry(QtCore.QRect(120, 90, 101, 31))
        self.label_8.setStyleSheet("font: 13pt \"MS Shell Dlg 2\";")
        self.label_8.setObjectName("label_8")
        self.textEdit_3 = QtWidgets.QTextEdit(self.tab)
        self.textEdit_3.setGeometry(QtCore.QRect(250, 90, 451, 31))
        self.textEdit_3.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.textEdit_3.setObjectName("textEdit_3")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.graphicsView = QtWidgets.QGraphicsView(self.tab_2)
        self.graphicsView.setGeometry(QtCore.QRect(0, 30, 591, 381))
        self.graphicsView.setObjectName("graphicsView")
        self.listView = QtWidgets.QListView(self.tab_2)
        self.listView.setGeometry(QtCore.QRect(600, 10, 381, 401))
        self.listView.setStyleSheet("font: 75 italic 12pt \"MS Sans Serif\";")
        self.listView.setObjectName("listView")
        self.pushButton_5 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_5.setGeometry(QtCore.QRect(820, 480, 151, 41))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_6.setGeometry(QtCore.QRect(820, 530, 151, 41))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_7.setGeometry(QtCore.QRect(820, 630, 151, 41))
        self.pushButton_7.setObjectName("pushButton_7")
        self.listWidget = QtWidgets.QListWidget(self.tab_2)
        self.listWidget.setGeometry(QtCore.QRect(0, 420, 811, 251))
        self.listWidget.setStyleSheet("font: 75 italic 15pt \"MS Sans Serif\";")
        self.listWidget.setObjectName("listWidget")
        self.label_4 = QtWidgets.QLabel(self.tab_2)
        self.label_4.setGeometry(QtCore.QRect(820, 420, 171, 22))
        self.label_4.setStyleSheet("font: 13pt \"Noto Sans\";\n"
                                   "text-decoration: underline;")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.tab_2)
        self.label_5.setGeometry(QtCore.QRect(880, 440, 81, 41))
        self.label_5.setStyleSheet("font: 87 19pt \"Noto Sans\";")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.tab_2)
        self.label_6.setGeometry(QtCore.QRect(100, 0, 391, 31))
        self.label_6.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.label_6.setObjectName("label_6")
        self.pushButton_9 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_9.setGeometry(QtCore.QRect(820, 580, 151, 41))
        self.pushButton_9.setObjectName("pushButton_9")
        self.tabWidget.addTab(self.tab_2, "")
        self.horizontalLayout.addWidget(self.tabWidget)
        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Form)


        self.pushButton.clicked.connect(self.resim_dosyasi_get)
        self.pushButton_2.clicked.connect(self.katilimci_dosyasi_get)
        self.pushButton_3.clicked.connect(self.dinamic_hediye_olustur)
        self.pushButton_4.clicked.connect(self.devam_et)
        self.pushButton_8.clicked.connect(self.temizle)
        self.pushButton_5.clicked.connect(self.guncelle)
        self.pushButton_6.clicked.connect(self.kazananSec)
        self.pushButton_7.clicked.connect(self.geriDon)
        self.textEdit_3.textChanged.connect(self.programAdi)
        self.textEdit.textChanged.connect(self.rsm_png)
        self.textEdit_2.textChanged.connect(self.ktlmci_txt)
        self.pushButton_9.clicked.connect(self.temizlik)


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Resim dosyası:"))
        self.label_2.setText(_translate("Form", "Katılımcı  dosyası:"))
        self.pushButton_2.setText(_translate("Form", "Gözat"))
        self.pushButton.setText(_translate("Form", "Gözat"))
        self.label_3.setText(_translate("Form", "Hediye Çeşiti:"))
        self.pushButton_3.setText(_translate("Form", "Oluştur"))
        self.pushButton_4.setText(_translate("Form", "Devam Et"))
        self.pushButton_8.setText(_translate("Form", "Temizle"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Hediye Adı"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Adedi"))
        self.label_7.setText(_translate("Form", "Çekiliş Motoru"))
        self.label_8.setText(_translate("Form", "Etkinlik Adı:"))
        self.textEdit_3.setHtml(_translate("Form",
                                           "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                           "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                           "p, li { white-space: pre-wrap; }\n"
                                           "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
                                           "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "Tab 1"))
        self.pushButton_5.setText(_translate("Form", "Katılımcıları Güncelle"))
        self.pushButton_6.setText(_translate("Form", "Çekiliş Yap"))
        self.pushButton_7.setText(_translate("Form", "Geri Dön"))
        self.label_4.setText(_translate("Form", "Çekilişteki Kişi Sayısı"))
        self.label_5.setText(_translate("Form", "0"))
        self.label_6.setText(_translate("Form", "Etkinlik Başlığı"))
        self.pushButton_9.setText(_translate("Form", "Temizle"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "Tab 2"))



        self.tabWidget.setTabText(0,"Ayarlamalar")
        self.tabWidget.setTabText(1, "Çekiliş Ekranı")
        self.tabWidget.removeTab(1)
        self.yedek_sayisi=1

    def temizle(self): #  TEmizleme Koud ama ek yapılacak oteki tarafı da silmesi lazım
        self.tableWidget.setRowCount(0)
    def programAdi(self):
        prgAdi=self.textEdit_3.toPlainText()
        self.label_6.setText(prgAdi)
    def rsm_png(self):
        rsmAdr=self.textEdit.toPlainText()
        self.resim_adr=rsmAdr
    def ktlmci_txt(self):
        ktlmcAdr=self.textEdit_2.toPlainText()
        self.katilimci_dosyasi=ktlmcAdr

    def dinamic_hediye_olustur(self):
        self.hediye_sayisi=self.spinBox.value()
        print("hediye sayısı:{}".format(self.hediye_sayisi))
        self.tableWidget.setRowCount(self.hediye_sayisi)

    def temizlik(self):
        self.listWidget.clear()
        kazananlar.clear()
        self.guncelle()
        print("kazananlar: {}".format(kazananlar))
        print(self.listWidget.count())

    def guncelle(self):
        try:
            with open(self.katilimci_dosyasi,encoding="utf-8") as fp:
                for line in fp:
                    x = line.split("\n")
                    if x[0] not in katilimcilar:
                        # print(x[0])
                        katilimcilar.append(x[0])
        except Exception as e:
            print("HATA!!! Katılımcı Dosyası Okunamadı")
        model = QtGui.QStandardItemModel()
        self.listView.setModel(model)
        for i in katilimcilar:
            item = QtGui.QStandardItem(i)
            model.appendRow(item)
        self.katilimci_sayisi=len(katilimcilar)
        self.label_5.setText(str(self.katilimci_sayisi))

    def resim_dosyasi_get(self):
        try:
            data_path, _ = QtWidgets.QFileDialog.getOpenFileName(None, 'Open File', r"/home/the-machine/Desktop", 'Image Files(*.png *.jpg *.jpeg)')
        except Exception as e:
            print("HATA!!! Resim Dosyası Okunamadı")
        self.textEdit.setText(data_path)
        self.resim_adr=data_path

    def katilimci_dosyasi_get(self):
        try:
            data_path, _ = QtWidgets.QFileDialog.getOpenFileName(None, 'Open File', r"/home/the-machine/Desktop", '*.txt')
        except Exception as e:
            print("HATA!!! Katılımcı Dosyası Okunamadı")
        self.textEdit_2.setText(data_path)
        self.katilimci_dosyasi=data_path
        with open(data_path,encoding="utf-8") as fp:
            for line in fp:
                x=line.split("\n")
                if x[0] not in katilimcilar:
                #print(x[0])
                    katilimcilar.append(x[0])

        print(katilimcilar)
        self.katilimci_sayisi=len(katilimcilar)
        self.label_5.setText(str(self.katilimci_sayisi))
        # print("boyut: {}".format(self.katilimci_sayisi))

    def kazananSec(self):
        if self.katilimci_sayisi != 0:
            kazanan=random.randint(0, self.katilimci_sayisi-1)
            print(katilimcilar[kazanan])
            kazananlar.append(katilimcilar[kazanan])
            sahip = katilimcilar[kazanan]
            katilimcilar.pop(kazanan)
            print(katilimcilar)
            try:
                hdy_ismi=hediye_listesi.pop(0)
            except Exception as e:

                hdy_ismi="Yedek"+str(self.yedek_sayisi)
                self.yedek_sayisi+=1
                print("yedek sayısı: {}".format(self.yedek_sayisi))
            syk=hdy_ismi+" : "+ sahip#self.tableWidget.
            print(syk)
            self.katilimci_sayisi-=1
            self.label_5.setText(str(self.katilimci_sayisi))
            self.listWidget.addItem(syk)

    def geriDon(self):
        self.tabWidget.addTab(self.tab,"Ayaralamalar")
        self.tabWidget.removeTab(0)

    def devam_et(self):
        try:
            model = QtGui.QStandardItemModel()
            self.listView.setModel(model)
            for i in katilimcilar:
              item = QtGui.QStandardItem(i)
              model.appendRow(item)
        except Exception as e:
            print("HATA!!! Devam et fonksiyonunda hata yaşandı")
        try:
            img=cv2.imread(self.resim_adr)
            print(self.resim_adr)
            dsize = (585, 375)
            imag = cv2.resize(img, dsize, cv2.INTER_AREA)
            adr="cekilis_motoru_resmi.png"
            cv2.imwrite(adr, imag)
            pixmap=QPixmap(adr)
            scene = QtWidgets.QGraphicsScene(self)
            item = QtWidgets.QGraphicsPixmapItem(pixmap)
            scene.addItem(item)
            self.graphicsView.setScene(scene)
        except Exception as e:
            print(e)
        self.hediyeOku()
        self.tabWidget.addTab(self.tab_2, "Çekiliş Ekranı")
        self.tabWidget.removeTab(0)

    def hediyeOku(self):
        hediye_listesi.clear()
        tablo=self.tableWidget
        try:
            for i in range(self.hediye_sayisi):
                hd_adi=str(tablo.item(i,0).text())
                hd_adet=int(tablo.item(i,1).text())
                # print("Hediye Adı: {}, Adedi: {}".format(hd_adi,hd_adet))
                for z in range(hd_adet):
                    hediye_listesi.append(hd_adi)
        except Exception as e:
            print("HATA!!! Hediye Sayısı Girilmedi")
        print("Hediye Listemiz Sırayla: {}".format(hediye_listesi))

class ExampleApp(QtWidgets.QMainWindow,Ui_Form):
    def __init__(self, parent=None):
        super(ExampleApp, self).__init__(parent)
        self.setupUi(self)

def main():
    app = QApplication(sys.argv)
    form = ExampleApp()
    form.show()
    app.exec_()

if __name__ == '__main__':
       main()