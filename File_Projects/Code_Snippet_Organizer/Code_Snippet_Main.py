# Main Driver for Code Snippet Organizer Application

# This Code Organizer will allow the user to upload functions, classes, and small code snippets to reference later
# Syntax Highlighting will be implemented for different languages for key words like class, func, if, operators etc
# User stores snippet with language and optional short description. Users can add and delete snippets as desired.
# Today (08/22/2020) and for the first iteration of this program there will be no GUI but it will be implemented later when I have more experience from other projects.

# I'm going to try and store the data in a txt file in the format detailed in the example file for now. Maybe JSON would be a better choice


# Import requried libraries and classes
from Snippet import Snippet
from errors import UserInputError
import os
# Class for a Code Snippet

# Eventually whatever is needed for a GUI will be imported and built here

class Snippet_Manager:
    # A list for easy lookup of snippets
    labels = []
    def __init__(self):
        self.set_user_directory()
    
    # need to make sure the user is in the correct directory otherwise we can't access the same storage file
    def set_user_directory(self):
        # This needs to be altered based on where you store the files for this program
        os.chdir(os.path.expanduser('~') + '/src/python_capstone_projects/File_Projects/Code_Snippet_Organizer')
    
    # Add the snippet to the code_snippets.txt file for long term storage
    def save_snippet(self,snippet):
        # having weird issues with storage, need to make sure that we can find the storage file
        storage_file = 'code_snippets.txt'
        
        with open(storage_file,'a') as storage_file:
            storage_file.write(f"Label: {snippet.label}\nLanguage: {snippet.language}\nCode:\n{snippet.snippet_string}\n")
        print("SAVED!")
    
    def delete_snippet(self, Label):
        pass
    # create a new snippet and display for user
    def create_snippet(self):
        # get info for snippet from user, create snippet
        label,language, snippet_string = self.get_snippet_info()

        while True:
            user_input = self.get_user_choice()
            if user_input == 'save':
                self.save_snippet(Snippet(label,language,snippet_string))
                break
            elif user_input == 'change':
                user_choice = self.get_user_choice(option=1)
                if user_choice == 'label':
                    label = input('What would you like to change the label to?\nEnter label: ')
                elif user_choice == 'language':
                    language = input('What would you like to change the language to?\nEnter language: ')

                elif user_choice == 'Snippet':
                    snippet_string = input('What would you like to change the code to?\nEnter code: ')
            else:
                break

        
    # Returns code snippet from storage file
    def get_snippet(self,_label):
        pass
    
    def get_user_choice(self,option = 0):
        # Checks user input when asking to save, change, or exit
        if option == 0:
            user_input = input("Do you want to save the snippet, make some changes or exit? (save/change/exit): ").lower()
            if user_input not in ['save','change','exit']:
                while(user_input != "save" and user_input != "change"):
                    user_input = input("Please enter either save or change: ").lower()
            return user_input
        # Checks user input for modifying a given snippet
        elif option == 1:
            # checking if user has entered what they would like to change correctly
            user_input = input("Would you like to change the label, language, snippet, or exit?\nEnter Choice: ").lower()
            # asks user for a valid input
            while user_input not in ["label","language","snippet"]:
                user_input = input("Please enter label, language, snippet, or exit: ").lower()
            return user_input
    #  Grab a short title/label, language of snippet, and snippet from user
    def get_snippet_info(self):
        user_Label = input("Please enter a Label: ")
        user_Language = input("Please enter a Language: ")
        user_snippet_string = input("Please enter a Code Snippet:\n")
        
        return user_Label, user_Language, user_snippet_string

    # Print a code snippet with syntax highlighting
    def print_code(self,_label):
        pass

    # Printing the basic menu with options for the user
    def print_menu(self):
        pass



if __name__ == '__main__':
    manager = Snippet_Manager()
    manager.create_snippet()