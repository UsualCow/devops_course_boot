Debugging Practice
I want to walk you through how I approach writing code, complete with all the debugging steps I take along the way.

The goal is to write small amounts of code, and then test each bit of code to make sure it's doing what we expect before moving on. Trying to write entire programs at once is a recipe for pain and suffering. The goal is to write a few lines, test them, and then write a few more lines, and repeat until you're done.

This isn't a technique that's unique to beginners. Even senior engineers write code this way.

Assignment
Let's complete the unlock_achievement function. It accepts 3 arguments:

before_xp: int

ach_xp: int

ach_name: str

It should return 2 values:

The player's xp after the achievement is unlocked (The sum of before_xp and ach_xp)

An alert message that says "Achievement Unlocked: ACHIEVEMENT_NAME", where ACHIEVEMENT_NAME is the name of the achievement

Let's start by running the code in its current state. You should see an error like this:

SyntaxError: expected an indented block after function definition on line 1

Hmm... looks like we're getting a syntax error: Python doesn't allow you to have an empty function body. To get past this error, let's just return two dummy values from the function since the function should return 2 values:

def unlock_achievement(before_xp, ach_xp, ach_name):
    return None, None

Run the code again. This time you shouldn't get a syntax error, but your tests should fail because you're returning the incorrect values. Let's fix that.

Let's start by calculating the new amount of xp. Update the function body:

def unlock_achievement(before_xp, ach_xp, ach_name):
    after_xp = before_xp - ach_xp
    print("!!! After xp:", after_xp)
    return None, None

Run the code again. This time you should see the after_xp value printed to the console. Does it look correct? It shouldn't... we have a bug! The after_xp should be the sum of the before_xp and ach_xp values. Fix the code and run it again to make sure it's working.

Once that's working, remove the print statement and return the after_xp value instead of the first None. Run the code again. The XP values in the "Expected" and "Actual" tuples should match, but the alert value is still broken. Let's fix it!

Now that we have the after_xp value, we need to create an alert message. Update the function body:

def unlock_achievement(before_xp, ach_xp, ach_name):
    after_xp = before_xp + ach_xp
    alert = f"!!! Achievement: {ach_name}"
    print(alert)
    return after_xp, None

Run the code. Is the console output what you expect? We want the alert to say:

Achievement Unlocked: ACHIEVEMENT_NAME

Looks like the output is missing the word "Unlocked." Fix the bug, then run the code again to make sure it's working.

When you're confident, remove the print statement and return the alert value instead of the second None. Run the code again. You should see that your tests are passing!

Now that your tests are passing, submit your code so that it runs against all the test cases. Remember, when you "run" instead of submit you're only able to see a few of the tests. The submit button will run all the tests, which might catch bugs you didn't know you had! That's why it's important to debug with print statements and the run button before submitting.