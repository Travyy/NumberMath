def add_numbers():
    numbers = input("Enter a list of numbers to add separated by spaces: ")
    numbers = str_list_to_num_list(numbers)
    total = 0
    for num in numbers:
        total += num
    print(total)
    print()


def multiply_num():
    numbers = input("Enter a list of numbers to multiply separated by spaces: ")
    numbers = str_list_to_num_list(numbers)
    total = 0
    for num in numbers:
        # make sure not multiplying by 0
        if total == 0:
            total += num
        else:
            total *= num
    print(total)
    print()

    
# im sure there is a way to not hardcode the numbers[0] & numbers[1] but really not sure it matters since
# those are the only ones used in here anyway.
def divide_num():
    numbers = []
    while len(numbers) <= 1 or len(numbers) > 2:
        numbers = input("Enter ONLY two numbers to divide separated by spaces(ex: dividend divisor): ")
        numbers = str_list_to_num_list(numbers)
        if len(numbers) == 2:
            # make sure no division by 0
            if numbers[0] == 0 or numbers[1] == 0:
                print("no division by 0, nice try. \n")
                numbers = []
                continue
            else:
                total = numbers[0] / numbers[1]
                print(total)
                break
        elif len(numbers) > 2:
            print("You entered too many numbers, try again \n")
        else:
            print("You entered too few numbers, try again \n")

# im sure there is a way to not hardcode the numbers[0] & numbers[1] but really not sure it matters since
# those are the only ones used in here anyway.
def subtract_num():
    numbers = []
    while len(numbers) <= 1 or len(numbers) > 2:
        numbers = input("Enter ONLY two numbers to subtract separated by spaces(ex: 100 10 = 100 - 10): ")
        numbers = str_list_to_num_list(numbers)
        if len(numbers) == 2:
            total = numbers[0] - numbers[1]
            print(total)
            break
        elif len(numbers) > 2:
            print("You entered too many numbers, try again \n")
        else:
            print("You entered too few numbers, try again \n")


# str_list_to_num_list takes user input and turns it into usable list with integers
def str_list_to_num_list(string1):
    numbers = string1.split()
    numbers = list(map(int, numbers))
    return numbers


def handle_user_choice(user_choice):
    user_choice = user_choice.lower()
    if user_choice == "add":
        return add_numbers()
    elif user_choice == "multiply":
        return multiply_num()
    elif user_choice == "divide":
        return divide_num()
    elif user_choice == "subtract":
        return subtract_num()
    elif user_choice == "exit":
        return "EXIT"
    else:
        print("You have entered an invalid argument: Try again. \n") # error if user types in incorrect string


def get_user_input():
    check = False
    user_choice = ''
    while not check:
        if user_choice == '':
            user_choice = input("Choose a function you want to run; add, subtract, multiply, divide. If you want to " 
                                "exit the program, type EXIT: ")
            
            # make sure input is only letters
            if not user_choice.isalpha():
                print("You may only enter letters, no numbers allowed. Try Again. \n")
                user_choice = ''
                continue
            else:
                check = True
    return user_choice


def main():
    x = ''
    while x != "EXIT":
        choice = get_user_input()
        x = handle_user_choice(choice)


main()

