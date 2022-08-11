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
                 colour(255, 140, 0, "Please re-enter question"), colour(0, 255, 0, "Yeah obviously"), colour(210, 4, 35, "Clearly not"),
                 colour(0, 255, 0, "Yeah, I am {} percent sure").format((random.randint(1, 100))), colour(210, 4, 35, "No, I am {} percent sure").format((random.randint(1, 100)))]
    while True:
        response = responses[random.randint(0, len(responses))]
        print(colour(106, 100, 230, "\nWhat would you like to ask the Magic 8 Ball? Yes/no questions only"))
        question = input(colour(255, 49, 49, "Press '0' to return to main menu\n"))
        if question == "0":
            main_menu()
            break
        else:
            print("\nYour question: {}\nMagic 8 Ball's answer: {}".format(colour(0, 193, 255, question), response))
            time.sleep(1.4)


def predefined_lists():
    fast_food = ["Subway", "Mcdonald's", "Burger King", "KFC", "Wendy's", "Domino's Pizza", "Pizza Hut", "Carl's Jr"]
    streaming_platforms = ["Netflix", "Disney+", "Neon", "Youtube", "Twitch", "Prime Video", "Hulu", "TVNZ", "Three Now"]
    while True:
        print(colour(106, 100, 230, "\nType in the number corresponding to the List you want a random item from"))
        the_predefined_lists = ("Press '0' to return to main menu\nPress '1' for Fast Food Restaurants\nPress '2' for Streaming Platforms\n"
                            "Press '3' for Burger Type\nPress '4' for Pizza Type\nPress '5' for a Video game\n")
        predefined_lists_input = int(input(the_predefined_lists))
        if predefined_lists_input == 0:
            main_menu()
            break
        elif predefined_lists_input == 1:
            print(fast_food[random.randint(0, len(fast_food) -1)])
        elif predefined_lists_input == 2:
            print(streaming_platforms[random.randint(0, len(streaming_platforms) -1)])




def admin_menu():
    print("pizza")
main_menu()
