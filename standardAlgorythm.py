array = []

def main():
    function = input("Would you like to load, print, sum, max, min, or end?  ").lower()
    if function == "load":
        load()
    elif function == "print":
        printFunct()
    elif function == "sum":
        summ()
    elif function == "max":
        max()
    elif function == "min":
        min()
    elif function == "end":
        SystemExit()
    else:
        print("That function does not exist, try again")
        main()

def load():
    number = input("What number would you like to load?  ")
    try:
        float(number)
    except ValueError:
        print("That is not a number")
        load()
    array.append(float(number))
    main()

def printFunct():
    print(*array)
    print("There are " + str(len(array))+" Items in the array")
    main()

def summ():
    print("The sum of the numbers is "+str(sum(array)))
    print("There are " + str(len(array))+" Items in the array")
    main()

def max():
    print("Function not yet implemented")
    main()

def min():
    print("Function not yet implemented")
    main()


main()