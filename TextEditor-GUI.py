from PyQt5 import QtCore, QtGui, QtWidgets
import win32clipboard,sys,os,win32print,win32api

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1220, 802)
        MainWindow.setStyleSheet("background: white;")
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.text = QtWidgets.QTextBrowser(self.centralwidget)
        self.text.setGeometry(QtCore.QRect(0, 0, 1221, 701))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        self.text.setFont(font)
        self.text.setReadOnly(False)
        self.text.setOpenLinks(False)
        self.text.setObjectName("text")

        self.statusBar = QtWidgets.QLabel(self.centralwidget)
        self.statusBar.setGeometry(QtCore.QRect(750, 710, 461, 41))
        font = QtGui.QFont()
        font.setFamily("Ink Free")
        font.setPointSize(10)
        self.statusBar.setFont(font)
        self.statusBar.setStyleSheet("*{\n"
        "border: 2px solid black;\n"
        "padding: 10px;\n"
            "}")
        self.statusBar.setAlignment(QtCore.Qt.AlignCenter)
        self.statusBar.setWordWrap(True)
        self.statusBar.setObjectName("statusBar")
        self.filename = QtWidgets.QLabel(self.centralwidget)
        self.filename.setGeometry(QtCore.QRect(0, 710, 731, 41))
        font = QtGui.QFont()
        font.setFamily("Ink Free")
        font.setPointSize(10)
        self.filename.setFont(font)
        self.filename.setStyleSheet("*{\n"
            "border: 2px solid black;\n"
            "padding: 10px;\n"
            "}")
        self.filename.setAlignment(QtCore.Qt.AlignCenter)
        self.filename.setObjectName("filename")
        self.filename.setText("Color: "+self.text.textColor().name())
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1220, 26))
        self.menubar.setObjectName("menubar")
        self.menu_File = QtWidgets.QMenu(self.menubar)
        self.menu_File.setObjectName("menu_File")
        self.menu_Run = QtWidgets.QMenu(self.menubar)
        self.menu_Run.setObjectName("menu_Run")
        MainWindow.setMenuBar(self.menubar)
        self.action_File_Name = QtWidgets.QAction(MainWindow)
        self.action_File_Name.setObjectName("action_File_Name")
        self.action_File_Name.triggered.connect(self.newFile)
        self.action_Open_File = QtWidgets.QAction(MainWindow)
        self.action_Open_File.setObjectName("action_Open_File")
        self.action_Open_File.setShortcut("Ctrl+O")
        self.action_Open_File.triggered.connect(self.openFile)
        self.action_Save_File = QtWidgets.QAction(MainWindow)
        self.action_Save_File.setObjectName("action_Save_File")
        self.action_Close = QtWidgets.QAction(MainWindow)
        self.action_Close.setObjectName("action_Close")
        self.action_Close.triggered.connect(self.exitApp)
        self.action_Run_File_in_Terminal = QtWidgets.QAction(MainWindow)
        self.runCpp = QtWidgets.QAction(MainWindow)
        self.runCpp.setText("Run C\C++")
        self.action_Run_File_in_Terminal.setObjectName("action_Run_File_in_Terminal")
        self.action_Print_File = QtWidgets.QAction(MainWindow)
        self.action_Print_File.setObjectName("action_Print_File")
        self.menu_File.addAction(self.action_File_Name)
        self.menu_File.addAction(self.action_Open_File)
        self.menu_File.addAction(self.action_Save_File)
        self.menu_File.addAction(self.action_Close)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.action_Print_File)
        self.menu_File.addSeparator()
        self.action_ChangeColor = QtWidgets.QAction(MainWindow)
        self.action_ChangeColor.triggered.connect(self.changeColor)
        self.action_ChangeColor.setText("Change Colour")
        self.menu_File.addAction(self.action_ChangeColor)
        self.action_snipet_py = QtWidgets.QAction(MainWindow)
        self.action_snipet_py.triggered.connect(self.snip_py)
        self.action_snipet_py.setText("Python Snipet: Main")
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.action_snipet_py)

        self.action_snipet_py_if = QtWidgets.QAction(MainWindow)
        self.action_snipet_py_if.setText("Python Snipet: If-Else")
        self.action_snipet_py_if.triggered.connect(self.snip_py_if)
        self.menu_File.addAction(self.action_snipet_py_if)

        self.action_snipet_py_whileLoop = QtWidgets.QAction(MainWindow)
        self.action_snipet_py_whileLoop.setText("Python Snipet: While Loop")
        self.action_snipet_py_whileLoop.triggered.connect(self.snip_py_while)
        self.menu_File.addAction(self.action_snipet_py_whileLoop)

        self.action_snipet_py_forLoop = QtWidgets.QAction(MainWindow)
        self.action_snipet_py_forLoop.setText("Python Snipet: For Loop")
        self.action_snipet_py_forLoop.triggered.connect(self.snip_py_for)
        self.menu_File.addAction(self.action_snipet_py_forLoop)

        self.action_snipet_py_fun = QtWidgets.QAction(MainWindow)
        self.action_snipet_py_fun.setText("Python Snipet: Fuction")
        self.action_snipet_py_fun.triggered.connect(self.snip_py_fun)
        self.menu_File.addAction(self.action_snipet_py_fun)

        self.action_snipet_py_class = QtWidgets.QAction(MainWindow)
        self.action_snipet_py_class.setText("Python Snipet: Class")
        self.action_snipet_py_class.triggered.connect(self.snip_py_class)
        self.menu_File.addAction(self.action_snipet_py_class)

        self.menu_File.addSeparator()
        self.action_snipet_c_main = QtWidgets.QAction(MainWindow)
        self.action_snipet_c_main.setText("C Snipet: Main")
        self.action_snipet_c_main.triggered.connect(self.snip_c_main)
        self.menu_File.addAction(self.action_snipet_c_main)

        self.menu_File.addSeparator()
        self.action_snipet_c_if = QtWidgets.QAction(MainWindow)
        self.action_snipet_c_if.setText("C\C++ Snipet: If-Else")
        self.action_snipet_c_if.triggered.connect(self.snip_c_if)
        self.menu_File.addAction(self.action_snipet_c_if)

        self.action_snipet_c_for = QtWidgets.QAction(MainWindow)
        self.action_snipet_c_for.setText("C\C++ Snipet: For Loop")
        self.action_snipet_c_for.triggered.connect(self.snip_c_for)
        self.menu_File.addAction(self.action_snipet_c_for)

        self.action_snipet_c_while = QtWidgets.QAction(MainWindow)
        self.action_snipet_c_while.setText("C\C++ Snipet: While Loop")
        self.action_snipet_c_while.triggered.connect(self.snip_c_while)
        self.menu_File.addAction(self.action_snipet_c_while)

        self.action_snipet_c_fun = QtWidgets.QAction(MainWindow)
        self.action_snipet_c_fun.setText("C\C++ Snipet: Funtion")
        self.action_snipet_c_fun.triggered.connect(self.snip_c_fun)
        self.menu_File.addAction(self.action_snipet_c_fun)

        self.menu_File.addSeparator()
        self.action_snipet_cpp_main = QtWidgets.QAction(MainWindow)
        self.action_snipet_cpp_main.setText("C++ Snipet: Main")
        self.action_snipet_cpp_main.triggered.connect(self.snip_cpp_main)
        self.menu_File.addAction(self.action_snipet_cpp_main)

        self.action_snipet_cpp_class = QtWidgets.QAction(MainWindow)
        self.action_snipet_cpp_class.setText("C++ Snipet: Class")
        self.action_snipet_cpp_class.triggered.connect(self.snip_cpp_class)
        self.menu_File.addAction(self.action_snipet_cpp_class)

        self.action_Print_File.triggered.connect(self.printFile)
        self.menu_Run.addAction(self.action_Run_File_in_Terminal)
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menu_Run.menuAction())
        self.menu_Run.addAction(self.runCpp)
        
        self.runCpp.triggered.connect(self.runCppFun)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def snip_go_boilerPlate(self):
        self.text.setText(self.text.toPlainText()+"\n"+'''package main

import "fmt"

func main() {
	
}
''')

    def snip_cpp_class(self):
        self.text.setText(self.text.toPlainText()+"\n"+'''class className{\n\t\n}''')

    def snip_cpp_main(self):
        self.text.setText(self.text.toPlainText()+"\n"+'''#include<iostream>\nint main(){\n\t\n}''')

    def snip_c_fun(self):
        self.text.setText(self.text.toPlainText()+"\n"+'''void funName(){\n\t\n}''')

    def snip_c_while(self):
        self.text.setText(self.text.toPlainText()+"\n"+'''#include<stdio.h>\nint main(){\n\tint i=0;\n\twhile(){\n\t\t\n\t}\n}''')

    def snip_c_for(self):
        self.text.setText(self.text.toPlainText()+"\n"+'''#include<stdio.h>\nint main(){\n\tint i=1;\n\tfor(i=1;i<=10;i++){\n\t\t\n\t}\n}''')

    def snip_c_if(self):
        self.text.setText(self.text.toPlainText()+"\n"+'''#include<stdio.h>\nint main(){\n\t\n\tif(){\n\t\t\n\t}\n}\nelse{\n\t\n}''')

    def snip_c_main(self):
        self.text.setText(self.text.toPlainText()+"\n"+'''#include<stdio.h>\nint main(){\n\t\n}''')

    def snip_py_class(self):
        self.text.setText(self.text.toPlainText()+"\n"+'''class ClassName:
            pass''')

    def snip_py_fun(self):
        self.text.setText(self.text.toPlainText()+"\n"+'''def funName():
            ''')

    def snip_py_if(self):
        self.text.setText(self.text.toPlainText()+"\n"+'''if(condition):
            pass\nelse:
            pass''')

    def snip_py_while(self):
        self.text.setText(self.text.toPlainText()+"\n"+'''while(condition):
            pass''')

    def snip_py_for(self):
        self.text.setText(self.text.toPlainText()+"\n"+'''for i in range(1,11):
            pass''')

    def snip_py(self):
        self.text.setText(self.text.toPlainText()+"\n"+'''if __name__ == "__main___":
            pass''')

    def changeColor(self):
        colorPicker = QtWidgets.QDialog()
        colorPicker.setGeometry(100, 100, 500, 400)
        color = QtWidgets.QColorDialog.getColor()
        label = QtWidgets.QLabel(self.centralwidget)
        colors  = {
            "#000000" : "Black",
            "#FFFFFF" : "White",
            "#ffff00" : "Yellow",
            "#ff0000" : "Red",
            "#00aaff" : "Light Blue",
            "#0000ff" : "Dark Blue",
            "#ff55ff" : "Light Pink",
            "#ff00ff" : "Dark Pink",
            "#aa5500" : "Brown",
            "#ffaa00" : "Orange",
            "#00ffff" : "Teal Blue"
        }
        try:
            c = colors[color.name()]
        except KeyError:
            c = color.name()
        self.filename.setText("Color: "+color.name())
        
        self.text.setTextColor(color)

    def printFile(self):
        data = self.text.toPlainText()
        f = open("C:\\Users\\sanja\\AppData\\Local\\Text_Editor\\print.txt","w")
        f.write(data)
        f.close()
        self.statusBar.setText("Printing to "+win32print.GetDefaultPrinter())
        try:
            win32api.ShellExecute(0,"print","C:\\Users\\sanja\\AppData\\Local\\Text_Editor\\print.txt",None,".",0)
        except Exception as e:
            print(e)

    def exitApp(self):
        exit(0)

    def newFile(self):
        self.text.setText("")

    def runCppFun(self):
        code = self.text.toPlainText()
        f = open("C:\\Users\\sanja\\AppData\\Local\\Text_Editor\\temp.cpp","w")
        f.write(code)
        f.close()
        os.system("g++ C:\\Users\\sanja\\AppData\\Local\\Text_Editor\\temp.cpp")
        os.system("a.exe | clip")
        win32clipboard.OpenClipboard()
        data  = win32clipboard.GetClipboardData()
        win32clipboard.CloseClipboard()
        d2 = QtWidgets.QDialog(None)
        d2.setWindowTitle("Output Window!")
        d2.setObjectName("Dialog")
        d2.resize(1000,500)
        # os.remove("a.exe")
        self.label = QtWidgets.QLabel(d2)
        self.label.resize(900,500)
        

        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(14)       
        self.label.setFont(font)
        self.label.setObjectName("run")
        self.label.setText(data)
        
        QtCore.QMetaObject.connectSlotsByName(d2)
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("Dialog", data))
        d2.exec()

    def saveFile(self):
        # filename = QtWidgets.QFileDialog.getOpenFileName(None, "Open " + "File Name" + " Data File", '.', 'All Text File (*.txt, *.py)')[0]
        
        dlg = QtWidgets.QDialog(None)
        dlg.setWindowTitle("File Name!")
        dlg.setObjectName("Dialog")
        dlg.resize(581, 373)
        self.fname = QtWidgets.QTextEdit(dlg)
        self.fname.setGeometry(QtCore.QRect(180, 170, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.fname.setFont(font)
        self.fname.setObjectName("fname")
        self.label = QtWidgets.QLabel(dlg)
        self.label.setGeometry(QtCore.QRect(230, 130, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.sub_btn = QtWidgets.QPushButton(dlg)
        self.sub_btn.setGeometry(QtCore.QRect(240, 240, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.sub_btn.setFont(font)
        self.sub_btn.setStyleSheet("background: rgb(0, 170, 255);")
        self.sub_btn.setObjectName("sub_btn")
        self.retranslateUi(dlg)
        QtCore.QMetaObject.connectSlotsByName(dlg)
        _translate = QtCore.QCoreApplication.translate
        dlg.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "File Name"))
        self.sub_btn.setText(_translate("Dialog", "Submit"))
        self.sub_btn.clicked.connect(self.clickSubBtn)
        dlg.exec()
        path = "C:\\Users\\sanja\\AppData\\Local\\Text_Editor\\"+self.fname.toPlainText()
        print(path)
        try:
            f = open(path,"w")
            f.write(self.text.toPlainText())
            f.close()
        except:
            pass
        
    def clickSubBtn(self):
        self.fileName = self.fname.toPlainText()

    def run(self):
        code = self.text.toPlainText()
        open("C:\\Users\\sanja\\AppData\\Local\\Text_Editor\\temp.txt","w").write(code)
        os.system("python C:\\Users\\sanja\\AppData\\Local\\Text_Editor\\temp.txt | clip")
        win32clipboard.OpenClipboard()
        data = win32clipboard.GetClipboardData()
        win32clipboard.CloseClipboard()
        d2 = QtWidgets.QDialog(None)
        d2.setWindowTitle("Output Window!")
        d2.setObjectName("Dialog")
        d2.resize(1000,500)
        
        self.label = QtWidgets.QLabel(d2)
        self.label.resize(900,500)
        

        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(14)       
        self.label.setFont(font)
        self.label.setObjectName("run")
        self.label.setText(data)
        
        QtCore.QMetaObject.connectSlotsByName(d2)
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("Dialog", data))
        d2.exec()

    def openFile(self):
        filename = QtWidgets.QFileDialog.getOpenFileName(None, "Open " + "File Name" + " Data File", '.', 'Text Files (*.txt), Python Files (*.py)')[0]

        f = open(filename,"r")
        self.text.setText(f.read())

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Text Editor"))
        MainWindow.setWindowIcon(QtGui.QIcon("icon.png"))
        self.statusBar.setText(_translate("MainWindow", "Status Bar"))
        self.filename.setText(_translate("MainWindow", "Colour: "+self.text.textColor().name()))
        self.menu_File.setTitle(_translate("MainWindow", "&File"))
        self.menu_Run.setTitle(_translate("MainWindow", "&Run"))
        self.action_File_Name.setText(_translate("MainWindow", "&New File"))
        self.action_File_Name.setShortcut("Ctrl+N")
        self.action_Open_File.setText(_translate("MainWindow", "&Open File"))
        self.action_Save_File.setText(_translate("MainWindow", "&Save File"))
        self.action_Save_File.setShortcut('Ctrl+S')
        self.action_Save_File.triggered.connect(self.saveFile)
        self.action_Close.setText(_translate("MainWindow", "&Close"))
        self.action_Close.setShortcut("Ctrl+Q")
        self.action_Run_File_in_Terminal.setText(_translate("MainWindow", "&Run Python"))
        
        self.action_Print_File.setText(_translate("MainWindow", "&Print File"))
        self.action_Print_File.setShortcut("Ctrl+P")
        self.action_Run_File_in_Terminal.triggered.connect(self.run)
        self.action_Run_File_in_Terminal.setShortcut("Ctrl+R")
        self.action_Run_File_in_Terminal.setShortcut("f9")
        self.runCpp.setShortcut("f10")
        self.action_ChangeColor.setShortcut("ctrl+alt+c")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
