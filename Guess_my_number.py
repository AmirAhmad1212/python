def Guess(number):
    while True:
        try:
            user_number = int(input("Guess the Number im Thinking about --->"))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if user_number > number:
            print("your number is bigger than mine")

        elif user_number < number:
            print("your number is smaller than mine")

        else:
            print("you Guessed it right")
            break

Guess(20)