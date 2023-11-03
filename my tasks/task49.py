import random
user_number = int(input('guess the number:'))
secret_number = random.randint(1,100)

for x in range(1,user_number+1):
    if user_number < secret_number:
        print('too low')
    elif user_number > secret_number:
        print('too high')
    else:
        print('you guess it right')
    break