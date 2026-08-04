import cython


@cython.cclass
class Bitboard:
    # Initialise variable like C for cython speedup
    value: cython.longlong

    def __init__(self, value):
        self.value = int(value)

    def __int__(self):
        return self.value

    def __str__(self):
        """
        Chessboard representation of the bitboard

        Returns:
            str: Formatted string of bitboard
        """

        # Output string
        output = ''
        # Copy bitboard so don't edit value
        bitboard = self.value
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

    def __eq__(self, other):
        return int(self) == int(other)

    def __add__(self, other):
        # Adds bits together, ignores overlap
        return Bitboard(self.value | other)

    def __sub__(self, other):
        # Subtracts bits, only overlap
        return Bitboard(self - (self.value & other))

    def __neg__(self):
        return Bitboard(-self.value)

    def __and__(self, other):
        return Bitboard(self.value & other)

    @property
    def least_significant_bit(self):
        return Bitboard(self.value & -self.value)

    @property
    def most_significant_bit(self):
        return Bitboard(1 << (self.value.bit_length() - 1) if self.value > 0 else 0)

    @property
    def count(self):
        """
        Counts number of bits = 1

        Returns:
            int: Number of positive bits
        """
        bits = self.value
        n_bits = 0
        while bits > 0:
            if bits & 1:
                n_bits += 1
            bits >>= 1
        return n_bits

    @cython.ccall
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
            return Bitboard(self.value << amount)
        else:
            return Bitboard(self.value >> -amount)

        
    
if __name__ == "__main__":
    bb = Bitboard(22)
    # bb = Bitboard(1037 << 4 * 8)
    print(bb.count)
    print(bb.shift(-1))