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

    # init method
    def __init__(self, start):
        self.start = start
        self.current = start

    # generate method
    def generate(self):
        self.current += 1
        return self.current - 1

    # reset method
    def reset(self):
        self.current = self.start
