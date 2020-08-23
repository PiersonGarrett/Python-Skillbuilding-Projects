# Definition of Snippet Class which will hold information of a snippet and return a modified string with syntax highlighting

# Handles the change in text color needed for syntax highlighting
class Colors_ANSI:
    RED = '\033[38;5;124m'
    GREEN = '\033[38;5;28m'
    ORANGE = '\033[38;5;202m'
    PURPLE =  '\033[38;5;98m'
    CYAN = '\033[38;5;43m'
    YELLOW = '\033[38;5;215m'
    ENDCOLOR = '\033[39m\033[39m'
    
    def get_color(self,color):
        color = color.upper()
        if color == "RED":
            return Colors_ANSI.RED
        elif color == "GREEN":
            return Colors_ANSI.GREEN
        elif color == "ORANGE":
            return Colors_ANSI.ORANGE
        elif color == "PURPLE":
            return Colors_ANSI.PURPLE
        elif color == "CYAN":
            return Colors_ANSI.CYAN
        elif color == "YELLOW": 
            return Colors_ANSI.YELLOW
        else:
            return Colors_ANSI.ENDCOLOR
    
    # Adds ANSI escape sequences to text to add specified color
    def change_color(self, text, color):
        return(self.get_color(color) + text + Colors_ANSI.ENDCOLOR)
    
class Snippet(Colors_ANSI):
    
    def __init__(self,_label,_language,_snippet_string):
        self.label = self.change_color(_label,"CYAN")
        self.language = self.change_color(_language,"CYAN")
        self.snippet_string = _snippet_string
        self.snippet_syntax_highlight = self.highlight_syntax(self.snippet_string)
        
    def __str__(self):
        return(f"""\nLabel: {self.label}\nLanguage: {self.language}\nCode: \n\t{self.snippet_syntax_highlight}""")

    # Adds ANSI escape characters to syntax terms like class, for, if, in else, elif,
    def highlight_syntax(self,snippet_string):
        syntax_terms = ["class","for","if","==","+","-","*"]
        snippet_list = snippet_string.split()
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