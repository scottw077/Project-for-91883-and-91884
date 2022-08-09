import random
import time
#creating the colour
def colour(r, g, b, text):
    return "\033[38;2;{};{};{}m{}\033[38;2;255;255;255m".format(r,g,b,text)

#main menu
def main_menu():
    while True:
        print(colour(106, 100, 230, "Type in the number corresponding to the Program you want to run"))
        menu = int(input("Press '0' to end program\nPress '1' to go to Magic 8 Ball\nPress '2' to go to Random Item from a Predefined List\nPress '3' to open Admin login menu\n")) #asks the user what program they want to run
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
    responses = [colour(210, 4, 35, "My sources say no"), colour(0, 255, 0, "My sources say yes"), colour(255, 140, 0, "I don't know"),
                 colour(255, 140, 0, "Please re-enter question"), "Yeah obviously", "Clearly not", "Yeah, I am {} percent sure".format((random.randint(1, 100))),
                 "No, I am {} percent sure".format((random.randint(1, 100)))]
    while True:
        response = responses[random.randint(1, len(responses))]
        print(colour(106, 100, 230, "What would you like to ask the Magic 8 Ball? Yes/no questions only"))
        question = input(colour(210, 4, 35, "Press '0' to return to main menu\n"))
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
