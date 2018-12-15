import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QInputDialog, QMainWindow,  QLineEdit
from PyQt5.QtCore import Qt

class Diary(QMainWindow):
    def __init__(self):
        self.first_num = 0
        super().__init__()
        uic.loadUi('proyekt.ui', self)
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

    def AddItem(self):
        date = self.date.selectedDate()
        date = date.toString()
        time = self.time.text()
        ewent = self.eventName.text()
        ewent_l = [ewent, date, time]
        self.events.addItem(' '.join(ewent_l))

    def remove_item(self):
        row = self.events.currentRow()
        self.events.takeItem(row)

    def delet_all(self):
        self.events.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Diary()
    ex.show()
    sys.exit(app.exec())