import random
import time
#creating the colour
def colour(r, g, b, text):
    return "\033[38;2;{};{};{}m{}\033[38;2;255;255;255m".format(r,g,b,text)


#the responses for the magic 8 ball
responses = [colour(210, 4, 35, "My sources say no"), colour(0, 255, 0, "My sources say yes"), colour(255, 140, 0, "I don't know"),
             colour(255, 140, 0, "Please re-enter question"), colour(0, 255, 0, "Yeah obviously"), colour(210, 4, 35, "Clearly not"),
             colour(0, 255, 0, "Yeah, I am {} percent sure").format((random.randint(1, 100))), colour(210, 4, 35, "No, I am {} percent sure").format((random.randint(1, 100)))]
#main menu
def main_menu():
    while True:
        print(colour(255, 195, 30, "Type in the number corresponding to the Program you want to run"))
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
            admin_login_menu()
            break
        else:
            print(colour(210, 4, 35, "Invalid input please try again"))
            time.sleep(.8)



def magic_8_ball():
    while True:
        response1 = responses[random.randint(0, len(responses) -1)] #chooses a random response
        print("\nWhat would you like to ask the Magic 8 Ball? Yes/no questions only")
        question = input(colour(255, 49, 49, "Press '0' to return to main menu\n")) #asks the user the question they would like to ask magic 8 ball
        if question == "0":
            main_menu()
            break #returns to menu
        else:
            print("\nYour question: {}\nMagic 8 Ball's answer: {}".format(colour(0, 193, 255, question), response1)) #prints response
            time.sleep(1.4)


def predefined_lists():
    #the predefined lists
    fast_food = ["Subway", "Mcdonald's", "Burger King", "KFC", "Wendy's", "Domino's Pizza", "Pizza Hut", "Carl's Jr"]
    streaming_platforms = ["Netflix", "Disney+", "Neon", "Youtube", "Twitch", "Prime Video", "Hulu", "TVNZ", "Three Now"]
    burger_type = ["Cheeseburger", "Deluxe Burger", "Chicken Burger", "Steak Burger"]
    pizza_type = ["Pepperoni Pizza", "Cheese Pizza", "Chicken Pizza", "Pepperoni Pizza with Ground Beef and Ailoi",
                  "Ham and Cheese Pizza", "BBQ Meat-lovers pizza", "Veg Pizza"]
    video_games = ["Minecraft", "Terraria", "Fortnite", "GTA", "RDR2", "God of War", "Roblox", "Fall Guys", "LoL", "Valorant",
                   "WoW", "Call of Duty", "Mario-Kart", "Halo", "Cyberpunk 2077", "Wii Sports", "Forza Horizon"]
    while True:
        print(colour(106, 100, 230, "\nType in the number corresponding to the List you want a random item from"))
        the_predefined_lists = ("Press '0' to return to main menu\nPress '1' for Fast Food Restaurants\nPress '2' for Streaming Platforms\n"
                                "Press '3' for Burger Type\nPress '4' for Pizza Type\nPress '5' for a Video game\n") #asks the user what list they would like to use
        predefined_lists_input = int(input(the_predefined_lists))
        #prints out a random item from the list they selected
        if predefined_lists_input == 0:
            main_menu()
            break
        elif predefined_lists_input == 1:
            print(colour(0, 255, 0, fast_food[random.randint(0, len(fast_food)-1)]))
            time.sleep(0.5)
        elif predefined_lists_input == 2:
            print(colour(0, 255, 0, streaming_platforms[random.randint(0, len(streaming_platforms)-1)]))
            time.sleep(0.5)
        elif predefined_lists_input == 3:
            print(colour(0, 255, 0, burger_type[random.randint(0, len(burger_type)-1)]))
            time.sleep(0.5)
        elif predefined_lists_input == 4:
            print(colour(0, 255, 0, pizza_type[random.randint(0, len(pizza_type)-1)]))
            time.sleep(0.5)
        elif predefined_lists_input == 5:
            print(colour(0, 255, 0, video_games[random.randint(0, len(video_games)-1)]))
            time.sleep(0.5)
        else:
            print(colour(210, 4, 35, "That's not a valid option!"))
            time.sleep(0.8)


def admin_login_menu():
    while True:
        admin_login_menu_input = input("Please input a username\nPress '0' to return to main menu\n").strip().lower() #username input
        if admin_login_menu_input == "0": #menu return
            main_menu()
            break
        elif admin_login_menu_input == "scottw":
            admin_pass = input("Please input a password\nPress '0' to return to main menu\n") #password input if username is correct
            if admin_pass == "0": #return to main menu
                main_menu()
                break
            elif admin_pass == "gruiscool123": #if password is correct takes user to admin menu
                print(colour(0, 255, 0, "Successfully signed in"))
                admin_menu()
                break
            else:
                print(colour(210, 4, 35, "Wrong password please try again")) #tells the user the password is incorrect
                time.sleep(1)
        else:
            print(colour(210, 4, 35, "Wrong username please try again")) #tells the user the username is incorrect
            time.sleep(1)


def admin_menu():
    while True:
        print(colour(255, 195, 30, "\nWelcome to The Admin Menu"))
        admin_menu_selector = int(input("Press '0' to return to main menu\nPress '1' to open Magic 8 Ball backend\nPress '2' to open Predefined lists backend\n"))
        if admin_menu_selector == 0:
            main_menu()
            break
        elif admin_menu_selector == 1:
            magic_8_ball_backend()
            break
        elif admin_menu_selector == 2:
            predefined_lists_backend()
            break
        else:
            print(colour(210, 4, 35, "That's not a valid option!"))

def magic_8_ball_backend():
    while True:
        print(colour(255, 195, 30, "Magic 8 Ball Backend"))
        magic8_admin_selector = int(input("Press '0' to return to admin menu\nPress '1' to add response to the magic 8 ball\nPress '2' to remove responses from the magic 8 ball\n"))
        if magic8_admin_selector == 0:
            admin_menu()
            break

        elif magic8_admin_selector == 1:
            new_response = input("Please type the response you want to add\n")
            new_response_colour = int(input("Press '0' to return to admin menu\nPress '1' to add the colour {} to new response\n"
                                            "Press '2' to add the colour {} to new response\nPress '3' to add the colour {} to new response\n".format(colour(0, 255, 0, "green"), colour(210, 4, 35, "red"), colour(255, 140, 0, "orange"))))

            if new_response_colour == 0:
                admin_menu()
                break

            elif new_response_colour == 1:
                new_response = colour(0, 255, 0, new_response)
                print(new_response)
                while True:
                    confirmation = input("Are you sure you want to add this?\nPress 'y' for yes\nPress 'n' for no\n").strip().lower()
                    if confirmation == "n":
                        print(colour(210, 4, 35, "Response has not been added"))
                        magic_8_ball_backend()
                        new_response = ""
                        break
                        break
                    elif confirmation == "y":
                        responses.append(new_response)
                        print("'{}' has been successfully added to responses".format(new_response))
                        break
                    else:
                        print(colour(210, 4, 35, "Invalid response please try again"))


            elif new_response_colour == 2:
                new_response = colour(210, 4, 35, new_response)
                print(new_response)
                while True:
                    confirmation = input("Are you sure you want to add this?\nPress 'y' for yes\nPress 'n' for no\n").strip().lower()
                    if confirmation == "n":
                        print(colour(210, 4, 35, "Response has not been added"))
                        magic_8_ball_backend()
                        new_response = ""
                        break
                        break
                    elif confirmation == "y":
                        responses.append(new_response)
                        print("'{}' has been successfully added to responses".format(new_response))
                        break
                    else:
                        print(colour(210, 4, 35, "Invalid response please try again"))

            elif new_response_colour == 3:
                new_response = colour(255, 140, 0, new_response)
                print(new_response)
                while True:
                    confirmation = input("Are you sure you want to add this?\nPress 'y' for yes\nPress 'n' for no\n").strip().lower()
                    if confirmation == "n":
                        print(colour(210, 4, 35, "Response has not been added"))
                        magic_8_ball_backend()
                        new_response = ""
                        break
                        break
                    elif confirmation == "y":
                        responses.append(new_response)
                        print("'{}' has been successfully added to responses".format(new_response))
                        break
                    else:
                        print(colour(210, 4, 35, "Invalid response please try again"))
            else:
                print(colour(210, 4, 35, "Invalid option please try again"))

        elif magic8_admin_selector == 2:
            while True:
                num = 0
                for response in responses:
                    num += 1
                    print("{}. {}".format(num, response))
                try:
                    response_del = int(input("What response would you like to delete? Please enter the number next to the response\n"))
                    del responses[(response_del-1)]
                    print(colour(210, 4, 35, "Response successfully removed"))
                    break
                except:
                    print(colour(210, 4, 35, "Please enter a valid number\n"))
                    time.sleep(0.8)

        else:
            print(colour(210, 4, 35, "Invalid input"))
            time.sleep(0.8)

def predefined_lists_backend():
    while True:
        print(colour(255, 195, 30, "Predefined Lists Backend"))
        predefined_lists_input = int(input("Press '0' to return to admin menu\nPress '1' to add a new predefined list\nPress '2' to remove a predefined list\n"
                                           "Press '3' to add items to an existing predefined list\nPress '4' to remove items from an existing predefined list\n"))
        if predefined_lists_input == 0:
            admin_menu()
            break
        elif predefined_lists_input == 1:
            new_predefined_list = input("Please enter the name for the new predefined list you are going to create")
        elif predefined_lists_input == 2:


main_menu()
