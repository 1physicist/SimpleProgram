print("welcome".upper().center(150))
createusername = input("create username: ".upper())
createpassword = input("create password: ".upper())
entryage = int(input("how old are you?: ".upper()))
entryjob = input("what is your occupation?: ".upper())
recoverycode = int(input("what is your recovery code?: ".upper()))
id = createusername
print("information was saved successfully.".upper())
print(
    "If you forget your login information, you can recover your account".upper() + ' '
    "by entering all your occupation, age and recovery code information correctly.".upper()
)

while True:
    loginusername = input("username: ".upper())
    loginpassword = input("password: ".upper())
    if (createusername == loginusername) and (createpassword == loginpassword):
        print("welcome".upper(), id)
        break
    elif (createusername != loginusername) and (createpassword == loginpassword):
        answer = str(input("do you forgot your username? (yes/no): ".upper()))
        if (answer == "no".upper()):
            print("try again.".upper())
        if (answer == "yes".upper()):
            while True:
                job = str(input("what is your occupation?: ".upper()))
                if (entryjob == job):
                    recoveryage = int(input("how old are you?: ".upper()))
                    if (entryage == recoveryage):
                        code = int(input("what is your recovery code?: ".upper()))
                        if (recoverycode == code):
                            print("congratulations. your username: ".upper(),createusername)
                            break
                        
                        elif (recoverycode != code):
                            print("recovery code is not correctly please try again.".upper())
                    elif (entryage != recoveryage):
                        print("your age is not correctly please try again.".upper())
                elif (entryjob != job):
                    print("your occupation is not correctly please try again.".upper())

    elif (createusername == loginusername) and (createpassword != loginpassword):
        answer = str(input("your password is not correctly. do you forgot password? (yes/no): ".upper()))
        if (answer == "no"):
            print("try again.".upper())
        if (answer == "yes"):
            while True:
                job = str(input("what is your occupation?: ".upper()))
                if (entryjob == job):
                    recoveryage = int(input("how old are you?: ".upper()))
                    if (entryage == recoveryage):
                        code = int(input("what is your recovery code?: ".upper()))
                        if (recoverycode == code):
                            newpassword = input("create new password: ".upper())
                            createpassword = newpassword
                            print("congratulations. you create a new password.",createusername)
                            break

                        elif (recoverycode != code):
                            print("recovery code is not correctly please try again.".upper())
                    elif (entryage != recoveryage):
                        print("your age is not correctly please try again.".upper())
                elif (entryjob != job):
                    print("your occupation is not correctly please try again.".upper())

    else:
        print("your username and your password is not correctly. please try again.".upper())
