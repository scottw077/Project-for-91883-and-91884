import random
import time
import json
#creating the colour
def colour(r, g, b, text):
    return "\033[38;2;{};{};{}m{}\033[38;2;255;255;255m".format(r,g,b,text)

#the responses for the magic 8 ball


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
    with open("magic8ballresponses.json","r") as m:
            responses = json.load(m)
    while True:
        response1 = responses[random.randint(0, len(responses) -1)] #chooses a random response
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
            print("\nYour question: {}\nMagic 8 Ball's answer: {}".format(colour(0, 193, 255, question), response1[0])) #prints response
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

        #prints out a random item from the list they selected
        if predefined_lists_input == 0:
            main_menu()
            break

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
        magic8_admin_selector = int(input("Press '0' to return to admin menu\nPress '1' to add response to the magic 8 ball\nPress '2' to remove responses from the magic 8 ball\n"
                                          "Press '3' to see all responses\n"))
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
                print(colour(0, 255, 0, new_response))
                confirmation(new_response, new_response_colour)


            elif new_response_colour == 2:
                print(colour(210, 4, 35, new_response))
                confirmation(new_response, new_response_colour)

            elif new_response_colour == 3:
                print(colour(255, 140, 0, new_response))
                confirmation(new_response, new_response_colour)

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
        elif magic8_admin_selector == 3:
            num = 0
            for response in responses:
                num += 1
                print("{}. {}".format(num, response))
            time.sleep(1.5)
        else:
            print(colour(210, 4, 35, "Invalid input"))
            time.sleep(0.7)

def predefined_lists_backend():
    while True:
        print(colour(255, 195, 30, "Predefined Lists Backend"))
        try:
            predefined_lists_input = int(input("Press '0' to return to admin menu\nPress '1' to create a new predefined list\nPress '2' to remove a predefined list\n"
                                           "Press '3' to add items to an existing predefined list\nPress '4' to remove items from an existing predefined list\n"))
        except:
            print(colour(210, 4, 35, "Invalid value please try again\n"))
            time.sleep(0.5)
        if predefined_lists_input == 0:
            admin_menu()
            break


        elif predefined_lists_input == 1:
            new_predefined_list_title = input("Please enter the name for the new predefined list you are going to create\n")
            new_list_responses  = []
            while True:
                new_list_input_responses = input("Please enter the responses for the list, one at a time.\nPress '0' once you have finished adding the responses\n")
                if new_list_input_responses == "0":
                    break
                else:
                    new_list_responses.append(new_list_input_responses)
                    print(new_list_responses)
                    print(colour(0, 255, 0, "Added\n"))

            while True:
                print(new_predefined_list_title)
                print(new_list_responses)
                confirmation = input("Are you sure you want to add this list?\nPress 'y' for yes and 'n' for no\n").strip().lower()
                if confirmation == "n":
                    predefined_lists_backend()
                    break
                elif confirmation == "y":
                    with open('predefined_lists_titles.json') as titles:
                        predefined_titles = json.load(titles)
                        predefined_titles.append(new_predefined_list_title)
                        with open('predefined_lists_titles.json', 'w') as json_update:
                            json.dump(predefined_titles, json_update)

                    with open('predefined_lists.json') as lists:
                        pre_lists = json.load(lists)
                        pre_lists.append(new_list_responses)
                        with open('predefined_lists.json', 'w') as json_update:
                            json.dump(pre_lists, json_update)
                    print(colour(0, 255, 0, "Successfully created new list!"))
                    break
                else:
                    print(colour(210, 4, 35, "Invalid Input! Please try again"))

        elif predefined_lists_input == 2:
            with open('predefined_lists_titles.json') as titles:
                predefined_list_titles = json.load(titles)

            with open('predefined_lists.json') as lists:
                predefined_list = json.load(lists)
                num = 0

                for title in predefined_list_titles:
                    num += 1
                    print("Press '{}' to remove the list {}".format(num, title))
                predefined_list_del = int(input(colour(255, 195, 30, "What predefined list would you like to delete? Please enter the number next to the response\n")))

                while True:
                    confirmation = input("Are you sure you want to remove this?\nPress 'y' for yes\nPress 'n' for no\n").strip().lower()
                    if confirmation == "n":
                        print(colour(210, 4, 35, "Response has not been removed"))
                        predefined_lists_backend()
                        new_response = ""
                        break

                    elif confirmation == "y":
                        del predefined_list[(predefined_list_del - 1)]
                        del predefined_list_titles[(predefined_list_del - 1)]
                        with open('predefined_lists.json', 'w') as json_update:
                            json.dump(predefined_list, json_update)

                        with open('predefined_lists_titles.json', 'w') as json_update:
                            json.dump(predefined_list_titles, json_update)
                        print("List has been successfully removed")
                        time.sleep(0.8)
                        break

                    else:
                        print(colour(210, 4, 35, "Invalid input please try again"))

        elif predefined_lists_input == 3:
            predefined_input_titles("add")
            while True:
                with open('predefined_lists_titles.json') as titles:
                    predefined_titles = json.load(titles)
                    with open('predefined_lists.json') as lists:
                        predefined_lists = json.load(lists)

                        print("Current Responses: {}".format(predefined_lists[predefined_list_input]))
                        time.sleep(0.8)
                        new_predefined_item = input("What response would you like to add to {}? Press '0' to stop adding responses and return to Predefined Lists Backend\n".format(predefined_titles[predefined_list_input]))
                        if new_predefined_item == "0":
                            predefined_lists_backend()
                            break
                        else:
                            predefined_lists[predefined_list_input].append(new_predefined_item)
                            with open('predefined_lists.json', 'w') as json_update:
                                json.dump(predefined_lists, json_update)

        elif predefined_lists_input == 4:
            predefined_input_titles("remove")
            while True:
                with open('predefined_lists_titles.json') as titles:
                    predefined_titles = json.load(titles)
                    with open('predefined_lists.json') as lists:
                        predefined_lists = json.load(lists)

                        print("Current Responses: {}".format(predefined_lists[predefined_list_input]))
                        time.sleep(0.8)
                        num = 1
                        print("What response would you like to remove from {}? Press '0' to stop removing responses and return to Predefined Lists Backend")
                        for item in predefined_lists[predefined_list_input]:
                            print("Press '{}' to remove {}".format(num, item))
                            num += 1
                        try:
                            remove_predefined_item = int(input())
                            if remove_predefined_item == 0:
                                predefined_lists_backend()
                                break
                            else:
                                remove_predefined_item -= 1
                                del predefined_lists[predefined_list_input][remove_predefined_item]
                                with open('predefined_lists.json', 'w') as json_update:
                                    json.dump(predefined_lists, json_update)
                        except:
                            print(colour(210, 4, 35, "Invalid Value! Please try again"))
                            time.sleep(0.8)
def predefined_input_titles(edit):
    global predefined_list_input
    while True:
        print("Press '0' to return to Predefined Lists Backend")
        num = 0
        with open('predefined_lists_titles.json') as titles:
            predefined_titles = json.load(titles)
            for title in predefined_titles:
                num += 1
                print("Press '{}' to {} responses of {}".format(num, edit, title))
            try:
                predefined_list_input = int(input())
                predefined_list_input -= 1
            except:
                print(colour(210, 4, 35, "Invalid Value! Please try again"))
                time.sleep(0.7)
            if predefined_list_input == 0:
                predefined_lists_backend()
                break
            elif predefined_list_input <= 0 or predefined_list_input > len(predefined_titles) + 1:
                print(colour(210, 4, 35, "Invalid Value! Please try again"))
            else:
                break

def confirmation(new_response, new_response_colour):
    while True:
        confirmation = input("Are you sure you want to add this?\nPress 'y' for yes\nPress 'n' for no\n").strip().lower()
        if confirmation == "n":
            print(colour(210, 4, 35, "Response has not been added"))
            magic_8_ball_backend()
            new_response = ""
            break

        elif confirmation == "y":
            with open("magic8ballresponses.json") as c:
                responses = json.load(c)
                new_list_response = [new_response, new_response_colour -1]
                responses.append(new_list_response)
                with open("magic8ballresponses.json", "w") as json_update:
                    json.dump(responses, json_update)
            print("'{}' has been successfully added to responses".format(new_response))
            break
        else:
            print(colour(210, 4, 35, "Invalid response please try again"))

magic_8_ball_backend()




