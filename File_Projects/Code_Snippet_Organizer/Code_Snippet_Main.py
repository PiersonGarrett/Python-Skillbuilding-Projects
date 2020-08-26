# Main Driver for Code Snippet Organizer Application

# This Code Organizer will allow the user to upload functions, classes, and small code snippets to reference later
# Syntax Highlighting will be implemented for different languages for key words like class, func, if, operators etc
# User stores snippet with language and optional short description. Users can add and delete snippets as desired.
# Today (08/22/2020) and for the first iteration of this program there will be no GUI but it will be implemented later when I have more experience from other projects.

# I'm going to try and store the data in a txt file in the format detailed in the example file for now. Maybe JSON would be a better choice


# Import requried libraries and classes
from Snippet import Snippet
from errors import UserInputError
# Class for a Code Snippet

# Eventually whatever is needed for a GUI will be imported and built here

class Snippet_Manager:
    # A list for easy lookup of snippets
    labels = []

    # Add the snippet to the code_snippets.txt file for long term storage
    def save_snippet(self,snippet):
        with open('Code_Snippet_Organizer/code_snippets.txt','a') as storage_file:
            storage_file.write(f"\nLabel: {snippet.label}\nLanguage: {snippet.language}\nCode:\n{snippet.snippet_string}")
        print("SAVED!")
    
    def delete_snippet(self, Label):
        pass
    # create a new snippet and display for user
    def create_snippet(self):
        # get info for snippet from user, create snippet
        label,language, snippet_string = self.get_snippet_info()
        temp_snippet = Snippet(label,language,snippet_string)

        # Ask user if they want to save the snippet
        user_input = ""
        while user_input != "exit":
            user_input = input("Do you want to save the snippet, make some changes or exit? (save/change/exit): ")
            # This block handles checking user input and allowing the user to make edits before saving or canceling the creation of the snippet (maybe in seperate function?)
            try:
                # checking if the user has entered a correct input
                if user_input == "save":
                    self.save_snippet(temp_snippet)
                    break
                elif user_input == "change":
                    # checking if user has entered what they would like to change correctly
                    user_decision = input("Would you like to change the Label, Language, Snippet, or Cancel?\nEnter Choice: ")
                    if user_decision.capitalize() == "Label":
                        temp_snippet.label = input("Please Enter Label: ")
                    elif user_decision.capitalize() == "Language":
                        temp_snippet.language = input("Please Enter Language: ")
                    elif user_decision.capitalize() == "Snippet":
                        temp_snippet.snippet_string = input("Please Enter Code Snippet:\n") 
                    elif user_decision.capitalize() == "Cancel":
                        pass
                    # if a valid choice was not made a custom error is raised
                    else:
                        raise UserInputError
                # check if user did not enter a valid choice
                elif user_input not in ["save","change","exit"]:
                    raise Exception
            except UserInputError: 
                # asks user for a valid input
                while user_decision not in ["Label","Language","Snippet"]:
                    user_decision = input("Please enter Langauge, Label, Snippet, or exit: ")
            except:
                # ask user for a valid input until valid input is given
                while(user_input != "save" and user_input != "change"):
                    user_input = input("Please enter either save or change: ")
        
        #TODO: conttinue implementing functions and adding them to this spagehtti (which I'll have to clean up later)
    # Returns code snippet from storage file
    def get_snippet(self,_label):
        pass

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