

import sys
import Window
from PyQt5.QtWidgets import QButtonGroup
from PyQt5 import QtWidgets
import numpy as np
import math
#Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Window.Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Window.Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # Área de los Signals
        self.buttongroup = QButtonGroup()
        self.buttongroup.setExclusive(True)

        self.btn_limpiar.clicked.connect(self.limpiar)
        self.btn_generar.clicked.connect(self.generar)

        self.buttongroup.addButton(self.pushButton)
        self.buttongroup.addButton(self.pushButton_2)
        self.buttongroup.addButton(self.pushButton_3)
        self.buttongroup.addButton(self.pushButton_4)
        self.buttongroup.addButton(self.pushButton_5)
        self.buttongroup.addButton(self.pushButton_6)
        self.buttongroup.addButton(self.pushButton_7)
        self.buttongroup.addButton(self.pushButton_8)
        self.buttongroup.addButton(self.pushButton_9)
        self.buttongroup.addButton(self.pushButton_10)
        self.buttongroup.addButton(self.pushButton_11)
        self.buttongroup.addButton(self.pushButton_12)
        self.buttongroup.addButton(self.pushButton_13)
        self.buttongroup.addButton(self.pushButton_14)
        self.buttongroup.addButton(self.pushButton_15)
        self.buttongroup.addButton(self.pushButton_16)
        self.buttongroup.addButton(self.pushButton_17)
        self.buttongroup.addButton(self.pushButton_18)
        self.buttongroup.addButton(self.pushButton_19)
        self.buttongroup.addButton(self.pushButton_20)
        self.buttongroup.addButton(self.pushButton_21)
        self.buttongroup.addButton(self.pushButton_22)
        self.buttongroup.addButton(self.pushButton_23)
        self.buttongroup.addButton(self.pushButton_24)
        self.buttongroup.addButton(self.pushButton_25)

        self.buttongroup.buttonClicked.connect(self.cambioColor)

        self.lista_botones = [
            self.pushButton, self.pushButton_2, self.pushButton_3, self.pushButton_4, self.pushButton_5,
            self.pushButton_6, self.pushButton_7, self.pushButton_8, self.pushButton_9, self.pushButton_10,
            self.pushButton_11, self.pushButton_12, self.pushButton_13, self.pushButton_14, self.pushButton_15,
            self.pushButton_16, self.pushButton_17, self.pushButton_18, self.pushButton_19, self.pushButton_20,
            self.pushButton_21, self.pushButton_22, self.pushButton_23, self.pushButton_24, self.pushButton_25]


    def cambioColor(self,button):
        if isinstance(button, QtWidgets.QPushButton):
            button.setStyleSheet("background-color : black")
            button.setEnabled(False)

    def limpiar(self):
        for i in self.lista_botones:
            i.setEnabled(True)
            i.setStyleSheet("background-color : white")

        self.lineEdit.setText("")

    def generar(self):
        A = [[-1, -1, 1, -1, -1], [-1, 1, -1, 1, -1], [1, -1, -1, -1, 1], [1, 1, 1, 1, 1], [1, -1, -1, -1, 1]]
        E = [[1, 1, 1, 1, 1], [1, -1, -1, -1, 1], [1, 1, 1, 1, -1], [1, -1, -1, -1, -1], [1, 1, 1, 1, 1]]
        I = [[1, 1, 1, 1, 1], [-1, -1, 1, -1, -1], [-1, -1, 1, -1, -1], [-1, -1, 1, -1, -1], [1, 1, 1, 1, 1]]
        O = [[1, 1, 1, 1, 1], [1, -1, -1, -1, 1], [1, -1, -1, -1, 1], [1, -1, -1, -1, 1], [1, 1, 1, 1, 1]]
        U = [[1, -1, -1, -1, 1], [1, -1, -1, -1, 1], [1, -1, -1, -1, 1], [1, -1, -1, -1, 1], [1, 1, 1, 1, 1]]
        lista = []

        letras = ["A", "E", "I", "O", "U"]

        if self.pushButton.styleSheet() == "background-color : black":
            lista.append(1)
        else:
            lista.append(-1)
        if self.pushButton_2.styleSheet() == "background-color : black":
            lista.append(1)
        else:
            lista.append(-1)
        if self.pushButton_3.styleSheet() == "background-color : black":
            lista.append(1)
        else:
            lista.append(-1)
        if self.pushButton_4.styleSheet() == "background-color : black":
            lista.append(1)
        else:
            lista.append(-1)
        if self.pushButton_5.styleSheet() == "background-color : black":
            lista.append(1)
        else:
            lista.append(-1)
        if self.pushButton_6.styleSheet() == "background-color : black":
            lista.append(1)
        else:
            lista.append(-1)
        if self.pushButton_7.styleSheet() == "background-color : black":
            lista.append(1)
        else:
            lista.append(-1)
        if self.pushButton_8.styleSheet() == "background-color : black":
            lista.append(1)
        else:
            lista.append(-1)
        if self.pushButton_9.styleSheet() == "background-color : black":
            lista.append(1)
        else:
            lista.append(-1)
        if self.pushButton_10.styleSheet() == "background-color : black":
            lista.append(1)
        else:
            lista.append(-1)
        if self.pushButton_11.styleSheet() == "background-color : black":
            lista.append(1)
        else:
            lista.append(-1)
        if self.pushButton_12.styleSheet() == "background-color : black":
            lista.append(1)
        else:
            lista.append(-1)
        if self.pushButton_13.styleSheet() == "background-color : black":
            lista.append(1)
        else:
            lista.append(-1)
        if self.pushButton_14.styleSheet() == "background-color : black":
            lista.append(1)
        else:
            lista.append(-1)
        if self.pushButton_15.styleSheet() == "background-color : black":
            lista.append(1)
        else:
            lista.append(-1)
        if self.pushButton_16.styleSheet() == "background-color : black":
            lista.append(1)
        else:
            lista.append(-1)
        if self.pushButton_17.styleSheet() == "background-color : black":
            lista.append(1)
        else:
            lista.append(-1)
        if self.pushButton_18.styleSheet() == "background-color : black":
            lista.append(1)
        else:
            lista.append(-1)
        if self.pushButton_19.styleSheet() == "background-color : black":
            lista.append(1)
        else:
            lista.append(-1)
        if self.pushButton_20.styleSheet() == "background-color : black":
            lista.append(1)
        else:
            lista.append(-1)
        if self.pushButton_21.styleSheet() == "background-color : black":
            lista.append(1)
        else:
            lista.append(-1)
        if self.pushButton_22.styleSheet() == "background-color : black":
            lista.append(1)
        else:
            lista.append(-1)
        if self.pushButton_23.styleSheet() == "background-color : black":
            lista.append(1)
        else:
            lista.append(-1)
        if self.pushButton_24.styleSheet() == "background-color : black":
            lista.append(1)
        else:
            lista.append(-1)
        if self.pushButton_25.styleSheet() == "background-color : black":
            lista.append(1)
        else:
            lista.append(-1)

        #lista-array
        listaR = np.array(lista).reshape(5,5)

        #lista-transpuesta
        #listaT = np.transpose(listaR)
        #self.lineEdit.setText(listaR.__str__())

        AT = np.transpose(A)
        ET = np.transpose(E)
        IT = np.transpose(I)
        OT = np.transpose(O)
        UT = np.transpose(U)

        T = (AT * A) + (ET * E) + (IT * I) + (OT * O) + (UT * U)
        #print(T)

        for i in range(5):
            T[i][i] = 0

        b = 0
        ej = 0
        while (b == 0):
            u0 = listaR
            u = u0 * T
            s = []

            for i in range(5):
                s.append([])
                for j in range(5):
                    if u[i][j] > 0:
                        #s[i] = 1
                        s[i].append(1)
                    elif u[i][j] < 0:
                        #s[i] = -1
                        s[i].append(-1)
                    elif u[i][j] == 0:
                        s[i].append(u[i][j])

            SR = np.array(s)
            cont = 0

            for i in range(5):
                for j in range(5):
                    if listaR[i][j] == SR[i][j]:
                        cont += 1

            if cont == 5:
                print("Se encontro estabilidad")
                b = 1
            else:
                listaR = SR

            ej += 1
            if ej == 50:
                b = 1

        #print(SR)
        Vps = np.sum(SR, axis=1)
        #Vpa = np.sum(A, axis=1)
        #Vpe = np.sum(E, axis=1)
        #Vpi = np.sum(I, axis=1)
        #Vpo = np.sum(O, axis=1)
        #Vpu = np.sum(U,axis=1)

        x = Vps
        y = [-3, -1, -1, 5, -1], [5, -1, 3, -3, 5], [5, -3, -3, -3, 5], [5, -1, -1, -1, 5], [-1, -1, -1, -1, 5]
        R = []
        d = []

        for i in range(len(y)):
            contador = 0
            for j in range(len(y[i])):
                contador += abs(x[j] - y[i][j])
            R.append(contador)
        #print(R)
        may = max(R)

        for i in range(len(y)):
            d.append((1 - R[i] / may) * 100)


        print(T)
        #print(d)

        letra = letras[d.index((max(d)))]
        self.lineEdit.setText(letra)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

