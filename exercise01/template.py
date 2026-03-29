# This file contains skeleton code to be copied

# Copy this function to your src/enigma.py, and complete it.
def prepare(text):
    """Prepare a message before encoding it.

    The enigma machine only has the 26 uppercase latin letters. There
    is no spacebar, digits, or punctuation.

    The most common way to handle this was to simply remove all
    whitespace and punctuation from the message. An alternative
    approach was to replace the characters with 'X' or 'Z'.
    """
    pass

# This lines under this if statement are executed if this file is run
# as a script from the command line. If the file is imported, then
# these lines are not run. Having this allows the exercise code to
# check the code you write above. You can add functions and classes
# above this line.
if __name__ == "__main__":

    # This line is declaring a variable with the identifier 'text', and
    # assigning it the string value "Hello world". When we refer to 'text'
    # later, it will have this value.
    text = "Hello world"

    # The print() function writes messages to the terminal
    print(text)

    # In your src/enigma.py, call the prepare function, and assign the value
    # to a new variable. Then print it out.
