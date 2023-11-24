


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

    def __init__(self, start=0):
        """
        Initialize the SerialGenerator object.

        Takes argument for starting value. The starting value of the serial number defaults to 0.
        """
        self.start = start
        self.current = start

    def generate(self):
        """
        Generate the next serial number.

        increments the current serial number by 1 and returns the new serial number.
        """
        serial_number = self.current
        self.current += 1
        return serial_number

    def reset(self):
        """
        Reset the serial number to the starting value and generate the next serial number.
    
        """
        self.current = self.start
        serial_number = self.current
        self.current += 1
        return serial_number
