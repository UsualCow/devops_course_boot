Even Teams
Fantasy Quest PvP teams are uneven when the match begins. We need a function that will correctly split the two teams evenly.

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

0


start

8


stop

2


step
champions[0:8:2]
Frodo
Legolas
Sam
Boromir
champions[0:8:2] returns [Frodo, Legolas, Sam, Boromir].
Assignment
Complete the get_even_and_odd_teams function.

It accepts a list of players (strings representing their names) and returns two lists in this order:

A new list of all the players with even-numbered indexes in the original list.

A new list of all the players with odd-numbered indexes in the original list.

Use the slice syntax with a "step" to create two new lists from the players list. Don't be afraid to consult your spellbook for list slicing help!