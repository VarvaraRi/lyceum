import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QInputDialog, QMainWindow,  QLineEdit
from PyQt5.QtCore import Qt


class Diary(QMainWindow):
    def __init__(self):
        self.first_num = 0
        super().__init__()
        uic.loadUi('diary.ui', self)
        self.addAll.clicked.connect(self.AddItem)
        self.events.itemClicked.connect(self.dialog)

    def keyPressEvent(self, eWent):
        if eWent.key() == Qt.Key_F:
            self.AddItem()

    def dialog(self):
        i, okBtnPressed = QInputDialog.getItem(
            self,
            "",
            "Выбирерите дейстивие",
            ("Удалить", "Изменить"),
            0,
            False
        )
        if i == 'Удалить' and okBtnPressed == True:
            self.onemore()
        if i == 'Изменить' and okBtnPressed == True:
            self.edit_item()

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

    def onemore(self):
        row = self.events.currentRow()
        self.events.takeItem(row)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Diary()
    ex.show()
    sys.exit(app.exec())
