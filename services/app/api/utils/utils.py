"""This module declares general helper methods."""
import os

from sqlalchemy_utils import database_exists


def create_db_conn_string() -> str:
    """Create the database connection string.

    Creates the database connection string for a given flask environment.

    Returns
    -------
    db_connection_string: str
        The database connection string
    """
    POSTGRES_HOST = os.environ["POSTGRES_HOST"]
    POSTGRES_PORT = os.environ["POSTGRES_PORT"]
    POSTGRES_USER = os.environ["POSTGRES_USER"]
    POSTGRES_PASSWORD = os.environ["POSTGRES_PASSWORD"]
    POSTGRES_DB = os.environ["POSTGRES_DB"]

    return f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"


def check_if_database_exists(db_connection_string: str) -> bool:
    """Check if database exists.

    Ensures that the database exists before starting the application.

    Attributes
    ----------
    db_connection: str
        The database URL

    Raises
    ------
    ValueError:
        If the db_connection_string is empty or is not a string.

    Returns
    -------
    db_exists: bool
        True if database exists or False if it does not
    """
    if not db_connection_string:
        raise ValueError("The db_connection_string cannot be a null value.")

    if not isinstance(db_connection_string, str):
        raise ValueError("The db_connection_string has to be string")

    db_exists = database_exists(db_connection_string)

    return db_exists
