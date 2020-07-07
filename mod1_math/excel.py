"""
Prompt
Given a column title as appears in an Excel sheet, return its corresponding column number.

Examples:
A -> 1
    
B -> 2
    
C -> 3
    
    ...
    
Z -> 26
    
AA -> 27
    
AB -> 28 


UMPIRE walkthrough

Understand:
First, note down all key information. 
What is the key action? 
What is the input? What is the data type?
What is the format of the output? What data type?

Match:
Think back- have you seen a problem like this before? 
Consider ASCII - the ord() function will return the ASCII value of any character- try passing each letter in and comparing the values.

Plan:
Walk through the steps of doing the conversion yourself. 
Write each step down.

Once you have written down the steps in english, try re-describing them in psudeocode.
If you repeat any steps, try expressing the steps as a loop.
If you ask any questions, try phrasing them as if statements.

"""


def excel_column_to_number(column):
  return column