"""This module declares the exceptions raised when creating a new user."""


class NameTooShortException(Exception):
    """Raised when the user name is less than two characters."""


class NameTooLongException(Exception):
    """Raised when the user name is more than twenty characters."""


class NameExistsException(Exception):
    """Raised when a duplicate name is used to register."""


class InvalidEmailAddressFormatException(Exception):
    """Raised when the email address format is invalid."""


class EmailAddressExistsException(Exception):
    """Raised when a duplicate email address is used to register."""


class PasswordTooShortException(Exception):
    """Raised when the password is less than six characters."""


class InvalidPasswordFormatException(Exception):
    """Raised when the password format is invalid.

    The password should be alphanumeric.
    """


class PasswordMissmatchException(Exception):
    """Raised when the two passwords do not match."""


class InvalidLoginDetails(Exception):
    """Raised when the login details are invalid."""
