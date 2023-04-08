name = input('what  is youe name : ')
while 1:
    if len(name) >= 3:
        break
    else:
        print('name doesnt valid please enter again!')
        name = input('what  is youe name : ')

lastname = input('what is your last name : ')
while 1:
    if len(lastname) >= 3:
        break
    else:
        print('last name doesnt valid please enter again!')
        lastname = input('what is your last name : ')

print(
    f"""
    your info
    
        name : {name}
        last name : {lastname}
    """
)