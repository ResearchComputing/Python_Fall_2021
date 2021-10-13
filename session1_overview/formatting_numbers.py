# Here are some examples showing how to control the formatting of numbers
# in python.
# You may find this website useful:
# http://mkaz.com/2012/10/10/python-string-format/
import math
# Part 1 - integer formatting.
print("//////////////////////////////////////////////")
print("Here are examples for formatting integers.")
number = 59000
print("My original number: ", number)
numstring = "{:,}".format(number)
print("")
print("Now with commas   : ", numstring)
print("")
print("We can pad with whitespace:")

numstring = "{:7d}".format(number)
print("7 digits, padded with whitespace  : ", numstring)

numstring = "{:8d}".format(number)
print("8 digits, padded with whitespace  : ", numstring)

numstring = "{:9d}".format(number)
print("9 digits, padded with whitespace  : ", numstring)

print("")
print("We can also pad with zeros.")

numstring = "{:0>7d}".format(number)
print("7 digits, padded with zeros  : ", numstring)

numstring = "{:0>8d}".format(number)
print("8 digits, padded with zeros  : ", numstring)

numstring = "{:0>9d}".format(number)
print("9 digits, padded with zeros  : ", numstring)

print("")
print("If we attempt to use fewer digits than the number actually has...")
print("Python does not comply...")

numstring = "{:0>3d}".format(number)
print("Attempting 3 digits: ", numstring)

print("We still see 5 digits.")
print("")
print("//////////////////////////////////////////////")
print("")
print("")
print("Now let's format some floating point numbers (floats).")
print("We will use pi x 1 million")
print("Notice the 'import math' at the top of the code.")
print("'pi' is defined in the math module.")
print("A module is a collection of code that we can import into our own code.")
print("Now that we have imported the module, we can 'get to' pi")
print("with math.pi (see the code).")
print("")

my_number = math.pi*1000000
print("Here is the original number: ", my_number)
print("")
print("First let's modify the number of digits after the decimal...")

my_string = "{:.2f}".format(my_number)
print("Two digits   : ", my_string)

my_string = "{:.1f}".format(my_number)
print("One digit    : ", my_string, "( notice that Python rounded )")

my_string = "{:.11f}".format(my_number)
print("Eleven digits: ", my_string)
print("")
print("Scientific notation is also useful.")
print("We can control the number of digits in a similar fashion.")
print("The format code is identical except that 'f' is replaced with 'e'")

my_string = "{:.2e}".format(my_number)
print("Two digits   : ", my_string)

my_string = "{:.1e}".format(my_number)
print("One digit    : ", my_string)

my_string = "{:.11e}".format(my_number)
print("Eleven digits: ", my_string)

