import random
import time

#main menu
def main_menu():
    while True:
        menu = int(input("Press '0' to end program\nPress '1' to go to Magic 8 Ball\nPress '2' to go to Random Item from a Predefined List\nPress '3' to open Admin login menu\n"))
        if menu == 0:
            quit()
        elif menu == 1:
            magic_8_ball()
            break
        elif menu == 2:
            predefined_lists()
            break
        elif menu == 3:
            admin_menu()
            break
        else:
            print("Invalid input please try again")
            time.sleep(.8)



def magic_8_ball():
    responses = ["My sources say no", "My sources say yes"]
    response = responses[random.randint(1, len(responses))]
    while True:
        question = input("What would you like to ask the Magic 8 Ball? Yes/no questions only\nPress '0' to return to main menu\n")
        if question == "0":
            main_menu()
            break
        else:
            print("Your question: {}\nMagic 8 Ball's answer: {}".format(question, response))
            time.sleep(1.4)





def predefined_lists():
    print("chicken")





def admin_menu():
    print("pizza")
main_menu()
