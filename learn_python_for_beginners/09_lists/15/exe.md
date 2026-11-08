Slicing Lists
Python makes it easy to slice and dice lists to work only with the section you care about. One way to do this is to use the simple slicing operator, which is just a colon :.

With this operator, you can specify where to start and end the slice, and how to step through the original list. List slicing returns a new list from the existing list.

The syntax is as follows:

my_list[start:stop:step]

For example:

scores = [50, 70, 30, 20, 90, 10, 50]
# Display list
print(scores[1:5:2])
# Prints [70, 20]

The above uses a start of 1, a stop of 5 (not included), and a step of 2. All of the sections are optional.

Omitting Sections
You can also omit various sections ("start," "stop," or "step"). For example, numbers[:3] means "get all items from the start up to (but not including) index 3." numbers[3:] means "get all items from index 3 to the end."

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers[:3]  # Gives [0, 1, 2]
numbers[3:]  # Gives [3, 4, 5, 6, 7, 8, 9]

Using Only the "step" Section
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers[::2]  # Gives [0, 2, 4, 6, 8]

Negative Indices
Negative indices count from the end of the list. For example, numbers[-1] gives the last item in the list, numbers[-2] gives the second last item, and so on.

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers[-3:]  # Gives [7, 8, 9]

Sequence Slicing
Adjust the slice controls and watch values move into the result.

0
1
2
3
4
5
6
7
stop
Frodo
Aragorn
Legolas
Gimli
Sam
Galadriel
Boromir
Eowyn
start

2


start

8


stop

step
champions[2:8]
Legolas
Gimli
Sam
Galadriel
Boromir
Eowyn
champions[2:8] returns [Legolas, Gimli, Sam, Galadriel, Boromir, Eowyn].
Assignment
Complete the given get_champion_slices function. It takes a list of champions and should return three new lists based on the given champions:

First, return a slice of the champions list that starts with the third champion and goes to the end of the list.

Next, return a slice of the champions list that starts at the beginning of the list and includes all champions except for the very last champion.

Last, return a slice of the champions list that only includes the champions in even numbered indexes (0, 2, 4, ...).

Tips
Remember, you can return multiple values from a function by separating them with commas:

return value1, value2, value3

Zero is an even number