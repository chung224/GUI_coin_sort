#In part 2, we once again create a coin sorter program. The main emphasis here however is the implementation of a text menu. 
# We identified certain scenarios that could cause to pgroam that could go wrong and adjust our code accordingly.
# for example if minimum is greater than maximum --> display an error.  

#Errors found and fixed with notification to user:
    #if user chooses to remove all coins - deal with this during calculation
    #if user sets the maximum to be smaller than the minimum (and vice verse with larger), deal with this
    #if user types a decimal for any coin inputs 
    #if the user types special keys for text or text for int (etc etc)
    #if the user types a key outside the desired range 
    #case sensitive inputs 
    #negative coin inputs
    #upon asking for coin removal by typing certain keys. if the user types a number more than once, we deal with this


def coin_sort_p02(): #define the function of our coin sorter program. 
##########################################SECTION 1 ###################################################
#######################################################################################################
#In the first section we grab all the essential tools we will need.     
    coin_dict =  {"£2": 200,"£1": 100,"50p": 50,"20p": 20,"10p":10 } # create a dictionary for program to grab all the coins 
    coins_interface = ["£2","£1","50p","20p","10p"] # this list is created inorder to dictionary keys efficiently
    keys = [1,2,3,4,5,6] #this list is created for the main menu of the program. the program checks for the user input in this list.
    settings = {"max_": 10000,"min_":0,"currency_":"GBX","currency_convert":1, "currency_list":["GBX","MGA","USD"]} # settings of program
    
##########################################SECTION 2 ###################################################
####################################################################################################### 
#In this section, we create the text menu for the user using the print statement. in subsequent sections we identify certain scenarios if a 
#key is chosen.    
    while True: # The while True condition here is important since is tells the user to keep the coin sorter program in action until a criteria is met
        try:   #The try statement here ensures that the user is notified of an error if an invalid input is entered
            print("\n          ***Coin Sorter - Main Menu***          \n" + # define the main menu through text
            "=============== Capstone LTD ================\n**Please input a key**\n") # the \n tells the string to go on new line
            navigation_1 = int(input( # we display this text, and ask the user for an input defined as -navigation_1-
                                "[1] - Coin calculator\n" +
                                "[2] - Multiple coin calculator\n" + 
                                "[3] - Print coin list\n" +
                                "[4] - Set details\n" +
                                "[5] - Display program configurations\n" + 
                                "[6] - Quit the program\n\nYour input: "))
##########################################SECTION 3 ###################################################
#######################################################################################################
#this section works with the scenario in which the user types [6] and wishes to leave the program, ultimately stopping the while True statement defined
#above.  
            if navigation_1 ==6: #if the user types -6-
                while True: # another while true statement - keep doing this loop until criterion met
                    try: # try this block of code. if it doesnt work notify user in the -except- block [see below]
                        are_you_sure = input("Are you sure you want to quit? [Y/N]\ninput: ") #prompt the user to type -y- to confirm they want to quit
                        if are_you_sure.upper() =="Y": # if user types -y- , thank the user and break While True loop. [see below]
                            print("\nThanks for using our service!\n **PROGRAM TERMINATED**") # as said, we thank the user.
                            break; # break statement stops the loop
                        if are_you_sure.upper() =="N": # if the user types no, break the loop
                            break; 
                        print("\nPlease enter a valid key.\n")    # if user hasnt pressed -y- or -n-. the while True loop has not stopped.
                        #thus, we keep propmting the user to enter a valid input key
                    except: # if an error occurs......... print statement below.
                        print("invalid input, please press type either [Y] or [N]\n") #Tell user to type either -y- or -n-
                    else: #this else block runs if either the -if- or -except- statement is run
                        continue # we tell computer to continue running the code. 
                if are_you_sure.upper() =="Y": # another second condition, because the user has already typed -y-, the program is stopped.
                    break;
            if navigation_1 not in keys: #condition to see if the input user has put is in the -keys- dictionary defined above.
                input("Please enter a valid key range [keys [1] to [6]].\nPress Enter to continue...")# if the user has not typed a key from -1- to -6- we notify user followed by 
            #asking them to press enter to continue to type another input
##########################################SECTION 3 ###################################################
#######################################################################################################
#in this section, if the user enters -5- from the main menu the configuration of the program is displayed, This still works if the user wishes to
#update settings (see next section)                
            if navigation_1 ==5: # condition to see if user types 5
                print("\n\n================ Current configuration ================ \n" + # using a print statement with formatting:
                  "Minimum input: {}\n".format(int(settings["min_"] * settings["currency_convert"])) + #we print all the settings using the predefined dictionary
                  "Maximum input: {}\n".format(settings["max_"] * settings["currency_convert"]) +
                  "Current Currency: {}\n".format(settings["currency_"] + "\n"))
                input("Press Enter to continue...\n") # after displaying all configurations, prompt user to press enter before continuing 
##########################################SECTION 4 ###################################################
#######################################################################################################
#in this section, the code allows the user to change certain settings. Upon entering key -4-, a sub menu will be displayed 
            if navigation_1 ==4: # condition if user inputs 4 from main menu
                while True: # the sub menu will keep being displayed unless the user wishes to leave
                    keys_sub_navigation =["1","2","3","4"] # define a list of keys to check if certain keys chosen
                    sub_navigation = input("\n================ Set Details Sub-Menu ================ \n" + # add text to user showing the sub-menu
                                                "[1] - Set currency\n" +  # an input is asked from the user after the text
                                                "[2] - Set minimum coin input value\n" + 
                                                "[3] - Set maximum coin input value\n" + 
                                                "[4] - Return to main menu\n\ninput: " )
                    while True: # condition loop, breaks if conditions are met and carry on with program
                        if sub_navigation not in keys_sub_navigation: # if a certain key not types 
                            sub_navigation = input("\nError. Please provide an appropiate input: ") # keep asking user to input valid value
                        else: # if appopiate response made....
                            break; # break the loop
                    if sub_navigation =="4": # if key -4- in the sub-menu entered:
                        break; #break the loop 
                    elif sub_navigation =="1": # if user types -1- in sub menu
                        while True: # create loop which is broken if valid input entered. 
                            try: # try this block of code. if and error occurs run block in -except-
                                settings["currency_"] =input("Please type on of the following currencies\n" + #ask user for a currency
                                                             "[GBX] - Penny sterling\n" +
                                                             "[USD] - US dollars\n" +
                                                             "[MGA] - malagasy ariary\n" +
                                                             "Input: ").upper()
                                if settings["currency_"] in settings["currency_list"]: # we check the condition if the user's input is within our list
                                #of currencies
                                    input("\nCurrency chosen: {}\n\nThanks! currency Changed \n\nPress Enter to continue...\n".format(settings["currency_"]))
                                    #above - we notify the user that settings have been changed and ask to press enter
                                    break; # we break the loop which constantly asks for a currency
                            except:
                                print("\nError. Please enter a valid currency") #print an error if weird input
                    elif sub_navigation =="2": # if user types key -2- in the sub menu we ask user to change the minimum coin setting
                        while True: #again creat a loop until criteria met or error occurs
                            try:
                                #below - we ask user to type an input to reassign the a value using a key [dictionary]
                                settings["min_"] = float(input("\nCurrent minimum: {}\nPlease enter the minimum coin amount for your currency:[{}]\ninput: ".format(settings["min_"],settings["currency_"])))
                                while not(settings["min_"].is_integer()): # checking if the input is not an integer
                                    input("Penny fractions do not exist. [Press enter to try again]") # if not an integer we keep asking and ask to press enter
                                    #below -we ask the user again for a minimum input after the user is notified
                                    settings["min_"] = float(input("\nCurrent minimum: {}\nPlease enter the minimum coin amount for your currency:[{}]\ninput: ".format(settings["min_"],settings["currency_"])))
                                while settings["min_"] > settings["max_"]: # second condition - we check if the minimum coin is greater than the max
                                #below - we notify user
                                    input("The minimum coin input is greater than maximum coin input. [Press enter to try again]")
                                    #ask user for another input after displaying an error
                                    settings["min_"] = float(input("\nCurrent minimum: {}\nPlease enter the minimum coin amount for your currency:[{}]\ninput: ".format(settings["min_"],settings["currency_"])))
                                while settings["min_"] < 0: # if the user types a negative number keep asking user
                                    input("Negative numbers are not allowed. press enter to  try again. ")#display error
                                    #below - ask user to type another input after error given
                                    settings["min"] = float(input("\nCurrent minimum: {}\nPlease enter the minimum coin amount for your currency:[{}]\ninput: ".format(settings["min_"],settings["currency_"])))
                                
                                #if all is good, then the status message below is printed and the loop breaks
                                print("\nStatus - Settings approved [Minimum input (Currency{}): {}]\nreturning to sub-menu.\n".format(settings["currency_"],str(settings["min_"])))
                                break;
                            except: # if the input is invalid notify user and ask again
                                print("\nInvalid input. Please try again. ") # error message
                            else:
                                continue # after error, continue with program
                    elif sub_navigation =="3": #if user types -3- in the sub menu the exact same is done but program asks for the max value
                        while True: # keep doing this block until broken
                            try: #try this block of code, otherwise notify user an error has occured and repeat. 
                            #below - ask user for max value
                                settings["max_"] = float(input("\nCurrent maximum: {}\nPlease enter the maximum coin amount for your currency: [{}]\ninput: ".format(settings["max_"],settings["currency_"])))
                                while not(settings["max_"].is_integer()):#if the input is not an integer.....
                                    input("Penny fractions do not exist. [Press enter to try again]") # notify this to user
                                    #ask the user again for another input
                                    settings["max_"] = float(input("\nCurrent maximum: {}\nPlease enter the maximum coin amount for your currency:[{}]\ninput: ".format(settings["max_"],settings["currency_"])))
                                while settings["max_"] > settings["max_"]: #if the max coin assignment is smaller than min notify user
                                    input("The maximum coin input is less than the minimum coin input. [Press enter to try again]") # print error
                                    #below. ask the user again after error displayed
                                    settings["max_"] = float(input("\nCurrent maximum: {}\nPlease enter the maximum coin amount for your currency:[{}]\ninput: ".format(settings["max_"],settings["currency_"])))                           
                                while settings["max_"] < 0: # if the input is less than zero tell the user
                                    input("Negative numbers are not allowed. Press enter try again. ") # notify 
                                    #below - ask the user again for an input
                                    settings["max_"] = float(input("\nCurrent maximum: {}\nPlease enter the maximum coin amount for your currency:[{}]\ninput: ".format(settings["max_"],settings["currency_"])))
                                #print a status message printing the changed setting
                                print("\nStatus - Settings approved [Maximum input (Currency{}): {}]\nreturning to sub-menu.\n".format(settings["currency_"],str(settings["max_"])))
                                break; # after making changes, break the loop return to  submenu
                            except: # if error in input - display message
                                print("\nInvalid input. Please try again. ")
                            else:
                                continue # after error continue running
                                
##########################################SECTION 5 ###################################################
#######################################################################################################
#In this section, we print the coin list according to the list called -coins_interfce- to the user
            if navigation_1 ==3: # from main menu if key -3- entered. continue with this block of code
                print("\n================ Coin list ================ \nThe coins used in this program are: \n") # coin list menu banner print
                for i in coins_interface: # for each item in the list 
                    print(i) # print each item
                input("Press Enter to continue...\n") # after all items dispalyted, tell user to press enter to continue
            if navigation_1 ==2:
                
##########################################SECTION 6 ###################################################
#######################################################################################################
#In this section, we use multiple coins, in order of denomination to find how many coins of each type can be obtained with a remainder in pennies
                print("\n================ Multiple Coin calculator ================\n") # print menu bannter
                while True: # keep this loop aftive until broken
                    try: # try this block of code
                        input_ = float(input("Please insert the amount of pennies you want converting:\ninput: ")) # ask user to input a coin amount
                        remainder = input_ # assign the input to another variable for calculation of the remainder
                        if input_ >=settings["min_"] and input_ <= settings["max_"]: # condition to see if input is within range
                            while not(input_.is_integer()): # if the input is not an integer. this this block of code
                                input("Penny fractions do not exist. [Press enter to try again]") # notify user of this error
                                input_ = float(input("Please insert the amount of pennies you want converting:\ninput: ")) # ask user again 
                            print("\nUsing all coins (in order of importance), you will have:\n ") # print information if everythings ok
                            for i in coin_dict: # for item in the dictionary
                                print( "***Type: {} -  Number of coins: {}***".format(i , int(remainder/coin_dict[i]))) # calculate and print the remainder
                                remainder = remainder % coin_dict[i] # upon calculating the number of coins, we calculate the remainder for next denomination
                            print("Your remainder is: {} pence.".format(int(remainder))) # final statement we print the final remainder after going through each coin
                            input("Press Enter to continue...\n") # ask user to press enter to continue
                            break; # break loop 
                            
                        else: # if the input is out of range....
                            print("Value out of range. Please try again!") # notify user of error and ask to press enter
                            input("Press Enter to continue...\n") # ask the user again
                            break;
                    except: # if invalid input.....
                        print("invalid input, please try again.\n") # notify user
                    else:
                        continue # after error. continue with loop
                                
##########################################SECTION 7 ###################################################
#######################################################################################################
#in the final section, we calculate the number of coins and the remainder if only a single type of coin is used.
#NB options to remove certain coins were not included in part 2, they have however been added in part1 + 3. No mention of this feature was mentioned
#in the brief          
            if navigation_1 ==1: # in the main menu if user types key -1-
                print("\n================ Coin calculator ================\n") # display menu banner.
                while True: # run this loop until we break it 
                    try: # try this block of code
                        input_ = float(input("Please insert the amount of pennies you want converting:\ninput: "))
                        #above - ask user to type the number of pennies
                        if (input_ >=settings["min_"] and input_ <= settings["max_"]): # check if input within coin settings range
                            while not(input_.is_integer()):# check if the input is not an integer
                                input("Penny fractions do not exist. [Press enter to try again]") # notify user of error
                                input_ = float(input("Please insert the amount of pennies you want converting:\ninput: ")) #ask user again for input
                            for i in coin_dict: # if everything is ok, we go through each item in the coin_dictionary and calcualte + print remainder and number of coins
                                print( "***Type: {} -  Number of coins: {} - Remainder: {} pence.***".format(i , int(input_/coin_dict[i]),int(input_ % coin_dict[i])))
                            input("Press Enter to continue...\n") # after calculations done, prompt user to press enter
                            break; # break loop to exit coin calculator
                        else: # if program has an error -i.e bad input do this block
                            print("\nValue out of range - Please try again.\n") #notify user that coin is out of range
                    except:# if an error errors
                        print("\ninvalid input. Please try again.\n") # notify user of error
                    else: 
                        continue # continue with loop and repeat
        except: # in the main menu, if a bad input is typesd, execute this block
            print("\nInvalid argument, please try again.\n") # notify user of bad input in main menu
            input("Press Enter to continue...\n") # prompt userto press enter after reading error
            
        else:
            continue # continue with While True loop

 
coin_sort_p02() # call the function we created              
            
                  
                
        