# Question:
# Define a class which has at least two methods:
# getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods.

# Hints:
# Use __init__ method to construct some parameters


# Solution:
class InputOutString(object):
    def __init__(self, string):  # create __init__ method
        self.string = string

    # create get_string() method
    def get_string(self):
        input_str = raw_input("Enter a word: ")
        return input_str

    def print_string(self):
        string = self.get_string()
        return string.upper()


willie = InputOutString("willie")  # instance of a class
print willie.get_string()
print willie.print_string()








