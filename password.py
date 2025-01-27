from colorama import Fore, Back, Style

password = input('Enter password: ')

if password == "password":
    print(Fore.LIGHTRED_EX + 'Password is incorrect' + Style.RESET_ALL)
    password = input('Enter password: ')
    if password == "incorrect":
        print(Fore.LIGHTRED_EX + 'Try again' + Style.RESET_ALL)
        password = input('Enter password: ')
        if password == "again":
            import time
            time.sleep(1)
            print('...')
            time.sleep(0.8)
            print('Are you kidding me?')
elif password == 'Romanarebest338':
    print(Fore.LIGHTGREEN_EX + 'Right!' + Style.RESET_ALL)
else:
    print(Fore.LIGHTRED_EX + 'Fatal error' + Style.RESET_ALL)