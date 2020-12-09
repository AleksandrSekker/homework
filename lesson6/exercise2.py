def login(input):
    """login success and fail use while loop"""
    
    while input != 'First':
        print('You failed login')
        break
    else:
        print('You successfully login')
login(str(input('Write you login: ')))