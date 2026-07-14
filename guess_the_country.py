secret_country = "India"
user_country = ""
guess_count = 0
guess_limit = 3
out_of_guess = False

while (user_country.lower() != secret_country.lower() and not out_of_guess):

    if guess_count < guess_limit:
        user_country = input("Guess my country: ")
        guess_count += 1
    else:
        out_of_guess = True

if out_of_guess:
    print("You lost your 3 chances and YOU LOSE!")
else:
    print("You WON")