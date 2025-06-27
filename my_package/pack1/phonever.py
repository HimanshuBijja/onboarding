p = input('Enter a phone number: ')
if p.isdigit() and len(p) == 10:
    print('Phone number is valid.')
else:
    print('Phone number is invalid.')

m = input('Enter an email address: ')
if m.endswith('.com') and '@' in m:
    print('Email address is valid.')
else:
    print('Email address is invalid.')
