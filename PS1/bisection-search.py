number_to_guess = int(input('Enter a number between 1 and 100: '))
lower_bound = 0
upper_bound = 100
success = False

num_guesses = 0
while success == False:
    current_guess = (lower_bound + upper_bound)//2
    num_guesses = num_guesses + 1
    if current_guess == number_to_guess:
        print(f'Guess {num_guesses}: Your number is {current_guess}')
        success == True
        break
    else:
        guess_feedback = input('Guess ' + str(num_guesses) + ': is your number ' + str(current_guess) + '? Enter "L" if my guess is too low, and "H" if my guess is too high: ')
        if guess_feedback.__eq__("L"):
            lower_bound = current_guess
        else:
            upper_bound = current_guess


