####In Part 01, we are tasked we creating a rudimentary script before building on this In part 02.

#part01 should have these key feaures:
    #A fixed configuration that has the option to be shown [features include max/min input and all currency conversions]
    # option to exclude certain coins
    # Option to use all coins in order of importance or use single coins
    # Use an API to convert GBP to USD and Malagasy currency

#The code is arguably larger than it needs to be at its most simpliest level. However, the emphasis we wanted to place here and in the future
#is quality assurance (QA). As a team, we identified anomalous scenarious by testing various inputs and used *While True* conditions to keep asking
# for the appropiate input Examples include:
    #if the user inputs 2.4, we round down and assume the user means 2.
    # If the user inputs say, letters, then keep asking for appropiate input and display error messages.
    #what if the user uses capital letters? we deal with itin our program.
    #For coin exclusions, if different numbers are pressed or certain keys pressed more than once, we handle this by using sets

#A brief description will be provided by each section followed by code comments 



def coin_sort_p01(): # define the coin sorting function or program
##########################################SECTION 1 ###################################################
#######################################################################################################
#In the first section we grab all the essential tools we will need. 

    import os #Import libraries OS used for file exploration, requests is used for API connectivity. 
    import requests
    URL_BASE = "https://www.amdoren.com/api/currency.php" # URL to grab information 
    TESTING = os.getenv("CI", True) # Test if API request works
    def split(word): # define a function to split an input -word- used later. 
        return [char for char in word] # for each element in string print them eg BOB prints [B, O, B]
    coin_dict =  {"£2": 200,"£1": 100,"50p": 50,"20p": 20,"10p":10 } # create dictionary used for reference
    coins_interface = ["£2","£1","50p","20p","10p"] #list here to grab keys in the dictionary 
    settings = {"max_":10000,"min_":0} # dictionary for configuration settings Max_ and min_ are static configurations required for part 01. The user can print these
    import requests
    URL_BASE = "https://www.amdoren.com/api/currency.php" # URL to grab information 
    API_KEY = "EXhU7kDVy7fkrHJYNtwGePkwzcxsxS" # API key required to grab data from web server NB limit of 10 per day for free users
    number_of_coins_list =[]; # create a list due to various scenarios that will cause incorrect output
    def convert_currency( #define a function to grab currency from a web server we USE JSON format and grab inputs needed to get a response back
                         #requires from_ (the current currency), to (currency to convert to), data_type and finally the API key defined above
        from_: str = "USD", to: str = "INR", amount: float = 1.0, api_key: str = API_KEY) -> str:
        """https://www.amdoren.com/currency-api/"""
        params = locals()
        params["from"] = params.pop("from_") #remove key 
        #print(params)
        res = requests.get(URL_BASE, params=params).json() # convert to JSON and use this to grab information from server
        return print("Your Conversion amount is: {:.2f} \nThank you come again!".format((res["amount"])) if res["error"] == 0 else res["error_message"])
        #Above - print information on currency. 

##########################################SECTION 2 ###################################################
#######################################################################################################
#Section 2 mainly gives the option to show the configuration of the program before providing coin inputs
    
    #say hello to user, describe what program is
    print("================ Coin_Sorter ================ \n=============== Capstone LTD ================")
    print("Hello there, we can exchange your pennies [p] to any of the following coins:\n- £2[200p]\n- £1[100p] \n- 50p\n- 20p\n- 10p")
    while True: # the -while True- statement is important here. If the user doesnt enter C or I keep asking for appropiate input
        continue_ = input("\nTo display configuration settings, type C. Otherwise type I to continue:\n")
        
        if continue_.upper() == "C": # if user, inputs C, display configuration to user defined by variables at start of function 
            print ("\nConfiguration settings:\nMax coin input: {}\nMin coin input: {}\nCurrencies: USD, Malagasy Dollars".format(settings['max_'],settings['min_']))
            while True: # After the configuration is seen, keep prompting the user to type I to continue. 
                continue_ = input("\nPress I to continue: \n")
                if continue_.upper() =="I":
                    break # break statements stop the loop to continue with the program. Recall the -While True- statement 
            break
            while True:
                continue_ = input("\nPress I to continue: \n") #after pressing C and 
                if continue_.upper() =="I":
                    break
        if continue_.upper()=="I": # Alternatively if user Ignores viewing configuration and Wants to continue, break loop
            break
##########################################SECTION 3 ###################################################
#This code asks the user to input a certain amount in pennies to be converted.
#Again, there is a while True condition to check for unexpected inputs 
    while True:      
        try: #try this block of code, if not valid, we loop and ask for input again. I.E input of letter instead of valid coin number
            pennies_input = input("Please input the amount of pennies (GBX) you want exchanging:\ninput:") # input number of pennies
            rounded_input = float(pennies_input) #we round the pennies down if a decimal is provided. 
            remainder = rounded_input #We create a remainder variable for later. This is used to print the remainding pennies after calculation
            
            while True: 
                if rounded_input >=settings['min_'] and rounded_input <= settings['max_']: # Condition to check if input is in the appropiate range
                        while not(rounded_input.is_integer()):
                            input("Penny fractions do not exist. [Press enter to try again]")
                            pennies_input = (input("Please input the amount of pennies (GBX) you want exchanging:\ninput:")) 
                            rounded_input = float(pennies_input) 
                        break;
                print("please enter correct coin range!") # notify user if input not in range
                pennies_input = (input("Please input the amount of pennies you want exchanging:\ninput:")) # asking user again if an error occurs
                rounded_input = int(pennies_input)
        except:
            pennies_input = print("Please provide a valid input.\n") # second type of error, input of a letter instead of number, weird characters etc
            continue
        else:
            break
##########################################SECTION 4 ###################################################
# The emphasis in section 4 gives the user the option to exclude certain coins from calculations
    while True:
        exclude = input("Do you want to exclude any certain coins? [Y/N]\ninput: ") # We ask the user if users wants to exclude certain coins
        if (exclude.upper() == "Y" or exclude.upper() == "N"): #if input =yes or no, tell program a valid input has been given
            print("\n") #print new line
            break # stop loop after valid input
        if (exclude.upper() != "Y" or exclude.upper() != "N"): # check to see if input is valid, (yes or no, y/n)
            print("please enter a valid input.")        
    if exclude.upper() =="Y": # If user wants to exclude inputs: ....(has input Y)
        while True:
            try:
                print ("Please insert the coins you want removed (Example input - [201] removes £2, £1 and 50p):") # type all keys to be removed
                for item in range(len(coins_interface)): # the keys correspond to the positions in the list. we record this and use it to
                #remove chosen values from dictionary
                    print (coins_interface[item] + "     key: [" + str(item) + "]")
                remove = input("\ninput:\n")
                for item in set(split(remove)):#we split all the keys pressed, and use it to remove it as said in the last comment
                    print ("Coin removed - {}".format(coins_interface[int(item)]))
                    coin_dict.pop(coins_interface[int(item)], None)
            except:
                print("invalid argument, please try again") # if error produced, i.e invalid value/out of range....notify user.
            else:
                break; 
    
    print("Your input: {} pence. \ncalculating number of coins you will have for each type:".format(rounded_input)) 
    for i in coin_dict: # for each item in the dictionary (after removal of some, if any...print number of coins + remainder)
        print( "***Type: {} -  Number of coins: {} - Remainder: {} pence.***".format(i , int(rounded_input/coin_dict[i]),rounded_input % coin_dict[i]))
    #The bottom secction includes all coins, and ranks the order based on importance (order of dictionary)
        if int(rounded_input/coin_dict[i])!= 0:
            number_of_coins_list.append(int(rounded_input/coin_dict[i])) # create a list due to various scenerios that will cause 
    try:
        print("\nThe maximum number of coins you can receive is: {}. | The minimum number of coins you can receive is {}.\n".format(max(number_of_coins_list),min(number_of_coins_list)))
    except:
        print("\nBoth the Maximum/Minimum number of coins obtained is zero! ")
    
    print("\nUsing all coins (in order of importance), you will have: ")  
    for i in coin_dict:
        print( "***Type: {} -  Number of coins: {}***".format(i , int(remainder/coin_dict[i])))
        remainder = remainder % coin_dict[i] # Going through each iteration, we find the remainder to tell the user at the end
    print("Your remainder is: {} pence.".format(int(remainder)))
            
        
    
##########################################SECTION 5 ###################################################
#This section uses the API defined above using the requests library.  We only ask the user to input the required amount and choice of currency
    while True:
        try:
            currency = input("Please Type: \n[0] for US currency conversion\n[1] for Malagay currency conversion\n[2] to quit\n")
            if currency =="2":
                print("Thank you come again!")
                break
            elif currency =="1":
                print(convert_currency("GBP".strip(),"USD".strip(),float(input("Enter the amount[£]: ").strip()),))
                break
            elif currency =="0":
                print(convert_currency("GBP".strip(),"MGA".strip(),float(input("Enter the amount[£]: ").strip()),))
                break
        except:
            continue

coin_sort_p01() # initiate the defined function
