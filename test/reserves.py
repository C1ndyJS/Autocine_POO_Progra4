import tkinter as tk

# Create the main window
root = tk.Tk()

# Create a frame for the seat map
frame = tk.Frame(root)
frame.pack()

# Create a 2D array of checkboxes representing the seats
seats = []
cols = ['A','B','C','D','F','G']
for row in range(6):
    seats.append([])
    for col in range(len(cols)):
        seat = tk.IntVar()
        #cb = tk.Checkbutton(frame, text=f'Parqueader {row},{col}', variable=seat)
        cb = tk.Button(frame,text=f'{cols[col]}{row}',bg="white",width=3, padx=25, pady=25)
        cb.grid(row=row, column=col)
        seats[row].append(seat)

# Create a button to reserve the selected seats
reserve_button = tk.Button(root, text='Reserve seats', command=lambda: reserve_seats(seats))
reserve_button.pack()

# Define the callback function for the reserve button
def reserve_seats(seats):
    # Iterate over the seat checkboxes
    for row in seats:
        for seat in row:
            # If the seat is selected, print its coordinates
            if seat.get() == 1:
                print(f'Reserving seat {seat.row},{seat.col}')

# Start the event loop
root.mainloop()