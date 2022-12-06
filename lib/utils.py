def reserve_seats(self, seats):
		# Iterate over the seat checkboxes
    for row in seats:
        for seat in row:
                # If the seat is selected, print its coordinates
            if seat.get() == 1:
                print(f'Reserving seat {seat.row},{seat.col}')
