#by Abhishek Mishra
import os
from tabulate import tabulate

class Colors:
    @staticmethod
    def Color(code: int):
        """
        Generate a color code between 1 and 612.
        """
        if 1 <= code <= 612:
            DEF_CODE = "\u001b[38;5;"
            color = DEF_CODE + str(code) + "m"
            return color
        else:
            raise ValueError("Color code must be between 1 and 612")

color_info = [(color_code, f"{Colors.Color(color_code)}{color_code} \u001b[0m") for color_code in range(1, 613)]

# here going to print this all in form of a table
table = tabulate(color_info, headers=["Color Code", "Color Number"], tablefmt="fancy_grid")
print(table)
