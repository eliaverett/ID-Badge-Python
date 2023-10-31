# This is a story of mad libs. I added to the end of the story the line "The "animal" said "statement" and took off into the sunset.
print()
print('Please enter the following:')
print()

adjective = input('Please insert one adjective:')
animal = input('Please input one animal:')
first_verb = input('Please put in your first verb:')
exclamation = input('Please input one exclamation here:')
exclamation = exclamation.capitalize()
second_verb = input('Please input your second verb:')
third_verb = input('Please input your third verb here:')
statement = input('Please input one statement here:')

mad_libs = (f"The other day, I was really in trouble. It all started when I saw a very {adjective} {animal} {first_verb} down the hallway. \"{exclamation.capitalize()}\" I yelled. But all I could think to do was {second_verb} over and over. Miraculously, that caused it to stop, but not before it tried to {third_verb} in front of my family. The {animal} said, \"{statement}\" and took off into the sunset" )

print(mad_libs)

