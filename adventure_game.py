#This is a fun video game I made! I decided to be entirely creative and make a video game I could control entirely. 
print("This is a text based video game. The user will be given options to choose from to see if they can make it out of the cave alive and escape Gollum and the goblins that surround the cave!")
print()

def start_story():
    
    print("You slipped down the wrong hole in the Mines of Moria and you find yourself face to face with Gollum and can hear goblins all around you! The ring is not here so it cannot save you. Gollum is slowly making his way over to you. Luckily, you fell with a torch and a sword! You only have one hand free as your other hand was hurt bad during the fall!")
    initial_choice = input("Do you choose the TORCH or SWORD?").lower()

    if initial_choice == "torch":
        torch_plotline()
    elif initial_choice == "sword":
        sword_plotline()
    else:
        print("Invalid choice. Please choose either TORCH or SWORD.")
        start_story()

def torch_plotline():
    print("With a torch to light your way, you slowly make your way through the caves dodging spiders and cave trolls. You stumble across a pond and look into it. There is a talking fish who tells you that the exit is right across the pond. He will go and get the boat for you and take you across if you can tell him what his favorite food is. You know this fish is a leaping carp and their favorite food is either JUMPING CAVE FROGS or STICKY MOTHS.")
    favorite_food = input("Is his favorite food JUMPING CAVE FROGS or STICKY MOTHS?").lower()

    if favorite_food == "jumping cave frogs":
        print("You guessed correctly! His favorite food is jumping cave frogs! He goes and grabs the boat and takes you across the pond. You begin the final trek to hopefully find your exit!")
        exit_story()
    elif favorite_food == "sticky moths":
        print("You guessed incorrectly. The fish is offended and tells you to go away. He does not grab the boat for you. You have to find another way around the pond as the pond is too cold to swim in. You walk around the pond but get hit in the face by a stink shooting spider. You are now blind in one eye.")
        exit_story()
    else:
        print("Invalid choice. Please choose either JUMPING CAVE FROGS or STICKY.") 
        torch_plotline()

def sword_plotline():
    print("You grab the sword and prepare for a fight. Gollum lunges at you, and you manage to fend him off, but you are wounded in the process. You'll need to find another way out of the Mines of Moria with your injuries.")
    print()
    print("You walk around the cave, but with no source of light you find it difficult to be able to figure out where you are going. You feel like you are walking in circles. You stumble across a rock and fall. When you look up, you see two stones in front of you. One red and one turquoise.")
    stone_choice = input("Do you choose the red or turquoise?").lower()

    if stone_choice in "red stone":
        print("You have picked up a stone of pathfinding! This stone will help you find the nearest exit but it may not be the right one you are looking for. You can follow the path that is laid in front of you now and also have a source of light that eminates from the red stone.")
        exit_story()
    elif stone_choice in "turquoise stone":
        print("You have grabbed the Queen Goblins' precious stone! Now all the goblins can track you down! You fight them off whilst running through the cave looking for an exit. Soon enough, a landslide comes crashing down behind you and stops all the goblins from attacking you.")
        exit_story()
    else:
        print("Invalid choice. Please choose between RED or TURQUOISE.")
        sword_plotline()

def exit_story():
    print("You have found the exit! But is it the one you hope for? There are 3 exits laid in front of you. One with a picture of a GOOSE, one with a picture of a BOAR, and one with a picture of a DRAGON! Which one do you choose?")
    exit_choice = input("Do you choose the GOOSE, BOAR, OR DRAGON?").lower()

    if exit_choice == "goose":
        print("You have found the queen goblin and she has set a trap for you! You get trapped in a cage with no chance to escape and taken back to the goblins lair never to be seen again! This is the end of your journey.")
    elif exit_choice == "boar":
        print("You have found the exit! Gandalf is jumping for joy to see you again! Enjoy your travels! The end.")
    elif exit_choice == "dragon":
        print("You have found the dragon of the deep! He shoots fire at you and burns you to a crisp! Better luck next time!")
    else:
        print("Invalid choice. Please choose goose, boar, or dragon.")
        exit_story()

def main():
    print("This is a text based video game. The user will be given options to choose from to see if they can make it out of the cave alive and escape Gollum and the goblins that surround the cave!")
    print()
    start_story()

if __name__ == "__main__":
    main()
