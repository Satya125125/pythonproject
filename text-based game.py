import random

def computer_guess(y):
    low = 1
    high = y
    Feedback = ''
    while Feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low  # could also be high b/c low = high
        Feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)?? ').lower()
        if Feedback == 'h':
            high = guess - 1
        elif Feedback == 'l':
            low = guess + 1

    print(f'Yay! The computer guessed your number, {guess}, correctly!')


computer_guess(10)
    
