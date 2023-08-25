def password_validator(password):
    result = []
    if len(password) in range(6, 11) and password.isalnum() and sum([c.isdigit() for c in password]) >= 2:
        result.append("Password is valid")
    if len(password) not in range(6, 11):
        result.append("Password must be between 6 and 10 characters")
    if not password.isalnum():
        result.append("Password must consist only of letters and digits")
    if sum([c.isdigit() for c in password]) < 2:
        result.append("Password must have at least 2 digits")
    return result


print(*password_validator(input()), sep="\n")