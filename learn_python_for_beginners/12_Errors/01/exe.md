Errors and Exceptions in Python
You've probably encountered some errors in your code from time to time if you've gotten this far in the course. In Python, there are two main kinds of distinguishable errors:

Syntax errors

Exceptions

Syntax Errors
You probably know what these are by now. A syntax error is just the Python interpreter telling you that your code isn't adhering to proper Python syntax.

this is not valid code, so it will error

If I try to run that sentence as if it were valid code I'll get a syntax error:

this is not valid code, so it will error
      ^
SyntaxError: invalid syntax

Exceptions
Even if your code has the right syntax, however, it may still cause an error when an attempt is made to execute it. Errors detected during execution are called "exceptions" and can be handled gracefully by your code. You can even raise your own exceptions when bad things happen in your code.

Python uses a try-except pattern for handling errors.

try:
    10 / 0
except Exception:
    print("can't divide by zero")

Dividing by zero raises an exception, so the except block runs. The same exception can happen inside a function:

def divide(a, b):
    return a / b

The try block runs until an exception is raised or it completes. If an exception is raised, execution jumps to the except block, skipping the remaining code in try. Use as to access the data from the exception:

try:
    divide(10, 0)
    print("division complete")
except Exception as e:
    print(e)

print("done")

Which prints:

division by zero
done

A try/except block lets the program handle exceptions gracefully without crashing.

Putting code inside a try/except block is often called "wrapping" the code in it.

Assignment
One of the calls to get_player_record will raise a player id not found exception.

Put all five existing function calls in a single try block.

Add an except block that prints the exception.
