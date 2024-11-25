class ATM:
    def display(self):
        print("Please insert the card")
        options=input("Please select your required option: ")
        if options=="cash withdrawal":
            print("Please select your ATM number")
            ATM_Number=int(input("Enter your ATM number: " ))            
            print("Available notes are 500 and 100 only")
            Amount=int(input("Please enter the amount: "))
            if Amount<=10000:
                    print("Transaction Pending")
                    print("Transaction succesfull")
                    print("Please collect your cash")
                    print("Please remove your card")
                    print("Thank you for banking with us")
            elif Amount>10000:   
                    print("The daily limt is 10000")
                    print("Transaction unsuccesfull")
                    print("Please remove your card")
                    print("Thank you for banking with us")    
        elif options=="balance enquiry":
                print("Please select your ATM number")
                ATM_Number=int(input(": " ))
                import random as rd
                print(("your balance is"),rd.randint(1,10000000))
                print("Please remove your card")
                print("Thank you for banking with us")
        elif options=="pin number change":
                print("enter your existing PIN number")
                pin_Number=int(input(": "))
                print("select change PIN option")
                print("enter your new PIN")
                New_PIN_Number=int(input(": " ))
                print("confirm your new PIN")
                new_pin_confirmation=int(input(": "))
                print("save the changes")
                print("Please remove your card")
                print("Thank you for banking with us")
        elif options=="cash deposit":
                print("accept the terms and conditions to proceed")
                terms_and_conditions=input("agree or disagree: ")
                if terms_and_conditions=="agree":
                    account_deposit=input("own account or third party account: ")
                    if account_deposit=="own account":
                        print("enter your ATM number")
                        ATM_Number=int(input(": " ))
                        print("place the amount in the box: ")
                        Amount=int(input(": "))
                        print("your cash is being verified")
                        import random as rd
                        list=["transaction succesful","transaction unsuccesful"]                   
                        print(rd.choice(list))
                    elif account_deposit=="third party account":
                        print("enter your ATM number")
                        ATM_Number=int(input(": " ))
                        print("place the amount in the box: ")
                        Amount=int(input(": "))
                        print("your cash is being verified")
                        import random 
                        list=["transaction succesful","transaction unsuccesful"]
                        chance=[90,10]
                        
                        random_choice = random.choices(list,chance)
        else:
            print("ATM is temporarly closed !!")
a=ATM()
a.display()
    
          
    
    
        
    
        
    



