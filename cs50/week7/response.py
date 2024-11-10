from validators import validator_collaction, checkers, errors
x = input("what's your email address? ")
try:
    email_address = validator_collaction.email(None)
except errors.EmptyValueError:
    print("invalid")
except errors.InvalidEmailError:
    print("invalid")
else:
    print("valid")