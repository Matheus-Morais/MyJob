from email_validate import validate


def validaEmail(email):
    if validate(email_address=email):
        return True
    else:
        return False
