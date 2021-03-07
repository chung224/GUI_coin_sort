def coin_sort_p02():
    coin_dict =  {"£2": 200,"£1": 100,"50p": 50,"20p": 20,"10p":10 }
    coins_interface = ["£2","£1","50p","20p","10p"]
    keys = [1,2,3,4,5,6]
    settings = {"max_": 10000,"min_":0,"currency_":"GBX","currency_convert":1, "currency_list":["GBX","MGA","USD"]}
    while True:
        try:  
            print("\n          ***Coin Sorter - Main Menu***          \n" +
            "=============== Capstone LTD ================\n**Please input a key**\n")
            navigation_1 = int(input(
                                "[1] - Coin calculator\n" +
                                "[2] - Multiple coin calculator\n" + 
                                "[3] - Print coin list\n" +
                                "[4] - Set details\n" +
                                "[5] - Display program configurations\n" + 
                                "[6] - Quit the program\n\nYour input: "))
###############################################################################################
            if navigation_1 ==6:
                while True:
                    try:
                        are_you_sure = input("Are you sure you want to quit? [Y/N]\ninput: ")
                        if are_you_sure.upper() =="Y":
                            print("\nThanks for using our service!\n **PROGRAM TERMINATED**")
                            break;
                        if are_you_sure.upper() =="N":
                            break;
                        print("\nPlease enter a valid key.\n")     
                    except:
                        print("invalid input, please press type either [Y] or [N]\n")
                    else: 
                        continue
                if are_you_sure.upper() =="Y":
                    break;
            if navigation_1 not in keys:
                input("Please enter a valid key range [keys [1] to [6]].\nPress Enter to continue...")
###############################################################################################                
            if navigation_1 ==5:
                print("\n\n================ Current configuration ================ \n" +
                  "Minimum input: {}\n".format(int(settings["min_"] * settings["currency_convert"])) + 
                  "Maximum input: {}\n".format(settings["max_"] * settings["currency_convert"]) + 
                  "Current Currency: {}\n".format(settings["currency_"] + "\n"))
                input("Press Enter to continue...\n")
###############################################################################################
            if navigation_1 ==4:
                while True:
                    keys_sub_navigation =["1","2","3","4"]
                    sub_navigation = input("\n================ Set Details Sub-Menu ================ \n" +
                                                "[1] - Set currency\n" + 
                                                "[2] - Set minimum coin input value\n" +
                                                "[3] - Set maximum coin input value\n" + 
                                                "[4] - Return to main menu\n\ninput: " )
                    while True:
                        if sub_navigation not in keys_sub_navigation:
                            sub_navigation = input("\nError. Please provide an appropiate input: ")
                        else:
                            break;
                    if sub_navigation =="4":
                        break; 
                    elif sub_navigation =="1":
                        while True:
                            try:
                                settings["currency_"] =input("Please type on of the following currencies\n" + 
                                                             "[GBX] - Penny sterling\n" +
                                                             "[USD] - US dollars\n" +
                                                             "[MGA] - malagasy ariary\n" +
                                                             "Input: ").upper()
                                if settings["currency_"] in settings["currency_list"]:
                                    input("\nCurrency chosen: {}\n\nThanks! currency Changed \n\nPress Enter to continue...\n".format(settings["currency_"]))
                                    break;
                            except:
                                print("\nError. Please enter a valid currency")
                    elif sub_navigation =="2":
                        while True:
                            try:
                                settings["min_"] = float(input("\nCurrent minimum: {}\nPlease enter the minimum coin amount for your currency:[{}]\ninput: ".format(settings["min_"],settings["currency_"])))
                                while not(settings["min_"].is_integer()):
                                    input("Penny fractions do not exist. [Press enter to try again]")
                                    settings["min_"] = float(input("\nCurrent minimum: {}\nPlease enter the minimum coin amount for your currency:[{}]\ninput: ".format(settings["min_"],settings["currency_"])))
                                while settings["min_"] >= settings["max_"]:
                                    input("The minimum coin input is equal to greater than maximum coin input. [Press enter to try again]")
                                    settings["min_"] = float(input("\nCurrent minimum: {}\nPlease enter the minimum coin amount for your currency:[{}]\ninput: ".format(settings["min_"],settings["currency_"])))
                                while settings["min_"] < 0:
                                    input("Negative numbers are not allowed. press enter to  try again. ")
                                    settings["min"] = float(input("\nCurrent minimum: {}\nPlease enter the minimum coin amount for your currency:[{}]\ninput: ".format(settings["min_"],settings["currency_"])))
                                
                                print("\nStatus - Settings approved [Minimum input (Currency{}): {}]\nreturning to sub-menu.\n".format(settings["currency_"],str(settings["min_"])))
                                break;
                            except:
                                print("\nInvalid input. Please try again. ")
                            else:
                                continue
                    elif sub_navigation =="3":
                        while True:
                            try:
                                settings["max_"] = float(input("\nCurrent maximum: {}\nPlease enter the maximum coin amount for your currency: [{}]\ninput: ".format(settings["max_"],settings["currency_"])))
                                while not(settings["max_"].is_integer()):
                                    input("Penny fractions do not exist. [Press enter to try again]")
                                    settings["max_"] = float(input("\nCurrent maximum: {}\nPlease enter the maximum coin amount for your currency:[{}]\ninput: ".format(settings["max_"],settings["currency_"])))
                                while settings["max_"] >= settings["max_"]:
                                    input("The maximum coin input is less than or equal to the minimum coin input. [Press enter to try again]")
                                    settings["max_"] = float(input("\nCurrent maximum: {}\nPlease enter the maximum coin amount for your currency:[{}]\ninput: ".format(settings["max_"],settings["currency_"])))                           
                                while settings["max_"] < 0:
                                    input("Negative numbers are not allowed. Press enter try again. ")
                                    settings["max_"] = float(input("\nCurrent maximum: {}\nPlease enter the maximum coin amount for your currency:[{}]\ninput: ".format(settings["max_"],settings["currency_"])))
                                print("\nStatus - Settings approved [Maximum input (Currency{}): {}]\nreturning to sub-menu.\n".format(settings["currency_"],str(settings["max_"])))
                                break;
                            except:
                                print("\nInvalid input. Please try again. ")
                            else:
                                continue
            if navigation_1 ==3:
                print("\n================ Coin list ================ \nThe coins used in this program are: \n")
                for i in coins_interface:
                    print(i)
                input("Press Enter to continue...\n")
            if navigation_1 ==2:
                print("\n================ Multiple Coin calculator ================\n")
                while True:
                    try:
                        input_ = float(input("Please insert the amount of pennies you want converting:\ninput: "))
                        remainder = input_
                        if input_ >=settings["min_"] and input_ <= settings["max_"]:
                            while not(input_.is_integer()):
                                input("Penny fractions do not exist. [Press enter to try again]")
                                input_ = float(input("Please insert the amount of pennies you want converting:\ninput: "))
                            print("\nUsing all coins (in order of importance), you will have:\n ")
                            for i in coin_dict:
                                print( "***Type: {} -  Number of coins: {}***".format(i , int(remainder/coin_dict[i])))
                                remainder = remainder % coin_dict[i]
                            print("Your remainder is: {} pence.".format(int(remainder)))
                            input("Press Enter to continue...\n")
                            break;
                            
                        else:
                            print("Value out of range. Please try again!")
                            input("Press Enter to continue...\n")
                            break;
                    except:
                        print("invalid input, please try again.\n")
                    else:
                        continue
                                
            
            if navigation_1 ==1:
                print("\n================ Coin calculator ================\n")
                while True:
                    try:
                        input_ = float(input("Please insert the amount of pennies you want converting:\ninput: "))
                        if (input_ >=settings["min_"] and input_ <= settings["max_"]):
                            while not(input_.is_integer()):
                                input("Penny fractions do not exist. [Press enter to try again]")
                                input_ = float(input("Please insert the amount of pennies you want converting:\ninput: "))
                            for i in coin_dict:
                                print( "***Type: {} -  Number of coins: {} - Remainder: {} pence.***".format(i , int(input_/coin_dict[i]),int(input_ % coin_dict[i])))
                            input("Press Enter to continue...\n")
                            break;
                        else:
                            print("\nValue out of range - Please try again.\n")
                    except:
                        print("\ninvalid input. Please try again.\n")
                    else:
                        continue
        except:
            print("\nInvalid argument, please try again.\n")
            input("Press Enter to continue...\n")
            
        else:
            continue
###############################################################################################

 
coin_sort_p02()              
            
                  
                
        