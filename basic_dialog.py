#!/usr/bin/env python

from PyQt4 import QtGui, QtCore

class BasicDialog(QtGui.QDialog):
    def __init__(self, parent=None):
        super(BasicDialog, self).__init__(parent=parent)
        #Instantiate a layout and set it as the dialogs main layout
        main_layout = QtGui.QVBoxLayout()
        self.setLayout(main_layout)

        # Add line edit labelled Name
        line_label = QtGui.QLabel("Name")
        main_layout.addWidget(line_label)

        line_edit = QtGui.QLineEdit()
        main_layout.addWidget(line_edit)

        # Add combo box labelled Type with options A, B, C
        combo_label = QtGui.QLabel("Type")
        main_layout.addWidget(combo_label)
        combo_box = QtGui.QComboBox()
        combo_box.addItem("A")
        combo_box.addItem("B")
        combo_box.addItem("C")
        main_layout.addWidget(combo_box)

        # Add Date widget labelled "Need By" - Defaults to one week in the future.
        # Can't modify to a date in the past
        date_label = QtGui.QLabel("Need By")
        main_layout.addWidget(date_label)
        dateWidget = QtGui.QDateEdit(QtCore.QDate.currentDate().addDays(7))
        dateWidget.setMinimumDate(QtCore.QDate.currentDate())
        main_layout.addWidget(dateWidget) 

        # Text Edit labelled Notes
        text_label = QtGui.QLabel("Notes")
        main_layout.addWidget(text_label)
        text_edit = QtGui.QTextEdit()
        main_layout.addWidget(text_edit) 

        #Add ok and cancel buttons
        #And hook them up to dialogs accept/reject methods
        button_box = QtGui.QDialogButtonBox(QtGui.QDialogButtonBox.Ok|\
                                            QtGui.QDialogButtonBox.Cancel)
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)
        main_layout.addWidget(button_box)

    def getValues(self):
        return None

if __name__ == '__main__':
    #Instantiate a QApplication - requirement for Qt
    app = QtGui.QApplication([])
    #Instantiate, show, then raise our dialog to the front
    dlg = BasicDialog()
    dlg.show()
    dlg.raise_()
    #only getValues if 'Ok' is clicked
    if dlg.exec_():
        print dlg.getValues()
