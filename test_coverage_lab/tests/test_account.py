"""
Test Cases for Account Model
"""
import json
from random import randrange
import pytest
from models import db
from models.account import Account, DataValidationError

ACCOUNT_DATA = {}

@pytest.fixture(scope="module", autouse=True)
def load_account_data():
    """ Load data needed by tests """
    global ACCOUNT_DATA
    with open('tests/fixtures/account_data.json') as json_data:
        ACCOUNT_DATA = json.load(json_data)

    # Set up the database tables
    db.create_all()
    yield
    db.session.close()

@pytest.fixture(scope="function", autouse=True)
def setup_and_teardown():
    """ Truncate the tables and set up for each test """
    db.session.query(Account).delete()
    db.session.commit()
    yield
    db.session.remove()


######################################################################
#  T O D O   T E S T S  (To Be Completed by Students)
######################################################################

"""
Each student in the team should implement **one test case** from the list below.
The team should coordinate to **avoid duplicate work**.

Each test should include:
- A descriptive **docstring** explaining what is being tested.
- **Assertions** to verify expected behavior.
- A meaningful **commit message** when submitting their PR.
"""

# TODO 1: Test Account Serialization
# - Ensure `to_dict()` correctly converts an account to a dictionary format.
# - Verify that all expected fields are included in the dictionary.

# TODO 2: Test Invalid Email Input
# - Check that invalid emails (e.g., "not-an-email") raise a validation error.
# - Ensure accounts without an email cannot be created.

# TODO 3: Test Missing Required Fields
# - Ensure that creating an `Account()` without required fields raises an error.
# - Validate that missing fields trigger the correct exception.

# TODO 4: Test Positive Deposit
# - Ensure `deposit()` correctly increases the account balance.
# - Verify that depositing a positive amount updates the balance correctly.

# TODO 5: Test Deposit with Zero/Negative Values
# - Ensure `deposit()` raises an error for zero or negative amounts.
# - Verify that balance remains unchanged after an invalid deposit attempt.

# TODO 6: Test Valid Withdrawal
# - Ensure `withdraw()` correctly decreases the account balance.
# - Verify that withdrawals within available balance succeed.

# TODO 7: Test Withdrawal with Insufficient Funds
# - Ensure `withdraw()` raises an error when attempting to withdraw more than available balance.
# - Verify that the balance remains unchanged after a failed withdrawal.

# TODO 8: Test Password Hashing
# - Ensure that passwords are stored as **hashed values**.
# - Verify that plaintext passwords are never stored in the database.
# - Test password verification with `set_password()` and `check_password()`.

# TODO 9: Test Role Assignment
# - Ensure that `change_role()` correctly updates an account’s role.
# - Verify that the updated role is stored in the database.

# TODO 10: Test Invalid Role Assignment
# ===========================
# Test: Test Email Uniqueness Enforcement
# Author: Jaison-Noah Sarte
# Date: 2025-02-01
# Description: Ensure that duplicate emails cannot be added to the database.
# ===========================
def validate_unique_email():
    # Create the first account with a unique email
    account1 = Account(name="Jai Noah", email="jainoah@example.com")
    db.session.add(account1) # Add the account to the session
    db.session.commit() # Commit
    # Try to create another account with the same email
    account2 = Account(name="Lionel Messi", email="jainoah@example.com")
    
    # Ensure that a duplicate email raises an error (DataValidationError)
    with pytest.raises(DataValidationError):
        db.session.add(account2) 
        db.session.commit()  # Error raised as dup email is not allowed

# TODO 11: Test Deleting an Account
# - Ensure that `delete()` removes an account from the database.
# - Verify that attempting to retrieve a deleted account returns `None` or raises an error.
