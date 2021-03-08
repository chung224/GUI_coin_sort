# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.15.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets, QtQuickWidgets
from PyQt5.QtWidgets import (QApplication, QMainWindow, QMessageBox,QDialog,QVBoxLayout, 
                             QDialogButtonBox,QPushButton, QGridLayout,QLineEdit,QWidget,
                             QLabel,QGroupBox,QCheckBox, QFileDialog)
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
import pyqtgraph as pg
pg.setConfigOption('background', 'k')
import sys

#==========================================================
coin_dict =  {"£2": 200,"£1": 100,"50p": 50,"20p": 20,"10p":10 }
coins_interface = ["£2","£1","50p","20p","10p"]
keys = [1,2,3,4,5,6]
settings = {"max_": 10000,"min_":0,"currency_":"GBX","currency_convert":1, "currency_list":["GBX","MGA","USD"]}
#==========================================================




#==========Grabbing live data on USD currencies============
#==========================================================
import pandas as pd
from datetime import datetime
start_date= str(datetime.today().strftime('%Y-%m-%d'))
'2021-01-26'
currency ="USDGBP"
currency_2 = "BTCGBP"
api_key = "C8aCRqjU_tDz--u6ZIZY"
start_date = "2019-10-01"
end_date= "2019-10-30"
format = "records"
fields = "ohlc"

df = pd.read_json("https://tm-marketdata.com/api/v1/pandasDF?currency="+currency+"&api_key="+api_key+"&start_date="+start_date+"&end_date="+end_date+"&format="+format+"&fields="+fields)
df = df.set_index("date")

x_axis = list(range(1,15))

df['5_day_MA'] =  df.close.rolling(5).mean()
df['5_day_volatility'] = df.close.rolling(5).std()
df = df.dropna()
y_axis = df['5_day_MA'].tolist()
y_axis = y_axis[:14]

df_2 = pd.read_json("https://tm-marketdata.com/api/v1/pandasDF?currency="+currency_2+"&api_key="+api_key+"&start_date="+start_date+"&end_date="+end_date+"&format="+format+"&fields="+fields)
df_2 = df_2.set_index("date")
df_2['5_day_MA'] =  df.close.rolling(5).mean()
df_2['5_day_volatility'] = df.close.rolling(5).std()
df_2 = df_2.dropna()
y_axis_2 = df_2['5_day_MA'].tolist()
y_axis_2 = y_axis_2[:14]

#=========================================================
#==========================================================


#=======Grabbing stock prices of Amazon and netflix========
#==========================================================
import yfinance as yf
data = yf.download("AMZN", start=start_date, end=end_date)

data_1_open = data["Open"].tolist()
data_1_open = data_1_open[:14]
data_1_high = data["High"].tolist()
data_1_high = data_1_high[:14]
data_1_low  = data["Low"].tolist()
data_1_low  = data_1_low[:14]

data = yf.download("NFLX", start=start_date, end=end_date)
data_2_open = data["Open"].tolist()
data_2_open = data_2_open[:14]
data_2_high = data["High"].tolist()
data_2_high = data_2_high[:14]
data_2_low = data["Low"].tolist()
data_2_low = data_2_low[:14]
#==========================================================
#==========================================================

#Neural network to read "bank note" after uploading an image of it of required size======================
#!!! Neural may take a while to train. if your computer is slow, 
#please delete this subsection from your code and ignore the
#currency converter button




#=========================================================================================================



class Ui_MainWindow(QWidget):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1091, 484)

        self.secondwindow = show_details()

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Coin Calculator Button
        self.b1 = QtWidgets.QPushButton(self.centralwidget)
        self.b1.setGeometry(QtCore.QRect(30, 90, 191, 32))
        self.b1.setObjectName("b1")
        self.b1.clicked.connect(self.clicked)

        # Multi Coin Calculator Button
        self.b2 = QtWidgets.QPushButton(self.centralwidget)
        self.b2.setGeometry(QtCore.QRect(30, 120, 191, 32))
        self.b2.setObjectName("b2")
        self.b2.clicked.connect(self.clicked2)
        
        # Print Coin List Button
        self.b3 = QtWidgets.QPushButton(self.centralwidget)
        self.b3.setGeometry(QtCore.QRect(30, 150, 191, 32))
        self.b3.setObjectName("b3")
        self.b3.clicked.connect(self.clicked3)
        
        # Set Details Button
        self.b4 = QtWidgets.QPushButton(self.centralwidget)
        self.b4.setGeometry(QtCore.QRect(30, 180, 191, 32))
        self.b4.setObjectName("b4")
        self.b4.clicked.connect(self.show_new_window)
        
        # Display Program Config. Button
        self.b5 = QtWidgets.QPushButton(self.centralwidget)
        self.b5.setGeometry(QtCore.QRect(30, 210, 191, 32))
        self.b5.setObjectName("b5")
        self.b5.clicked.connect(self.config_popup)

        # Currency Exchange Button
        self.b6 = QtWidgets.QPushButton(self.centralwidget)
        self.b6.setGeometry(QtCore.QRect(30, 240, 191, 32))
        self.b6.setObjectName("b6")
        self.b6.clicked.connect(self.neural_net_warning)
        # Need to add click event here

        # Quit the Program Button
        self.b7 = QtWidgets.QPushButton(self.centralwidget)
        self.b7.setGeometry(QtCore.QRect(30, 270, 191, 32))
        self.b7.setObjectName("b7")
        self.b7.clicked.connect(self.clicked7)

        # Company Name Label
        self.l1 = QtWidgets.QLabel(self.centralwidget)
        self.l1.setGeometry(QtCore.QRect(10, 10, 321, 31))
        self.l1.setFont(QtGui.QFont('Arial', 18))
        self.l1.setObjectName("l1")
        
        # Main Menu Label
        self.l2 = QtWidgets.QLabel(self.centralwidget)
        self.l2.setGeometry(QtCore.QRect(10, 50, 231, 41))
        self.l2.setFont(QtGui.QFont('Arial', 15))
        self.l2.setAlignment(QtCore.Qt.AlignCenter)
        self.l2.setObjectName("l2")

        # Large box on right
        self.quickWidget = QtQuickWidgets.QQuickWidget(self.centralwidget)
        self.quickWidget.setGeometry(QtCore.QRect(250, 50, 311, 371))
        self.quickWidget.setResizeMode(QtQuickWidgets.QQuickWidget.SizeRootObjectToView)
        self.quickWidget.setObjectName("quickWidget")

        # Label in box on right
        self.l3 = QtWidgets.QLabel(self.centralwidget)
        self.l3.setGeometry(QtCore.QRect(260, 60, 291, 351))
        self.l3.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.l3.setWordWrap(True)
        self.l3.setObjectName("label")
        
        # Top left graphics view box
        self.graphicsView = pg.PlotWidget(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(570, 10, 256, 201))
        self.graphicsView.setObjectName("graphicsView")
        self.graphicsView.addLegend(size=(10,30),offset=(-120,-80))
        self.graphicsView.plot(x_axis,data_1_open,name="Open",pen="y")
        self.graphicsView.plot(x_axis,data_1_high,name="High",pen="g")
        self.graphicsView.plot(x_axis,data_1_low,name="Low",pen = "r")
        self.graphicsView.setLabels(title='Amazon Shares - daily',left = "Stock price (£)",bottom = "days [most recent]")
        # Top right graphics view box
        self.graphicsView_2 = pg.PlotWidget(self.centralwidget)
        self.graphicsView_2.setGeometry(QtCore.QRect(830, 10, 256, 201))
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.graphicsView_2.addLegend(size=(10,30),offset=(-120,-80))
        self.graphicsView.addLegend(size=(10,30),offset=(-120,-80))
        self.graphicsView_2.plot(x_axis,data_2_open,name="Open",pen="y")
        self.graphicsView_2.plot(x_axis,data_2_high,name="High",pen="g")
        self.graphicsView_2.plot(x_axis,data_2_low,name="Low",pen = "r")
        self.graphicsView_2.setLabels(title='Netflix Shares - daily',left = "Stock price (£)", bottom = "days [most recent]")
        
        # Bottom left graphics view box
        self.graphicsView_3 = pg.PlotWidget(self.centralwidget)
        #self.graphicsView_3.addLegend(size=(10,30),offset=(70,10))
        self.graphicsView_3.setGeometry(QtCore.QRect(570, 221, 256, 201))
        self.graphicsView_3.setObjectName("graphicsView_3")
        self.graphicsView_3.plot(x_axis,y_axis,pen='r',name = "Change over time")
        self.graphicsView_3.setLabels(title="USD currency changes [days]",left="USD/GBP")
        
        # Bottom right graphics view box
        self.graphicsView_4 = pg.PlotWidget(self.centralwidget)
        self.graphicsView_4.setGeometry(QtCore.QRect(830, 221, 256, 201))
        self.graphicsView_4.setObjectName("graphicsView_4")
        self.graphicsView_4.plot(x_axis,y_axis_2, pen="b")
        self.graphicsView_4.setLabels(title="BTC currency changes [days]",left = "BTC/GBP")
        
        MainWindow.setCentralWidget(self.centralwidget)
        
        # Status bar
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Capstone Financial Services Ltd."))
        self.b1.setText(_translate("MainWindow", "Coin Calculator"))
        self.b2.setText(_translate("MainWindow", "Multi Coin Calculator"))
        self.b3.setText(_translate("MainWindow", "Print Coin List"))
        self.b4.setText(_translate("MainWindow", "Set Details"))
        self.b5.setText(_translate("MainWindow", "Display Program Config."))
        self.b6.setText(_translate("MainWindow", "Currency exchange - upload"))
        self.b7.setText(_translate("MainWindow", "Quit the Program"))
        self.l1.setText(_translate("MainWindow", "Capstone Financial Services Ltd."))
        self.l2.setText(_translate("MainWindow", "***Coin Sorter - Main Menu***"))
        self.l3.setText(_translate("MainWindow", "Welcome to Capstone Financial Services Ltd.  Please click on a button to navigate through the program."))
     

    # Buttons 1, 2, 3 and 6 currently call this function when clicked, changing the label in the box on right
    # Button 1 
    def clicked(self):
        text, okPressed = QtWidgets.QInputDialog.getText(None, "Coin Calculator","Please input the amount of pennies (GBX):" )   
        if okPressed:
            while True:
                try:
                    input_ = float(text)
                    if not(input_.is_integer()) == True:
                        self.l3.setText("Penny fractions do not exist. Please enter new input to try again")
                        break
                        
                    elif (input_ >=settings["min_"] and input_ <= settings["max_"]):
                        output_ = "Input: {}\n".format(text) 
                        print(coins_interface)
                        for i in coin_dict:
                            if coin_dict[i] != None:
                                sub_output = ( "Type: {} -  Number of coins: {} - Remainder: {} pence.\n".format(i , int(input_/coin_dict[i]),int(input_ % coin_dict[i])))
                                output_ = output_ + sub_output
                        self.l3.setText(output_)
                        break
                    else:
                        self.l3.setText("Input out of range. Please try again!")
                        break
                except:
                    self.l3.setText("invalid input. PLease try again!")
                    break
                
            
    # Button 2
    def clicked2(self):
        text, okPressed = QtWidgets.QInputDialog.getText(None, "Multi Coin Calculator","Please input the amount of pennies (GBX):" )   
        output_ = ""
        if okPressed:
            while True:
                try:
                    input_ = float(text)
                    remainder = input_
                    if not(input_.is_integer()) == True:
                        self.l3.setText("Penny fractions do not exist. Please enter new input to try again")
                        break
                    elif (input_ >=settings["min_"] and input_ <= settings["max_"]):
                        while not(input_.is_integer()):
                            self.l3.setText("Penny fractions do not exist. [Press enter to try again]")
                            break
                        output_ = "Input: {}\nUsing all coins (in order of importance), you will have:\n\n".format(text)
                        for i in coin_dict:
                            if coin_dict[i] != None:
                                output_ = output_ + ( "Type: {} -  Number of coins: {}\n".format(i , int(remainder/coin_dict[i])))
                                remainder = remainder % coin_dict[i]
                        output_ = output_ + ("\nYour remainder is: {} pence.".format(int(remainder)))
                        self.l3.setText(output_)
                    else:
                        self.l3.sexText("Input out of range. Please try again!")
                    break
                except:
                    self.l3.setText("Invalid input. Please try again!")
                    break
                    


    # Button 3
    def clicked3(self):
        output_ = "\n========== Coin list=========== \nThe *Current* coins used in this program are: \n"
        for i in coin_dict:
            if coin_dict[i] != None:
                output_ = output_ +  "{} \n".format(i)
        self.l3.setText(output_)

    # Button 7
    def clicked7(self):
        sys.exit(app.exec_())

    # Adjusts the size of l1 on click depending on the text changed to
    def update(self): # Call update method when button clicked
        self.l1.adjustSize()

    # Set Details / Button 4 pop up window - a dialogue box is better but need to find out how to do this
    def details_popup(self):
        self.window = QtWidgets.QMainWindow()
        self.window.show()
        self.window.resize(400, 400)
        self.window.setObjectName("Set Details")
        self.window.setWindowTitle(("Set Details"))
        
    def show_new_window(self):
        self.l3.setText("")
        self.w = show_details()
        self.w.show()
        
    def passingInformation(self):
        self.secondwindow.setText(self.l3.text())
        self.secondwindow.displayinfo()
        

    # Display Prog. Config / Button 5 pop up window
    def config_popup(self):
        msg = QMessageBox()
        msg.setWindowTitle("Program Configurations")
        msg.setText("Currency: {}\nMaximum coin limit: {}\nMinimum coin limit: {}".format(settings["currency_"],int(settings["max_"]),int(settings["min_"]))) # Change text to include configs.
        msg.setInformativeText("You can change the program configurations by clicking set details.")
        msg.setIcon(QMessageBox.Information) # Information icon 
        msg.setStandardButtons(QMessageBox.Ok)
        msg.buttonClicked.connect(self.popup_button)
        x = msg.exec_()    
        

    def popup_button(self, i):
        print(i.text())
    # Added this function as it logs which buttons are clicked in the terminal
    # May be useful for tracking the user inputs
    
    def neural_net_warning(self):
        msg = QMessageBox()
        msg.setWindowTitle("testing Neural Network with GUI")
        msg.setText("This button serves as a protype for neural network implementation in the future for bank note detection. Please upload a jpeg image of any kind to see if it works!")
        msg.setInformativeText("Warning - \n\n[1] - Although we use a previously trained model, Neural network training times may still be large depending on your laptop/PC's performance.\n\n[2] - Certain Python libraries are required\n\nPlease press ok to continue.Otherwise click cancel")
        msg.setIcon(QMessageBox.Information) # Information icon 
        neural_net_accept = QtGui.QPushButton("OK")
        neural_net_decline = QtGui.QPushButton("Cancel")
        msg.addButton(neural_net_accept, QtGui.QMessageBox.YesRole)
        msg.addButton(neural_net_decline, QtGui.QMessageBox.NoRole)
        #msg.setStandardButtons(QMessageBox.Ok)
        #msg.setStandardButtons(QMessageBox.Cancel)
        #msg.buttonClicked.connect(self.neuralnet_detect_banknote)
        neural_net_accept.clicked.connect(self.neuralnet_detect_banknote)
        x = msg.exec_()
        
        
    
    def neuralnet_detect_banknote(self):
        output_final = "==========Neural Network==========\n\n\nThe image you uploaded was found to be a:\n "
        image = QFileDialog.getOpenFileName(None, 'OpenFile', '', "Image file(*.jpg)")
        imagePath = image[0]
        try:
            from tensorflow.keras.preprocessing.image import load_img
            from tensorflow.keras.preprocessing.image import img_to_array
            from tensorflow.keras.applications.vgg16 import preprocess_input
            from tensorflow.keras.applications.vgg16 import decode_predictions
            from tensorflow.keras.applications.vgg16 import VGG16
            import tensorflow as tf

            gpus = tf.config.experimental.list_physical_devices('GPU')

            if gpus:
                    for gpu in gpus:
                        tf.config.experimental.set_memory_growth(gpu, True)
        except:
            self.l3.setText("\nError: \nRequired Libraries or GPU not availble")
        try:
            model = VGG16()
            image = load_img(imagePath, target_size=(224, 224))
            image = img_to_array(image)
            image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))
            image = preprocess_input(image)
            yhat = model.predict(image)
            label = decode_predictions(yhat)
            label = label[0][0]
            #sub_ = "test123\n{} with accuracy {}".format(label[1], label[2]*100)
            #self.l3.setText(output_final)
            self.l3.setText("\n\nThe neural detected your image to be a {}\n with percentage probability {:.2f}.".format(label[1],label[2]))
            
            
            
            
        except: 
            self.l3.setText("\nError: interuption during model training")
        



    

class show_details(QWidget):
    def __init__(self):
        super().__init__()
        self.create_grid_layout()
        windowLayout = QVBoxLayout()
        windowLayout.addWidget(self.horizontalGroupBox)
        self.setLayout(windowLayout)
        self.test123 = Ui_MainWindow()
        
        self.setLayout(windowLayout)
    
    def create_grid_layout(self):
        self.horizontalGroupBox = QGroupBox()
        layout = QGridLayout()
        layout.setColumnStretch(1, 4)
        layout.setColumnStretch(2, 4)
        
        self.input_currency = QLineEdit()
        self.input_max_coin = QLineEdit()
        self.input_min_coin = QLineEdit()
        self.confirm_settings = QPushButton("ok")
        self.two_quid = QCheckBox("£2")
        self.one_quid = QCheckBox("£1")
        self.fifty_p = QCheckBox("50p")
        self.twenty_p = QCheckBox("20p")
        self.ten_p = QCheckBox("10p")
        
        layout.addWidget(QLabel('Please set your configuration!'),0,0,1,1)
        layout.addWidget(QLabel('Currency'),1,0)
        layout.addWidget(self.input_currency,1,1)
        layout.addWidget(QLabel('Max coin input'),2,0)
        layout.addWidget(self.input_max_coin,2,1)
        layout.addWidget(QLabel("Min coin input"),3,0)
        layout.addWidget(self.input_min_coin,3,1)
        layout.addWidget(QLabel('Coins active'),4,0,1,1)
        layout.addWidget(self.two_quid,5,0)
        layout.addWidget(self.one_quid,6,0)
        layout.addWidget(self.fifty_p,7,0)
        layout.addWidget(self.twenty_p,8,0)
        layout.addWidget(self.ten_p,9,0)
        
        layout.addWidget(self.confirm_settings,10,1,1,1)
        
        self.horizontalGroupBox.setLayout(layout)
        
        self.confirm_settings.clicked.connect(self.change_settings)
        
    def change_settings(self):

        try:
            coin_dict["£2"] = 200
            coin_dict["£1"] = 100
            coin_dict["50p"] = 50
            coin_dict["20p"] = 20
            coin_dict["10p"] = 10 
            text_input_currency = (self.input_currency.text()).upper()
            text_maximum = float(self.input_max_coin.text())
            text_minimum = float(self.input_min_coin.text())
            if not(self.two_quid.isChecked()):
                coin_dict["£2"] = None
            if not(self.one_quid.isChecked()):
                coin_dict["£1"] = None
            if not(self.fifty_p.isChecked()):
                coin_dict["50p"] = None
            if not(self.twenty_p.isChecked()):
                coin_dict["20p"] = None
            if not(self.ten_p.isChecked()):
                coin_dict["10p"] = None
            if not(text_maximum.is_integer()) or not(text_minimum.is_integer()) :
                msg = QMessageBox()
                msg.setWindowTitle("Error")
                msg.setText("Error - coin fractions do not exist") # Change text to include configs.
                x = msg.exec_()
            elif text_input_currency not in settings["currency_list"]:
                msg = QMessageBox()
                msg.setWindowTitle("Error")
                msg.setText("Please enter one of the following currencies:\n [GBX] [USD] [MGA]") # Change text to include configs.
                x = msg.exec_()
            elif (text_minimum > text_maximum):
                print("hi")
                msg = QMessageBox()
                msg.setWindowTitle("Error")
                msg.setText("Contradiction in coin limits") # Change text to include configs.
                x = msg.exec_()
            else:
                settings["max_"] = text_maximum
                settings["min_"] = text_minimum
                settings["currency_"] = text_input_currency
                self.close()
        except:
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("Please enter input arguments!") # Change text to include configs.
            x = msg.exec_()



        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
