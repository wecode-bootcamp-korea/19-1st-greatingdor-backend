import re


def validator_name(name):
    validator = re.compile('^[가-힣a-zA-Z]{2,21}$')
    
    if validator.match(name):
        return True
    return False

def validator_account(account):
    validator = re.compile('^[0-9a-z]{6,17}$')

    if validator.match(account):
        return True
    return False

def validator_password(password):
    validator = re.compile('^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$@$!%*?&])[A-Za-z\d$@$!%*?&]{8,}')
    
    if validator.match(password):
        return True
    return False

def validator_email(email):
    validator = re.compile('^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')

    if validator.match(email):
        return True
    return False

def validator_date_birth(date_birth):
    validator = re.compile('^[0-9-]{10,}$')

    if validator.match(date_birth):
        return True
    return False

def validator_phone_number(phone_number):
    validator = re.compile('^[0-9]{9,}$')

    if validator.match(phone_number):
        return True
    return False
