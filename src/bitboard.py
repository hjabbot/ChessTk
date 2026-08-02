import numpy as np


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

    def __repr__(self):
        return str(self)

    def __add__(self, other):
        assert type(self) == type(other), "Can only add two Bitboard objects together"
        # Combine bitboards together as union
        return Bitboard(self | other)

    def __sub__(self, other):
        assert type(self) == type(other), "Can only subtract two Bitboard objects together"
        # Subtract any overlap from the first
        # int(self) to avoid recursion calling self.__sub__
        return Bitboard(int(self) - (self & other))

    @property
    def least_significant_bit(self):
        return Bitboard(np.log2(self & -self))

    @property
    def most_significant_bit(self):
        return Bitboard(np.log2(self))

    @property
    def count(self):
        """
        Counts number of bits = 1

        Returns:
            int: Number of positive bits
        """
        bits = int(self)
        n_bits = 0
        while bits > 0:
            if bits % 1:
                n_bits += 1
            bits = bits >> 1
        return n_bits

    def shift(self, amount):
        """
        Shifts the bits by an amount
        Positive is <<
        Negative is >>

        Args:
            amount (int): How much to shift bitboard by

        Returns:
            Bitboard: New shifted bitboard
        """
        if amount > 0:
            return Bitboard(self << amount)
        else:
            return Bitboard(self >> -amount)

        
    
if __name__ == "__main__":
    bb = Bitboard(32)
    # bb = Bitboard(1037 << 4 * 8)
    print(bb)
    print(bb.least_significant_bit)
    print(bb.most_significant_bit)