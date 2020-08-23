# Main Driver for Code Snippet Organizer Application

# This Code Organizer will allow the user to upload functions, classes, and small code snippets to reference later
# Syntax Highlighting will be implemented for different languages for key words like class, func, if, operators etc
# User stores snippet with language and optional short description. Users can add and delete snippets as desired.
# Today (08/22/2020) and for the first iteration of this program there will be no GUI but it will be implemented later when I have more experience from other projects.

# I'm going to try and store the data in a txt file in the format detailed in the example file for now. Maybe JSON would be a better choice


# Import requried libraries and classes

# Class for a Code Snippet

# Eventually whatever is needed for a GUI will be imported and built here

# Add the snippet to the code_snippets.txt file for long term storage
def save_snippet(snippet):
    pass

# Returns code snippet from storage file
def get_snippet(snippet_object):
    pass

# Print a code snippet with syntax highlighting
def print_code(snippet_object):
    pass

# Grab a short title/label, language of snippet, and snippet from user
def get_snippet_info():
    pass

# Printing the basic menu with options for the user
def print_menu():
    pass

# Grab user input choice while handling errors
def get_userinput():
    pass

if __name__ == '__main__':
    print("hello")