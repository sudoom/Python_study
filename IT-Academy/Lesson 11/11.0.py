import figure
print('\nChoose what we go calculated')
choice = ''
while choice != 'q':
    print("\n[p] Enter p to calculate perimetr.")
    print("\n[a] Enter a to calculate area.")
    print("\n[q] Enter q to exit.")
    choice = input("\nWhat would you like to do? ")
    if choice == 'a':
        print("\n[1] Enter 1 to calculate triangle area.")
        print("\n[2] Enter 2 to calculate rectangle area.")
        print("\n[3] Enter 3 to calculate square area.")
        print("\n[4] Enter 4 to calculate trapezoid area.")
        print("\n[5] Enter 5 to calculate circle area.")
        choice = input("\nWhat figure would you like to calculate? ")
        if choice == '1':
            x = int(input('Enter first side: ',))
            y = int(input('Enter second side: ',))
            z = int(input('Enter third side: ',))
            print('Triangle area is ', figure.tri_area(x, y, z))
        elif choice == '2':
            x = int(input('Enter first side: ',))
            y = int(input('Enter second side: ',))
            if x == y:
                print('Square area is ', figure.square_area(x))
            else:
                print('Rectangular area is ', figure.rect_area(x, y))
        elif choice == '3':
            x = int(input('Enter square side: ',))
            print('Square area is ', figure.square_area(x))
        elif choice == '4':
            x = int(input('Enter lowest base: ',))
            y = int(input('Enter highest base: ',))
            z = int(input('Enter left side: ',))
            t = int(input('Enter right side: ',))
            print('Trapezoid area is ', figure.tra_area(x, y, z, t))
        elif choice == '5':
            r = int(input('Enter radius: ',))
            print('Circle area is ', figure.circle_area(r))
        else:
            print("\nI don't understand that choice, please try again.\n")
    elif choice == 'p':
        print("\n[1] Enter 1 to calculate triangle perimetr.")
        print("\n[2] Enter 2 to calculate rectangle perimetr.")
        print("\n[3] Enter 3 to calculate square perimetr.")
        print("\n[4] Enter 4 to calculate trapezoid perimetr.")
        print("\n[5] Enter 5 to calculate circle perimetr.")
        choice = input("\nWhat figure would you like to calculate? ")
        if choice == '1':
            x = int(input('Enter first side: ',))
            y = int(input('Enter second side: ',))
            z = int(input('Enter third side: ',))
            print('Triangle perimetr is ', figure.tri_perimetr(x, y, z))
        elif choice == '2':
            x = int(input('Enter first side: ',))
            y = int(input('Enter second side: ',))
            if x == y:
                print('Square perimetr is ', figure.square_perimetr(x))
            else:
                print('Rectangular perimetr is ', figure.rect_perimetr(x, y))
        elif choice == '3':
            x = int(input('Enter first side: ',))
            print('Square perimetr is ', figure.square_perimetr(x))
        elif choice == '4':
            x = int(input('Enter first side: ',))
            y = int(input('Enter second side: ',))
            z = int(input('Enter third side: ',))
            t = int(input('Enter fourth side: '))
            print('Trapezoid perimetr is ', figure.tra_perimetr(x, y, z, t))
        elif choice == '5':
            r = int(input('Enter radius: ',))
            print('Circle perimetr is ', figure.circle_perimetr(r))
        else:
            print("\nI don't understand that choice, please try again.\n")
    elif choice == 'q':
        print("\nSee you later.\n")
    else:
        print("\nI don't understand that choice, please try again.\n")
