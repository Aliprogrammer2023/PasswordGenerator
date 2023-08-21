# my required libraries
import random
import string

import tkinter as tk # import the tkinter module

# create a root window
root = tk.Tk()
root.title("Password Generator")

# create a frame to hold the widgets
frame = tk.Frame(root)
frame.pack()

# create a label to display the password level
level_label = tk.Label(frame, text="Choose your password level (simple, medium, high):")
level_label.grid(row=0, column=0, sticky="w")

# create a variable to store the password level
level_var = tk.StringVar()

# create an entry to get the password level
level_entry = tk.Entry(frame, textvariable=level_var)
level_entry.grid(row=0, column=1)

# create a label to display the password character number
char_num_label = tk.Label(frame, text="How many characters does your password have?")
char_num_label.grid(row=1, column=0, sticky="w")

# create a variable to store the password character number
char_num_var = tk.IntVar()

# create an entry to get the password character number
char_num_entry = tk.Entry(frame, textvariable=char_num_var)
char_num_entry.grid(row=1, column=1)

# create a label to display the generated password
password_label = tk.Label(frame, text="Your password is:")
password_label.grid(row=2, column=0, sticky="w")

# create a variable to store the generated password
password_var = tk.StringVar()

# create an entry to show the generated password
password_entry = tk.Entry(frame, textvariable=password_var)
password_entry.grid(row=2, column=1)

# define a function to generate the password
def generate_password():
    # get the user inputs
    level = level_var.get()
    char_num = char_num_var.get()

    # validate the user inputs
    if level not in ("simple", "medium", "high"):
        # show an error message if the level is invalid
        password_var.set("Invalid level. Please try again.")
        return

    if char_num <= 0:
        # show an error message if the character number is invalid
        password_var.set("Invalid number. Please enter a positive integer.")
        return

    # generate the password based on the level and character number
    try:
        if level == "simple":
            # generate a simple password with only digits
            password = "".join(random.choices(string.digits, k=char_num))
        elif level == "medium":
            # generate a medium password with only letters
            password = "".join(random.choices(string.ascii_letters, k=char_num))
        elif level == "high":
            # generate a high password with both letters and digits
            password = "".join(random.choices(string.ascii_letters + string.digits, k=char_num))
        
        # set the generated password to the variable
        password_var.set(password)
    except:
        # show an error message if something goes wrong
        password_var.set("Sorry! Something went wrong!")

# create a button to trigger the password generation
generate_button = tk.Button(frame, text="Generate", command=generate_password)
generate_button.grid(row=3, columnspan=2)

# start the main loop of the window
root.mainloop()
