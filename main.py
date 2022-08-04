import random
import time

#main menu
def main_menu():
    while True:
        menu = int(input("Press '1' to go to Magic 8 Ball\nPress '2' to go to Random Item from a Predefined List\nPress '0' to end program\n"))
        if menu == 0:
            quit()
        elif menu == 1:
            magic_8_ball()
            break
        elif menu == 2:
            predefined_lists()
            break
        elif menu == 6969:
            admin_menu()
            break
        else:
            print("Invalid input please try again")
            time.sleep(1.2)



def magic_8_ball():
    print("pie")






def predefined_lists():
    print("chicken")





def admin_menu():
    print("pizza")
main_menu()
