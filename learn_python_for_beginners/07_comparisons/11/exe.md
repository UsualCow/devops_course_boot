Early Returns
So you think you understand conditionals? Get ready to invert your logic!

An early return exits a function before reaching the code below it. We can use this to avoid nesting: placing one if inside another.

For example, this works, but the checks are nested:

def can_cast_spell(mana, on_cooldown):
    if mana >= 10:
        if not on_cooldown:
            return "ready to cast"
        else:
            return "on cooldown"
    else:
        return "not enough mana"

We can invert the checks and return a message as soon as we know the spell can't be cast:

def can_cast_spell(mana, on_cooldown):
    if mana < 10:
        return "not enough mana"
    if on_cooldown:
        return "on cooldown"
    return "ready to cast"

These checks are guard clauses: they return early when a requirement isn't met. The final return "ready to cast" runs only if neither guard returns early.

Assignment
In Fantasy Quest, players can go to a town's local pub. Drinking virtual beer refills their stamina!

Complete the should_serve_customer function that determines if a bartender should serve drinks to a customer. Use guard clauses to return False if any condition below isn't met, and return True otherwise:

The customer's age is 21 or older

The bartender is working

The time is between 5 and 10 o'clock (inclusive of both 5 and 10)