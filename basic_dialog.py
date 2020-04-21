#!/usr/bin/env python

from PyQt4 import QtGui, QtCore

class BasicDialog(QtGui.QDialog):

    def __init__(self, parent=None):
        super(BasicDialog, self).__init__(parent=parent)
        #Instantiate a layout and set it as the dialogs main layout
        main_layout = QtGui.QVBoxLayout()
        self.setLayout(main_layout)

        # Add line edit labelled "Name"
        name_label = QtGui.QLabel("Name")
        main_layout.addWidget(name_label)

        self.name_edit = QtGui.QLineEdit()
        main_layout.addWidget(self.name_edit)

        # Add combo box labelled "Type" with options A, B, C
        combo_label = QtGui.QLabel("Type")
        main_layout.addWidget(combo_label)

        self.combo_box = QtGui.QComboBox()
        self.combo_box.addItem("A")
        self.combo_box.addItem("B")
        self.combo_box.addItem("C")
        main_layout.addWidget(self.combo_box)

        # Add Date widget labelled "Need By" - Defaults to one week in the future.
        # Can't modify to a date in the past
        date_label = QtGui.QLabel("Need By")
        main_layout.addWidget(date_label)

        self.dateWidget = QtGui.QDateEdit(QtCore.QDate.currentDate().addDays(7))
        self.dateWidget.setMinimumDate(QtCore.QDate.currentDate())
        main_layout.addWidget(self.dateWidget) 

        # Text Edit labelled "Notes"
        text_label = QtGui.QLabel("Notes")
        main_layout.addWidget(text_label)

        self.note_edit = QtGui.QTextEdit()
        main_layout.addWidget(self.note_edit) 

        #Add ok and cancel buttons
        #And hook them up to dialogs accept/reject methods
        button_box = QtGui.QDialogButtonBox(QtGui.QDialogButtonBox.Ok|\
                                            QtGui.QDialogButtonBox.Cancel)
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)
        main_layout.addWidget(button_box)

    def getValues(self):
        """Gets the current values of each widget
        
        Returns:
            Dictionary of all widget values with the label as the key
        """
        d = {}
        d['Name'] = str(self.name_edit.text())
        d['Type'] = str(self.combo_box.currentText())
        d['Need By'] = str(self.dateWidget.date().toString('yyyy-MM-dd'))
        d['Notes'] = str(self.note_edit.toPlainText())
        return d

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
