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







def predefined_lists():
    print("chicken")





def admin_menu():
    print("pizza")
main_menu()
