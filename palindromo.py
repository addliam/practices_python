while True:
    var = str(input('In something: '))
    if var == 'exit':
        exit()
    elif var == var[::-1]:
        print("That string is a palindrome")
    else:
        print("That string isn't a palindrome")