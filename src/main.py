import sys
import math
import random as rd
import numpy as np
from collections import namedtuple
Pair = namedtuple('Pair', ['first', 'second'])

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QLabel, QGraphicsScene, QGraphicsView
from PyQt5.QtGui import QPixmap, QPen
from PyQt5.QtCore import Qt, QPoint

from main_gui import Ui_MainWindow
from DijkstraAlgorithm import Graph

class DijkstraGui(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # event
        self.btnGenerate.clicked.connect(self.btnGenerate_Clicked)
        self.btnFind.clicked.connect(self.btnFind_Clicked)
        self.cbxShowSteps.stateChanged.connect(self.cbxShowSteps_Clicked)
        self.lineEditPoint.textChanged.connect(self.lineEditPoint_TextChanged)
        self.lineEditLine.textChanged.connect(self.lineEditLine_TextChanged)

        self.countPoints = self.lineEditPoint.text()
        self.countLines = self.lineEditLine.text()

        self.RADIUS = 20
        self.RADIUS2 = self.RADIUS * 2
        self.RADIUS3 = self.RADIUS + 3
        self.SIZE = 150
        self.countPoint, self.countLine, self.countStep, self.maxStep = 0, 0, 0, 0
        self.newDistance, self.listSteps, self.listPath = [], [], []
        self.points = [QPoint(0, 0) for i in range(20)]
        self.listLine = [QPoint(0, 0) for i in range(400)]
        self.distance = np.empty((20, 20), dtype=object)
        self.lines = np.empty((20, 20), dtype=Pair)
        self.start, self.end = -1, -1
        self.isDone, self.isFounded = False, False
        self.chooseState = 0
        self.textChoose = ['vuongdq85', 'Choose point start...', 'Choose point end...']


        pen = QPen(Qt.black, 2)
        penStart = QPen(Qt.darkGreen, 4)
        penDest = QPen(Qt.darkRed, 4)

        pencil = QPen(Qt.red, 4)


        # draw canvas
        self.scene = QGraphicsScene()
        self.scene.addLine(400, 100, 100, 100, pencil)
        self.graphicsViewPaint.setScene(self.scene)

        #
        self.reset()
        self.generate()

    # func event
    def btnGenerate_Clicked(self):
        print("btnGenerate")
        print("Point: {0}".format(self.countPoints))
        print("Line: {0}".format(self.countLines))

        self.reset()
        ok = False

        try:
            self.countPoints = int(self.lineEditPoint.text())
            self.countLines = int(self.lineEditLine.text())
            if ((0 < self.countPoints and self.countPoints <= 20)
                 and (0 < self.countLines and self.countLines <= 380)):
                ok = True
        except Exception as ex:
            pass

        print(ok)

        if ok:
            self.generate()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Wrong amount of points")
            msg.setWindowTitle("Error")
            msg.exec_()


    def btnFind_Clicked(self):
        print("btnFind")

    def cbxShowSteps_Clicked(self, int):
        if (self.cbxShowSteps.isChecked()):
            print("cbxShowSteps Checked")
        else:
            print("cbxShowSteps unChecked")

    def lineEditPoint_TextChanged(self):
        self.countPoints = self.lineEditPoint.text()

    def lineEditLine_TextChanged(self):
        self.countLines = self.lineEditLine.text()

    def graphicsViewPaint_draw(self):
        self.scene.addEllipse(400, 100, 100, 100)
        self.graphicsViewPaint.setScene(self.scene)

    def generate(self):
        print('generate')
        
        array = np.zeros(20, dtype=np.int64)
        
        k = 0
        count = 20
        region = 0
        for i in range(0, int(self.countPoints)):
            for j in range(0, int(self.countPoints)):
                self.distance[i, j] = 0
                if (i != j):
                    self.listLine[k] = QPoint(i, j)
                    k = k + 1

            n = rd.randint(0, count-1)
            region = array[n]
            count = count - 1
            array[n] = array[count]
            p = self.randomInRegion(region)
            self.points[i] = p

        for i in range(0, int(self.countLines)):
            n = rd.randint(0, k)
            p = self.listLine[n]
            k = k - 1
            self.listLine[n] = self.listLine[k]
            self.distance[p.x()][p.y()] = self.calDistance(self.points[p.x()], self.points[p.y()])
            px1 = self.points[p.x()].x()
            px2 = self.points[p.y()].x()
            py1 = self.points[p.x()].y()
            py2 = self.points[p.y()].y()

            try:
                offsetX = (px2 - px1) * self.RADIUS3 / self.distance[p.x()][p.x()]
                offsetY = (py2 - py1) * self.RADIUS3 / self.distance[p.x()][p.x()]
            except ZeroDivisionError as e:
                pass
            finally:
                self.lines[p.x(), p.y()] = Pair(QPoint(px1 + offsetX, py1 + offsetY), QPoint(px2 - offsetX, py2 - offsetY))


        for i in range(0, int(self.countPoints)):
            for j in range(0, int(self.countPoints)):
                if self.distance[i, j] != 0:
                    self.scene.addLine(self.lines[i, j].first, self.lines[i, j].second)

        self.graphicsViewPaint.setScene(self.scene)


    def randomInRegion(self, region):
        minX = region % 5 * self.SIZE + self.RADIUS
        maxX = minX + self.SIZE - self.RADIUS2
        minY = region / 5 * self.SIZE + self.RADIUS
        maxY = minY + self.SIZE - self.RADIUS2
        return QPoint(rd.randint(minX, maxX), rd.randint(minY, maxY))

    def calDistance(self, p1, p2):
        x = p1.x() - p2.x()
        y = p1.y() - p2.y()
        return int(math.sqrt(x * x + y * y))

    def reset(self):
        self.start, self.end = -1, -1

        self.listPath = list()
        self.chooseState = 0
        self.lblStatus.setText(self.textChoose[self.chooseState])
        self.lblPointStart.setText('Point start: ')
        self.lblPointEnd.setText('Point end: ')
        self.lblSteps.setText('Steps: ')
        self.lblNodes.setText('Nodes: ')
       

        self.isFouded = False
        self.isDone = False


def main():
    app = QApplication(sys.argv)

    ui = DijkstraGui()
    ui.show()

    # Start the event loop
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
