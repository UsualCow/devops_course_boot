def summon_mount(has_mount, distance):
    if not has_mount:
        return None

    if distance > 420:
        return None

    return "Battle Horse"
