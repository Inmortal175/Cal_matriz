from paquetes.mainApplication.mainApp import matrizApp
from PyQt5.QtWidgets import QApplication
import sys
if __name__ == '__main__':
  app = QApplication(sys.argv)
  myApp = matrizApp()
  myApp.show()
  sys.exit(app.exec_())