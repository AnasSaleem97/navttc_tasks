# Task 23 - User Defined Exception Handling
# Reference: https://www.programiz.com/python-programming/user-defined-exception

class InvalidAgeError(Exception):
    pass

class InsufficientBalanceError(Exception):
    def __init__(self, message="Account balance is too low"):
        super().__init__(message)

def check_voter_eligibility(age):
    if age < 18:
        raise InvalidAgeError("Age must be at least 18 to vote.")
    print("Eligible voter.")

try:
    check_voter_eligibility(15)
except InvalidAgeError as e:
    print("Caught custom exception:", e)

def withdraw_cash(balance, amount):
    if amount > balance:
        raise InsufficientBalanceError(f"Cannot withdraw {amount}, current balance is {balance}")
    return balance - amount

account_balance = 5000
try:
    account_balance = withdraw_cash(account_balance, 7000)
except InsufficientBalanceError as err:
    print("Abubakar transaction failed:", err)
