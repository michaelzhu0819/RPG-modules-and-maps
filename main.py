# Python modules and maps - text based adventure game
# Michael Zhu
# Oct 6th, 2021
# CS30
# Ms.Cotcher

# Importing all of the modules
import mapping
import character
import inventory
import sys
import time

""" This is the menu for a game where you are an adventurer trying to escape
a wasteland with a locked door, navigate through the biome with four
movements, encounter and defeat enemies, collect resources, and try to find
the key to the door. Now comes with mulitple modules,two inventories,
a map showing potential locations,along with descriptions for potential
characters and locations in the main menu"""

""" These variables set up the catagories for actions and the coordinate
system, the dictionaries holding your two inventories by executing the
inventory module, and the dictionaries holding descriptions for character
and location, health, attack and focus points are introduced"""

x = 0
y = 0

health = 0
attack = 0
focus = 0
heal = 5

choice = 0

# The options for menus
general_action = ["explore", "combat", "character selection"]
explore = ["forward", "backward", "left", "right", "inventory", "quit"]
combat = ["attack", "dodge", "defend", "inventory", "quit"]

# exploration inventory
exploring_bag = {}
exploring_bag = inventory.explore_inv(exploring_bag)

# Combat inventory
combat_pouch = {}
combat_pouch = inventory.combat_inv(combat_pouch)

# Potential characters and their descriptions
characters = ["beserker", "healer", "mage", "tank"]

# Print out to verify that all modules are imported successfully
if "inventory" in sys.modules and "character" in sys.modules and \
        "inventory" in sys.modules:
    print("Successfully imported character, inventory and mapping modules")
time.sleep(2)

""" The while loop that makes sure the general menu is running constantly until
quit is inputted, during this you can either select explore or combat"""
while True:
    print("\nyou can do the following catagory of actions:")
    for i in general_action:
        print (i)
    print("side note: you can type quit to quit anytime\n")
    time.sleep(1)
    cata_input = input("\nwhich one do you choose?\n")

    # The section is what happens when you select explore, it constantly
    # loops and ask for input until you type quit which will return to the
    # general menu
    if cata_input.lower() == general_action[0]:
        mapping.Map()
        time.sleep(1)
        if choice > 0:
            print(f"you are playing as {characters[choice-1]}")
        while True:
            print("\nu can go either")
            for option in explore:
                print(option)
            time.sleep(1)
            direction_input = input("\nwhich one do you choose?\n")
            time.sleep(1)

            # The coordinate system
            if direction_input.lower() in explore:
                print("\n" + direction_input.lower() + "!\n")
                coord_change = direction_input.lower()
                if coord_change == explore[0]:
                    y += 1
                    print("your y value increased by one, " +
                          "your coord now is " + str(x)+" ," + str(y))
                elif coord_change == explore[1]:
                    y -= 1
                    print("your y value decreased by one, " +
                          "your coord now is " + str(x)+" ," + str(y))
                elif coord_change == explore[2]:
                    x -= 1
                    print("your x value decreased by one, " +
                          "your coord now is " + str(x) + " ," + str(y))
                elif coord_change == explore[3]:
                    x += 1
                    print("your x value increased by one, " +
                          "your coord now is " + str(x) + " ," + str(y))

                # Displays your exploration inventory
                elif direction_input.lower() == explore[4]:
                    for item in exploring_bag:
                        print(f"^{item}^:")
                        for thing in exploring_bag[item]:
                            print(f"{thing} - {exploring_bag[item][thing]}")
                        print("\n")
                elif direction_input.lower() == explore[5]:
                    print("going back to the main menu\n")
                    break
            else:
                print("invalid action!")

    # Happens when selecting combat in main menu, constantly loops
    # till quit is inputted
    elif cata_input.lower() == general_action[1]:
        while True:
            print("\nu can do either")
            for action_type in combat:
                print(action_type)
            time.sleep(1)
            combat_input = input("\nwhich one do you choose?\n")
            if combat_input.lower() in combat:
                print("\n" + combat_input.lower() + "!\n")

                # Shows you all the accessories in the combat inventory and
                # lets you choose one of them and use it"""
                if combat_input.lower() == combat[0]:
                    combat_pouch = inventory.combat_inv(combat_pouch)
                    print("You have:\n")
                    for item in combat_pouch:
                        print(f"- {item}")
                    time.sleep(1)
                    combat_input_2 = input("\nWhich one do you want to use?\n")
                    if combat_input_2.lower() in combat_pouch:
                        print(f"You used {combat_input_2.lower()}!")
                    elif combat_input_2.lower() == "quit":
                        print("\nreturning to combat menu")
                        break
                    else:
                        print("invalid action!")

                # displays your combat inventory
                elif combat_input.lower() == combat[3]:
                    for item in combat_pouch:
                        print(f"^{item}^:")
                        for info in combat_pouch[item]:
                            print(f"{info}- {combat_pouch[item][info]}")
                        print("\n")

                # breaks the loop if inputted quit
                elif combat_input.lower() == combat[4]:
                    print("going back to the main menu")
                    break

            # accepts wrong inputs
            else:
                print("invalid action!")

    # prints descriptions of characters as statements if inputted characters
    elif cata_input.lower() == general_action[2]:
        print("\nYou can choose the following characters:\n")
        for i in characters:
            print(i)
        time.sleep(1)
        character_input = input("\nwhich one do you choose?\n")

        # Selecting characters
        if character_input.lower() == characters[0]:
            print(f"you have chosen {characters[0]}")
            choice = 1
            character.beserker(health, attack, focus)
        elif character_input.lower() == characters[1]:
            print(f"you have chosen {characters[1]}")
            character.healer(health, attack, focus, heal)
            choice = 2
        elif character_input.lower() == characters[2]:
            print(f"you have chosen {characters[2]}")
            character.mage(health, attack, focus)
            choice = 3
        elif character_input.lower() == characters[3]:
            print(f"you have chosen {characters[3]}")
            character.tank(health, attack, focus)
            choice = 4
        else:
            print("invalid action!")

    # Breaks the loop when inputted quit and accepts wrong inputs
    elif cata_input.lower() == "quit":
        break
    else:
        print("invalid action!")
        time.sleep(1)
