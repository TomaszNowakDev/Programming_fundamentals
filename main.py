# Tomasz Nowak
# 07 DEC 2020
# Blackwater Annual Concert, The program collects data about performers from the user and saves them in a file. \
# Generates a list of performers to display.

# Setting up choice menus as constants:
MAIN_MENU = "Blackwater Annual Concert \n---------------------------- \n1. Adding Performers" \
            + "\n2. Generate Concert Details \n3. Quit" \

PERFORMANCE_TYPE = "Type of Performance \n---------------------------- \n\t1. Musical" \
                   + "\n\t2. Singer \n\t3. Dancer" \

# Asking the user to select an option:
print(MAIN_MENU)
choice_main = int(input("==>"))

# Main loop
while True:
    # option 1, entering data.
    if choice_main == 1:
        print("(1) Adding Performers \n----------------------------")
        performers = int(input("How many performers are you adding: "))
        performers_details = ''
        number_to_display = 0
        num_musicians = 0
        num_singers = 0
        num_dancers = 0
        total_time_required = 0
        performers_details_for_screen = ''
        longest = ''
        long = 0

        for i in range(1, performers + 1):

            print(f" \nPerformer {i}/{performers}:")
            name = input("Enter your name: ")
            surname = input("Enter your surname: ")
            performers_details += surname + ' ' + name + ' '
            number_to_display += 1
            performers_details_for_screen += str(number_to_display) + '. ' + surname + ',' + name + '\t\t'

            print(PERFORMANCE_TYPE)
            choice_performance = int(input("==>"))
            if choice_performance == 1:
                num_musicians += 1
                choice_performance = "Musician"
            elif choice_performance == 2:
                num_singers += 1
                choice_performance = "Singer"
            elif choice_performance == 3:
                num_dancers += 1
                choice_performance = "Dancer"

            performers_details += choice_performance + ' '
            time_slot_required = int(input("Time slot required (mins): "))
            # The longest act
            if long < time_slot_required:
                long_name = name
                long_surname = surname
                long_choice_performance = choice_performance
                long_time_slot_required = time_slot_required
                longest = f'The longest act added is {long_name} {long_surname}({long_choice_performance})' \
                          f' {long_time_slot_required} minutes.\n'
                long = time_slot_required

            total_time_required = total_time_required + time_slot_required
            performers_details_for_screen += choice_performance + '\t\t' + str(time_slot_required) + ' minutes.' + '\n'
            performers_details += (str(time_slot_required)) + '\n'
        # printing what information has been added an saving to the file.
        print('\nThe following information has been added.\n')

        with open("performers.txt", 'a') as performers_file:
            print(performers_details[0:-1], file=performers_file)

        print(performers_details_for_screen[0:-1])

        # printing summary notes.
        print('\nSummary Notes:\n------------------------')
        print(f'{num_musicians} Musicians')
        print(f'{num_singers} Singers')
        print(f'{num_dancers} Dancers')
        hours = total_time_required // 60
        minutes = total_time_required % 60
        print(f'Total time required: {hours} hours, {minutes} mins.')
        print(longest)

    # option 2 reading from a file.
    elif choice_main == 2:
        print("(2) Generate Concert Details \n--------------------------------------")
        try:
            with open("performers.txt", 'r') as performers_file:
                counter = 0
                fname = ''
                lname = ''
                performer_type = ''
                time_from_line = ''
                for line in performers_file:
                    counter += 1
                    line_a = line.rstrip()
                    contents = line_a
                    fname, lname, performer_type, time_from_line = contents.split()
                    # if act is longer than 15min print"*" next to the name.
                    if int(time_from_line) > 15:
                        print(f'{counter}: {fname},{lname}*      ({performer_type}){time_from_line:>10} minutes.')
                    else:
                        print(f'{counter}: {fname},{lname:<10}({performer_type}){time_from_line:>10} minutes.')
        except IOError:
            print("Could not find the file.\n")

    # option 3, exit.
    elif choice_main == 3:
        break

    else:
        print("Choose one of the options from 1 to 3.")
    print(MAIN_MENU)
    choice_main = int(input("==>"))
