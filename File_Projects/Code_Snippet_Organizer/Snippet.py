# Definition of Snippet Class which will hold information of a snippet and return a modified string with syntax highlighting

# Handles the change in text color needed for syntax highlighting
from Colors_ANSI import Colors_ANSI
    
class Snippet(Colors_ANSI):
    
    def __init__(self,_label,_language,_snippet_string):
        self.label = _label
        self.language = _language
        self.snippet_string = _snippet_string
        self.snippet_syntax_highlight = self.highlight_syntax()
        
    def __str__(self):
        return(f"""\nLabel: {self.label}\nLanguage: {self.language}\nCode: \n\t{self.snippet_syntax_highlight}""")

    # Adds ANSI escape characters to syntax terms like class, for, if, in else, elif,
    def highlight_syntax(self):

        syntax_terms = ["class","for","if","==","+","-","*"]
        snippet_list = self.snippet_string.split()

        for index,word in enumerate(snippet_list):
            if word in syntax_terms:
                if word.lower() == "class":
                    snippet_list[index] = self.change_color(word,"YELLOW")
                elif word.lower() in ["for","if","==","+","-","*"]:
                    snippet_list[index] = self.change_color(word,"PURPLE")
        return " ".join(snippet_list)   
        
                    

if __name__ == '__main__':
    thing = Snippet("label","language","class for if")
    print(thing)