# the programme asks for a string to be input, strips leading and trailing spaces and makes the string lower case.
# The output is the length of the string as entered and after normalising.

# Author: Kirstin Barnett
# Based on code from Andrew Beatty

raw_string = input("Please enter a string: ")
normalised_string = raw_string.strip().lower()

length_raw_string = len(raw_string)
length_normalised_string = len (normalised_string)

print (f"That string normalised is: {normalised_string}")
print (f"We reduced the length of the input string from {length_raw_string} to {length_normalised_string} characters")
