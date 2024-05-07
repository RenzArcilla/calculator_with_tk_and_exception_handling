import tkinter as tk
from tkinter import *

# pseudocode:
#    start:
#         initialize value_1 and value_2 (will be used for calculation)
#
#         create a window
#         name window
#         adjust window size
#         make window non-resizable
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
#
#         create a function called submit_operator_button_clicked:
#             if the current value in operator input widget is the same as the default text:
#                 pass
#             else:
#                 call a function named calculate, store the returned value in variable named final_result
#                 concatenate the value to a string: "RESULT:"
#                 update the text in the result label widget
#
#         create function named calculate:
#             get the current value in entry_widget_for_operators
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
#             test if the user submitted any other character:
#                 display an error message in the operator submission widget
#
#         create a result label widget that will display the final result
#         create variable named result that stores a value:"RESULT:"
#         set the text in the result label widget to the variable "result"
#    end:


#         initialize value_1 and value_2 (will be used for calculation)
value_1 = 0
value_2 = 0

#         create a window
#         name window
#         adjust window size
#         make window non-resizable
window = Tk()
window.geometry("1100x670")
window.title("Calculator")
window.resizable(False, False)

#         create a widget for entry of numbers, add text instructing the user what to input
entry_widget_for_numbers = tk.Entry(window, width=50)
entry_widget_for_numbers.pack()
entry_widget_for_numbers.insert(0, "Enter a number here.")


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
def submit_value_1_clicked():
    if entry_widget_for_numbers.get() == "Enter a number here.":
        pass
    else:
        global value_1
        value_1 = entry_widget_for_numbers.get()
        try:
            value_1 = float(entry_widget_for_numbers.get())
            entry_widget_for_numbers.delete(0, tk.END)
            entry_widget_for_numbers.insert(0, "Please enter another number in this box")
        except ValueError:
            entry_widget_for_numbers.delete(0, tk.END)
            entry_widget_for_numbers.insert(0, "Error encountered! Pls enter a number.")


#         create a button for user to submit value 1
#         in button, add a command that calls a function when clicked
num_1_send_button = tk.Button(window, text="SEND NUM 1", command=submit_value_1_clicked)
num_1_send_button.pack()


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
def submit_value_2_clicked():
    if entry_widget_for_numbers.get() == "Please enter another number in this box":
        pass
    else:
        global value_2
        value_2 = entry_widget_for_numbers.get()
        try:
            value_2 = float(entry_widget_for_numbers.get())
            entry_widget_for_numbers.delete(0, tk.END)
        except ValueError:
            entry_widget_for_numbers.delete(0, tk.END)
            entry_widget_for_numbers.insert(0, "Error encountered! Pls enter a number.")


#         create another button for users to submit value 2
#         in button add a command that calls a function when clicked
num_2_send_button = tk.Button(window, text="SEND NUM 2", command=submit_value_2_clicked)
num_2_send_button.pack()


#         create widget for users to input an operator, create a text stating what to input
entry_widget_for_operators = tk.Entry(window, width=30)
entry_widget_for_operators.pack()
entry_widget_for_operators.insert(0, "Enter an operator here: +, -, x, /")


#         create function named calculate:
#             get the current value in entry_widget_for_operators
#             test if the user submitted the addition sign:
#                 add value_1 and value_2, store in variable result
#                 return variable result
#             test if the user submitted the dash sign:
#                 subtract value_1 by value_2, store in variable result
#                 return variable result
#             test if the user submitted "x":
#                 multiply value_1 by value_2, store in variable result
#                 return variable result
def calculate():
    operator = entry_widget_for_operators.get()
    if operator == "+":
        result = value_1 + value_2
        return result
    elif operator == "-":
        result = value_1 - value_2
        return result
    elif operator == "x":
        result = value_1 * value_2
        return result


#         create a function called submit_operator_button_clicked:
#             if the current value in operator input widget is the same as the default text:
#                 pass
#             else:
#                 call a function named calculate, store the returned value in variable named final_result
def submit_operator_button_clicked():
    if entry_widget_for_operators.get() == "Enter an operator here: +, -, x, /":
        pass
    else:
        final_result = calculate(value_1, value_2)


#         create a submit button for the operator widget
#         in button, add a command that calls a function when submit_operator_button is clicked
submit_operator_button = tk.Button(window, text="SEND OPERATOR", command=submit_operator_button_clicked)
submit_operator_button.pack()

window.mainloop()
