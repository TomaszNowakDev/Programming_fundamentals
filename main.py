# Tomasz Nowak
# 07 DEC 2020
# Blackwater Annual Concert, The program collects data about performers from the user and saves them in a file. \
# Generates a list of performers to display.

# Setting up choice menus as constants:
MAIN_MENU = "Blackwater Annual Concert \n---------------------------- \n1. Adding Performers" \
            + "\n2. Generate Concert Details \n3. Quit" \

print(MAIN_MENU)
choice_main = int(input("==>"))
while True:
    # option 1, entering data.
    if choice_main == 1:
        print("(1) Adding Performers \n----------------------------")

    # option 2 reading from a file.
    elif choice_main == 2:
        print("(2) Generate Concert Details \n----------------------------\n")

    # option 3, exit.
    elif choice_main == 3:
        break

    else:
        print("Choose one of the options from 1 to 3.")
    print(MAIN_MENU)
    choice_main = int(input("==>"))
