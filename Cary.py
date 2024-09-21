class Cary:
    # properties
    color = ""
    brand = ""
    number_of_wheel = 4
    number_of_seat = 4
    maxspeed = 0

    # Constructor
    def __init__(self, color, brand, number_of_wheel, number_of_seat, maxspeed):
        self.color = color
        self.brand = brand
        self.number_of_wheel = number_of_wheel
        self.number_of_seat = number_of_seat
        self.maxspeed = maxspeed

    # Create method set color (optional)
    def setcolor(self, x):
        self.color = x

    # Create method set brand (optional)
    def setbrand(self, x):
        self.brand = x

    # Create method set max speed (optional)
    def setmaxspeed(self, x):
        self.maxspeed = x

    # Method to print car data
    def printData(self):
        print("Color of this Car:", self.color)
        print("Brand of this Car:", self.brand)
        print("Max Speed of this Car:", self.maxspeed)

    # Deconstructor (optional, not used in this example)
    def __del__(self):
        print()  # You can add custom cleanup code here

# Create an instance of the Cary class
objcar1 = Cary("Red", "Toyota", 4, 5, 200)

# Call the printData method on the objcar1 instance
objcar1.printData()