import os,sys
os.system("")

class Colors:
    @staticmethod
    def Color(code:int):
        """
        Need a Color code between 1-256
        Check Image on github for more info
        """
        DEF_CODE = "\u001b[38;5;"
        color =  DEF_CODE + str(code)+"m"
        return color
