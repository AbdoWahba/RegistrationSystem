import json

cont = 'y'
while cont == 'y' or cont == 'Y':
    email = input("Please enter email: ")

    while not('@' in email) or not('.'in email) or ("@." in email) \
            or (email[0] == '@') or (email[-1] == '@') or (email[-1] == '.') \
            or (' ' in email):
        email = input("please reenter email correctly: ")

    day = input('Please enter day: ')

    email = email.lower()

    thisdict = {
        "email": email,
        "day": day,
    }

    myJson = json.dumps(thisdict)

    with open("reg.txt", mode='r+') as reg:
        if email in reg.read():
            print("sorry, this email has been regestered")
        else:
            reg.write(myJson)
            reg.write(",\n")

    cont = input("do you want to cont?[y/n]")
