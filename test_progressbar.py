#新增progressbar及horizontalSlider

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from progressbar_test import Ui_Dialog
import sys

def clicked_press_me():
    x = ui.lineEdit.text()
    #message = QMessageBox()
    #message.setWindowTitle("surprise")
    #message.setInformativeText(x)
    #message.exec_()
    ui.progressBar.setValue(40)

def clicked_show_string():
    #把please enter value改成hello
    ui.label.setText("hello")

    #確認radiobutton是否有勾選
    #print(ui.radioButton.isChecked())
    
    #選擇下拉選單，顯示下拉選單的文字及第幾個
    #print(ui.comboBox.currentText()) #顯示下拉選單的文字及第幾個
    #print(ui.comboBox.currentIndex()) #顯示下拉選單的文字在第幾個
    ui.progressBar.setValue(90)

def pic_click(event): #event:點下去的位置
    message = QMessageBox()
    message.setWindowTitle("surprise")
    message.setInformativeText("你按了圖片")
    message.exec_()

def clicked_radio():
    print("click radio")

def change(i):
    print(i)
    ui.progressBar.setValue(90)

def slider_change():
    #print("change")
    x = ui.horizontalSlider.value()
    print("change value is " + str(x))

def slider_release():
    message = QMessageBox()
    message.setWindowTitle("surprise")
    message.setInformativeText("選擇的數值是"+ str(ui.horizontalSlider.value()))
    message.exec_()

app = QApplication(sys.argv)
widge = QWidget() #把Dialog放進widge裡
#----------【翻譯匯入(譯文)】--------------#
#ts轉成qm後，設置translate
t = QTranslator()
t.load("chinese.qm")
app.installTranslator(t)
#-----------------------------------------#
ui = Ui_Dialog()
ui.setupUi(widge)


#設定按鈕連接
ui.pressMeButton.clicked.connect(clicked_press_me) # ui.按鈕objectName(在Qt設定的)
ui.helloButton.clicked.connect(clicked_show_string)

#設定圖片連接
ui.pic.mouseReleaseEvent = pic_click #滑鼠放開時執行動作

#【設定radiobutton連接】
#設定group讓button間互斥
group1 = QButtonGroup(widge)
group1.addButton(ui.radioButton)
group1.addButton(ui.radioButton_2)
ui.radioButton.clicked.connect(clicked_radio) #()內為callback function

#設定comboBox
ui.comboBox.addItems(["cat","dog","bird"])
ui.comboBox.activated.connect(change)

#設定progressBar
ui.progressBar.setMaximum(100)
ui.progressBar.setMinimum(0)
ui.progressBar.setValue(3)

ui.horizontalSlider.setMaximum(110)
ui.horizontalSlider.setMinimum(-3)
ui.horizontalSlider.valueChanged.connect(slider_change)
ui.horizontalSlider.sliderReleased.connect(slider_release)


widge.show()
sys.exit(app.exec_())


