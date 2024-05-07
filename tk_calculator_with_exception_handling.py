import tkinter as tk
from tkinter import *

# pseudocode:
#    start:
#         initialize value_1 and value_2 (will be used for calculation)
#
#         create a window
#         name window
#         adjust window size
#         make window unresizable
#
#         create a widget for entry of numbers, add text instructing the user what to input
#
#         create a button for user to submit value 1
#         in button, add a command that calls a function when clicked
#         create a function called submit_value_1_clicked:
#             test if the text in the widget did not change:
#                 pass
#             else:
#                 set value_1 to global
#                 get the current value inside the widget for submission of numbers
#                 if value is a number:
#                     store as float in value_1
#                     update the text instruction in number submission widget
#                 if value is NOT a number:
#                     send an error message
#
#         create another button for users to submit value 2
#         in button add a command that calls a function when clicked
#         create a function called submit_value_1_clicked:
#             if the new text instruction is unchanged:
#                 pass
#             else:
#                 set value_2 to global
#                 get the current value inside the widget for submission of numbers
#                 if value is a number:
#                     store as float in value_2
#                     clear text in number submission widget
#                 if value is NOT a number:
#                     send an error message in the number submission widget
#
#         create widget for users to input an operator, create a text stating what to input
#         create a submit button for the operator widget
#         in button, add a command that calls a function when submit_operator_button is clicked
#         create a function called submit_operator_button_clicked:
#             if the current value in operator input widget is the same as the default text:
#                 pass
#             else:
#                 call a function named calculate, store the returned value in variable named final_result
#                 concatenate the value to a string: "RESULT:"
#                 update the text in the result label widget
#
#         create function named calculate:
#             test if the user submitted the addition sign:
#                 add value_1 and value_2, store in variable result
#                 return variable result
#             test if the user submitted the dash sign:
#                 subtract value_1 by value_2, store in variable result
#                 return variable result
#             test if the user submitted "x":
#                 multiply value_1 by value_2, store in variable result
#                 return variable result
#             test if the user submitted "/":
#                 if value 2 is zero:
#                     display an error in the operator submission widget
#                 if value 2 is not zero:
#                     divide value_1 by value_2, store in variable result
#                     set the numbers of digits after decimal to 2 digits
#                     return variable result
#
#             test if the user submitted any other character:
#                 display an error message in the operator submission widget
#
#         create a result label widget that will display the final result
#         create variable named result that stores a value:"RESULT:"
#         set the text in the result label widget to the variable "result"
#    end:



value_1 = 0
value_2 = 0

window = Tk()
window.geometry("1100x670")
window.title("Calculator")
window.resizable(False, False)

