# This manager will allow you to input a password for whatever account you want. You can store as many
# as you want and allow to call any password.

# Probably going to store passwords with account as a dictionary and make it so you call on a key
# probably save it all capitalized or lower or both for searching

# To do list: Make it so it remembers your name once inputted, doesn't create new file aka lets me keep info
# make sure code is writing and reading from file in correct spots
# be able to name file
import json

passwords = {

}


prompt = "If you want to make a new password, type 'Make password'."
prompt += "\nIf you want to look for a password, type 'Look for password'.\n"
answer = input(prompt)


def password_list(account_name, password_name):

    passwords[account_name] = password_name


answer = answer.upper()

found = 0

if answer == "MAKE PASSWORD":
    account_name = input("What use is this password for? ")
    account_name = account_name.upper()
    password_name = input("What is the password? ")
    password_list(account_name, password_name)
    with open("passwords.txt", 'w+') as f:
        f.write(json.dumps(passwords))
    print("Your password was saved!")
elif answer == "LOOK FOR PASSWORD":
    with open("passwords.txt", "r") as f:
        passwords = json.loads(f.read())
        if not passwords:
            print("Sorry but there are no passwords available. Make a new one!")
        elif passwords:
            search_account = input("What account is this password for? ")
            search_account = search_account.upper()
            for name in passwords.keys():
                if search_account == name:
                    print(f"The password is '{passwords.get(name)}'.")
                    found = 1
                    break
            if found != 1:
                print("Sorry, we can't find such name.")


# make it a while loop that lets you exit