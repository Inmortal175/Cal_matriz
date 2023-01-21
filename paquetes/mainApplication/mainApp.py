from PyQt5.QtWidgets import QApplication, QMainWindow, QHeaderView
from PyQt5.QtCore import QPropertyAnimation, QEasingCurve
from PyQt5 import QtCore, QtWidgets
from PyQt5.uic import loadUi
import PyQt5

class matrizApp(QMainWindow):
  def __init__(self):
    super(matrizApp, self).__init__()
    loadUi('app.ui', self)

    #ocultar btn_resize
    self.btn_resize.hide()
    #control de barra de titulos
    self.btn_cerrar_ventana.clicked.connect(lambda : self.close())
    self.btn_maximize

    #mover ventana
    self.frame_superior.mouseMoveEvent = self.moverVentana

    ##eliminar barar de titulo
    self.setWindowFlag(PyQt5.QtCore.Qt.FramelessWindowHint)
    self.RenderFlags()
  
  def mousePressEvent(self,event):
    self.click_position = event.globalPos()
  
  def moverVentana(self, event):
    if self.isMaximized() == False:
      if event.buttons() == QtCore.Qt.LeftButton:
        self.move(self.pos() + event.globalPos() - self.click_position)
        self.click_position = event.globalPos()
        event.accept()
    if event.globalPos().y() <= 10:
      self.showMaximized()
      self.btn_maximize.hide()
      self.btn_resize.show()
    else:
      self.showNormal()
      self.btn_resize.hide()
      self.btn_maximize.show()