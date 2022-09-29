import random
import time
import json
#creating the colour
def colour(r, g, b, text):
    return "\033[38;2;{};{};{}m{}\033[38;2;255;255;255m".format(r,g,b,text)

#main menu
def main_menu(): #this is the main menu/hub of the code and this code connects all the programs together
    while True:
        print(colour(255, 195, 30, "Type in the number corresponding to the Program you want to run"))
        menu = input("Press '0' to end program\nPress '1' to go to Magic 8 Ball\nPress '2' to go to Random Item from a Predefined List\nPress '3' to open Admin login menu\n") #asks the user what program they want to run
        if menu == "0":
            quit()
        elif menu == "1":
            magic_8_ball()
            break
        elif menu == "2":
            predefined_lists()
            break
        elif menu == "3":
            admin_login_menu()
            break
        else:
            print(colour(210, 4, 35, "Invalid input please try again"))
            time.sleep(.8)


def magic_8_ball():
    with open("magic8ballresponses.json","r") as m:
            responses = json.load(m)
    while True:
        response1 = responses[random.randint(0, len(responses) -1)] #randomly gets a response
        if response1[1] == 0:
            response1[0] = colour(0, 255, 0, response1[0])
        elif response1[1] == 1:
            response1[0] = colour(210, 4, 35, response1[0])
        elif response1[1] == 2:
            response1[0] = colour(255, 140, 0, response1[0])
        print("\nWhat would you like to ask the Magic 8 Ball? Yes/no questions only")
        question = input(colour(255, 49, 49, "Press '0' to return to main menu\n")) #asks the user the question they would like to ask magic 8 ball
        if question == "0":
            main_menu()
            break #returns to menu
        else:
            print("\nYour question: {}\nMagic 8 Ball's answer: {}".format(question, response1[0])) #prints response
            time.sleep(1.4)


def predefined_lists():
    while True:
        print(colour(106, 100, 230, "\nType in the number corresponding to the List you want a random item from"))
        print("Press '0' to return to main menu")
        num = 0
        with open('predefined_lists_titles.json', 'r') as f:
            titles = json.load(f)
            for title in titles:
                num += 1
                print("Press '{}' for {}".format(num, title))
            predefined_lists_input = int(input())

        #redirecting the user to the main menu
        if predefined_lists_input == 0:
            main_menu()
            break
        #prompting the user that you cannot input negative numbers
        elif predefined_lists_input < 0:
            print(colour(210, 4, 35, "Please do not input negative numbers!"))
            time.sleep(0.5)
        # prints out a random item from the list they selected
        else:
            try:
                dict = open('predefined_lists.json')
                predefined_list = json.load(dict)
                list_user_wants = (predefined_list[predefined_lists_input -1])
                print(list_user_wants[random.randint(0, len(list_user_wants)-1)])
                time.sleep(0.7)
            except:
                print(colour(210, 4, 35, "Invalid Input! Please try again"))
                time.sleep(1.2)

# this allows users to access the admin menu
def admin_login_menu():
    while True:
        with open("admins.json") as o: #getting the current admins and their passwords
            admins = json.load(o)
        users = [user[0] for user in admins] #making only the users into one variable
        admin_login_menu_input = input("Please input a username\nPress '0' to return to main menu\n").strip().lower() #asks the user for the username
        if admin_login_menu_input == "0": #returns the user to the main menu
            main_menu()
            break
        elif admin_login_menu_input in users: # if the username is correct asks the user for the password
            position = users.index(admin_login_menu_input) # gets the position of the admin in order to check if it's their password and not another admin's
            admin_pass = input("Please input a password\nPress '0' to return to main menu\n")
            if admin_pass == "0":
                main_menu()
                break
            elif admin_pass in admins[position][1]:
                print(colour(0, 255, 0, "Successfully signed in"))
                admin_menu()
                break
            else:
                print(colour(210, 4, 35, "Wrong password please try again")) #tells the user that the password they entered is incorrect
                time.sleep(1)
        else:
            print(colour(210, 4, 35, "Wrong/invalid username please try again")) #tells the user that the username is incorrect/invalid
            time.sleep(1)


def admin_menu():
    # this is the hub of all the admin programs which connects all the programs together
    while True:
        print(colour(255, 195, 30, "\nWelcome to The Admin Menu"))
        admin_menu_selector = int(input("Press '0' to return to main menu\nPress '1' to open Magic 8 Ball backend\nPress '2' to open Predefined lists backend\nPress '3' to add/remove admins\n"))
        if admin_menu_selector == 0:
            main_menu()
            break
        elif admin_menu_selector == 1:
            magic_8_ball_backend()
            break
        elif admin_menu_selector == 2:
            predefined_lists_backend()
            break
        elif admin_menu_selector == 3:
            admin_backend()
            break
        else:
            print(colour(210, 4, 35, "That's not a valid option!"))


def admin_backend():
    while True:
        print(colour(255, 195, 30, "Welcome to the Admin Backend")) # asks the user what they would like to do in the admin backend
        admin_backend_selector = int(input("Press '0' to return to admin menu\nPress '1' to add a new admin\nPress '2' to remove an admin\nPress '3' to see all admins and their passwords\n"))


        if admin_backend_selector == 0:
            admin_menu()


        elif admin_backend_selector == 1:
            new_admin_user = input("Please create a username for the new admin\n")
            with open("admins.json") as j: # opens the admin json and checks if the username the user inputted is already taken
                admins = json.load(j)
                existing_users = [existing_user[0] for existing_user in admins]
                if new_admin_user in existing_users:
                    print(colour(210, 4, 35, "Username already exists!"))
                else: # asks the user for a password for this new admin
                    new_admin_pass = input("Please create a password for the new admin\n")
                    print("Username: " + new_admin_user)
                    print("Password: " + new_admin_pass)
                    confirmation(new_admin_user, 0, new_admin_pass, "admin", "add") # sends the user to the confirmation function


        elif admin_backend_selector == 2:
            with open("admins.json") as u: # gets the current admins and their passwords
                admins = json.load(u)
                usernames = [username[0] for username in admins] #makes it only their usernames
                def admin_usernames(): # prints out all of the admins usernames
                    num = 1
                    print("Press '0' to return to {}".format(colour(255, 195, 30, "admin backend")))
                    for username in usernames:
                        print("Press '{}' to remove {} as admin".format(num, colour(255, 195, 30, username)))
                        num += 1
                try:
                    admin_usernames()
                    admin_remove_input = int(input())
                    if admin_remove_input == 0:
                        admin_backend()
                    while admin_remove_input < 0 or admin_remove_input > len(admins): # checks if number is invalud
                        print(colour(210, 4, 35, "Invalid value entered! Please try again"))
                        time.sleep(0.8)
                        admin_usernames()
                        admin_remove_input = int(input())
                    del admins[admin_remove_input - 1] # deletes the admin and their password from the json
                    with open("admins.json", "w") as json_update:
                        json.dump(admins, json_update)
                    print(colour(0, 255, 0, "Successfully removed admin"))
                except:
                    print(colour(210, 4, 35, "Please enter a valid number!"))


        elif admin_backend_selector == 3:
            with open("admins.json") as b: # gets the current admins
                admins = json.load(b)
                for admin_user, admin_pass in admins: # gets the admins usernames and passwords
                    print("Username: {}\nPassword: {}\n".format(admin_user, admin_pass))
                print("Total number of admins: {}".format(len(admins)))
                time.sleep(1)


def magic_8_ball_backend():
    while True:
        print(colour(255, 195, 30, "Magic 8 Ball Backend"))
        magic8_admin_selector = int(input("Press '0' to return to admin menu\nPress '1' to add response to the magic 8 ball\nPress '2' to remove responses from the magic 8 ball\n"
                                          "Press '3' to see all responses\n")) # asks the user what they would like to do with the magic 8 ball responses
        if magic8_admin_selector == 0: # returns user to admin menu
            admin_menu()
            break

        elif magic8_admin_selector == 1:
            new_response = input("Please type the response you want to add\n")
            new_response_colour = int(input("Press '0' to return to admin menu\nPress '1' to add the colour {} to new response\n"
                                            "Press '2' to add the colour {} to new response\nPress '3' to add the colour {} to new response\n".format(colour(0, 255, 0, "green"), colour(210, 4, 35, "red"), colour(255, 140, 0, "orange"))))
            if new_response_colour == 0:
                admin_menu()
                break

            elif new_response_colour == 1: # makes the response the colour the admin chooses and sends it to the confirmation code
                new_resp_with_colour = colour(0, 255, 0, new_response)
                print(new_resp_with_colour)
                confirmation(new_response, new_response_colour, new_resp_with_colour, "magic8ball", "add")


            elif new_response_colour == 2:
                new_resp_with_colour = colour(210, 4, 35, new_response)
                print(new_resp_with_colour)
                confirmation(new_response, new_response_colour, new_resp_with_colour, "magic8ball", "add")

            elif new_response_colour == 3:
                new_resp_with_colour = colour(255, 140, 0, new_response)
                print(new_resp_with_colour)
                confirmation(new_response, new_response_colour, new_resp_with_colour, "magic8ball", "add")
            else:
                print(colour(210, 4, 35, "Invalid option please try again"))


        elif magic8_admin_selector == 2:
            while True: # opens the magic 8 ball responses
                with open("magic8ballresponses.json") as k:
                    responses = json.load(k)
                num = 0
                for response in responses: # prints out all the current responses
                    num += 1
                    print("Press '{}' to remove {}".format(num, response[0]))
                try: # deletes the response the user chooses then writes it back to the json file
                    response_del = int(input("What response would you like to delete? Please enter the number next to the response\n"))
                    del responses[(response_del-1)]
                    with open("magic8ballresponses.json", "w") as json_update:
                        json.dump(responses, json_update)
                    print(colour(210, 4, 35, "Response successfully removed"))
                    break
                except:
                    print(colour(210, 4, 35, "Please enter a valid number\n"))
                    time.sleep(0.8)


        elif magic8_admin_selector == 3:
            num = 0
            with open("magic8ballresponses.json") as o: # opens the current responses from the json file
                responses = json.load(o)
            for response in responses: # prints the current responses
                num += 1
                print("{}. {}".format(num, response[0]))
            response_colour = [response[1] for response in responses]
            # prints the number of yes/no/don't know responses
            print("Number of {} responses: {}".format(colour(0, 255, 0, "yes"), response_colour.count(0)))
            print("Number of {} responses: {}".format(colour(210, 4, 35, "no"), response_colour.count(1)))
            print("Number of {} responses: {}".format(colour(255, 140, 0, "don't know"), response_colour.count(2)))
            time.sleep(2.7)
        else:
            print(colour(210, 4, 35, "Invalid input"))
            time.sleep(0.7)


def predefined_lists_backend():
    while True:
        print(colour(255, 195, 30, "Predefined Lists Backend"))
        try: # asks the user what they would like to do with the predefined list responses
            predefined_lists_input = int(input("Press '0' to return to admin menu\nPress '1' to create a new predefined list\nPress '2' to remove a predefined list\n"
                                           "Press '3' to add items to an existing predefined list\nPress '4' to remove items from an existing predefined list\n"))
        except:
            print(colour(210, 4, 35, "Invalid value please try again\n"))
            time.sleep(0.5)

        if predefined_lists_input == 0: # returns user back to admin menu
            admin_menu()
            break


        elif predefined_lists_input == 1:
            new_predefined_list_title = input("Please enter the name for the new predefined list you are going to create\n") #asks the user for the title of the new predef list
            new_list_responses  = []
            while True:
                new_list_input_responses = input("Please enter the responses for the list, one at a time.\nPress '0' once you have finished adding the responses\n")
                if new_list_input_responses == "0":
                    break
                else:
                    new_list_responses.append(new_list_input_responses) # adding the users responses to the list
                    print(new_list_responses)
                    print(colour(0, 255, 0, "Added\n"))

            print(new_predefined_list_title)
            print(new_list_responses)
            confirmation(new_list_responses, 0, new_predefined_list_title, "predeflists", "add")

        elif predefined_lists_input == 2:
            with open('predefined_lists_titles.json') as titles: # accessing the current titles and their items
                predefined_list_titles = json.load(titles)

            with open('predefined_lists.json') as lists:
                predefined_list = json.load(lists)
                num = 0

                for title in predefined_list_titles: # printing out the lists
                    num += 1
                    print("Press '{}' to remove the list '{}'".format(num, title))
                predefined_list_del = int(input(colour(255, 195, 30, "What predefined list would you like to delete? Please enter the number next to the response\n")))

                confirmation(predefined_list, predefined_list_del, predefined_list_titles, "predeflists", "remove")

        elif predefined_lists_input == 3:
            predefined_input_titles("add") # asks the admin what title they would like to add items to
            while True: # opens the titles and lists json
                with open('predefined_lists_titles.json') as titles:
                    predefined_titles = json.load(titles)
                    with open('predefined_lists.json') as lists:
                        predefined_lists = json.load(lists)

                        print("Current Responses: {}".format(predefined_lists[predefined_list_input])) # prints out the items from the admin selected titles
                        time.sleep(0.8)
                        # asks the admin for the item they would like to add
                        new_predefined_item = input("What response would you like to add to {}?\nPress '0' to stop adding responses and return to Predefined Lists Backend\n".format(predefined_titles[predefined_list_input]))
                        if new_predefined_item == "0": # sends the admin back to the predef list menu
                            predefined_lists_backend()
                            break
                        else: # adds the response to the json
                            predefined_lists[predefined_list_input].append(new_predefined_item)
                            with open('predefined_lists.json', 'w') as json_update:
                                json.dump(predefined_lists, json_update)
                            print(colour(0, 255, 0, "Response successfully added"))

        elif predefined_lists_input == 4:
            predefined_input_titles("remove") # asks the user what title they would like to remove
            while True:
                with open('predefined_lists_titles.json') as titles: # opens the json files
                    predefined_titles = json.load(titles)
                    with open('predefined_lists.json') as lists:
                        predefined_lists = json.load(lists)

                        print("Current Responses: {}".format(predefined_lists[predefined_list_input])) # prints the current responses from the list the admin has selected
                        time.sleep(0.8)
                        num = 1
                        print("What response would you like to remove from {}?\n\nPress '0' to stop removing responses and return to Predefined Lists Backend".format(predefined_titles[predefined_list_input]))
                        for item in predefined_lists[predefined_list_input]: # prints responses
                            print("Press '{}' to remove {}".format(num, item))
                            num += 1
                        try:
                            remove_predefined_item = int(input())
                            if remove_predefined_item == 0: # returns to predefined list backend
                                predefined_lists_backend()
                                break
                            else: # deletes the response from the list and writes it back to the json file
                                remove_predefined_item -= 1
                                del predefined_lists[predefined_list_input][remove_predefined_item]
                                with open('predefined_lists.json', 'w') as json_update:
                                    json.dump(predefined_lists, json_update)
                                print(colour(0, 255, 0, "Response successfully {}".format(colour(210, 4, 35, "removed"))))
                        except:
                            print(colour(210, 4, 35, "Invalid Value! Please try again"))
                            time.sleep(0.8)


def predefined_input_titles(edit):
    global predefined_list_input
    while True:
        print("Press '0' to return to {}".format(colour(210, 195, 30, "Predefined Lists Backend")))
        num = 0
        with open('predefined_lists_titles.json') as titles: # opens json file
            predefined_titles = json.load(titles)
            for title in predefined_titles:
                num += 1
                print("Press '{}' to {} responses from/to {}".format(num, edit, colour(210, 195, 30, title))) # prints the predef list titles
            try:
                predefined_list_input = int(input())
                predefined_list_input -= 1
            except:
                print(colour(210, 4, 35, "Invalid Value! Please try again"))
                time.sleep(0.7)
            # checks if number is invalid
            if predefined_list_input == 0:
                predefined_lists_backend()
                break
            elif predefined_list_input <= 0 or predefined_list_input > len(predefined_titles) + 1:
                print(colour(210, 4, 35, "Invalid Value! Please try again"))
            else:
                break


def confirmation(program, edit):
    while True:
        confirmation = input("Are you sure you want to {} this?\nPress 'y' for yes\nPress 'n' for no\n".format(edit)).strip().lower()
        if confirmation == "n":
            if program == "magic8ball":
                print(colour(210, 4, 35, "Response has not been added"))
                magic_8_ball_backend()
                new_response = ""
                break
            elif program == "predeflists":
                if edit == "remove":
                    print(210, 4, 35, "Response has not been removed")
                    predefined_lists_backend()
                    break
                else:
                    print(colour(210, 4, 35, "Response has not been added"))
                    predefined_lists_backend()
                    break

            elif program == "admin":
                admin_backend()
                break

        elif confirmation == "y":
            break
        else:
            print(colour(210, 4, 35, "Invalid response please try again"))


main_menu()




