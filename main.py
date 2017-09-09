# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'suduku.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!
# import Suduku5
import createSudokuProblem
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import sqlite3

insA = 'INSERT INTO A VALUES(?)'
insB = 'INSERT INTO B VALUES(?)'
insC = 'INSERT INTO C VALUES(?)'


class Ui_MainWindow(object):
    def __init__(self):
        self.sudokulst = None
        self.mode = 1


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(530, 160, 210, 411))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(10)


        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        # MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        # MainWindow.setStatusBar(self.statusbar)
        self.actionguize = QtWidgets.QAction(MainWindow)
        self.actionguize.setObjectName("actionguize")
        self.actionguize.triggered.connect(lambda :QtWidgets.QMessageBox.information(self.centralwidget, "游戏规则",
        "    玩家需要根据9×9盘面上的已知数字，推理出所有剩余空格的数字，并满足每一行、每一列、每一个粗线宫内的数字均含1-9，不重复。"))

        self.actiontuichu = QtWidgets.QAction(MainWindow)
        self.actiontuichu.setObjectName("actiontuichu")
        self.actiontuichu.triggered.connect(QtWidgets.qApp.quit)
        self.menu.addAction(self.actionguize)
        self.menu.addAction(self.actiontuichu)
        self.menubar.addAction(self.menu.menuAction())


        for i in range(4):
            self.tableWidget.setColumnWidth(i, 50)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        for i in range(0, 10):
            self.tableWidget.setRowHeight(i, 38)
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setVerticalHeaderItem(i, item)
            item = QtWidgets.QTableWidgetItem()
            item.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
            self.tableWidget.setItem(i, 0, item)
            item = QtWidgets.QTableWidgetItem()
            item.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
            self.tableWidget.setItem(i, 1, item)
            item = QtWidgets.QTableWidgetItem()
            item.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
            self.tableWidget.setItem(i, 2, item)
            item = QtWidgets.QTableWidgetItem()
            item.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
            self.tableWidget.setItem(i, 3, item)

        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)


        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(60, 531, 108, 40))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.show_answer)

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(186, 531, 108, 40))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.restar)

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(312, 531, 108, 40))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(QtWidgets.qApp.quit)

        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(435, 200, 80, 40))
        self.pushButton_4.setObjectName("easy")
        self.pushButton_4.clicked.connect(self.change_to_easy)

        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(435, 280, 80, 40))
        self.pushButton_5.setObjectName("normal")
        self.pushButton_5.clicked.connect(self.change_to_normal)

        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(435, 360, 80, 40))
        self.pushButton_6.setObjectName("hard")
        self.pushButton_6.clicked.connect(self.change_to_hard)

        self.lineEditlst = []

        for i in range(9):
            for j in range(9):
                temp = QtWidgets.QLineEdit(self.centralwidget)
                self.lineEditlst.append(temp)
                temp.setGeometry(QtCore.QRect(60 + j * 40, 160 + i * 40, 40, 40))
                temp.setObjectName("lineEdit_" + str(i) + str(j))
                temp.setAlignment(QtCore.Qt.AlignCenter)
                temp.setFont(QtGui.QFont("微软雅黑", 12))
                temp.textChanged.connect(self.judge)
        # self.lineEditlst[1].setText(str(3))

            self.menubar = QtWidgets.QMenuBar(MainWindow)
        # self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        # self.menubar.setObjectName("menubar")
        # MainWindow.setMenuBar(self.menubar)
        # self.statusbar = QtWidgets.QStatusBar(MainWindow)
        # self.statusbar.setObjectName("statusbar")
        # MainWindow.setStatusBar(self.statusbar)

        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(310, 60, 180, 70))
        self.lcdNumber.setObjectName("lcdNumber")

        self.timer = QtCore.QTimer()
        self.timer.setInterval(1000)
        self.timer.start()
        self.timer.timeout.connect(self.next_second)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "显示答案"))
        self.pushButton_2.setText(_translate("MainWindow", "再来一局"))
        self.pushButton_3.setText(_translate("MainWindow", "退出"))
        self.pushButton_4.setText(_translate("MainWindow", "简单"))
        self.pushButton_5.setText(_translate("MainWindow", "中等"))
        self.pushButton_6.setText(_translate("MainWindow", "困难"))
        self.menu.setTitle(_translate("MainWindow", "帮助"))
        self.actionguize.setText(_translate("MainWindow", "游戏规则"))
        self.actiontuichu.setText(_translate("MainWindow", "退出"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "排名"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "简单"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "中等"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "困难"))
        for i in range(10):
            item = self.tableWidget.item(i, 0)
            item.setText(_translate("MainWindow", str(i+1)))

    def change_to_easy(self):
        self.mode = 1
        self.pushButton_4.setEnabled(False)
        self.pushButton_5.setEnabled(True)
        self.pushButton_6.setEnabled(True)
        createSudokuProblem.blockNum = 25
        self.restar()

    def change_to_normal(self):
        self.mode = 2
        self.pushButton_4.setEnabled(True)
        self.pushButton_5.setEnabled(False)
        self.pushButton_6.setEnabled(True)
        createSudokuProblem.blockNum = 35
        self.restar()

    def change_to_hard(self):
        self.mode = 3
        self.pushButton_4.setEnabled(True)
        self.pushButton_5.setEnabled(True)
        self.pushButton_6.setEnabled(False)
        createSudokuProblem.blockNum = 45
        self.restar()

    def print_number(self):
        self.sudokulst = createSudokuProblem.create()
        lst = self.sudokulst[0]
        for i in range(9):
            for j in range(9):
                self.lineEditlst[i * 9 + j].textChanged.disconnect(self.judge)
                if lst[i][j]:
                    self.lineEditlst[i * 9 + j].setText(str(lst[i][j]))
                    self.lineEditlst[i * 9 + j].setReadOnly(True)
                    if (i // 3 * 3 + j // 3) % 2 == 1:
                        self.lineEditlst[i * 9 + j].setStyleSheet("background-color:#eeeeee;color:black")
                    else:
                        self.lineEditlst[i * 9 + j].setStyleSheet("color:black")

                else:
                    self.lineEditlst[i * 9 + j].setText(None)
                    self.lineEditlst[i * 9 + j].setReadOnly(False)
                    if (i // 3 * 3 + j // 3) % 2 == 1:
                        self.lineEditlst[i * 9 + j].setStyleSheet("background-color:#eeeeee;color:blue")
                    else:
                        self.lineEditlst[i * 9 + j].setStyleSheet("color:blue")
                self.lineEditlst[i * 9 + j].textChanged.connect(self.judge)


    def restar(self):
        self.print_number()
        self.lcdNumber.display(0)
        self.timer.start()  # 需要清零
        self.reflash_range()


    def show_answer(self):
        self.timer.stop()
        for i in self.lineEditlst:
            i.textChanged.disconnect(self.judge)
        lst = self.sudokulst[1]
        for i in range(9):
            for j in range(9):
                if lst[i][j]:
                    self.lineEditlst[i*9+j].setText(str(lst[i][j]))
                else:
                    self.lineEditlst[i * 9 + j].setText(None)
        for i in self.lineEditlst:
            i.textChanged.connect(self.judge)


    def next_second(self):
        self.lcdNumber.display(self.lcdNumber.intValue() + 1)

    def judge(self):
        lst = self.sudokulst[1]
        for i in range(81):
            if self.sudokulst[0][i//9][i%9] == 0:#self.sudokulst[1][i][j] ==
                try:
                    t = int(self.lineEditlst[i].text())
                except:
                    t = -1
                if t != self.sudokulst[1][i//9][i%9]:
                    break
        else:
            # print("end")
            self.timer.stop()
            conn = sqlite3.connect('score.db')
            curs = conn.cursor()
            score = self.lcdNumber.intValue()
            if self.mode == 1:
                curs.execute(insA, (score,))
            elif self.mode == 2:
                curs.execute(insB, (score,))
            else:
                curs.execute(insC, (score,))
            curs.close()
            conn.commit()
            conn.close()
            QtWidgets.QMessageBox.information(self.centralwidget, "恭喜", "游戏完成！")
            self.reflash_range()


    def reflash_range(self):
        _translate = QtCore.QCoreApplication.translate
        conn = sqlite3.connect('score.db')
        curs = conn.cursor()

        curs.execute("select * from A order by score limit 10")
        lst = curs.fetchall()
        for i in range(len(lst)):
            item = self.tableWidget.item(i, 1)
            item.setText(_translate("MainWindow", str(lst[i][0])))

        curs.execute("select * from B order by score limit 10")
        lst = curs.fetchall()
        for i in range(len(lst)):
            item = self.tableWidget.item(i, 2)
            item.setText(_translate("MainWindow", str(lst[i][0])))

        curs.execute("select * from C order by score limit 10")
        lst = curs.fetchall()
        for i in range(len(lst)):
            item = self.tableWidget.item(i, 3)
            item.setText(_translate("MainWindow", str(lst[i][0])))


        curs.close()
        conn.close()



if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QWidget()
    ui = Ui_MainWindow()
    ui.setupUi(widget)
    widget.show()
    # time.sleep(2)

    ui.change_to_normal()
    # sudo = Suduku5.get_sudo(30)
    # show(sudo)

    sys.exit(app.exec_())