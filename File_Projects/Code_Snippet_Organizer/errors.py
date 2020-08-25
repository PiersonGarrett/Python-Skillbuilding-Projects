# Errors used for checking user input so I don't have to raise random errors to get things to work

class UserInputError(Exception):
    """ You didn't enter a correct input! """