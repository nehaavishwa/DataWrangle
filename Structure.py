__author__ = 'nvishwakarma'

from PyQt4.QtCore import *
from PyQt4 import QtGui
from PyQt4.QtGui import *
from PyQt4.QtSql import *
import sys


class Utility(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        #super(HelloWorld, self).__init__()

        layout = QGridLayout()

        label = QLabel("Utility")
        line_edit = QLineEdit()
        button = QPushButton("Execute")

        layout.addWidget(label, 0, 0)
        layout.addWidget(line_edit, 0, 1)
        layout.addWidget(button, 1, 1)
        self.closeTheWindow(button)
        self.setLayout(layout)

        line_edit.textChanged.connect(self.changeTextLabel)

    def changeTextLabel(self, text):
        self.label.setText(text)

    def closeTheWindow(self, button):
        button.clicked.connect(self.close)

    def dbCon(self):
        db = QSqlDatabase.addDatabase('QODBC')
        db.setDatabaseName('DRIVER={SQL Server};SERVER=mmdevsql;DATABASE=master')
        db.open()
        QSqlQueryModel *model = new QSqlQueryModel
        query = "select db_name()"
        model->setQuery(query, db)
        db.close()

        '''QSqlDatabase dbname
            db =QSqlDatabase.addDatabase("QODBC3")
        db.setDatabaseName("DRIVER={SQL Server};Server=ITPL_PC1;Database=Test;Uid=sa;Port=1433;Pwd=*******;WSID=.")
        db.open()
        QSqlQueryModel *model = new QSqlQueryModel
        QString query = "insert into qttable(PID) values('ARINDAM')";
        model->setQuery(query, db);
        db.close();'''

app = QApplication(sys.argv)
dialog = Utility()
dialog.show()
app.exec_()