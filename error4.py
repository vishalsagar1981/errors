

def interact():
    my_input = 'y'
    while (my_input == 'y'):
        user_input_raw = input("Enter the Integer Value :- ")
        try:
            user_input = int(user_input_raw)
            print (f"You Entered {user_input} ")
            if  user_input % 2 == 0 :
                print(f"{user_input} Is an Even No ")
            else:
                print (f"{user_input} Is an Odd No ")
        except ValueError:
            print (f"The Entered Value {user_input_raw} is Incorrect")
        finally:
            my_input = input ("Do you want to check another number:- ")

interact()