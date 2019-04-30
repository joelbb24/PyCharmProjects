
def Calculator():
    while True:

        print("\t\t\t\t WELCOME TO JOE'S CALCULATOR")

        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Modulo")
        choice = int(input("Enter your choice: "))
        var1 = int(input("Enter variable one: "))
        var2 = int(input("Enter variable two: "))
        var3 = 0
        if choice == 1:
            var3 = var1 + var2
            print("The sum is: " + str(var3))
        elif choice == 2:
            var3 = var1 - var2
            print("The difference is: " + str(var3))
        elif choice == 3:
            var3 = var1 * var2
            print("The product is: " + str(var3))
        elif choice == 4:
            var3 = var1 / var2
            print("The dividend is: " + str(var3))
        elif choice == 5:
            var3 = var1 % var2
            print("The remainder is: " + str(var3))
        else:
            print("You've entered incorrect choice.")
        print("Do you want to calculate again?")
        recalc = input("Y/N")
        if recalc == "Y" or recalc == "y":
            Calculator()
        else:
            exit()


Calculator()
