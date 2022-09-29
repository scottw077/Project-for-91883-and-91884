if program == "magic8ball":
   with open("magic8ballresponses.json") as c:
      responses = json.load(c)
      new_list_response = [main_value, number_value - 1]
      responses.append(new_list_response)
      with open("magic8ballresponses.json", "w") as json_update:
         json.dump(responses, json_update)
   print("'{}' has been successfully added to responses".format(other_value))
   break


               del main_value[(number_value - 1)]
                del other_value[(number_value - 1)]
                with open('predefined_lists.json', 'w') as json_update:
                    json.dump(main_value, json_update)

                with open('predefined_lists_titles.json', 'w') as json_update:
                    json.dump(other_value, json_update)
                print("List has been successfully removed")
                time.sleep(0.8)
                break

with open('predefined_lists_titles.json') as titles:
   predefined_titles = json.load(titles)
   predefined_titles.append(other_value)
   with open('predefined_lists_titles.json', 'w') as json_update:
      json.dump(predefined_titles, json_update)

with open('predefined_lists.json') as lists:
   pre_lists = json.load(lists)
   pre_lists.append(main_value)
   with open('predefined_lists.json', 'w') as json_update:
      json.dump(pre_lists, json_update)
print(colour(0, 255, 0, "Successfully created new list!"))
break


with open("admins.json") as i:
   admins = json.load(i)
new_admin_user_pass = [main_value, other_value]
admins.append(new_admin_user_pass)
with open("admins.json", "w") as json_update:
   json.dump(admins, json_update)
print(colour(0, 255, 0, "Admin has been added"))
break