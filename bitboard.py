class Bitboard(int):

    def __str__(self):
        """
        Chessboard representation of the bitboard

        Returns:
            str: Formatted string of bitboard
        """

        # Output string
        output = ''
        # Copy bitboard so don't edit value
        bitboard = int(self)
        # For each row
        for r in range(8,-1,-1):
            # Add in row number if first character
            if r > 0:   row = str(r) + ' '
            # No row number for column labels
            else:       row = '  '

            # For each column
            for c in range(1,9):
                # If column label row, write in column label
                if r == 0: row += chr(ord('a') + c - 1) + ' '
                # If drawing the board
                if r > 0:
                    # If spot occupied
                    if bitboard & 1 << ((r-1) * 8 + c - 1): 
                        row += '# '
                    # If spot empty
                    else:
                        row += '. '

            # Add newline to each row
            output += row + '\n'
        return output

if __name__ == "__main__":
    bb = Bitboard(1037 << 4 * 8)
    print(bb)
