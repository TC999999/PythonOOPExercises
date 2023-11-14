"""Python serial number generator."""


class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start):
        """Initializes the start number and the number to reset to"""
        self.start = start
        self.res = start

    def __repr__(self):
        """shows representation"""
        return f"<SerialGenerator start = {self.res} next = {self.start})"

    def generate(self):
        """generates and increases the start number by 1 everytime the function is run"""
        self.start += 1
        return self.start - 1

    def reset(self):
        """resets the start number to the initial start input"""
        self.start = self.res
