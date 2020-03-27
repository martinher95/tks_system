"""main file of the project. Used to run the mainview firstly"""

from gui.mainview import *
import sys

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = myMainWindow()
    main_window.show()
    sys.exit(app.exec_())