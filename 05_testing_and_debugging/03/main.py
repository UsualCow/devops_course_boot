def take_magic_damage(health, resist, amp, spell_power):
    damage = spell_power * amp - resist 
    new_health = health - damage
    return new_health

print(take_magic_damage(100, 10, 2, 20))
