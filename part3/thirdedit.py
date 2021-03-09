#In part 3, we combine everything we have done for the  previous programs and implement a Graphical user interface, 
#We will use PyQt5 to develop the GUI. It should be noted we implement new packages such as tensorflow for neural network implementation
#and the python -yfinance- library to grab stock price data

#It is noted that widgets reverse to components of the GUI. 


#Errors found and fixed with notification to user (GUI):
    #if user chooses to remove all coins - deal with this during calculation
    #if user sets the maximum to be smaller than the minimum (and vice verse with larger), deal with this
    #if user types a decimal for any coin inputs 
    #if the user types special keys for text or text for int (etc etc)
    #if the user types a key outside the desired range 
    #case sensitive inputs 
    #negative coin inputs


##########################################SECTION 1 ###################################################
#######################################################################################################
#In the first load all necessary modules and use an API to grab stock price data and currencies. 
#It should be noted the tensorflow library is optionally loaded in should the user choose to do so.
#a notifcation will be provided if the neural network + library was not loaded in


#==================Sub-section 1==========================
#==========================================================
#We load most of the necessary tools for the GUI
from PyQt5 import QtCore, QtGui, QtWidgets, QtQuickWidgets # we load all components to create components
from PyQt5.QtWidgets import (QApplication, QMainWindow, QMessageBox,QDialog,QVBoxLayout,  # here we load all components individually
                             QDialogButtonBox,QPushButton, QGridLayout,QLineEdit,QWidget, # For example QLabel refers to a text box
                             QLabel,QGroupBox,QCheckBox, QFileDialog) # QLine edit for example loads a textbox and allows users to edit
import pyqtgraph as pg # load package to create graphs in pyQt
pg.setConfigOption('background', 'k') #we set the background color of the graphs
import sys # load functions to manipulate different parts of the Python runtime environment

 
#================Sub-section 2=============================
#==========================================================
# we grab all the essential tools we will need.
coin_dict =  {"£2": 200,"£1": 100,"50p": 50,"20p": 20,"10p":10 }# create a dictionary for program to grab all the coins 
coins_interface = ["£2","£1","50p","20p","10p"]# this list is created inorder to dictionary keys efficiently
keys = [1,2,3,4,5,6]#this list is created for the main menu of the program. the program checks for the user input in this list.
settings = {"max_": 10000,"min_":0,"currency_":"GBX","currency_convert":1, "currency_list":["GBX","MGA","USD"]} # settings of program
#==========================================================


#================Sub-section 3=============================
#==========================================================
#we load all the necessary tools to grab stock price + currency data
import pandas as pd #load package to manipulate data obtained
currency ="USDGBP" #currency term to be added to URL [see below] to grab the conversion of USD to GBP
currency_2 = "BTCGBP"#Second currency term to be added to URL [see below] to grab the conversion of BTC[bitcoin] to GBP
api_key = "C8aCRqjU_tDz--u6ZIZY" #API key to grab data from server - limit per key is 1000 requests
start_date = "2019-01-01" # define start date to grab information of currency + stock price
end_date= "2019-10-30" # define end date to grab information of currency + stock price
format = "records" # format of the data
fields = "ohlc" #format of the data
x_axis = list(range(1,100)) #We define the items for the X-axis of the graphs here. range refers to add all numbers from x to x_2. 


#================Sub-section 4=============================
#==========================================================
#here we use the packages in sub section 3 and grab all the necessary data to create graphs
#we read define a URL using variables in Sub section 3 to ask program to grab data from this link. the data is initially in Json format
df = pd.read_json("https://tm-marketdata.com/api/v1/pandasDF?currency="+currency+"&api_key="+api_key+"&start_date="+start_date+"&end_date="+end_date+"&format="+format+"&fields="+fields)
df = df.set_index("date") #we ask user to set the column name
df['5_day_MA'] =  df.close.rolling(5).mean() # we compute the 5 day main average by grabbing previous 5 items for every variable and calculate mean
df['5_day_volatility'] = df.close.rolling(5).std() #calculate standard deviation using .std function
y_axis_vol = df['5_day_volatility'].tolist() #convert the column to list
y_axis_vol = y_axis_vol[:99] #We just keep the first 100 items 
df = df.dropna() # drop any NA values
y_axis = df['5_day_MA'].tolist() # convert json item to list
y_axis = y_axis[:99] #keep the first 100 items

#The exact same but for bitcoin data - we read define a URL using variables in Sub section 3 to ask program to grab data from this link. the data is initially in Json format
df_2 = pd.read_json("https://tm-marketdata.com/api/v1/pandasDF?currency="+currency_2+"&api_key="+api_key+"&start_date="+start_date+"&end_date="+end_date+"&format="+format+"&fields="+fields)
df_2 = df_2.set_index("date")#we ask user to set the column name
df_2['5_day_MA'] =  df.close.rolling(5).mean()# we compute the 5 day main average by grabbing previous 5 items for every variable and calculate mean
df_2['5_day_volatility'] = df.close.rolling(5).std()#calculate standard deviation using .std function
df_2 = df_2.dropna()#drop all NA values
y_axis_2 = df_2['5_day_MA'].tolist()#convert the column to list
y_axis_2 = y_axis_2[:99]#We just keep the first 100 items 
y_axis_2_vol = df_2['5_day_volatility'].tolist()#convert the column to list
y_axis_2_vol = y_axis_2_vol[:99]#We just keep the first 100 items 



#================Sub-section 5=============================
#==========================================================
#we import the yfinance module and grab stock price data of Amazon and Netflix
import yfinance as yf
data = yf.download("AMZN", start=start_date, end=end_date) #the function asks for the ticker code for stock, followed by the start + end date

data_1_open = data["Open"].tolist() #convert the column to list
data_1_open = data_1_open[:99]# we keep the first 100 items
data_1_high = data["High"].tolist() 
data_1_high = data_1_high[:99]
data_1_low  = data["Low"].tolist()
data_1_low  = data_1_low[:99]

data = yf.download("NFLX", start=start_date, end=end_date) # same as above, but ticker code NFLX to grab Netflix price data
data_2_open = data["Open"].tolist() #convert the column to list
data_2_open = data_2_open[:99]# we keep the first 100 items
data_2_high = data["High"].tolist()
data_2_high = data_2_high[:99]
data_2_low = data["Low"].tolist()
data_2_low = data_2_low[:99]
#==========================================================
#==========================================================



##########################################SECTION 2 ###################################################
#######################################################################################################
#this section essentially defines the design + functionality of the main window. 
#we first design + add all elements in the function setupUI (UI_mainwindow) where the buttons are also connected to alternative functions
#where we tell the program what to do upon button clicking/closing for example. 
#all of the functions within the main window are encapsulated within the class Ui_Mainwindow - it serves as a blue print.

#================Sub-section 1=============================
#==========================================================
#We set up the visulisation aspects aswell as connect all the buttons or interactive features to all the functions we 
#will define in sub-section 2 of Section 2
class Ui_MainWindow(QWidget): #define a class that takes components or widgets defined at the start if program
    def setupUi(self, MainWindow): #we define a function to setup the UI including the widget mainwindow. 
    #the self part refers to "make itself" --> I.E a function human can create a third leg using self.thirdleg
        MainWindow.setObjectName("MainWindow") # we set the object name of mainwindow to make it easier for later
        MainWindow.resize(1091, 484) #define window size

        self.secondwindow = show_details() #we defined another blueprint for a second window, we initialise it here within the main window

        self.centralwidget = QtWidgets.QWidget(MainWindow) # we add component mainwindow to start the building process
        self.centralwidget.setObjectName("centralwidget") #we set the object name for later reference

        # Coin Calculator Button
        self.b1 = QtWidgets.QPushButton(self.centralwidget) #we keep adding widgets to the parent widget -> main window
        self.b1.setGeometry(QtCore.QRect(30, 90, 191, 32)) #choose position of widget
        self.b1.setObjectName("b1") #we set the object name for later reference
        self.b1.clicked.connect(self.clicked) # we connect the button to the function named after the self.XXXX see the function below

        # Multi Coin Calculator Button
        self.b2 = QtWidgets.QPushButton(self.centralwidget) #add button widget
        self.b2.setGeometry(QtCore.QRect(30, 120, 191, 32)) #choose position of widget
        self.b2.setObjectName("b2") #we set the object name for later reference
        self.b2.clicked.connect(self.clicked2) # we connect the button to the function named after the self.XXXX see the function below
        
        # Print Coin List Button
        self.b3 = QtWidgets.QPushButton(self.centralwidget)#add button widget
        self.b3.setGeometry(QtCore.QRect(30, 150, 191, 32))#choose position of widget
        self.b3.setObjectName("b3") #we set the object name for later reference
        self.b3.clicked.connect(self.clicked3)# we connect the button to the function named after the self.XXXX see the function below
        
        # Set Details Button
        self.b4 = QtWidgets.QPushButton(self.centralwidget)#add button widget
        self.b4.setGeometry(QtCore.QRect(30, 180, 191, 32))#choose position of widget
        self.b4.setObjectName("b4") #we set the object name for later reference
        self.b4.clicked.connect(self.show_new_window)# we connect the button to the function named after the self.XXXX see the function below
        
        # Display Program Config. Button
        self.b5 = QtWidgets.QPushButton(self.centralwidget)#add button widget
        self.b5.setGeometry(QtCore.QRect(30, 210, 191, 32))#choose position of widget
        self.b5.setObjectName("b5") #we set the object name for later reference
        self.b5.clicked.connect(self.config_popup)# we connect the button to the function named after the self.XXXX see the function below

        # Currency Exchange Button
        self.b6 = QtWidgets.QPushButton(self.centralwidget)#add button widget
        self.b6.setGeometry(QtCore.QRect(30, 240, 191, 32))#choose position of widget
        self.b6.setObjectName("b6") #we set the object name for later reference
        self.b6.clicked.connect(self.neural_net_warning)# we connect the button to the function named after the self.XXXX see the function below
        # Need to add click event here

        # Quit the Program Button
        self.b7 = QtWidgets.QPushButton(self.centralwidget)#add button widget
        self.b7.setGeometry(QtCore.QRect(30, 270, 191, 32))#choose position of widget
        self.b7.setObjectName("b7") #we set the object name for later reference
        self.b7.clicked.connect(self.clicked7)# we connect the button to the function named after the self.XXXX see the function below

        # Company Name Label
        self.l1 = QtWidgets.QLabel(self.centralwidget) # add text box
        self.l1.setGeometry(QtCore.QRect(10, 10, 321, 31))#choose position of widget
        self.l1.setFont(QtGui.QFont('Arial', 18))
        self.l1.setObjectName("l1") #we set the object name for later reference
        
        # Main Menu Label
        self.l2 = QtWidgets.QLabel(self.centralwidget) # add text box
        self.l2.setGeometry(QtCore.QRect(10, 50, 231, 41))#choose position of widget
        self.l2.setFont(QtGui.QFont('Arial', 15))
        self.l2.setAlignment(QtCore.Qt.AlignCenter)
        self.l2.setObjectName("l2") #we set the object name for later reference

        # Large box on right
        self.quickWidget = QtQuickWidgets.QQuickWidget(self.centralwidget) # we add a box for the output
        self.quickWidget.setGeometry(QtCore.QRect(250, 50, 311, 371))#choose position of widget
        self.quickWidget.setResizeMode(QtQuickWidgets.QQuickWidget.SizeRootObjectToView) # resize the object to users view
        self.quickWidget.setObjectName("quickWidget") #we set the object name for later reference

        # Label in box on right
        self.l3 = QtWidgets.QLabel(self.centralwidget)
        self.l3.setGeometry(QtCore.QRect(260, 60, 291, 351))#choose position of widget
        self.l3.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop) # align the widget within center and top
        self.l3.setWordWrap(True)
        self.l3.setObjectName("label") #we set the object name for later reference
        
        # Top left graphics view box
        self.graphicsView = pg.PlotWidget(self.centralwidget)#we add a nd graphics box
        self.graphicsView.setGeometry(QtCore.QRect(570, 10, 256, 201))#choose position of widget
        self.graphicsView.setObjectName("graphicsView")#we set the object name for later reference
        self.graphicsView.addLegend(size=(10,30),offset=(-120,-80)) #we add a legend and choose a position offset
        self.graphicsView.plot(x_axis,data_1_open,name="Open",pen="y")#we add lines, the name is for the legend 
        self.graphicsView.plot(x_axis,data_1_high,name="High",pen="g")# the pen value refers to the color
        self.graphicsView.plot(x_axis,data_1_low,name="Low",pen = "r")# x and y values are self explanatory
        self.graphicsView.setLabels(title='Amazon Shares - daily',left = "Stock price (£)",bottom = "days [most recent]")
        # Top right graphics view box
        self.graphicsView_2 = pg.PlotWidget(self.centralwidget) #we add a 2nd graphics box
        self.graphicsView_2.setGeometry(QtCore.QRect(830, 10, 256, 201))#choose position of widget
        self.graphicsView_2.setObjectName("graphicsView_2")#we set the object name for later reference
        self.graphicsView_2.addLegend(size=(10,30),offset=(-120,-80)) #we add a legend and choose a position offset
        self.graphicsView_2.plot(x_axis,data_2_open,name="Open",pen="y") #we add lines, the name is for the legend 
        self.graphicsView_2.plot(x_axis,data_2_high,name="High",pen="g") # the pen value refers to the color
        self.graphicsView_2.plot(x_axis,data_2_low,name="Low",pen = "r") # x and y values are self explanatory
        self.graphicsView_2.setLabels(title='Netflix Shares - daily',left = "Stock price (£)", bottom = "days [most recent]")
        
        # Bottom left graphics view box
        self.graphicsView_3 = pg.PlotWidget(self.centralwidget) #we add a 3rd graphics box
        #self.graphicsView_3.addLegend(size=(10,30),offset=(70,10))
        self.graphicsView_3.setGeometry(QtCore.QRect(570, 221, 256, 201))#choose position of widget
        self.graphicsView_3.setObjectName("graphicsView_3")#we set the object name for later reference
        self.graphicsView_3.addLegend(size=(10,30),offset=(80,-120)) #we add a legend and choose a position offset
        self.graphicsView_3.plot(x_axis,y_axis,pen='g',name = "5 day MA")
        self.graphicsView_3.setLabels(title="USD currency changes [days]",left="USD/GBP",bottom = "days [most recent]")
        
        # Bottom right graphics view box
        self.graphicsView_4 = pg.PlotWidget(self.centralwidget) #we add a 4th graphics box
        self.graphicsView_4.setGeometry(QtCore.QRect(830, 221, 256, 201))#choose position of widget
        self.graphicsView_4.setObjectName("graphicsView_4")#we set the object name for later reference
        self.graphicsView_4.addLegend(size=(10,30),offset=(80,-120)) #we add a legend and choose a position offset
        self.graphicsView_4.plot(x_axis,y_axis_2, pen="g",name="5 day MA")
        self.graphicsView_4.setLabels(title="BTC currency changes [days]",left = "BTC/GBP",bottom = "days [most recent]")
        
        MainWindow.setCentralWidget(self.centralwidget) #after adding all widgets to the central widget, we add it to main window
        
        # Status bar
        self.statusbar = QtWidgets.QStatusBar(MainWindow) # add status bar widget
        self.statusbar.setObjectName("statusbar")# set name
        MainWindow.setStatusBar(self.statusbar) # add to main window

        self.retranslateUi(MainWindow) # function to change the names in the GUI
        QtCore.QMetaObject.connectSlotsByName(MainWindow) 
        
#================Sub-section 2=============================
#==========================================================
#This subsection assigns all the etext to the widgets such as labels and widgets defined above.

    def retranslateUi(self, MainWindow): #define function to assign names according to widget
        _translate = QtCore.QCoreApplication.translate # define function as variable to translate below
        MainWindow.setWindowTitle(_translate("MainWindow", "Capstone Financial Services.")) #set window title
        self.b1.setText(_translate("MainWindow", "Coin Calculator"))
        self.b2.setText(_translate("MainWindow", "Multi Coin Calculator"))# we assign all names according to the widget
        self.b3.setText(_translate("MainWindow", "Print Coin List")) # example button3 or b3, is relabelled to Print coin list
        self.b4.setText(_translate("MainWindow", "Set Details"))
        self.b5.setText(_translate("MainWindow", "Display Program Config."))
        self.b6.setText(_translate("MainWindow", "Currency upload"))
        self.b7.setText(_translate("MainWindow", "Quit the Program"))
        self.l1.setText(_translate("MainWindow", "Capstone Financial Services"))
        self.l2.setText(_translate("MainWindow", "***Coin Sorter - Main Menu***"))
        self.l3.setText(_translate("MainWindow", "Welcome to Capstone Financial Services. Please click on a button to navigate through the program.\n\nSee right for interactive graphs"))
     

##########################################SECTION 2 ###################################################
#######################################################################################################
#this section defines all the interactivity of the mainwindow after designing all the widgets.
#these functions were called above using functions such as -.connect.clicked(self.XXXX)-

#================Sub-section 1=============================
#==========================================================
#we seperate the first 3 functions into the first subsection as it's the most similar to part 1 + 2 of this project

    def clicked(self): # defines the function for the first button b1. it defines the coin calculator as previously seen
        text, okPressed = QtWidgets.QInputDialog.getText(None, "Coin Calculator","Please input the amount of pennies (GBX):" )   
        #above we add an input text, as well as an ok button. According to what the text says, conditions will arise below.
        if okPressed: # if OK button is pressed
            while True: # keep calling this loop until we break out
                try: # Try this block of code, if an error occurs, go to block of code in -except-
                    input_ = float(text) #convert input to a float variable.
                    if not(input_.is_integer()) == True: # if the float variable is not an integer
                        self.l3.setText("Penny fractions do not exist. Please enter new input to try again")
                        #display an error to user in the output box if a decimal detected
                        break # we break the function to stop the white true loop
                        
                    elif (input_ >=settings["min_"] and input_ <= settings["max_"]): # if the input is an integer, we check another condition
                    #this condition checks if input is within the range of max and min coin settings
                        output_ = "Input: {}\n".format(text)  #the print input to user if succesful 
                        for i in coin_dict: # for all items in the dictionary defined at start
                            if coin_dict[i] != None: # if the items in the dictionary are not equal to None (see later in settings)
                                sub_output = ( "Type: {} -  Number of coins: {} - Remainder: {} pence.\n".format(i , int(input_/coin_dict[i]),int(input_ % coin_dict[i])))
                                #above, we define sub outputs that gets keeps getting added as we go through the loop
                                output_ = output_ + sub_output 
                        self.l3.setText(output_) # after adding all the strings we output this to the text box
                        break # break loop and continue
                    else: # if the input is out of range
                        self.l3.setText("Input out of range. Please try again!") # notify user and break the white true loop
                        break
                except: # if an error occurs in the program
                    self.l3.setText("invalid input. PLease try again!") # the user has put a weird output. notify user
                    break # break loop
                
            
    # Button 2
    def clicked2(self): # defines the function for the second button b2. it defines the Multi-coin calculator as previously seen
        text, okPressed = QtWidgets.QInputDialog.getText(None, "Multi Coin Calculator","Please input the amount of pennies (GBX):" )   
        #above we add an input text, as well as an ok button. According to what the text says, conditions will arise below.
        output_ = "" # define an empty string to print stuff later
        if okPressed: # if OK button is pressed
            while True: # keep calling this loop until we break out
                try: # Try this block of code, if an error occurs, go to block of code in -except-
                    input_ = float(text) #convert input to a float variable.
                    remainder = input_ # add a remainder variable to calculate the remainder this will keep getting updated as we go through all coins
                    if not(input_.is_integer()) == True: # if the float variable is not an integer
                        self.l3.setText("Penny fractions do not exist. Please enter new input to try again")
                        #display an error to user in the output box if a decimal detected
                        break # we break the function to stop the white true loop
                    elif (input_ >=settings["min_"] and input_ <= settings["max_"]): # if the input is an integer, we check another condition
                    #this condition checks if input is within the range of max and min coin settings
                        while not(input_.is_integer()):  # if the float variable is not an integer
                            self.l3.setText("Penny fractions do not exist. [Press enter to try again]") #display an error to user in the output box if a decimal detected
                            break # break the white True loop
                        output_ = "Input: {}\nUsing all coins (in order of importance), you will have:\n\n".format(text) # print first output
                        for i in coin_dict: # for item in list we do calcualtions and update the remainder veriable
                            if coin_dict[i] != None: # if the items in the dictionary are not equal to None (see later in settings)
                                output_ = output_ + ( "Type: {} -  Number of coins: {}\n".format(i , int(remainder/coin_dict[i])))
                                #above we do calcualtions, convert to string and add it to the output variable for later showing in text box 
                                #after the loop
                                remainder = remainder % coin_dict[i] # going through each item in list, we update the remainder
                        output_ = output_ + ("\nYour remainder is: {} pence.".format(int(remainder))) #after final remainder we add this to string
                        self.l3.setText(output_) # send output to text box
                    else: # if the input is out of range....
                        self.l3.sexText("Input out of range. Please try again!") # display error
                    break#break loop
                except: # if error in console
                    self.l3.setText("Invalid input. Please try again!") #notify user of error
                    break # break loop
                    

    # Button 3
    def clicked3(self): # defines the function to print all items in the coin list. This is updated if the user changes the coin list
        output_ = "\n========== Coin list=========== \nThe *Current* coins used in this program are: \n" # print menu banner to user
        for i in coin_dict: # if item in the coin_dictionary
            if coin_dict[i] != None: # if the items in the dictionary are not equal to None (see later in settings)
                output_ = output_ +  "{} \n".format(i) # we add the coin item to variable and send it
        self.l3.setText(output_) # we final string to output box in GUI

#================Sub-section 2=============================
#==========================================================
#Apart from the first function in this sub section, all of them emphasise the nature of notificaitons in the GUI. 

    # Button 7
    def clicked7(self):# defines the function exits the GUI if the quit button is pressed
        sys.exit(app.exec_()) # sys function to exit the applicaiton

    # Adjusts the size of l1 on click depending on the text changed to
    def update(self): # Call update method when button clicked
        self.l1.adjustSize() #updates the size of widgetl1
      
    def show_new_window(self): # #define a function upon clicking the button defined above, a second window will appear see blueprint later
        self.l3.setText("") #we empty the output text
        self.w = show_details() # we load the second window if function called
        self.w.show() # we intiate the second window
        
    def passingInformation(self): # we pass information from the second window to the first
        self.secondwindow.setText(self.l3.text()) # assign text to output
        self.secondwindow.displayinfo() 
        

    # Display Prog. Config / Button 5 pop up window
    def config_popup(self): # this function displays a window of current configurations loaded from the list + dictioanary at the start of the program
        msg = QMessageBox() # load the window
        msg.setWindowTitle("Program Configurations") # set title of window
        #below - we prnt the configurations such as max/min and currency in the window
        msg.setText("Currency: {}\nMaximum coin limit: {}\nMinimum coin limit: {}".format(settings["currency_"],int(settings["max_"]),int(settings["min_"]))) # Change text to include configs.
        msg.setInformativeText("You can change the program configurations by clicking set details.")
        #above provides alternative text as a tip to the user
        msg.setIcon(QMessageBox.Information) # Information icon 
        msg.setStandardButtons(QMessageBox.Ok) # add an ok button
        msg.buttonClicked.connect(self.popup_button) #connect it to the function below
        x = msg.exec_()    # this line is needed for the widget to show upon execution
        

    def popup_button(self, i):
        print(i.text())
    # Added this function as it logs which buttons are clicked in the terminal
    # May be useful for tracking the user inputs
    
    
    
#================Sub-section 3=============================
#==========================================================   
#this section defines the neural network implementation for future work. the user can still update a random image and try it out
#images such as mugs, cars, animals can be tested.
#the first section displays a message box displaying a warning.
#if the user presses OK, the function will call the second one and neural network implementation starts 
    
    
    def neural_net_warning(self): # 
        msg = QMessageBox() # load message window
        msg.setWindowTitle("testing Neural Network with GUI") # add window title
        #below - set information
        msg.setText("This button serves as a protype for neural network implementation in the future for bank note detection. Please upload a jpeg image of any kind to see if it works!")
        #below - informative text
        msg.setInformativeText("Warning - \n\n[1] - Although we use a previously trained model, Neural network training times may still be large depending on your laptop/PC's performance.\n\n[2] - Certain Python libraries are required\n\nPlease press ok to continue.Otherwise click cancel")
        msg.setIcon(QMessageBox.Information) # Information icon 
        neural_net_accept = QtGui.QPushButton("OK") #add ok button and assign variable
        neural_net_decline = QtGui.QPushButton("Cancel") # add cancel button
        msg.addButton(neural_net_accept, QtGui.QMessageBox.YesRole)
        msg.addButton(neural_net_decline, QtGui.QMessageBox.NoRole)
        #msg.setStandardButtons(QMessageBox.Ok)
        #msg.setStandardButtons(QMessageBox.Cancel)
        #msg.buttonClicked.connect(self.neuralnet_detect_banknote)
        neural_net_accept.clicked.connect(self.neuralnet_detect_banknote) # if we click ok, we go to the second function
        x = msg.exec_() # this line is needed for the widget to show upon execution
        
        
    
    def neuralnet_detect_banknote(self):
        image = QFileDialog.getOpenFileName(None, 'OpenFile', '', "Image file(*.jpg)") # upon pressing OK above, a window is shown
        #where a user can upload an image
        imagePath = image[0] # we assign the variable imagePath to the file directory location string
        try: # we attempt to load packages, otherwise an error will be displayed inthe output text box
            from tensorflow.keras.preprocessing.image import load_img # load all required tensorflow packages
            from tensorflow.keras.preprocessing.image import img_to_array
            from tensorflow.keras.applications.vgg16 import preprocess_input
            from tensorflow.keras.applications.vgg16 import decode_predictions
            from tensorflow.keras.applications.vgg16 import VGG16
            import tensorflow as tf

            gpus = tf.config.experimental.list_physical_devices('GPU') # we list all the devices for calculations

            if gpus: # if a GPU is detected
                    for gpu in gpus: # we use GPU for training
                        tf.config.experimental.set_memory_growth(gpu, True)
        except:#if error occurs in detecting a GPU or loading package
            self.l3.setText("\nError: \nRequired Libraries or GPU not availble") #display error
        try: # attempt to load the model.
            model = VGG16() # load the VGG16 pretained model
            image = load_img(imagePath, target_size=(224, 224)) # we reshape the image loaded to take 224 by 224 pixels of RGB 
            image = img_to_array(image) # covnert image to array with 3 channels
            image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2])) #assign dimentions
            image = preprocess_input(image) # preprocess image
            yhat = model.predict(image) # classify the image using more than 1000 classes. we load the image
            #using the fine directory string 
            label = decode_predictions(yhat) # grab the list that has the label and precentage detection
            label = label[0][0] # grab score
            self.l3.setText("\n\n==========Neural Network==========\n\nThe neural detected your image to be a {}\n with highest score of {:.2f}.".format(label[1],label[2]))
            
            
            
            
        except: #if model load unsuccesful run this block
            self.l3.setText("\nError: interuption during model training") # display error to output text box
        

##########################################SECTION 3 ###################################################
#######################################################################################################
#In this final section we define the blueprint for the second window before executing everything.

#================Sub-section 1=============================
#==========================================================
#In this subsection we define a popup of class show details. This section mainly focuses on the design aspects.
#in sub section 2 we work on teh functionality using functions  
    

class show_details(QWidget): # define the function that shows details and allows user to update
    def __init__(self): # initialiseand create own variables to itself
        super().__init__() #grab information from parent modules
        self.create_grid_layout() # add a grid layout to assign widgets to
        windowLayout = QVBoxLayout() # add vertical box layout
        windowLayout.addWidget(self.horizontalGroupBox) #add group box widget
        self.setLayout(windowLayout) # set the QVlayout
        self.test123 = Ui_MainWindow() # add connectivity to mainwindow
        
        self.setLayout(windowLayout) # add QVboxlayout
    
    def create_grid_layout(self): # function that adds widgets to different parts of the grid
        self.horizontalGroupBox = QGroupBox() # add group box
        layout = QGridLayout() # define layout
        layout.setColumnStretch(1, 4) # define size of the columns
        layout.setColumnStretch(2, 4) 
        
        self.input_currency = QLineEdit()#define all the widgets here add input box
        self.input_max_coin = QLineEdit()#add input box
        self.input_min_coin = QLineEdit()#add input box
        self.confirm_settings = QPushButton("ok")#add button
        self.two_quid = QCheckBox("£2") #add checkbox
        self.one_quid = QCheckBox("£1")#add checkbox
        self.fifty_p = QCheckBox("50p")#add checkbox
        self.twenty_p = QCheckBox("20p")#add checkbox
        self.ten_p = QCheckBox("10p")#add checkbox
        
        layout.addWidget(QLabel('Please set your configuration!'),0,0,1,1) # the four numbers refers to the [x,y] position and the size 
        #at which the widgets span i.e (0,0,1,1) starts at [x,y] and is of size [1,1] horizontally and vertically
        layout.addWidget(QLabel('Currency'),1,0) #add label
        layout.addWidget(self.input_currency,1,1)
        layout.addWidget(QLabel('Max coin input'),2,0) #add label
        layout.addWidget(self.input_max_coin,2,1)
        layout.addWidget(QLabel("Min coin input"),3,0) #add label
        layout.addWidget(self.input_min_coin,3,1)
        layout.addWidget(QLabel('Coins active'),4,0,1,1) #add label
        layout.addWidget(self.two_quid,5,0) #add the check boxes to positions
        layout.addWidget(self.one_quid,6,0)#add the check boxes to positions
        layout.addWidget(self.fifty_p,7,0)#add the check boxes to positions
        layout.addWidget(self.twenty_p,8,0)#add the check boxes to positions
        layout.addWidget(self.ten_p,9,0)#add the check boxes to positions
        
        layout.addWidget(self.confirm_settings,10,1,1,1) # add an ok button
        
        self.horizontalGroupBox.setLayout(layout) #set layout
        
        self.confirm_settings.clicked.connect(self.change_settings) #upon pressing ok, we change all the variables of the 
        #settings dictionary according to the function below
        
#================Sub-section 2=============================
#==========================================================     
#we develop a function, if called adjust settings according to dictionary + list defined at start of program    
        
    def change_settings(self): # define function

        try:#try this block of code else go to the except block
            temp = 0 # define temp variable
            coin_dict["£2"] = 200 #define items according to keys
            coin_dict["£1"] = 100
            coin_dict["50p"] = 50#each of these refer to the number of pennies
            coin_dict["20p"] = 20
            coin_dict["10p"] = 10 
            text_input_currency = (self.input_currency.text()).upper() # convert input to capitals 
            text_maximum = float(self.input_max_coin.text()) # convert coin inputt from string to float
            text_minimum = float(self.input_min_coin.text())# convert coin inputt from string to float
            if not(self.two_quid.isChecked()): # if the user has  not  checked the coin, we assign the item of the coin key to type None 
                coin_dict["£2"] = None
            if not(self.one_quid.isChecked()): # if the user has  not  checked the coin, we assign the item of the coin key to type None 
                coin_dict["£1"] = None
            if not(self.fifty_p.isChecked()):# if the user has  not  checked the coin, we assign the item of the coin key to type None 
                coin_dict["50p"] = None
            if not(self.twenty_p.isChecked()):# if the user has  not  checked the coin, we assign the item of the coin key to type None 
                coin_dict["20p"] = None
            if not(self.ten_p.isChecked()):# if the user has  not  checked the coin, we assign the item of the coin key to type None 
                coin_dict["10p"] = None
            for i in coin_dict:
                if coin_dict[i] == None:# if the user has  not  checked the coin, we assign the item of the coin key to type None 
                    temp +=1 # we add 1 to temp, this condition checks if no coins are chosen by counting None values
            if not(text_maximum.is_integer()) or not(text_minimum.is_integer()) : # we check if the input is not an integer
                msg = QMessageBox() # we show a message box
                msg.setWindowTitle("Error") # set window title
                msg.setText("Error - coin fractions do not exist") # Change text to include configs.
                x = msg.exec_()#need this to execute window
            elif text_input_currency not in settings["currency_list"]:
                msg = QMessageBox() # we show a message box
                msg.setWindowTitle("Error")# set window title
                msg.setText("Please enter one of the following currencies:\n [GBX] [USD] [MGA]") # Change text to include configs.
                x = msg.exec_() #need this to execute window
            elif (text_minimum > text_maximum):
                print("hi")
                msg = QMessageBox()# we show a message box
                msg.setWindowTitle("Error")# set window title
                msg.setText("Contradiction in coin limits") # Change text to include configs.
                x = msg.exec_()#need this to execute window
            elif temp ==5:
                msg = QMessageBox()# we show a message box
                msg.setWindowTitle("Error")# set window title
                msg.setText("Error - No coins selected") # Change text to include configs.
                x = msg.exec_()#need this to execute window
                
            else:
                settings["max_"] = text_maximum #if none of the conditions are met, the input should be fine and we reassign old variables to 
                #the new ones according to the settings window
                settings["min_"] = text_minimum
                settings["currency_"] = text_input_currency
                self.close() # we close the window upon pressing ok
        except:#if an error occurs notify user
            msg = QMessageBox()# we show a message box
            msg.setWindowTitle("Error")# set window title
            msg.setText("Please enter input arguments!") # Change text to include configs.
            x = msg.exec_()#need this to execute window



        

if __name__ == "__main__": # if this is the main script and not a import, run things below
    import sys # load functions to manipulate different parts of the Python runtime environment
    app = QtWidgets.QApplication(sys.argv) #load the widgets
    MainWindow = QtWidgets.QMainWindow() # load teh widgets
    ui = Ui_MainWindow() # assign main menu widget
    ui.setupUi(MainWindow) # load 
    MainWindow.show() # show the widget
    sys.exit(app.exec_()) # tell program to keep running unless user closes through GUI 
