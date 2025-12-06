while True:
    import time
    import random
    print("Select language:")
    print("1. English")
    print("2. Hindi")
    language = input("Enter 1 or 2: ")
    if language == "1":
        attempts = 3
        while attempts > 0:
            print("Welcome to ATM machine.")
            option = input("You have three options:\na) Cash withdrawal\nb) Cash deposit\nc) Set your PIN.\n").lower()
            if option == "c":
                mobile_number_declare = int(input("Set your mobile number: "))
                print("Please confirm your mobile number.")
                mobile_number = int(input("Enter mobile number: "))
                if mobile_number != mobile_number_declare:
                    print("Wrong mobile number.")
                    attempts -= 1
                    print("Attempts left:", attempts)
                    continue
                otp = random.choice([9860, 8768, 7658])
                print("Your OTP is coming...")
                time.sleep(5)
                print(f"The OTP is {otp}")
                otp_input= int(input("Enter the OTP: "))
                if otp_input == otp:
                    pin_declare = int(input("Set your PIN: "))
                    atm_balance = 2000
                    print("PIN set successfully. Account balance is ₹", atm_balance)
                    break
                else:
                    print("Wrong OTP.")
                    attempts -= 1
                    print("Attempts left:", attempts)
            else:
                print("Please set your PIN first by selecting option 'c'.")
                continue
        while attempts > 0:
            card = input("Type 'card' to insert your card: ").lower()
            if card != "card":
                print("Invalid card input.")
                attempts -= 1
                print("Attempts left:", attempts)
                continue
            pin = int(input("Enter your PIN: "))
            if pin != pin_declare:
                print("Wrong PIN.")
                attempts -= 1
                print("Attempts left:", attempts)
                continue
            selection = input("Choose:\na) Withdraw\nb) Deposit\nYour choice: ").lower()
            if selection == "a":
                def sub(a,b):
                    return a - b
                withdrawal = int(input("Enter amount to withdraw: "))
                withdrawal_result=sub(atm_balance,withdrawal)
                if withdrawal_result <= atm_balance:
                    atm_balance-=withdrawal
                    print("Withdrawn ₹", withdrawal_result)
                    print("Remaining balance ₹", atm_balance)
                    print("Thanks for withdrawal.")
                    break
                else:
                    print("Insufficient balance.")
                    attempts -= 1
                    print("Attempts left:", attempts)
            elif selection == "b":
                pocket=1500
                print(f"The money in your pocket is {pocket}")
                def add(a,b):
                    return a+b
                deposition = int(input("Enter amount to deposit: "))
                deposition_result = add(deposition,atm_balance)
                if deposition_result <= pocket:
                    atm_balance += deposition
                    print("Deposited ₹", deposition)
                    print("New balance ₹", atm_balance)
                else:
                    print("Insufficient money in the pocket.")
                    print("Thanks for deposition.")
                break
        if attempts == 0:
            print("3 attempts used. Please wait...")
            for i in range(10, 0, -1):
                print(i)
                time.sleep(1)
            print("You can try again now.")
    elif language == "2":
        attempts = 3
        while attempts > 0:
            print("एटीएम मशीन में स्वागत है.")
            option = input("आपके पास तीन विकल्प हैं:\na) पैसा निकालो\nb) पैसा जमा करो\nc) पिन सेट करो\n").lower()
            if option == "c":
                mobile_number_declare = int(input("अपना मोबाइल नंबर सेट करो: "))
                print("कृपया मोबाइल नंबर की पुष्टि करो.")
                mobile_number = int(input("मोबाइल नंबर डालो: "))
                if mobile_number != mobile_number_declare:
                    print("गलत मोबाइल नंबर.")
                    attempts -= 1
                    print("बचे प्रयास:", attempts)
                    continue
                print("आपका OTP आ रहा है...")
                time.sleep(5)
                otp = random.choice([9860, 8768, 7658,])
                print(f"OTP है: {otp}")
                otp_input=int(input("OTP डालो: "))
                if otp_input == otp:
                    pin_declare = int(input("अपना पिन सेट करो: "))
                    atm_balance = 2000
                    print("पिन सेट हो गया. खाता बैलेंस ₹", atm_balance)
                    break
                else:
                    print("गलत OTP.")
                    attempts -= 1
                    print("बचे प्रयास:", attempts)
            else:
                print("कृपया पहले पिन सेट करो, विकल्प 'c' चुनकर.")
                continue
        while attempts > 0:
            card = input("'card' लिखो कार्ड डालने के लिए: ").lower()
            if card != "card":
                print("गलत इनपुट.")
                attempts -= 1
                print("बचे प्रयास:", attempts)
                continue
            pin = int(input("पिन डालो: "))
            if pin != pin_declare:
                print("गलत पिन.")
                attempts -= 1
                print("बचे प्रयास:", attempts)
                continue
            selection = input("क्या करना है?\na) पैसा निकालना\nb) पैसा जमा करना\nचॉइस: ").lower()
            if selection == "a":
                def sub(a,b):
                    return b - a 
                withdrawal = int(input("कितना पैसा निकालना है: "))
                withdrawal_result = sub(atm_balance,withdrawal)
                atm_balance -= withdrawal
                if withdrawal <= atm_balance:
                    print("निकाला गया ₹", withdrawal)
                    print("बैलेंस ₹", atm_balance)
                    break
                else:
                    print("बैलेंस कम है.")
                    attempts -= 1
                    print("बचे प्रयास:", attempts)
            elif selection == "b":
                pocket = 1500
                print(f"आपके पास अभी {pocket} रुपये है .")
                def add(a,b):
                    return a+b
                deposition = int(input("कितना पैसा जमा करना है: "))
                deposition_result = add(atm_balance,deposition)
                atm_balance += deposition
                if deposition <= pocket:
                    print("जमा किया ₹", deposition)
                    print("नया बैलेंस ₹", atm_balance)
                else:
                    print("आपके पास अभी उतने पैसे नहीं है .")
                break
        if attempts == 0:
            print("3 प्रयास पूरे हुए. कृपया प्रतीक्षा करें...")
            for i in range(10, 0, -1):
                print(i)
                time.sleep(1)
            print("अब फिर से कोशिश कर सकते हो.")
    else:
        print("गलत चॉइस.")
