# pylint: disable=missing-docstring

import os

def start():
    """returns the right message"""
    environment = os.getenv("FLASK_ENV")
    if environment == "development":
        return "Starting in development mode..."
    if environment == "production":
        return "Starting in production mode..."
    return "Starting in empty mode..."

if __name__ == "__main__":
    print(start())
