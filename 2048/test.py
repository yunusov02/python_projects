def slide_and_merge(row):
    # Step 1: Slide non-zero numbers to the left
    row = [num for num in row if num != 0]
    
    # Step 2: Merge adjacent equal numbers
    for i in range(len(row) - 1):
        if row[i] == row[i + 1]:
            row[i] *= 2  # Double the value
            row[i + 1] = 0  # Set the merged cell to zero
    
    # Step 3: Slide again to remove gaps
    row = [num for num in row if num != 0]
    
    # Fill the remaining spaces with zeros
    row += [0] * (4 - len(row))  # Assuming fixed size of 4
    return row

def process_board(board):
    return [slide_and_merge(row) for row in board]

# Example usage
board = [
    [2, 4, 8, 0],
    [2, 2, 4, 0],
    [0, 2, 2, 0],
    [2, 2, 0, 2],
    [0, 0, 0, 2],
]

new_board = process_board(board)
for row in new_board:
    print(row)
