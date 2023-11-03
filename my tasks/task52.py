user_input = input('number:')
user_input = int(user_input)

count = 1

while count <= 20:

    product = count * user_input
    print(user_input, '*', count, '=', product)
    count = count + 1
