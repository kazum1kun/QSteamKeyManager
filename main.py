# Driver file of the QSKM. Think of it as a ignition switch.
from PyQt5 import QtSql

from package.Env import Env

if __name__ == '__main__':
    import sys
    from package.MainWindow import MainWindow
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)

    # Database connection
    db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
    db.setDatabaseName(Env.rel_db_path)

    app.setStyle('fusion')
    main = MainWindow()
    sys.exit(app.exec_())
