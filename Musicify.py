import numpy as np
from collections import deque


class Musicify:

    # Establish necessary global variables. These will not need to be changed, but will be rotated in a deque
    global F, B, C, sharps, flats, toCM, roots
    F = [0, 1, 2, 2, 3, 4, 5, 5, 6, 7]
    B = [-5, -4, -3, -3, -2, -1, -1, 0, 1, 2]
    C = [-1, -1, 0, 1, 1, 2, 3, 4, 4, 5]

    # The elements in the sharps and flats arrays correspond to notes that should be incremented or decremented
    # depending on the key. For example, the first subarray of sharps has one element, so there is 1 sharp in the
    # key making it G major(or e minor in the Aeolian mode).
    sharps = [[5], [0, 5], [0, 5, 7], [0, 2, 5, 7], [0, 2, 5, 7, 9], [0, 2, 4, 5, 7, 9], [0, 2, 4, 5, 7, 9, 11]]
    flats = [[11], [4, 11], [4, 9, 11], [2, 4, 9, 11], [2, 4, 7, 9, 11], [0, 2, 4, 7, 9, 11], [0, 2, 4, 5, 7, 9, 11]]

    # First row is the root notes of sharp scales on the circle of fifths. Second row is the root notes of flat scales
    # on the circle of fifths.
    roots = [[9, 2, 11, 4, 14, 7, 0], [7, 14, 4, 11, 2, 9, 0]]

    #To C-Major
    toCM = [1, 3, 6, 8, 10]

    ''' Explanation of 'key' variable:
        The value of 'key' is equal to number of sharps or flats.
        Positive values of 'key' are sharps, negative values of 'key' are flats.
        Examples: Say I want a key of D Major. Set 'key = 2' for to sharps.
        Now, if I want E-flat major, set 'key = -3' for 3 flats.
        All keys are major by default, but by changing mode one can produce a minor key.
    '''
    notes = []
    key = 0
    mode = 0
    octave = 0

    def __init__(self, notes, key, mode, octave):
        self.notes = notes
        self.key = key
        self.mode = mode
        self.octave = octave

    def to_key_extension(self, extension):
        E = Musicify.use_extension(self, extension, self.notes)
        E = Musicify.use_mode(self.mode, self.key, E)
        Musicify.use_key(self.notes, self.mode, self.key, E)
        Musicify.change_octave(self.notes, self.octave)

    @staticmethod
    def use_extension(self, extension, notes):
        # Check to see if extension is valid
        extensions = ["F", "B", "C", "M"]
        if extension not in extensions:
            raise Exception("Invalid extension type. Choose from 'F'(Forward), 'B'(Backward), or 'C'(Center).")
        if extension == "F":
            return F
        if extension == "B":
            return B
        if extension == "C":
            return C
        if extension == "M":
            self.notes = [x % 6 for x in notes]
            return F


    @staticmethod
    def use_mode(mode, key, E):
        # Check to see if mode is valid
        if mode > 6 or mode < 0:
            raise Exception("mode should be between 0 and 6, inclusive. Otherwise, change octave.")

        scale_root = 0
        if key < 0:
            scale_root = roots[1][abs(key) - 1]
        if key > 0:
            scale_root = roots[0][key - 1]
        index = mode + scale_root + 1

        for i in range(0, index):
            E = deque(E)
            E.rotate(-1)
            E[len(F)-1] = E[2] + 5

        return E

    @staticmethod
    def use_key(notes, mode, key, E):
        # Check to see if key is valid
        if abs(key) > 7:
            raise Exception("Invalid key. Please reference circle of fifths and source code.")

        for i in range(len(notes)):
            notes[i] = notes[i] + list(E)[notes[i]] + mode + 48

            for j in range(len(toCM)):
                if notes[i] % 12 == toCM[j]:
                    notes[i] -= 1
                    break

            # Change key, if necessary
            if key > 0:
                for j in range(len(sharps[key - 1])):
                    if notes[i] % 12 == sharps[key - 1][j]:
                        notes[i] += 1
                        break
            if key < 0:
                for j in range(len(flats[abs(key) - 1])):
                    if notes[i] % 12 == flats[abs(key) - 1][j]:
                        notes[i] -= 1
                        break

    @staticmethod
    def change_octave(notes, octave_number):

        for i in range(len(notes)):
            notes[i] = notes[i] + (12*octave_number)

        if max(notes) > 127 or min(notes) < 0:
            raise Exception("This octave is out of the range that MIDI can produce. Pick a lower octave.")
