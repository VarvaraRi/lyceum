import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QInputDialog, QMainWindow,  QLineEdit
from PyQt5.QtCore import Qt

class Diary(QMainWindow):
    def __init__(self):
        self.first_num = 0
        super().__init__()
        uic.loadUi('diary.ui', self)
        file = open('diary.txt', mode='r', encoding='utf8')
        for string in file.readlines():
            self.events.addItem(string.strip())
        file.close()
        self.addAll.clicked.connect(self.AddItem)
        self.events.itemClicked.connect(self.dialog)

    def keyPressEvent(self, event):
        key = event.key()
        if key == Qt.Key_Enter:
            self.AddItem()

    def dialog(self):
        i, okBtnPressed = QInputDialog.getItem(
            self,
            "",
            "Выбирерите дейстивие",
            ("Удалить", "Изменить","Очистить все"),
            0,
            False
        )
        if i == 'Удалить' and okBtnPressed == True:
            self.remove_item()
        if i == 'Изменить' and okBtnPressed == True:
            self.edit_item()
        if i == 'Очистить все' and okBtnPressed == True:
            self.delet_all()

    def edit_item(self):
        row = self.events.currentRow()
        item = self.events.item(row)
        if item is not None:
            text, ok_button =   QInputDialog.getText(self, '', '', QLineEdit.Normal, item.text())
            if text and ok_button is not None:
                item.setText(text)
        file = open('diary.txt', mode='w', encoding='utf8')
        for i in range(self.events.count()):
            item = self.events.item(i).text()
            file.write(item+'\n')
        file.close()


    def AddItem(self):
        date = self.date.selectedDate()
        date = date.toString()
        time = self.time.text()
        ewent = self.eventName.text()
        ewent_l = [ewent, date, time]
        self.events.addItem(' '.join(ewent_l))
        file = open('diary.txt', mode='a', encoding='utf8')
        file.write(' '.join(ewent_l)+'\n')
        file.close()

    def remove_item(self):
        row = self.events.currentRow()
        self.events.takeItem(row)
        file = open('diary.txt', mode='w', encoding='utf8')
        for i in range(self.events.count()):
            item = self.events.item(i).text()
            file.write(item + '\n')
        file.close()

    def delet_all(self):
        self.events.clear()
        file = open('diary.txt', mode='w', encoding='utf8')
        file.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Diary()
    ex.show()
    sys.exit(app.exec())