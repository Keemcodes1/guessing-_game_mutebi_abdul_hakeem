import random
secret_number = random.randint(1,99)
while True:
    guess = int(input("guess the number: "))
    if guess < secret_number:
        print("your guess is less.")
    elif guess >secret_number:
        print("your guess is too high.")
    else:
        print("congratulations you guessed right")
        break    