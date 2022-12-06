import tkinter as tk
'''
# Create the main window
root = tk.Tk()

# Create a list of strings that will be used as the labels for the buttons
button_labels = ["A", "B", "C", "D", "E", "F", "G"]

# Create a list to store the buttons
buttons = []

# Create a function that will be called when a button is clicked
def button_clicked(index):
    # Disable the button that was clicked
    buttons[index].configure(state="disabled")

# Create the buttons using a loop
for i in range(len(button_labels)):
    # Create the button and add it to the list of buttons
    button = tk.Button(root, text=button_labels[i], command=lambda i=i: button_clicked(i))
    buttons.append(button)

    # Add the button to the window
    button.grid(row=i // 3, column=i % 3)

# Start the main event loop
root.mainloop()
'''
import tkinter as tk
# Create the main window
root = tk.Tk()
lista = ['A','B','C','D','E','F']
# Create a matrix of buttons
buttons = []
for i in range(6):
    buttons.append([])
    for j in range(6):
        # Create a button and add it to the matrix
        button = tk.Button(root, text="{}-{}".format(lista[i], (j+1)))
        button.grid(row=i, column=j)
        buttons[i].append(button)

# Disable the button when it is clicked
def disable_button(button):
    button.config(state="disabled")

# Set the command for each button to call the disable_button function
for i in range(6):
    for j in range(6):
        buttons[i][j].config(command=lambda b=buttons[i][j]: disable_button(b))

root.mainloop()