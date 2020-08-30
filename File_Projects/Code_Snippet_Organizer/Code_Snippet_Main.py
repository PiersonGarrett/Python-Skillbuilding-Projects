# Main Driver for Code Snippet Organizer Application

# This Code Organizer will allow the user to upload functions, classes, and small code snippets to reference later
# Syntax Highlighting will be implemented for different languages for key words like class, func, if, operators etc
# User stores snippet with language and optional short description. Users can add and delete snippets as desired.
# Today (08/22/2020) and for the first iteration of this program there will be no GUI but it will be implemented later when I have more experience from other projects.

# I'm going to try and store the data in a txt file in the format detailed in the example file for now. Maybe JSON would be a better choice


# Import requried libraries and classes
from Snippet import Snippet
from errors import UserInputError
import re, os, sys

# Eventually whatever is needed for a GUI will be imported and built here with a better method for inputing user code snippets. Currently the user can only input one line of code

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
            storage_file.write(f"\nLabel: {snippet.label}\nLanguage: {snippet.language}\nCode:\n{snippet.snippet_string}\n")
        print("SAVED!")
    
    def delete_snippet(self, _label):
        temp_snippet_arr = []
        # open storage file
        with open('code_snippets.txt','r') as storage_file:
            # Read in all the lines from the text file
            lines = storage_file.read()
            
            # Finds all the lables, languages, and snippets
            labels = re.findall(r'Label:(.+)',lines)
            languages = re.findall(r'Language:(.+)',lines)
            code = re.findall(r'Code:\n(.+)',lines)

            # prints all snippets with the given label
            for index,label in enumerate(labels):
                # had to use strip because of a weird space that was getting added to the front of strings
                if label.strip() != _label:
                    temp_snippet_arr.append(Snippet(labels[index].strip(),languages[index],code[index]))
        with open('code_snippets.txt','w') as storage_file:
            for snippet in temp_snippet_arr:
                storage_file.write(f"\nLabel: {snippet.label}\nLanguage: {snippet.language}\nCode:\n{snippet.snippet_string}\n")
        print("Deleted!")
        input("Press enter to continue.")
    
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

                elif user_choice == 'snippet':
                    snippet_string = input('What would you like to change the code to?\nEnter code: ')
            else:
                break

        
    # Returns code snippet from storage file and prints it with syntax highlighting
    def get_snippet(self,_label):
        
        # open storage file
        with open('code_snippets.txt','r') as storage_file:
            # Read in all the lines from the text file
            lines = storage_file.read()
            
            # Finds all the lables, languages, and snippets
            labels = re.findall(r'Label:(.+)',lines)
            languages = re.findall(r'Language:(.+)',lines)
            code = re.findall(r'Code:\n(.+)',lines)
            
            # prints all snippets with the given label
            for index,label in enumerate(labels):
                # had to use strip because of a weird space that was getting added to the front of strings
                if label.strip() == _label:
                    print(Snippet(labels[index],languages[index],code[index]))
            input("Press enter to continue.")
    
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


    # Printing the basic menu with options for the user
    def print_menu(self):
        print("Welcome to the Code Snippet Organizer! This is a prototype for a later version, which will feature a GUI and the ability to enter in multiple lines of code.")
        print("1) Create a New Snippet\n2) View an Existing Snippet\n3) Delete an Existing Snippet\n4) Exit")
        

if __name__ == '__main__':
    
    manager = Snippet_Manager()
    
    while(True):
        # clears terminal, only for mac and linux
        os.system('clear')
        manager.print_menu()
        
        while(True):
            try:
                user_input = int(input("Enter Number of Choice: "))
                if type(user_input) != int or (user_input > 4 and user_input <= 0):
                    raise Exception
            except:
                while(user_input not in [1,2,3,4]):
                    user_input = int(input("Please Enter the Number of your Choice: "))
            break

        if user_input == 1:
            manager.create_snippet()
        
        elif user_input == 2:
            user_label = input("Please enter the label of the snippet you wish to view: ")
            manager.get_snippet(user_label)
        
        elif user_input == 3:
            snippet_to_delete = input("Enter the label of the snippet you wish to delete: ")
            manager.delete_snippet(snippet_to_delete)

        else:
            break
    