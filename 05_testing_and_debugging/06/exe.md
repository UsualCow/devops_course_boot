Stack Trace
A stack trace (or "traceback") is a scary-looking error message that the Python interpreter prints to the console when it encounters certain problems. Stack traces are most common (at least for you right now) when you're trying to run invalid Python code.

You need to get used to figuring out scary error messages as a programmer. We might as well start now.

Assignment
Go ahead and run the code in its current state. You should see something like this:

File "main.py", line 3
    msg = f"You have {strength} strength, {wisdom} wisdom, and {dexterity} dexterity for a total of {total} stats.
                                                                                                                  ^
SyntaxError: unindent does not match any outer indentation level

File "main.py", line 3

This is the start of the "trace". The purpose of a trace is to take us step-by-step along the path that the Python interpreter took through our code before it encountered an error. More often than not, this will help us figure out what went wrong!

In this case, the interpreter was executing the code in the main.py file when it encountered an error on line 3.

msg = f"You have {strength} strength, {wisdom} wisdom, and {dexterity} dexterity for a total of {total} stats.

This is the actual line of code that caused the error.

SyntaxError: unindent does not match any outer indentation level

This is the error type. In this case, it's a SyntaxError which is just a general type of error related to invalid code. The Python interpreter expected a certain amount of indentation (whitespace at the beginning of the line) but didn't find what was expected.

Don't be fooled! The proper amount of indentation in Python is 4 spaces (or one <tab> stroke). In this case, line 2 is actually indented 6 spaces, which is why the interpreter is confused.

Fix line 2.

Run the code again. You should see another error!

File "main.py", line 3
    msg = f"You have {strength} strength, {wisdom} wisdom, and {dexterity} dexterity for a total of {total} stats.
          ^
SyntaxError: unterminated f-string literal (detected at line 3)

Now we have another SyntaxError. Take a close look at line 3 and fix the problem.