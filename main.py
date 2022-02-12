import string,random

while True:
    # print ('==' * 19 )
    lenght = int(input('| Please enter your password lenght : |'))
    # print ('==' * 18 )


    chars = string.ascii_letters + string.digits + '!@$%&*()-+'

    password = ''.join([random.choice(chars) for i in range(lenght)])

    print ('Your password : {}'.format(password))


    while True:
        answer = input ('Do you want another one? (Y/N) ').lower()

        if answer == 'n' or answer == 'y' :
            break


    if answer == 'n' :
        break