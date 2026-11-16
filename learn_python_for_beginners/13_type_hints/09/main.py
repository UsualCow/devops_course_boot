def get_reward_summary(items: list, item_counts: dict) -> tuple:
    total_items = 0

    for count in item_counts.values():
        total_items += count

    first_item = items[0]
    return first_item, total_items
