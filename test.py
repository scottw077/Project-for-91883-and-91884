elif predefined_lists_input == 1:
   print(fast_food[random.randint(0, len(fast_food)-1)])
   time.sleep(0.7)
elif predefined_lists_input == 2:
   print(streaming_platforms[random.randint(0, len(streaming_platforms)-1)])
   time.sleep(0.7)
elif predefined_lists_input == 3:
   print(burger_type[random.randint(0, len(burger_type)-1)])
   time.sleep(0.7)
elif predefined_lists_input == 4:
   print(pizza_type[random.randint(0, len(pizza_type)-1)])
   time.sleep(0.7)
elif predefined_lists_input == 5:
   print(video_games[random.randint(0, len(video_games)-1)])
   time.sleep(0.7)
else:
   print(colour(210, 4, 35, "That's not a valid option!"))
   time.sleep(0.8)
