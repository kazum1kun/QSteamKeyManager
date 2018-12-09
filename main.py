# Driver file of the QSKM. Think of it as a ignition switch.

if __name__ == '__main__':
    import sys
    from package.MainWindow import MainWindow
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    app.setStyle('fusion')
    main = MainWindow()
    sys.exit(app.exec_())
