# Colors_ANSI can add color to text using ANSI escape sequences
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