password = input("Write a password: ")
while True:
    answer = input("Write the password: ")
    if answer == password:
        print("Welcome")
        exit()
    elif answer.lower()== "help": #HELP,help
        print(password[0])
        continue
    else:
        print("Wrong")
        continue